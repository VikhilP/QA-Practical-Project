from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/getpickorder', methods= ["GET"])
# Draft pick number
def pick():
    return jsonify(random.randint(1,1200))

if __name__=="__main__": app.run(port=5002, host='0.0.0.0', debug=True)  