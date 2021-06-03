from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQL_DATABASE_URI'] = "sqlite:///"
app.config['SECRET_KEY'] = "dfs"

from application import routes