import os
import json

import PyPDF2
import logging

from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Set logging later.
logging.basicConfig(
    level=logging.INFO,
)

# Add langchain text splitter
def load_data_split_text(use_dir:str, cleaned_text=None, input_dir=None):

    splitter = RecursiveCharacterTextSplitter1(
        chunk_size=3200,
        chunk_overlap=150,
        length_function=len,
        is_separator_regex=False,

    )

    if use_dir == "true":

        logging.info("Loading doc..")
        loader = DirectoryLoader(input_dir, show_progress=True)
        documents = loader.load()

        logging.info ("Splitting doc into chunks")
        pages = splitter.split_documents(documents)

        metadata_src = pages[0].metadata["source"]
        filename = ""

        return pages, filename
    
    elif use_dir == "false":
        pages = splitter.split_text(cleaned_text)
        return pages
    else:
        return "Input data not loaded."
    

# Find the valid file path and raise exception if not found.
def find_valid_file_path(paths: list):

    for path in paths:
        try:
            if os.path.isfile(path):
                print ("found valid file path: {path}")
                return path
        
        except Exception as e:
            print (f"Error checking path {path}: {e}")
        
        raise ValueError("No valid path found.")
    

# Extract PDF data:
