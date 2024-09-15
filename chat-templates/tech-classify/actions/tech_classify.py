from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# Database setup (for illustration purposes, use a proper database setup for production)
def get_document_for_topic(topic):
    # Mock database query
    documents = {
        "PHP": "This is the PHP document content.",
        "AWS": "This is the AWS document content.",
        "Python": "This is the Python document content.",
        "JavaScript": "This is the JavaScript document content.",
        "Java": "This is the Java document content."
    }
    return documents.get(topic, "No document found for this topic.")

class ActionSetTopic(Action):

    def name(self) -> Text:
        return "action_set_topic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        topic = next(tracker.get_latest_entity_values("topic"), None)
        if topic:
            dispatcher.utter_message(text=f"Topic set to {topic}.")
            return [SlotSet("topic", topic)]
        else:
            dispatcher.utter_message(text="I couldn't recognize the topic. Please try again.")
            return []

class ActionFetchDocument(Action):

    def name(self) -> Text:
        return "action_fetch_document"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        topic = tracker.get_slot("topic")
        if topic:
            document_content = get_document_for_topic(topic)
            dispatcher.utter_message(text=document_content)
        else:
            dispatcher.utter_message(text="No topic set. Please specify a topic.")
        return []

class ActionAnswerFurtherQuestion(Action):

    def name(self) -> Text:
        return "action_answer_further_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        topic = tracker.get_slot("topic")
        if topic:
            # Here, you should implement logic to fetch specific answers from the document based on the user's question
            dispatcher.utter_message(text=f"Answering your question based on the {topic} document.")
        else:
            dispatcher.utter_message(text="No topic set. Please specify a topic first.")
        return []
