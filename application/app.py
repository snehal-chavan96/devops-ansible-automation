from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Ansible Automated Deployment!",
        "application": "DevOps Flask Application",
        "status": "Running Successfully",
        "deployment": "Amazon Linux 2023 EC2",
        "managed_by": "Ansible"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "timestamp": datetime.utcnow().isoformat()
    })


if __name__ == "__main__":
    app.run()
