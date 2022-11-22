from flask import Flask, render_template, request
from google.cloud import dialogflow
from utils.settings import *
from utils.handler import get_twilio_messsage, proto_to_dict, webhook_handler
from google.api_core.exceptions import InvalidArgument
from twilio.rest import Client
from utils.wadMapper import WADMapper

app = Flask(__name__)

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

data = WADMapper()

@app.route("/app/", methods=['POST'])
def app_index():
    if 'twilio' in request.headers.get('User-Agent').lower():   # Sends user-query to dialogflow
        data.setContext(get_twilio_messsage(request.values))
        session_client = dialogflow.SessionsClient()
        data.setSession(session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID))
        data.setQuery(dialogflow.QueryInput(text=dialogflow.TextInput(text=data.context['body'], language_code=DIALOGFLOW_LANGUAGE_CODE)))
        try:
            data.setResponse(session_client.detect_intent(session=session, query_input=data.query_input))
        except InvalidArgument:
            raise
    
    if 'google' in request.headers.get('User-Agent').lower():   # Dialogflow generates response
        while not data.response:
            continue
        result = webhook_handler(proto_to_dict(data.response), data.context)
        _ = twilio_client.messages.create(
            from_=TWILIO_SENDER,
            to='whatsapp:+91{}'.format(data.context['contact']),
            body=result['response']
        )

    return 'Ok'

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

app.run()

