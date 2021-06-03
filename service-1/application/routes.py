from flask import render_template, request, url_for, Response, jsonify, json
from application import app, db
from application.models import draft, GenerateDraft
from sqlalchemy import desc
import random

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = GenerateDraft()
    if request.method == 'GET':
        return render_template('index.html', title='Draft', form = form)
