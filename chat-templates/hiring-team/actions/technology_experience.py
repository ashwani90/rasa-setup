from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCollectTechnologyExperience(Action):

    def name(self) -> Text:
        return "action_collect_technology_experience"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        technology_experience = tracker.latest_message.get("text")
        dispatcher.utter_message(template="utter_ask_technology_experience")
        return [SlotSet("technology_experience", technology_experience)]