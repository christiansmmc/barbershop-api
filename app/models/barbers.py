from . import db


class Barbers(db.Model):
    __tablename__ = "barbers"

    id = db.Column(db.Integer, primary_key=True)
    barber_shop_id = db.Column(db.Integer, db.ForeignKey("barber_shop.id"))
    name = db.Column(db.String(40), nullable=False, unique=False)