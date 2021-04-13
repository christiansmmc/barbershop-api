from flask import Flask


def init_app(app: Flask):
    from app.views.appointments_views import bp_appointments
    app.register_blueprint(bp_appointments)

    from app.views.barber_shop_view import bp_barber_shop
    app.register_blueprint(bp_barber_shop)
