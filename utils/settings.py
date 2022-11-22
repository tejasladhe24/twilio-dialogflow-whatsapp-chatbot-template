import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dialogflow.json' # Save "dialogflow.json" in root directory

DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

TWILIO_ACCOUNT_SID='<twilio-account-sid>'               # get it from twilio account settings
TWILIO_AUTH_TOKEN='<twilio-auth-token>'                 # get it from twilio account settings
TWILIO_SENDER = '<twilio-whatsapp-number>'              # get it from twilio whatsapp sandbox settings
DIALOGFLOW_PROJECT_ID = '<dialogflow-project-id>'       # get it from GCP console
