from application import db
from flask_wtf import FlaskForm
from wtforms import SubmitField

class draft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(10), nullable = False)
    pick = db.Column(db.Integer, nullable = False)
    # school = db.Column(db.String(100))
    # name = db.Column(db.String(100))

class GenerateDraft(FlaskForm):
    submit = SubmitField('Draft Player')