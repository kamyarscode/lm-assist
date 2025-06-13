# Set up chat API routes.
from flask import session
from collections import deque


def get_chat_history():
    """Get chat history from session as a deque."""
    
    return deque(session.get('chat_history', []), maxlen=10)

def clear_chat_history():
    """Clear the chat history stored in the session."""
    
    session['chat_history'] = []
    return session['chat_history']

def add_to_chat_history(chat_history: deque, user_input, llm_response):

    """
    Adds a user input and bot response to the chat history.
    
    Parameters:
    - user_input: The input from the user.
    - llm_response: The response from the language model.
    - chat_history: The deque that holds the chat history.
    
    Returns:
    - The entire chat history after adding the new entry.
    """
    # Ensure chat_history is a deque
    if not isinstance(chat_history, deque):
        raise TypeError("chat_history must be a deque")

    # Add user input and model response pairs to chat history. 
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": llm_response})

    return chat_history

