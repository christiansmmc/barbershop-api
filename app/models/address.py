from . import db


class Address(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    barber_shop_id = db.Column(db.Integer, db.ForeignKey("barber_shop.id"))
    state = db.Column(db.String(40), nullable=False, unique=False)
    city = db.Column(db.String(40), nullable=False, unique=False)
    street_name = db.Column(db.String(40), nullable=False, unique=False)
    building_number = db.Column(db.String(20), nullable=False, unique=False)
    zip_code = db.Column(db.String(20), nullable=False, unique=False)
