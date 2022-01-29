from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, Response
from datetime import datetime, timedelta
import jwt

db: SQLAlchemy = SQLAlchemy()


def make_json_response(
        status=0,
        message=None,
        data=None
):
    response = jsonify({
        "status": status,
        "message": message,
        "data": data,
    })
    return response
