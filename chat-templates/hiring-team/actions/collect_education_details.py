from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCollectEducationDetails(Action):

    def name(self) -> Text:
        return "action_collect_education_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        education_details = tracker.latest_message.get("text")
        dispatcher.utter_message(template="utter_ask_education_details")
        return [SlotSet("education_details", education_details)]