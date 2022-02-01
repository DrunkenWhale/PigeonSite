from flask import Blueprint, request
from rosemary.model import User
from rosemary.extension import need_login, res
from os import getcwd, sep, path, mkdir

upload_bp = Blueprint('upload', __name__, url_prefix='/api/file')

directory_path = getcwd() + sep + "repository" + sep

if not path.exists(directory_path):
    mkdir(directory_path)


@upload_bp.post("/upload")
@need_login
def file_upload(mailbox):
    file = request.files['upload_file']
    filename = file.filename
    if ".." in filename or "/" in filename:
        return res(), 702
    else:
        user_prefix = str((User.query.filter_by(mailbox=mailbox).first()).id)
        file_path = user_prefix + sep + filename
        if not path.exists(directory_path + user_prefix):
            mkdir(directory_path + user_prefix)
        file.save(directory_path + file_path)
        return res(), 200
