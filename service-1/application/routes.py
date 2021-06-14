from flask import render_template, request, url_for, Response, jsonify, json
from application import app, db
from application.models import draft, GenerateDraft
from sqlalchemy import desc
import random, requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = GenerateDraft()

    if form.validate_on_submit():
    #if request.method == "POST":
        draft_number = requests.get('http://service_3:5002/getpickorder').json()
        position = requests.get('http://service_2:5001/getpositions').text

        senditems = {"dnum": draft_number, "pos": position}
        info = requests.post("http://service_4:5003/round", json=senditems).json()

        new_rookie = draft(
            position = info["position"],
            pick = info["draft_number"]
            )
        db.session.add(new_rookie)
        db.session.commit()
        
        last_picks = draft.query.order_by(desc(draft.id)).limit(5).all()
        
        return render_template('index.html', title='SHOW UP PLEASE', form = form, info=info, last_picks = last_picks)
    return render_template('index.html', title='Draft', form = form)
