from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! First time trying flask this is kinda cool..!"

if __name__ == "__main__":
    app.run(debug=True)