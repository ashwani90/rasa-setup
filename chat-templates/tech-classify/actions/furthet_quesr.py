from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRespondFurtherQuestions(Action):

    def name(self) -> Text:
        return "action_respond_further_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic = tracker.get_slot("topic")
        dispatcher.utter_message(template="utter_ask_further_questions", topic=topic)
        return []