from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:password@34.105.162.197:3306/draft" # getenv("DATABASE_URI") # "sqlite:///data.db"
app.config['SECRET_KEY'] = "dfs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from application import routes