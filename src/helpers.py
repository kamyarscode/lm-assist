import server.ollama as ollama_client
from src.load_config import project_config

import os
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.StreamHandler()
        ]
    )

def return_client_version():
    response = ollama_client.heartbeat()

    return response

# Depending on user input short name, we want to retrieve the full name to call from client.
def get_models_real_name(short_model_name):
    match short_model_name:
        case None:
            return project_config['models']['llama3.2-instruct']
        
        case "default":
            return project_config['models']['llama3.2-instruct']
        
        case "llama3.2-instruct":
            return project_config['models']['llama3.2-instruct']
        
        case "llama3.2":
            return project_config['models']['llama3.2']
        

# Check which model to use with universal function
def check_which_prompt(type_of_task):
    match type_of_task:
        case None:
            return project_config['prompts']["TEST_PROMPT"]
        
        case "default":
            return project_config['prompts']["TEST_PROMPT"]
        
        case "test":
            return project_config['prompts']["TEST_PROMPT"]
        
        case "summarize":
            return project_config['prompts']["SUMMARIZE_PROMPT"]
        
        case "resume":
            return project_config['prompts']["RESUME_ASSIST"]
        
        case "code assist":
            return project_config['prompts']["CODE_ASSIST"]
        


# Set to lowercase
def lowercase_string(x):
    if isinstance(x, str):
        x.lower()

    return x

# List the files in directory
def files_in_directory(directory):
    file_list = []

    for filename in os.listdir(directory):
        if not os.path.isfile(os.path.join(directory, filename)):
            file_list.append(filename)

    return file_list