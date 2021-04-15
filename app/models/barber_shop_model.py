from . import db


class Barber_shop(db.Model):
    __tablename__ = "barber_shop"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    cnpj = db.Column(db.String(14), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False, unique=False)
    user_type = db.Column(db.String(30), nullable=False, unique=False)
    address_list = db.relationship("Address", uselist=False, backref="barber_shop")
