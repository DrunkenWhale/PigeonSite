# from rosemary.auth.register import auth_register_bp
from rosemary.auth.login import auth_login_bp


def auth_register_blueprints(app):
    # app.register_blueprint(auth_register_bp)
    app.register_blueprint(auth_login_bp)
    # app.register_blueprint(auth_home_bp)
