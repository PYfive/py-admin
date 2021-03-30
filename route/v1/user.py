#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request, g, Response
from instance.my_app import db
from service.user import user_service
from tools.pesponse import Constant, resp_wrapper as rw

user = Blueprint('user', __name__)


@user.before_request
def before_request():
    g.obj = 'user'


@user.teardown_request
def teardown_request(err):
    db.session.remove()


# 登录接口定义，参数获取
@user.route('/login', methods=["POST"])
def login():
    data = request.get_json(force=True)
    err, result = user_service(data['username'], data['password'])
    if err:
        return rw(err, {})
    else:
        return rw(Constant.STATUS_OK, result)
