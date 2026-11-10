from flask import Flask, jsonify
import os
app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "1")
ENV = os.environ.get("APP_ENV", "DEV")
@app.route("/")
def home():
    return jsonify(service="backend", env=ENV, version=VERSION, message="Hello from Backend API")
@app.route("/api/data")
def data():
    return jsonify(service="backend", env=ENV, version=VERSION, items=["ECR","EKS","Istio"], status="ok")
@app.route("/health")
def health():
    return jsonify(status="healthy"), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
