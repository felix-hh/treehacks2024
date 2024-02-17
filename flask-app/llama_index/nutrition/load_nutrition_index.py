import logging
import sys
import os
from llama_index import (
    StorageContext,
    load_index_from_storage,
    IndexStructType
)

def get_index() -> IndexStructType:
    this_file = os.path.dirname(__file__)
    persist_dir = os.path.join(this_file, 'storage')

    # set up logging 
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
    
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)

    # load index
    index = load_index_from_storage(storage_context)
    return index