from application import db
from application.models import draft


db.drop_all()
db.create_all()