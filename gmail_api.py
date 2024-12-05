from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import config

def get_gmail_credentials():
    return Credentials.from_authorized_user_file(config.GMAIL_CLIENT_SECRET_FILE, config.GMAIL_SCOPES)

def create_message(sender, recipient, subject, body_text):
    message = MIMEText(body_text)
    message['to'] = recipient
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_email(sender, recipient, subject, body_text):
    creds = get_gmail_credentials()
    service = build('gmail', 'v1', credentials=creds)
    message = create_message(sender, recipient, subject, body_text)
    response = service.users().messages().send(userId='me', body=message).execute()
    return response
