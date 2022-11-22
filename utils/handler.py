import json
import requests
from pprint import pprint

def webhook_handler(req, context):
    action = req["queryResult"]["action"]
    queryText = req["queryResult"]["queryText"]

    # Create actions in dialogflow agent
    if action == 'input.welcome':
        return {'response': 'Hello World!'}

    else:
        return print("Error in webhook_handler function - Action not found")


def get_twilio_messsage(values):
    context = {}
    context['name'] = values.get('ProfileName')
    context['body'] = values.get('Body')
    context['contact'] = values.get('From')[-10:]
    return context

def proto_to_dict(message) -> dict:
    return json.loads(message.__class__.to_json(message))
