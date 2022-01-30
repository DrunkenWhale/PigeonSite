from flask import Blueprint, request
from rosemary.extension import need_login, res
from os import getcwd, sep

upload_bp = Blueprint('upload', __name__, url_prefix='/api/file')

directory_path = getcwd() + sep + "repository" + sep


@upload_bp.post("/upload")
@need_login
def file_upload(mailbox):
    file = request.files['upload_file']
    filename = file.filename
    if ".." in filename or "/" in filename:
        return res(), 702
    else:
        file_path = str(User.query.filter_by(mailbox=mailbox).first()) + sep + filename
        return directory_path
