import logging
import sys
from llama_index import (
    PandasIndex
)

from load_email_index import get_index

index = get_index()

# set up logging 
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
log = logging.getLogger()

chat_engine = index.as_chat_engine(verbose=True)


print('Type in a question, or exit() to quit')
user_input = input()
while user_input != 'exit()':
    response = chat_engine.chat(user_input)
    print(response)
    print()
    print('Type in a question, or exit() to quit')
    user_input = input()

