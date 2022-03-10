# 随机涩图
from flask import Blueprint, send_file, request
from os import getcwd, sep, path, listdir
from rosemary.extension import res
from rosemary.extension import need_login
from multiprocessing import Process
import random
import requests

sex_pic_bp = Blueprint('sex_pic', __name__, url_prefix='/api/sex')

random_sex_pic_url = "https://api.lolicon.app/setu/v2"

reverse_proxy = "http://45.140.88.20:3777/"

directory_path = getcwd() + sep + "sex_picture_repository" + sep

if not path.exists(directory_path):
    mkdir(directory_path)


def walk(obj):
    url = obj["urls"]["original"]
    res = requests.post(reverse_proxy,
                        headers={
                            "Authorization": "Bearer 9cdd8706-9007-4fc1-9783-25102cc7605d"
                        },
                        data={
                            "URL": url
                        })
    f = open(directory_path + obj["title"] + ".jpg", "wb+")
    f.write(res.content)
    f.close()


@sex_pic_bp.post("/expand/")
@need_login
def expend_sex_picture_repository(mailbox):
    thread_list = []
    r = requests.get(random_sex_pic_url + "?num=7")
    for obj in r.json()["data"]:
        thread = Process(target=walk, args=(obj,))
        thread_list.append(thread)
        thread.start()
    for i in thread_list:
        i.join()
    return res(), 200


@sex_pic_bp.post("/")
@need_login
def get_random_sex_picture_name(mailbox):
    pic_list = listdir(directory_path)
    size = len(pic_list)
    pic_name = pic_list[random.randint(0, size - 1)]
    return res({
        "pic": pic_name
    }), 200


@sex_pic_bp.get('/')
def get_random_sex_picture():
    name = request.args.get("pic")
    if name is None:
        return "", 703
    if path.exists(directory_path + sep + name):
        return send_file(directory_path + sep + name)
    else:
        return "", 703
