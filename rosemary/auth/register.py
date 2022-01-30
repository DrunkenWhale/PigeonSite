from flask import Blueprint, request
from rosemary.model import User
from werkzeug.security import generate_password_hash
from rosemary.extension import db, res

register_bp = Blueprint('register', __name__, url_prefix='/api/auth')


@register_bp.post("/register")
def register():
    mailbox = request.form.get("mailbox")
    password = request.form.get("password")
    username = request.form.get("username")
    user = User.query.get(mailbox)
    if user is None:
        if username is None or password is None or mailbox is None:
            return res(), 702
        else:
            password = generate_password_hash(password)
            user_ = User(mailbox=mailbox, name=username, password=password)
            db.session.add(user_)
            db.session.commit()
            return res(), 200
    else:
        return res(), 701
