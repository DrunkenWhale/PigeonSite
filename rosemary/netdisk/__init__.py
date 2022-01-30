from flask import Flask
from rosemary.netdisk.upload import upload_bp

def netdisk_register_blueprints(app: Flask):
    app.register_blueprint(upload_bp)
