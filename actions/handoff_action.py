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
import pathlib
from rasa_sdk.events import SlotSet, ConversationPaused
import spacy
import ruamel.yaml
import json

here = pathlib.Path(__file__).parent.absolute()
handoff_config = (
    ruamel.yaml.safe_load(open(f"{here}/handoff_config.yml", "r")) or {}
).get("handoff_hosts", {})
#
#
class HandoffAction(Action):
    
    def name(self) -> Text:
        return "handoff_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_handoff")
        handoff_to = "assistant"
        handoff_bot = handoff_config.get(handoff_to, {})
        url = handoff_bot.get('url')
        if url:
            # don't need to check channel or other things
            dispatcher.utter_message(
                json.dumps({
                    "handoff_host": url,
                    "title": "assistant"
                })
            )
             
        # return [ConversationPaused()]
        return []
