from rosemary.auth.register import register_bp
from rosemary.auth.login import login_bp


def auth_register_blueprints(app):
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    # app.register_blueprint(auth_home_bp)
