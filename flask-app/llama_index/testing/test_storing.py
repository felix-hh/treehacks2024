import logging
import sys
import os
from llama_index import (
    LLMPredictor,
    ServiceContext,
    TreeIndex,
    SimpleWebPageReader,
)
from langchain import OpenAI

file_loc = os.path.dirname(__file__)

# set up logging 
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
log = logging.getLogger()

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-002"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# build index

with open(os.path.join(file_loc, 'webpages.txt'), 'r') as file:
    data = file.read()
    websites = data.split('\n')


documents = SimpleWebPageReader(html_to_text=True).load_data(websites)
index = TreeIndex.from_documents(documents, service_context=service_context)

# Store Data
persist_dir = 'llama_index/testing/storage'
index.storage_context.persist(persist_dir=persist_dir)
log.info('Successfully stored data')
