from flask import Flask


def init_app(app: Flask):
    from app.views.appointments_views import bp_appointments

    app.register_blueprint(bp_appointments)

    from app.views.barber_shop_view import bp_barber_shop

    app.register_blueprint(bp_barber_shop)

    from app.views.client_view import bp_client

    app.register_blueprint(bp_client)

    from app.views.address_view import bp_address

    app.register_blueprint(bp_address)