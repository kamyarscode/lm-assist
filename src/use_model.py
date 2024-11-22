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

