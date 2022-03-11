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

sex_pic_directory_path = getcwd() + sep + "sex_picture_repository" + sep

if not path.exists(sex_pic_directory_path):
    mkdir(sex_pic_directory_path)


def walk(obj):
    url = obj["urls"]["original"]
    res = requests.post(reverse_proxy,
                        headers={
                            "Authorization": "Bearer 9cdd8706-9007-4fc1-9783-25102cc7605d"
                        },
                        data={
                            "URL": url
                        })
    f = open(sex_pic_directory_path + obj["title"] + ".jpg", "wb+")
    f.write(res.content)
    f.close()


@sex_pic_bp.put("/")
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
def get_sex_picture_name(mailbox):
    is_random = request.form.get("random")
    if is_random is not None:
        pic_list = listdir(sex_pic_directory_path)
        size = len(pic_list)
        pic_name = pic_list[random.randint(0, size - 1)]
        return res({
            "pic": pic_name
        }), 200
    else:
        return res({"pic_list": listdir(sex_pic_directory_path)})


@sex_pic_bp.get('/')
async def get_random_sex_picture():
    name = request.args.get("pic")
    if name is None:
        return "", 702
    if path.exists(sex_pic_directory_path + sep + name):
        return send_file(sex_pic_directory_path + sep + name)
    else:
        return "", 703
