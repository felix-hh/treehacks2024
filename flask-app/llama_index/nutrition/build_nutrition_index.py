import logging
import sys
import os
import urllib
from llama_index import (
    LLMPredictor,
    ServiceContext,
    ListIndex,
    TreeIndex,
    SimpleWebPageReader,
)
from langchain import OpenAI

from utils import parse_websites, insert_documents, parse_website_links

this_file = os.path.dirname(__file__)
key = os.environ['OPENAI_API_KEY']


# set up logging 
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
log = logging.getLogger()


# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-002", openai_api_key=key))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
index = TreeIndex([], service_context=service_context, build_tree=False)
# index = ListIndex([], service_context=service_context) 


# build index
websites = parse_website_links(os.path.join(this_file, 'webpages.txt'))
documents = parse_websites(websites, log, verbose=False)

# insert_documents(index, documents, log, verbose=False)
index = TreeIndex.from_documents(documents, service_context=service_context)


# Store Data
persist_dir = os.path.join(this_file, 'storage')
index.storage_context.persist(persist_dir=persist_dir)
log.info(f'Successfully stored index info in {persist_dir}')
