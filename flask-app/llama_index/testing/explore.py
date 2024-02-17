import logging
import sys
from llama_index import ListIndex, SimpleWebPageReader


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

documents = SimpleWebPageReader(html_to_text=True).load_data(["https://www.webmd.com/fitness-exercise/guide/muscle-strain"])
log = logging.getLogger()
log.info('Loaded webpage')
index = ListIndex.from_documents(documents)
log.info('Formed ListIndex')
query_engine = index.as_query_engine()
log.info('Formed Query Engine')
response = query_engine.query("What are the common symptoms of muscle strain")
log.info('Submitted and recieved query')
print(response)