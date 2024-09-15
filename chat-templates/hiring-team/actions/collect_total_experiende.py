from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCollectWorkingExperience(Action):

    def name(self) -> Text:
        return "action_collect_working_experience"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        working_experience = tracker.latest_message.get("text")
        dispatcher.utter_message(template="utter_ask_working_experience")
        return [SlotSet("working_experience", working_experience)]