from flask import Flask, send_from_directory
from flask_cors import CORS
from rosemary.extension import db
from rosemary.auth import auth_register_blueprints
from rosemary.netdisk import netdisk_register_blueprints
from rosemary.config import Config
import os


# I'm the only user
# so I decide to use session instead token  :p
# cors... cookie... yikes forever..
def create_app(name=__name__):
    app = Flask(name)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    CORS(app, origins='*')
    return app


def register_blueprints(app):
    auth_register_blueprints(app)
    netdisk_register_blueprints(app)


def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
