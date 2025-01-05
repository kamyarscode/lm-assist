import server.ollama as ollama_client
import json

import numpy as np

import pandas as pd
from helpers import check_which_prompt, lowercase_string, get_models_real_name


def parse_model_output(model_output: str) -> dict:
    """
    Parses response from model, usually a string, and output response as json.
    
    Args:
        output (str): The output string from model.
    
    Returns:
        dict: A dict of the parsed output or an error message if applicable.
            status: if successful or not,
            data: the response we got,
            type: response type
    """
    
    try:
        # Try parsing the string as JSON with strict set to false.
        parsed_output = json.loads(model_output, strict=False)
        return {
            "status": "success",
            "data": parsed_output,
            "type": type(parsed_output).__name__, # In the past observed dict and list
        }
    
    except json.JSONDecodeError as e:
        # Handle invalid JSON and provide raw output for debugging.
        return {
            "status": "error",
            "message": "Invalid JSON format",
            "raw_output": model_output,
            "error_details": str(e),
        }

# Function to go through and pick out model to use with its configurations.
def prompt_model(input_str: str, metadata={}, short_model_name="default", type_of_task="summarize") -> dict:
    """
    Takes in user parameters and sends to model for an answer. Returns dict of the response.
    
    Args:
        input_str (str): The output string from model.
        metadata (dict): Data to unpack for model params.
        short_model_name (str): The name of the model in short form i.e "llama3.2" or "llama3.2-instruct"
        type_of_task (str): A string dictating what task we want the model to do.

    Returns:
        dict: A dict of the parsed response.
    """

    # Get name of model from short name
    model = get_models_real_name(short_model_name)

    # Get prompt based off task type.
    system_task_prompt = check_which_prompt(type_of_task)

    # Set model hyperparameters. Do this with config file later.
    model_config = {
        'num_ctx': 8096,
        'num_predict': 2048,
        'top_k': 30,
        'top_p': 0.85,
        'repeat_last_n': 512,
        'temperature': 0.7
    }


    # User prompt begins here
    user_prompt = f"{input_str}<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>"
    response, _ = ollama_client.generate(model_name=model,system=system_task_prompt,prompt=user_prompt,options=model_config)

    try:
        # Check if result is a list and not empty.
        #if isinstance(result, list) and len(result) > 0:

        #Check if response isnt empty.
        if len(response) > 0:
            result = parse_model_output(response)

        #     result = [dict(item, **metadata) for item in result]
        # else:
        #     result = None

    except Exception as e:
        print (f"Error with output, view response: {response}, {e}")
        result = None

    return result

# Go through results model spits out and parse them. If not parsable into array, return empty array. Specifically used for dataframes
# if they are involved.
def parse_model_resp(dataframe: pd.DataFrame, model=None) -> list:

    results = dataframe.apply(lambda row: (print(f"Processing..\n"), prompt_model(row.text, {"data": row.data}, model))[1], axis=1
                                        )

    results = results.dropna()
    results = results.reset_index(drop=True)

    if results.empty:
        print (f"Empty list, review {results}")
        return []
    

    try:
        final_output_msg = np.concatenate(results).ravel().tolist()

    except ValueError as e:
        print (f"Error concatenating: {e}")
        return []
    
    return final_output_msg

# Converts and replaces to lowercase to clean response up and standardize. Applicable to ones that are in dataframes.
def clean_model_resp(response_array):

    response_df = pd.DataFrame(response_array).replace(["", " "], np.nan)
    response_df = response_df.dropna(subset=["val1", "val2"])

    for i, value in response_df["val1"].items():
        try:
            response_df.at[i, "val1"] = lowercase_string(value)
        except AttributeError as e:
            print (f"Error {e} at index {i}")

    
    return response_df