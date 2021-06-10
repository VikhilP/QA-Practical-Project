from flask import Flask
import random

app = Flask(__name__)

#positions
positions = ["SS","1B","2B","3B","LF","RF","CF","DH","C"]


@app.route('/getpositions', methods= ["GET"])
# Player Position
def pos():
    return random.choice(positions)

if __name__=="__main__": app.run(port=5001, host='0.0.0.0', debug=True)  

