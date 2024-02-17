import logging
import sys
from llama_index import (
    StorageContext,
    load_index_from_storage
)

# set up logging 
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
log = logging.getLogger()

# rebuild storage context
persist_dir = 'llama_index/testing/storage'
storage_context = StorageContext.from_defaults(persist_dir=persist_dir)

# load index
index = load_index_from_storage(storage_context)

# execute query
query_engine = index.as_query_engine()
log.info('Formed Query Engine')
response = query_engine.query("What are the most commonly injured muscles")
log.info('Submitted and recieved query')
log.info(response)