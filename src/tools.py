import server.ollama as ollama_client
from src.load_config import project_config
from api.chat_utils import add_to_chat_history
import json
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.StreamHandler()
        ]
    )


default_model = project_config['models']['default']
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

# 
def chat_tool(chat_history, input_txt: str, default_model=default_model) -> dict:
    model = default_model

    SYSTEM_PROMPT = "Your role is to chat with the user. Recall previous messages in the chat history to provide relevant responses. " \
                    "If you don't know the answer, say 'I don't know'."

    prompt = f"chat history context: ```{list(chat_history)}``` user: ```{input_txt}``` \n\n output: "

    response, _ = ollama_client.generate(model_name=model, system=SYSTEM_PROMPT, prompt=prompt)
    print ("Adding this INPUT: ", input_txt)
    print ("Adding this RESPONSE: ", response)

    chat_history = add_to_chat_history(chat_history, user_input=input_txt, llm_response=response)

    print ("New chat history: ", chat_history)
    try:
        result_output = {
            "original_text": input_txt,
            "model_used": model,
            "chat_history": list(chat_history),
            "model_response": response
        }

    except json.decoder.JSONDecodeError as e:
        logging.info(f"\n\nOutput not valid for response: {response}")
        logging.info(f"\n\nException thrown - {e}")
        result_output = None
    
    return result_output

#TODO add support for vision model

    