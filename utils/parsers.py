import os
import json

import PyPDF2
import logging

import pandas as pd
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Set logging later.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    handlers=[
            logging.StreamHandler() # log to console from here.
        ] 
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
def extract_from_pdf(pdf_path) -> str:
    ind_page = []

    # Check if file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found.")
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            if len(pdf_reader.pages) > 0:
                # Empty string, store text
                text = ""

                # Iterate through pages:
                for page_number in range(len(pdf_reader.pages)):
                    # Get page count
                    page = pdf_reader.pages[page_number]

                    page_text = page.extract_text()

                    text += page_text
                    ind_page.append(page_text)

            else:
                raise ValueError("File provided not valid")
        
    except Exception as e:
        raise RuntimeError(f"Error reading PDF file.")
    
    return text, ind_page


# Parse json files

def parse_json(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            json_file.close()
            return data
        
    except FileNotFoundError:
        print (f"File not found - {file_path}")
        return None
    
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None


# Parse xls file into chunks. return the array.
def parse_xls_into_chunks(path):
    
    df = pd.read_excel(path, header=None)
