import json
import time

from flask import Flask, request

app = Flask(__name__)

# Test endpoint here.

@app.route('/api/test')
def test():
    
    return "This is test endpoint."

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

# Return server client version
@app.route('/api/cv')
def get_client_version():

    response, status, version = return_client_version()
    data = {
        "status": status,
        "message": response,
        "llm_server_version": version
    }