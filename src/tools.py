import server.ollama as ollama_client
from src.load_config import project_config

import json
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.StreamHandler()
        ]
    )


default_model = project_config['models']['llama3.1']
llama3_instruct = project_config['models']['llama3.2-instruct']

def summarize_tool(input_txt: str, default_model=default_model) -> dict:
    model = default_model

    SYSTEM_PROMPT = "Summarize this text in a few sentences."

    prompt = f"context: ```{input_txt}``` \n\n output: "
    response, _ = ollama_client.generate(model_name=model, system=SYSTEM_PROMPT, prompt=prompt)
    try:
        result_output = {
            "original_text": input_txt,
            "model_used": model,
            "summary_text": response
        }

    except json.decoder.JSONDecodeError as e:
        logging.info(f"\n\nOutput not valid for response: {response}")
        logging.info(f"\n\nException thrown - {e}")
        result_output = None
    
    return result_output

#TODO add support for vision model

    