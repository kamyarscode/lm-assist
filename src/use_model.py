from server.ollama import client
import json

from helpers import check_which_prompt
def prompt_model(input_str: str, metadata={}, model="default"):

    SYSTEM_PROMPT_DICT = {
        "prompt_to_use": check_which_prompt(model)
    }

    # Set model hyperparameters. Do this with config file later.
    model_config = {
        'num_ctx': 8096,
        'num_predict': 2048,
        'top_k': 30,
        'top_p': 0.85,
        'repeat_last_n': 512,
        'temperature': 0.5
    }

    SYSTEM_PROMPT = SYSTEM_PROMPT_DICT['prompt_to_use'][1]

    # User prompt begins here
    user_prompt = f"{input_str}<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>"
    response, _ = client.generate(model_name=model,system=SYSTEM_PROMPT,prompt=user_prompt,options=model_config)

    try:

        result=json.loads(response, strict=False)

        # Check if result is a list and not empty.
        if isinstance(result,list) and len(result) > 0:
            result = [dict(item, **metadata) for item in result]
        else:
            result = None

    except Exception as e:
        print ("Error with output, view response {response}, {e}")
        result = None

    return result

