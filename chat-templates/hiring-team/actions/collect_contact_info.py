from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCollectContactInfo(Action):

    def name(self) -> Text:
        return "action_collect_contact_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        contact_info = tracker.latest_message.get("text")
        dispatcher.utter_message(template="utter_ask_contact_info")
        return [SlotSet("contact_info", contact_info)]