from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, Response
from datetime import datetime, timedelta
import jwt

db: SQLAlchemy = SQLAlchemy()


def res(data=None):
    if data is None:
        data = {}
    return jsonify(data)


def need_login(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        try:
            token_string = jwt.decode(token, key="priority_queue", algorithms="HS256")
            mailbox = token_string.get('mailbox', None)
        except:
            return res(), 702
        if mailbox is not None:
            return func(mailbox, *args, **kwargs)
        else:
            return res(), 777  # unknown error

    wrapper.__name__ = func.__name__
    return wrapper


def generate_token(mailbox):
    payload = {
        "exp": datetime.utcnow() + timedelta(days=7),
        "mailbox": mailbox,
    }
    msg = jwt.encode(payload=payload, key="priority_queue", algorithm="HS256")
    return msg
