from flask import Flask
from rosemary.netdisk.upload import upload_bp
from rosemary.netdisk.download import download_bp
from rosemary.netdisk.delete import delete_bp


def netdisk_register_blueprints(app: Flask):
    app.register_blueprint(upload_bp)
    app.register_blueprint(download_bp)
    app.register_blueprint(delete_bp)
