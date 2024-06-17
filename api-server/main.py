from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")

def home():
    return "This is the home."

@app.route("/api/persona/create-persona")
def create_persona():
    pass

@app.route("/api/persona/update-persona")

def update_persona():
    pass

@app.route("/api/persona/delete-persona")

def delete_persona():
    pass

if __name__ == "__main__":
    app.run(debug=True)