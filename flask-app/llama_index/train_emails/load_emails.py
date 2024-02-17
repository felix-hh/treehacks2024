from __future__ import print_function
import os.path
import base64
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd
df_columns = ['id', 'Date', 'To', 'From', 'Subject', 'Body']

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
    this_dir = os.path.dirname(__file__)

    if os.path.exists(os.path.join(this_dir, 'emails_read.csv')):
        messages_df = pd.read_csv(os.path.join(this_dir, 'emails_read.csv'))
        old_message_ids = set(messages_df['id'].values)
        print(old_message_ids)
    else:
        messages_df = pd.DataFrame([], columns=df_columns)
        old_message_ids = set()

    if os.path.exists(os.path.join(this_dir, 'token.json')):
        creds = Credentials.from_authorized_user_file(os.path.join(this_dir, 'token.json'), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.path.join(this_dir, 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.path.join(this_dir, 'token.json'), 'w') as token:
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
            new_messages_data = []
            new_message_ids = set()
            for message in messages:
                message_data = dict()
                id = message['id']
                if id in old_message_ids or id in new_message_ids:
                    print(f'Skipping email {id}')
                    continue

                new_message_ids.add(id)
                message_data['id'] = id
                msg = service.users().messages().get(userId='me', id=id).execute()
                email_data = msg['payload']['headers']
                for values in email_data:
                    name = values['name']
                    value = values['value']
                    if name.lower() == 'subject':
                        message_data['Subject'] = value
                    elif name.lower() == 'from':
                        message_data['From'] = value
                    elif name.lower() == 'to':
                        message_data['To'] = value
                    elif name.lower() == 'date':
                        message_data['Date'] = value

                try:
                    payload = msg['payload']
                    if 'parts' in payload.keys():
                        body = parse_parts(payload['parts'][0])
                    else:
                        body = parse_parts(payload)
                    message_data['Body'] = body
                    new_messages_data.append(message_data)
                except BaseException as error:
                    print('An error occurred: ', error)
                    print(msg['payload'])
                message_count += 1
                print(f'Read message {id}')
            
            if len(new_messages_data) > 0:
                new_messages_df = pd.DataFrame(new_messages_data)
                messages_df = pd.concat((messages_df, new_messages_df), axis=0)
            save_file = os.path.join(this_dir, 'emails_read.csv')
            messages_df.to_csv(save_file)
            print(f'Saved email dataframe at {save_file}')

    except HttpError as error:
        print('An error occurred: ', error)

if __name__ == '__main__':
    main()
