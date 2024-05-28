
# main.py

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

pet = {
    "name": "No Name",
    "description": "No Description",
    "tricks": [],
    "hunger": 50,
    "boredom": 50,
    "img": "pet-default.png"
}

@app.route("/")
def index():
    return render_template("index.html", pet=pet)

@app.route("/pet", methods=["POST"])
def create_pet():
    data = request.get_json()
    pet["name"] = data["name"]
    pet["description"] = data["description"]
    return jsonify(pet)

@app.route("/pet/action", methods=["GET"])
def perform_action():
    action = request.args.get("action")
    if action == "feed":
        pet["hunger"] = max(0, pet["hunger"] - 10)
    elif action == "play":
        pet["boredom"] = max(0, pet["boredom"] - 10)
    elif action == "describe":
        pet["description"] = request.args.get("description")
    elif action == "learn":
        trick = request.args.get("trick")
        pet["tricks"].append(trick)
    return jsonify(pet)

if __name__ == "__main__":
    app.run(debug=True)
