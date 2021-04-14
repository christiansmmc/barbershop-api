from . import db


class Appointments(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    barber_id = db.Column(
        db.Integer, db.ForeignKey("barbers.id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False, unique=False
    )
    barber_shop_id = db.Column(
        db.Integer, db.ForeignKey("barber_shop.id"), nullable=False, unique=False
    )
    services_id = db.Column(
        db.Integer, db.ForeignKey("services.id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False, unique=False
    )
    client_id = db.Column(
        db.Integer, db.ForeignKey("client.id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False, unique=False
    )
    date_time = db.Column(db.String(20), nullable=False, unique=False)