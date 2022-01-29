from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from rosemary.extension import db, res, generate_token
from rosemary.model import User

auth_login_bp = Blueprint('login', __name__, url_prefix='/api/auth')


@auth_login_bp.post("/login")
def login():
    mailbox = request.form.get("mailbox")
    password = request.form.get("password")
    if mailbox is None or password is None:
        return res(), 702
    user = User.query.get(mailbox)
    if user is None or not check_password_hash(pwhash=user.password, password=password):
        return res(), 700
    else:
        return res({"token": str(generate_token(mailbox))[2:-1]}), 200
