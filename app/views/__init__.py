from flask import Flask


def init_app(app: Flask):
    from app.views.appointments_views import bp_appointments

    app.register_blueprint(bp_appointments)