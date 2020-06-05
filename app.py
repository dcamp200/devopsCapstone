from flask import Flask, request, jsonify
import subprocess
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/run", methods=["POST"])
def run_command():
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")
    command = json_payload["commandLine"]
    logging.debug(f"Executing {command}")
    process = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    LOG.info(process.stdout)
    return jsonify(str(process.stdout))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)  # specify port=80
