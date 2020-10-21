from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    fullname = db.Column(db.String(128))
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255),nullable=False)
    role = db.Column(db.Integer(),nullable=False,default=0)
