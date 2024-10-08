from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
# import sqlite3

# Database setup (for illustration purposes, use a proper database setup for production)
# def get_db_connection():
#     conn = sqlite3.connect('hiring_database.db')
#     return conn

# def save_user_details(contact_info, education_details, technology, experience):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (contact_info, education_details, technology, experience) VALUES (?, ?, ?, ?)",
#                    (contact_info, education_details, technology, experience))
#     conn.commit()
#     conn.close()

class ActionSaveDetailsInfo(Action):

    def name(self) -> Text:
        return "action_save_details_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Hello")
        contact_info = tracker.get_slot('contact_info')
        education_details = tracker.get_slot('education_details')
        technology = tracker.get_slot('technology')
        experience = tracker.get_slot('experience')
        if contact_info:
            dispatcher.utter_message(text=f"Got it! Your details are saved. Thanks. {contact_info}.")
            return []
        else:
            dispatcher.utter_message(text="I couldn't get your contact info. Please provide it again.")
            return []

# class ActionSaveEducationDetails(Action):

#     def name(self) -> Text:
#         return "action_save_education_details"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         education_details = next(tracker.get_latest_entity_values("education_details"), None)
#         if education_details:
#             dispatcher.utter_message(text=f"Got it! Your education details are {education_details}.")
#             return [SlotSet("education_details", education_details)]
#         else:
#             dispatcher.utter_message(text="I couldn't get your education details. Please provide them again.")
#             return []

# class ActionSaveTechnology(Action):

#     def name(self) -> Text:
#         return "action_save_technology"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         technology = next(tracker.get_latest_entity_values("technology"), None)
#         if technology:
#             dispatcher.utter_message(text=f"Got it! Your technology skills are {technology}.")
#             return [SlotSet("technology", technology)]
#         else:
#             dispatcher.utter_message(text="I couldn't get your technology skills. Please provide them again.")
#             return []

# class ActionSaveExperience(Action):

#     def name(self) -> Text:
#         return "action_save_experience"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         experience = next(tracker.get_latest_entity_values("experience"), None)
#         if experience:
#             dispatcher.utter_message(text=f"Got it! Your experience is {experience}.")
#             return [SlotSet("experience", experience)]
#         else:
#             dispatcher.utter_message(text="I couldn't get your experience. Please provide it again.")
#             return []

# class ActionSaveUserDetails(Action):

#     def name(self) -> Text:
#         return "action_save_user_details"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         contact_info = tracker.get_slot("contact_info")
#         education_details = tracker.get_slot("education_details")
#         technology = tracker.get_slot("technology")
#         experience = tracker.get_slot("experience")
        
#         if contact_info and education_details and technology and experience:
#             save_user_details(contact_info, education_details, technology, experience)
#             dispatcher.utter_message(text="Your details have been saved successfully.")
#         else:
#             dispatcher.utter_message(text="I am missing some of your details. Please provide all the required information.")
        
#         return []
