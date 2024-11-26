from server.ollama import client

LLAMA_SYS_PROMPT = "some llama prompt here for purpose"
LLAMA_Q_SYSTEM_PROMPT = "prompt for quantized llama3.1"
def return_client_version():
    response = client.heartbeat()

    return response

# Check which model to use with universal function
def check_which_prompt(model):
    if model == None:
        model = "llama3.1"

    elif model == "llama3:latest":

        SYSTEM_PROMPT = LLAMA_SYS_PROMPT

    elif model == "llama3.1:8b":
        SYSTEM_PROMPT = LLAMA_Q_SYSTEM_PROMPT

# Set to lowercase
def lowercase_string(x):
    if isinstance(x, str):
        x.lower()

    return x