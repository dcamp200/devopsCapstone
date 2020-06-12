from flask import Flask, request, jsonify
import subprocess
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/", methods=["GET"])
def run_command():    
    return 'Hello World!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)  # specify port=9000
