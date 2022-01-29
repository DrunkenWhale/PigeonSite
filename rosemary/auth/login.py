from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from rosemary.extension import db
from rosemary.model import User

auth_login_bp = Blueprint('login', __name__, url_prefix='/auth')


@auth_login_bp.post("/login")
def login():
    mailbox = request.form.get("mailbox")
    password = request.form.get("password")
    user = User.query.get(mailbox)
    if user is None or not check_password_hash(pwhash=user.password, password=password):
        return "", 701
