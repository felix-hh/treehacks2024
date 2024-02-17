# llama_index.nutrition.utils

import func_timeout
import logging
from llama_index import (
    SimpleWebPageReader,
    BeautifulSoupWebReader,
    IndexStructType,
    Document
)
import urllib

max_wait_time = 3

def timeout_controller(func, args, max_wait_time=max_wait_time) -> tuple[object, bool]:
    try:
        result = func_timeout.func_timeout(max_wait_time, func, args=args)
        return result, True
    except:
        return None, False
    
def is_valid_url(url):
        parsed = urllib.parse.urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

def parse_website_links(file) -> list[str]:
    with open(file, 'r') as file:
        data = file.read()
        raw_websites = set(data.split('\n'))
    websites = filter(is_valid_url, raw_websites)
    return websites


def get_website_document(website, reader: SimpleWebPageReader) -> Document:
    return reader.load_data([website])[0]

def parse_websites(websites, log=logging.getLogger(), verbose=False) -> list[Document]:
    sucesses = 0
    total = 0
    documents = []
    # reader = SimpleWebPageReader(html_to_text=True)
    reader = BeautifulSoupWebReader()
    for website in websites:
        total += 1
        try:
            if verbose: log.info(f'Parsing website: {website}')
            document, success = timeout_controller(get_website_document, (website, reader))
            if success:
                documents.append(document)
                sucesses += 1
                if verbose: log.info(f'Sucessfully parsed website: {website}')
            else:
                log.warn(f'Failed to parse website: {website}')
        except BaseException as err:
            log.error(f'Uncaught error {err}')
    
    log.info(f'Parsed {sucesses}/{total} websites')
    return documents

def insert_document(index: IndexStructType, document: Document):
    index.insert(document)

def insert_documents(index: IndexStructType, documents:list[Document], log=logging.getLogger(), verbose=False):
    sucesses = 0
    total = 0
    for document in documents:
        total += 1
        try:
            assert document is not None
            _, success = timeout_controller(insert_document, (index, document))
            if success:
                if verbose: log.info(f'Sucessfully inserted document')
                sucesses += 1
            else:
                log.warn(f'Failed to insert document {document.doc_id}')
        except BaseException:
            log.error(f'Uncaught error')
    log.info(f'Inserted {sucesses}/{total} documents')

    