# LM Assist
General purpose use of language models to perform tasks, but the direction of the project could also go in other directions.
A good use case for this is being able to interact with these models via API while not necessarily needing to host the models yourself. You can use docker to build this system on a server and use their compute/storage. 

2 Use cases for this will be syncing large files, specifically code to understand what happens inside them, and parsing PDFs. 

## Project Structure

### API
The API directory will house the interface to the language model and serve as the communication layer.
### Server
This directory will pertain to any of the language model engine/work that needs to be done.
### src
This directory holds the core source for most of the repo.
### utils
This directory has helper functions to assist with anything needed for computation.

## Procedure

## How To Run

## Endpoints

### Dockerized

### Without Docker
Follow the instructions on [Ollama's page](https://ollama.com/download) to install on your machine.

## Tools/Software
Ollama - Model hosting server.  
Conda - virtual environment management.  
Docker - Build images and host anywhere.  
Flask - API Development and Management.  

## Installation
Run the install script by going into the project root directory. Make sure permissions are set such that it is executable. `./install.sh` should start things up. The installation will build a docker image and container on your local machine that contains the API.

## TODO:
- Add code recognition
    - use old commits for context when writing new sections of code