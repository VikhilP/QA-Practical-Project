from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/getpickorder', methods= ["GET"])
# Draft pick number
def pick():
    return jsonify(random.randint(1,224))