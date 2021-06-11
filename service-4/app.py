from flask import redirect, url_for, request, jsonify, Flask
import random, requests

app = Flask(__name__)

@app.route('/round', methods = ['GET', 'POST'])
def calculatedraftround():
    draft_number = request.json["dnum"]
    position = request.json["pos"]

    # calculations done here so i dont have to do it on the front end
    for i in range (41):
        if draft_number/30 <=i:
            draft_round = i
            break

    round_pick = draft_number%30

    if round_pick == 0:
        round_pick = 30

    info = {"position": position, "draft_number": draft_number, "draft_round": draft_round, "round_pick": round_pick } 
    return jsonify(info)

if __name__=="__main__": app.run(port=5003, host='0.0.0.0', debug=True)  