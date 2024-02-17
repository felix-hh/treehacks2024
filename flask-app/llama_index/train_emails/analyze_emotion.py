import os
import pandas as pd
import asyncio
from hume import HumeStreamClient
from hume.models.config import LanguageConfig

this_dir = os.path.dirname(__file__)

messages_df = pd.read_csv(os.path.join(this_dir, 'emails_read.csv'), index_col='id')
email_bodies = messages_df['Body']

async def main():
    client = HumeStreamClient(os.environ['HUME_API_KEY'])
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        emotions_data = []
        for index, message in email_bodies.items():
            print('Starting')
            try:
                print(message)
                result = await socket.send_text(message)
                emotions = result["language"]["predictions"][0]["emotions"]
                print(emotions)
                emotions_data.append(emotions)
                messages_df.loc[index]['Emotions'] = emotions
            except:
                print("Couldn't analyze emotions")
                emotions_data.append([])
                continue
    
        messages_df['Emotions'] = emotions_data
    messages_df.to_csv(os.path.join(this_dir, 'emails_with_emotions.csv'), index_label='id')


asyncio.run(main())