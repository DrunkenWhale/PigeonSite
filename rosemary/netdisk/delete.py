from flask import Blueprint, request
from rosemary.model import User
from rosemary.extension import need_login, res
from os import getcwd, sep, path, mkdir, listdir, remove
from shutil import copyfile

delete_bp = Blueprint('delete', __name__, url_prefix='/api/file')

dir_path = getcwd() + sep + "repository" + sep

recycle_path = getcwd() + sep + "recycle" + sep

if not path.exists(recycle_path):
    mkdir(recycle_path)


@delete_bp.delete("/delete")
@need_login
def file_delete(mailbox):
    filename = request.form.get("file_name", None)
    if filename is None:
        return res(), 702
    user_id = str(User.query.filter_by(mailbox=mailbox).first().id)
    source_file_path = dir_path + user_id + sep + filename
    if not path.exists(recycle_path+user_id):
        mkdir(recycle_path + user_id)
    destination_file_path = recycle_path + user_id + sep + filename
    copyfile(source_file_path,destination_file_path)
    remove(source_file_path)
    return res(), 200
