from flask import Blueprint, request, send_file
from rosemary.model import User
from rosemary.extension import need_login, res
from os import getcwd, sep, path, mkdir, listdir
import datetime

download_bp = Blueprint('download', __name__, url_prefix='/api/file')

dir_path = getcwd() + sep + "repository" + sep


@download_bp.get("/list")
@need_login
def file_list(mailbox):
    result_list = []
    user_id = str(User.query.filter_by(mailbox=mailbox).first().id)
    user_dir_path = dir_path + user_id + sep
    for file in listdir(user_dir_path):
        result_list.append({
            "file_name": file,
            "file_size": path.getsize(user_dir_path + file),
            "file_time": path.getmtime(user_dir_path + file)
        })
    return res(result_list), 200


@download_bp.get("/download")
@need_login
def file_download(mailbox):
    filename = request.args.get("file_name", None)
    user_id = str(User.query.filter_by(mailbox=mailbox).first().id)
    if filename is None:
        return res(), 702
    file_path = dir_path + user_id + sep + filename
    return send_file(file_path)
