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
import spacy
#
#
class ActionProductSearchss(Action):
    nlp = spacy.load("en_core_web_sm")

    def name(self) -> Text:
        return "product_search_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        product_search_query = tracker.get_slot('product_search_query')
        if product_search_query:
            entities = self.extract_product_entities(product_search_query)
            keywords = self.extract_nouns(product_search_query)
            
            # so we extracted nouns and other things as well
            # keywords will be used to search the product
            data = {}
            data, entity_items = self.normalize_query_items(entities=entities, data=data, entity_items=[])
            data, entity_items = self.normalize_query_items(keywords=keywords, data=data, entity_items=entity_items)
            print(data)
            
        # extract entities
        # call the api and return the results
        # so now we have enerything we need to call the api
        # query https://product.amazon.com/
        # decide on the action to do that
        dispatcher.utter_message(text="OK lets search your product")
        # if not order_no:
        #     # maybe add response message here
        #     dispatcher.utter_message(text="Please let me know order number")
        # else:
        #     dispatcher.utter_message(text="Recorded your complaint and have created ticket")

        # return [SlotSet("complete_complaint_text", complete_complaint_text)]
        return []
        
    def extract_product_entities(self, text):
        # Process the text with spaCy
        doc = self.nlp(text)
        
        # Define a list of relevant entity types for product details
        # relevant_entities = ["PRODUCT", "MONEY", "QUANTITY", "GPE", "ORG", "DATE"]
        relevant_entities = ["PRODUCT", "ORG" ]
        
        # Extract entities and filter by relevant types
        extracted_entities = []
        for ent in doc.ents:
            if ent.label_ in relevant_entities:
                extracted_entities.append((ent.text, ent.label_))
        
        return extracted_entities
    
    def extract_nouns(self, sentence):
        # Process the sentence with spaCy
        doc = self.nlp(sentence)
        
        # Extract tokens that are nouns
        nouns = [token.text for token in doc if token.pos_ == "NOUN"]
        
        return nouns
    
    def normalize_query_items(self, entities=None, keywords=None, data={}, entity_items=[]):
        if  keywords:
            keyword_string = ""
            for k in keywords:
                if not (entity_items and k in entity_items):
                    keyword_string += k + " "
            data['keywords'] = keyword_string
        if entities:
            for entity in entities:
                entity_items = entity[0]
                data[entity[1]] = entity[0]
        return data, entity_items