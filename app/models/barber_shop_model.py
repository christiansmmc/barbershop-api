from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Barber_shop(db.Model):
    __tablename__ = "barber_shop"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    cnpj = db.Column(db.String(14), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=True, unique=False)
    user_type = db.Column(db.String(30), nullable=False, unique=False)
    address_list = db.relationship("Address", uselist=False, backref="barber_shop")

    @property
    def password(self):
        raise TypeError("The password can`t be accessed")

    @password.setter
    def password(self, new_password):
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)