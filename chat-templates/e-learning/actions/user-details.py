from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSetTechnology(Action):

    def name(self) -> Text:
        return "action_set_technology"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        technology = next(tracker.get_latest_entity_values("technology"), None)
        return [SlotSet("technology", technology)]

class ActionSetDemographics(Action):

    def name(self) -> Text:
        return "action_set_demographics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        demographics = next(tracker.get_latest_entity_values("demographics"), None)
        return [SlotSet("demographics", demographics)]