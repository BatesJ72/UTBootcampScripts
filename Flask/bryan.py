from flask import Flask, jsonify

app = Flask(__name__)

tonight = [
    {"activity": "Watch Supernatural", "duration": "3 episodes"},
    {"activity": "Watch Z-Nation", "duration": "end of series"},
    {"activity": "Play with puppies", "duration": "anytime, always"},
    {"activity": "Eat snacks", "duration": "eat some, then eat some more"},
    {"activity": "Have a drink", "duration": "I think there's whiskey left in that bottle"},
    {"activity": "Play video games", "duration": "Until you get tired of me making us die"},
    {"activity": "Have sex", "duration": "all night long"}
]


@app.route("/")
def home():
    return "Hello, Bryan!"

@app.route("/did_you_know")
def know():
    return "I love you!"

@app.route("/tonight")
def menu():
    return jsonify(tonight)

@app.route("/activity/<thing>")
def show(thing):
    return jsonify([t for t in tonight if t["activity"].lower() == thing.lower()])

@app.route("/duration/<length>")
def show_by_age(length):
    return jsonify([l for l in tonight if l["duration"].lower() == length.lower()])

if __name__ == "__main__":
    app.run(debug = True)