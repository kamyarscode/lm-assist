import json
import time

from flask import Flask, request
from server.ollama import ollama_health
from src.use_model import prompt_model
app = Flask(__name__)

# Test endpoint here.

@app.route('/api/test')
def test():
    input_str = "hello there"
    model_name = "llama3.2-instruct"
    result = prompt_model(input_str, short_model_name=model_name, type_of_task="test")

    data = {
        "result": result
    }

    return data

@app.route('/api/version')
def get_version():

    data = {
        "status": 200,
        "version": "0.1"
    }

    return data

@app.route('/')
def homepage():
        
    data = {
        "status": 200,
        "message": "App is running."
    }

    return data

# Return server client version
@app.route('/api/cv')
def get_client_version():
    
    data = ollama_health()

    return data

def main():
    app.run(port=7777, debug=False)
    print ("Server is running now.")

if __name__ == "__main__":

    main()