# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

messages = [
    {"id":1, "message": "hey yall!"},
]

def _find_next_id():
    return max(message["id"] for message in messages) + 1

@app.get("/messages")
def get_messages():
    return jsonify(messages)

@app.post("/messages")
def add_message():
    if request.is_json:
        message = request.get_json()
        message["id"] = _find_next_id()
        messages.append(message)
        return message, 201
    return {"error": "Request must be JSON"}, 415
