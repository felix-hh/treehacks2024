import logging
import sys
import os
from llama_index import (
    LLMPredictor,
    ServiceContext,
    TreeIndex,
    StorageContext,
    load_index_from_storage,
)
from langchain.chat_models import ChatOpenAI
import pandas as pd

this_file = os.path.dirname(__file__)
persist_dir = os.path.join(this_file, 'storage')
key = os.environ['OPENAI_API_KEY']

def get_index():
    # set up logging 
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
    
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
    return index