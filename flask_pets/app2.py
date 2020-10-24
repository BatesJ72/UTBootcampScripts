from flask import Flask, jsonify

app = Flask(__name__)

pets = [
    {"name": "Suki", "age": 1},
    {"name": "Lacey", "age": 4},
    {"name": "Toby", "age": 9},
    {"name": "Winston", "age": 3},
    {"name": "Shank", "age": 2},
    {"name": "Shiv", "age": 2},
    {"name": "Max", "age": 8},
]


@app.route("/")
def home():
    return "Hello, Jessica!"

@app.route("/all_pets")
def all_pets():
    return jsonify(pets)

# Get info on specific pets
@app.route("/pets/<pet_name>")
def show(pet_name):
    return jsonify([pet for pet in pets if pet["name"].lower() ==  pet_name.lower()])

@app.route("/age/<target_age>")
def show_by_age(target_age):
    return jsonify([pet for pet in pets if pet["age"] == int(target_age)])

@app.route("/api/age")
def query_by_age():
    min_age = request.args.get("min_age")
    max_age = request.args.get("max_age")
    return {
        "min_age": min_age, 
        "max_age": max_age
    }

if __name__ == "__main__":
    app.run(debug = True)