from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendBook(Action):

    def name(self) -> Text:
        return "action_recommend_book"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Replace with your logic to recommend books based on user's request
        books = ["Book 1", "Book 2", "Book 3"]
        book_recommendations = ", ".join(books)

        dispatcher.utter_message(text=f"Sure! Here are some books you might be interested in: {book_recommendations}. Which one catches your attention?")

        return []