from flask import Flask, jsonify, request

app = Flask(__name__)

pets = []

@app.route("/")
def main():
    return "The app is up!"

@app.route("/add_pet", methods=["POST"])
def add_pet():
    pets.append(request.json)
    return {"msg": "success"}

@app.route("/search")
def query():
    min_age = int(request.args.get("min_age", 0))
    max_age = int(request.arg.get("max_age", 9999))
    name = request.args.get("name", None)

    if name != None: 
        return jsonify(
            [
                pet
                for pet in pets if min_age <= pet["age"] <= max_age
                and pet["name"].lower() == name.lower()
            ]
        )
    else:
        return jsonify([pet for pet in pets if min_age <= pet["age"] <= max_age])

if __name__ == "__main__":
    app.run(debug = True)