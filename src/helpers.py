from server.ollama import client

def return_client_version():
    response = client.heartbeat()

    return response