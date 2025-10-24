from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = os.environ.get("DATA_FILE", "sample_data.json")

def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)

@app.route("/")
def home():
    return "Welcome to the Docker Learning Project!"

@app.route("/data", methods=["GET"])
def get_data():
    data = load_data()
    return jsonify(data)

@app.route("/data", methods=["POST"])
def add_data():
    new_item = request.json
    data = load_data()
    data.append(new_item)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return jsonify({"message": "Data added successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
