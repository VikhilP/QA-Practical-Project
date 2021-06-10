from flask import Flask
import random

app = Flask(__name__)
#positions
positions = ["QB","HB","FB","WR","T","G","C","TE",
    "CB","LB","DT","DE","SS","FS","K","KR","P"]

@app.route('/getpositions', methods= ["GET"])
# Player Position
def pos():
    return random.choice(positions)

if __name__=="__main__": app.run(port=5001, host='0.0.0.0', debug=True)  

