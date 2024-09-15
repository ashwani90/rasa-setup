from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCourseDetails(Action):

    def name(self) -> Text:
        return "action_course_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Replace with your logic to provide course details based on user's request
        course_details = "[Course details]"

        dispatcher.utter_message(text=f"Sure! Here are the details for the course you're interested in: {course_details}. Is there anything specific you'd like to know?")

        return []