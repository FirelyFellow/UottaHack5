# app.py
from flask import Flask, request, jsonify, make_response
import json

import GPT_API
import Webscraper

app = Flask(__name__)


def _find_next_id():
    return max(message["id"] for message in messages) + 1

@app.route("/messages", methods=['GET', 'POST', 'OPTIONS'])
def add_message():

    messages = {}

    if request.method == 'POST':
        data = request.data.decode()
        messages["summary"] = GPT_API.get_summary(Webscraper.scrape(data))

    resp = make_response(jsonify(messages), 200)

    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization'

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)