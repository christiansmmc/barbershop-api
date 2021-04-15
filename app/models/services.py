from . import db


class Services(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(40), nullable=False, unique=False)
    service_price = db.Column(db.String(4), nullable=False, unique=False)
    barber_id = db.Column(
        db.Integer,
        db.ForeignKey("barbers.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
