# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re
from rasa_sdk.events import SlotSet
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_complaint_record"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot_value = tracker.get_slot('complaint_content')
        order_no = self.extract_order_number(slot_value)
        order_no = tracker.get_slot('orderNo')
        # keep on adding the value to context value
        
        complete_complaint_text = str(tracker.get_slot('complete_complaint_text')) + tracker.get_slot('complaint_content')
            
        print(order_no)
        print(slot_value)
        if not order_no:
            # maybe add response message here
            dispatcher.utter_message(text="Please let me know order number")
        else:
            dispatcher.utter_message(text="Recorded your complaint and have created ticket")

        return [SlotSet("complete_complaint_text", complete_complaint_text)]

    def extract_order_number(self, slot_value):
        pattern = r'ORD\d+'

        # Search for the pattern in the order_string
        match = re.search(pattern, slot_value)
        
        # If a match is found, return the matched string
        if match:
            return match.group()
        else:
            return None