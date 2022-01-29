from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, Response
from datetime import datetime, timedelta
import jwt

db: SQLAlchemy = SQLAlchemy()


def res(data=None):
    return jsonify(data)
