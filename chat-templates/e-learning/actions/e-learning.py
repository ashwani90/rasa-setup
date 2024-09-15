from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

# Database setup (for illustration purposes, use a proper database setup for production)
def get_db_connection():
    conn = sqlite3.connect('learning_platform.db')
    return conn

class ActionAskUserDetails(Action):

    def name(self) -> Text:
        return "action_ask_user_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Please provide your technology of interest and your proficiency level.")
        return []

class ActionRecommendCourseOrBook(Action):

    def name(self) -> Text:
        return "action_recommend_course_or_book"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        technology = next(tracker.get_latest_entity_values("technology"), None)
        demographics = next(tracker.get_latest_entity_values("demographics"), None)
        
        if technology and demographics:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute("SELECT course_name FROM courses WHERE technology = ? AND demographics = ?", (technology, demographics))
            courses = cursor.fetchall()
            
            cursor.execute("SELECT book_name FROM books WHERE technology = ? AND demographics = ?", (technology, demographics))
            books = cursor.fetchall()
            
            conn.close()
            
            response = "Based on your interest in {technology} and your level as a {demographics}, I recommend the following:\n"
            response += "Courses:\n"
            for course in courses:
                response += f"- {course[0]}\n"
            
            response += "Books:\n"
            for book in books:
                response += f"- {book[0]}\n"
        else:
            response = "I'm sorry, I didn't catch that. Could you please provide your technology of interest and your proficiency level?"

        dispatcher.utter_message(text=response)
        return []

class ActionCourseDetails(Action):

    def name(self) -> Text:
        return "action_course_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        course_name = next(tracker.get_latest_entity_values("course_name"), None)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE course_name = ?", (course_name,))
        course = cursor.fetchone()
        conn.close()

        if course:
            response = f"Course Name: {course[0]}, Technology: {course[1]}, Level: {course[2]}, Description: {course[3]}"
        else:
            response = f"I couldn't find any details for the course {course_name}."

        dispatcher.utter_message(text=response)
        return []

class ActionBookDetails(Action):

    def name(self) -> Text:
        return "action_book_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        book_name = next(tracker.get_latest_entity_values("book_name"), None)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE book_name = ?", (book_name,))
        book = cursor.fetchone()
        conn.close()

        if book:
            response = f"Book Name: {book[0]}, Technology: {book[1]}, Level: {book[2]}, Description: {book[3]}"
        else:
            response = f"I couldn't find any details for the book {book_name}."

        dispatcher.utter_message(text=response)
        return []
