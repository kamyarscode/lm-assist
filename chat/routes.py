from flask import Blueprint, jsonify, request, session

from src.chat_utils import clear_chat_history, get_chat_history
from src.tools import chat_tool


chat_bp = Blueprint('chat', __name__, url_prefix='/api')

@chat_bp.route('/clearChat', methods=['POST'])
def clear_chat():
    resp = clear_chat_history()
    return jsonify({"status": "success", "data": resp})


@chat_bp.route('/chat', methods=['POST'])
def chat_func():
    # Get user input from the request
    user_input = request.json.get("message")


    if not user_input:
        return jsonify({"error": "Empty input"}), 400


    chat_tool_response = chat_tool(chat_history=get_chat_history(), input_txt=user_input)

    session['chat_history'] = chat_tool_response['chat_history']
    print ("Current chat history: ", session['chat_history'])

    # Set up session to store chat history.

    return jsonify(chat_tool_response)

