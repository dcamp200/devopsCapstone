from flask import Flask, json
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/", methods=["GET"])
def run_command():    
    return '''
           <!DOCTYPE html>
           <html><body style="background-color:blue;">
           <p style="color:white;">Hello World!</p>
           </body></html>
           '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)  # specify port=9000
