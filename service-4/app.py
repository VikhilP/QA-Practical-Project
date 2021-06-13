from flask import redirect, url_for, request, jsonify, Flask
import random, requests

app = Flask(__name__)

@app.route('/round', methods = ['GET', 'POST'])
def calculatedraftround():
    draft_number = request.json["dnum"]
    position = request.json["pos"]

    # calculations done here so i dont have to do it on the front end
    for i in range (8):
        if draft_number/32 <=i:
            draft_round = i
            break
        # elif draft_number/32 <=2:
        #     draft_round = 2
        # elif draft_number/32 <=3:
        #     draft_round = 3
        # elif draft_number/32 <=4:
        #     draft_round = 4
        # elif draft_number/32 <=5:
        #     draft_round = 5
        # elif draft_number/32 <=6:
        #     draft_round = 6
        # elif draft_number/32 <=7:
        #     draft_round = 7

    round_pick = draft_number%32

    if round_pick == 0:
        round_pick = 32

    info = {"position": position, "draft_number": draft_number, "draft_round": draft_round, "round_pick": round_pick } 
    return jsonify(info)

if __name__=="__main__": app.run(port=5003, host='0.0.0.0', debug=True)  