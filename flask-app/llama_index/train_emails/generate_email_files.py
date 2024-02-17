import pandas as pd
import os

this_dir = os.path.dirname(__file__)
email_dir = os.path.join(this_dir, 'emails')

messages_df = pd.read_csv(os.path.join(this_dir, 'emails_with_emotions.csv'), index_col='id')

for id, row in messages_df.iterrows():
    with open(os.path.join(email_dir, f'{id}.txt'), 'w') as file:
        file.write(row['Date'])
        file.write('\n')
        file.write(row['To'])
        file.write('\n')
        file.write(row['From'])
        file.write('\n')
        file.write(row['Subject'])
        file.write('\n')
        file.write(str(row['Body']))
        file.write('\n')
        file.write(row['Emotions'])
        file.write('\n')