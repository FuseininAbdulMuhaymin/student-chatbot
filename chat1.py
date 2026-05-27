import os
import uuid                          # generates a unique random ID for each chat session
from flask import Flask, jsonify, request
from flask_cors import CORS
from chatbot import send_message, get_history   # import only what we need from chat.py
                                             # start_chat is no longer needed from chat.py
                                             # because we now handle sessions here in app.py


# ============================================================
# SESSION STORAGE — moved here from chat.py
# ============================================================
# This dictionary stores ALL active chat sessions.
# It lives here at the top level so every route can access it.
#
# Structure:
# {
#   "abc-123": { "history": [] },
#   "xyz-456": { "history": [] },
# }
#
# Each KEY   = a unique session ID (like a student ID card)
# Each VALUE = that student's conversation history
chat_sessions = {}


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    CORS(app)

    @app.route('/hello')
    def hello():
        return jsonify({"message": "Flask is running!"})

    # ============================================================
    # ROUTE — start a new chat session
    # ============================================================
    @app.route('/chat/start', methods=['POST'])
    def route_start_chat():

        session_id = str(uuid.uuid4())
        # uuid4() creates a random unique ID like: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
        # str() converts it to a string so it can be used as a dictionary key

        chat_sessions[session_id] = {"history": []}
        # we create a new entry in the dictionary for this student
        # history starts empty — no messages yet

        return jsonify({"session_id": session_id}), 201
        # send the session_id back to the frontend
        # the frontend must save this and send it with every message

    # ============================================================
    # ROUTE — send a message
    # ============================================================
    @app.route('/chat/message', methods=['POST'])
    def route_send_message():

        data = request.get_json()
        # reads the JSON body the frontend sent

        if not data:
            return jsonify({"error": "No data was sent"}), 400

        session_id = data.get("session_id")
        if not session_id:
            return jsonify({"error": "session_id is required"}), 400

        if session_id not in chat_sessions:
            return jsonify({"error": "Session not found. Call /chat/start first"}), 404
            # checks our dictionary — if the session_id doesn't exist, reject the request

        user_message = data.get("message")
        if not user_message:
            return jsonify({"error": "message is required"}), 400
        
        chat_session = chat_sessions[session_id]
        # grab this student's session from the dictionary using their session_id

        reply = send_message(chat_session, user_message)
        # pass the session object and message to send_message in chat.py
        # send_message saves the message to history and returns Gemini's reply

        return jsonify({"reply": reply}), 200

    # ============================================================
    # ROUTE — get conversation history
    # ============================================================
    @app.route('/chat/history/<session_id>', methods=['GET'])
    def route_get_history(session_id):

        if session_id not in chat_sessions:
            return jsonify({"error": "Session not found"}), 404
            # session_id comes from the URL, check it exists in our dictionary

        return jsonify({"history": chat_sessions[session_id]["history"]}), 200
        # return the history list directly from the dictionary

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)