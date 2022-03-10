## 涩涩 涩涩 涩涩

from flask import Flask
from rosemary.sex.sex_pic import sex_pic_bp


def sex_register_blueprints(app: Flask):
    app.register_blueprint(sex_pic_bp)
