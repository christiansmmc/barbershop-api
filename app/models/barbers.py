from . import db


class Barbers(db.Model):
    __tablename__ = "barbers"

    id = db.Column(db.Integer, primary_key=True)
    barber_shop_id = db.Column(
        db.Integer,
        db.ForeignKey("barber_shop.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    name = db.Column(db.String(40), nullable=False, unique=False)
    user_type = db.Column(db.String(30), nullable=False, unique=False)
    service_list = db.relationship("Services", backref="barbers")