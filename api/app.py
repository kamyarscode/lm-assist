import json
import time

from flask import Flask, request

app = Flask(__name__)

# Test endpoint here.

@app.route('/apt/test')
def test():
    
    return "This is test endpoint."