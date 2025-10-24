# Import necessary modules
from flask import Flask, jsonify, request  # Flask framework for web app
import json  # For reading/writing JSON data
import os    # For accessing environment variables

# Create a Flask application instance
app = Flask(__name__)

# Get the data file path from environment variable, default to "sample_data.json"
DATA_FILE = os.environ.get("DATA_FILE", "sample_data.json")

# Function to load JSON data from the data file
def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)

# Define a route for the home page
@app.route("/")
def home():
    return "Welcome to the Docker Learning Project!"

# Define a route to GET data from the JSON file
@app.route("/data", methods=["GET"])
def get_data():
    data = load_data()  # Load the current data
    return jsonify(data)  # Return it as JSON response

# Define a route to POST new data to the JSON file
@app.route("/data", methods=["POST"])
def add_data():
    new_item = request.json  # Get JSON data from request body
    data = load_data()       # Load current data
    data.append(new_item)    # Append the new item
    # Save updated data back to the file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    # Return a success message with HTTP status 201
    return jsonify({"message": "Data added successfully"}), 201

# Run the Flask app when executing this script directly
if __name__ == "__main__":
    # Listen on all interfaces, port 5000, with debug mode enabled
    app.run(host="0.0.0.0", port=5000, debug=True)
