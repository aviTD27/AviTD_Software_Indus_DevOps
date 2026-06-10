import os
from flask import Flask, jsonify

app = Flask(__name__)

INSTANCE_NAME = os.environ.get("INSTANCE_NAME", "unknown")
VERSION = os.environ.get("VERSION", "unknown")

@app.route("/version")
def version():
    return jsonify({
        "instance": INSTANCE_NAME,
        "version": VERSION
    })
