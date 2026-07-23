import os

from flask import Flask, jsonify

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")


@app.get("/")
def home():
    return "Welcome to CloudMart Solutions!"


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


def calculate_total(price, quantity):
    return price * quantity


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
