from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBookDetails(Action):

    def name(self) -> Text:
        return "action_book_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Replace with your logic to provide book details based on user's request
        book_details = "[Book details]"

        dispatcher.utter_message(text=f"Sure! Here are the details for the book you're interested in: {book_details}. Is there anything specific you'd like to know?")

        return []