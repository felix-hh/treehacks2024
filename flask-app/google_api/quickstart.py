from __future__ import print_function
import os.path
import base64
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def parse_parts(parts):
    """
    Utility function that parses the parts of a message.
    """
    data = parts['body']['data']
    data = data.replace("-", "+").replace("_", "/")
    decoded_data = base64.b64decode(data)
    return decoded_data.decode()

def main():
    """
    Shows basic usage of the Gmail API.
    Lists the subject and content of the latest 10 emails.
    """
    creds = None
    if os.path.exists('google_api/token.json'):
        creds = Credentials.from_authorized_user_file('google_api/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('google_api/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('google_api/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('gmail', 'v1', credentials=creds)
        # Call the Gmail API to fetch INBOX
        results = service.users().messages().list(userId='me', labelIds=['SENT'], maxResults=20).execute()
        messages = results.get('messages', [])
        if not messages:
            print('No new messages.')
        else:
            message_count = 0
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                email_data = msg['payload']['headers']
                for values in email_data:
                    name = values['name']
                    if name == 'Subject':
                        subject = values['value']
                        print('Subject: ', subject)
                try:
                    payload = msg['payload']
                    body = parse_parts(payload['parts'][0])
                    print('Body: ', body)
                except BaseException as error:
                    print('An error occurred: ', error)
                message_count += 1

    except HttpError as error:
        print('An error occurred: ', error)

if __name__ == '__main__':
    main()
