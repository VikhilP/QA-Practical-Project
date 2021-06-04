from flask import Flask
import random

app = Flask(__name__)

positions = ["QB","HB","FB","WR","T","G","C","TE",
    "CB","LB","DT","DE","SS","FS","K","KR","P"]

@app.route('/getpositions', methods= ["GET"])
# Player Position
def pos():
    return random.choice(positions)

