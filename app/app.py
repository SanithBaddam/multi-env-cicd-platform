from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/")
def index():
    return jsonify(service="delivery-reference", version="1.0"), 200
