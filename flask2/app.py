from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_bryan():
        return "Hello Bryan You're Cool"
if __name__ == "__main__":
        app.run()
