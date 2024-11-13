import logging
from pathlib import Path
import json

# Set up logging

# Load json configs.
with open (Path('./params.json'), 'r') as json_config_file:
    project_config = json.load(json_config_file)
    json_config_file.close()

    