import json
import time

from flask import Flask, request
from server.ollama import ollama_health
from src.use_model import prompt_model
app = Flask(__name__)

# Test endpoint here.

@app.route('/api/test')
def test():
    input_str = "The National Aeronautics and Space Administration (NASA /ˈnæsə/) is an independent agency of the US federal government responsible for the United States' civil space program, aeronautics research and space research. Established in 1958, it succeeded the National Advisory Committee for Aeronautics (NACA) to give the US space development effort a distinct civilian orientation, emphasizing peaceful applications in space science. It has since led most of America's space exploration programs, including Project Mercury, Project Gemini, the 1968–1972 Apollo Moon landing missions, the Skylab space station, and the Space Shuttle. Currently, NASA supports the International Space Station (ISS) along with the Commercial Crew Program, and oversees the development of the Orion spacecraft and the Space Launch System for the lunar Artemis program. NASA's science division is focused on better understanding Earth through the Earth Observing System; advancing heliophysics through the efforts of the Science Mission Directorate's Heliophysics Research Program; exploring bodies throughout the Solar System with advanced robotic spacecraft such as New Horizons and planetary rovers such as Perseverance; and researching astrophysics topics, such as the Big Bang, through the James Webb Space Telescope, the four Great Observatories, and associated programs. The Launch Services Program oversees launch operations for its uncrewed launches."
    model_name = "llama3.2-instruct"
    result = prompt_model(input_str, short_model_name=model_name, type_of_task="summarize")

    # data = {
    #     "result": result
    # }

    return result

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