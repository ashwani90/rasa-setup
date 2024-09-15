from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Database setup (for illustration purposes, use a proper database setup for production)
def get_db_connection():
    conn = sqlite3.connect('cricket_database.db')
    return conn

def fetch_player_details(player_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE name = ?", (player_name,))
    player = cursor.fetchone()
    conn.close()
    return player

def fetch_match_details(match_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matches WHERE id = ?", (match_id,))
    match = cursor.fetchone()
    conn.close()
    return match

def fetch_statistics(statistic_type):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT player_name, {statistic_type} FROM statistics")
    stats = cursor.fetchall()
    conn.close()
    return stats

class ActionPlayerDetails(Action):

    def name(self) -> Text:
        return "action_player_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        player_name = tracker.get_slot("player_name")
        player = fetch_player_details(player_name)
        
        if player:
            response = f"Player Name: {player[0]}, Team: {player[1]}, Role: {player[2]}, Runs: {player[3]}, Wickets: {player[4]}"
        else:
            response = f"I couldn't find any details for the player {player_name}."
        
        dispatcher.utter_message(text=response)
        return []

class ActionMatchDetails(Action):

    def name(self) -> Text:
        return "action_match_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        match_id = tracker.get_slot("match_id")
        match = fetch_match_details(match_id)
        
        if match:
            response = f"Match ID: {match[0]}, Date: {match[1]}, Teams: {match[2]} vs {match[3]}, Score: {match[4]} - {match[5]}"
        else:
            response = f"I couldn't find any details for the match {match_id}."
        
        dispatcher.utter_message(text=response)
        return []

class ActionStatistics(Action):

    def name(self) -> Text:
        return "action_statistics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        statistic_type = tracker.get_slot("statistic_type")
        stats = fetch_statistics(statistic_type)
        
        if stats:
            players = [stat[0] for stat in stats]
            values = [stat[1] for stat in stats]
            
            plt.figure(figsize=(10, 5))
            sns.barplot(x=players, y=values)
            plt.xlabel('Players')
            plt.ylabel(statistic_type.capitalize())
            plt.title(f'{statistic_type.capitalize()} by Player')
            
            image_path = '/mnt/data/statistics.png'
            plt.savefig(image_path)
            plt.close()
            
            dispatcher.utter_message(text=f"Here are the {statistic_type} statistics.", image=image_path)
        else:
            dispatcher.utter_message(text=f"I couldn't find any statistics for {statistic_type}.")
        
        return []
