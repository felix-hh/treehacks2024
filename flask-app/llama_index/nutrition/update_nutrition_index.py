import logging
import sys
import os
from llama_index import (
    TreeIndex
)


from load_nutrition_index import get_index
from utils import parse_website_links, parse_websites, insert_documents

index = get_index()
this_file = os.path.dirname(__file__)

# set up logging 
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
log = logging.getLogger()


websites = parse_website_links(os.path.join(this_file, 'update_webpages.txt'))
documents = parse_websites(websites, log, verbose=False)
insert_documents(index, documents, log)


