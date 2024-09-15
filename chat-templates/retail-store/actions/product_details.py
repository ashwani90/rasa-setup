from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideProductInfo(Action):

    def name(self) -> Text:
        return "action_provide_product_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        product = next(tracker.get_latest_entity_values("product"), None)
        
        if product:
            # Replace this with actual product information fetching logic
            product_info = f"The {product} is one of our best-selling products. It has excellent reviews and is available in various sizes and colors."
            dispatcher.utter_message(text=product_info)
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't catch the product name. Can you please specify which product you are asking about?")
        
        return []
