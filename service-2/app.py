from flask import Flask
import random

app = Flask(__name__)


@app.route('/', methods= ["GET"])
# Player Position
def pos():
    positions = ["QB","HB","FB","WR","T","G","C","TE",
    "CB","LB","DT","DE","SS","FS","K","KR","P"]

    player_position = random.choice(positions)
    return player_position

