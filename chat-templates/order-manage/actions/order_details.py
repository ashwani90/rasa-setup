from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

# Database setup (for illustration purposes, use a proper database setup for production)
def get_db_connection():
    conn = sqlite3.connect('orders.db')
    return conn

class ActionListOrders(Action):

    def name(self) -> Text:
        return "action_list_orders"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_id = tracker.sender_id
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, order_date FROM orders WHERE user_id = ?", (user_id,))
        orders = cursor.fetchall()
        conn.close()

        if orders:
            response = "Here are your recent orders:\n"
            for order in orders:
                response += f"Order ID: {order[0]}, Date: {order[1]}\n"
        else:
            response = "I couldn't find any recent orders for you."

        dispatcher.utter_message(text=response)
        return []

class ActionOrderDetails(Action):

    def name(self) -> Text:
        return "action_order_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        order_id = next(tracker.get_latest_entity_values("order_id"), None)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
        order = cursor.fetchone()
        conn.close()

        if order:
            response = f"Order ID: {order[0]}, Date: {order[1]}, Status: {order[2]}, Items: {order[3]}"
        else:
            response = f"I couldn't find any details for order ID {order_id}."

        dispatcher.utter_message(text=response)
        return []

class ActionOrderStatus(Action):

    def name(self) -> Text:
        return "action_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        order_id = next(tracker.get_latest_entity_values("order_id"), None)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
        status = cursor.fetchone()
        conn.close()

        if status:
            response = f"The status of your order {order_id} is {status[0]}."
        else:
            response = f"I couldn't find any status for order ID {order_id}."

        dispatcher.utter_message(text=response)
        return []

class ActionRaiseConcern(Action):

    def name(self) -> Text:
        return "action_raise_concern"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        order_id = next(tracker.get_latest_entity_values("order_id"), None)
        concern = next(tracker.get_latest_entity_values("concern"), None)
        user_id = tracker.sender_id

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO concerns (order_id, user_id, concern) VALUES (?, ?, ?)", (order_id, user_id, concern))
        conn.commit()
        conn.close()

        response = f"Your concern about order {order_id} has been recorded. We will address it shortly."
        dispatcher.utter_message(text=response)
        return []
