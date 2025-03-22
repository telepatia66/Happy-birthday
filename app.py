from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Happy 2nd Anniversary! ❤️</h1><p>Love you always!</p>"

if __name__ == "__main__":
    app.run(debug=True)
