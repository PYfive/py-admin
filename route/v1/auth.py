#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request, g
from instance.my_app import db
from service.auth import login_service
from tools.pesponse import Constant, resp_wrapper as rw

auth = Blueprint('auth', __name__)


@auth.before_request
def before_request():
    g.obj = 'auth'


@auth.teardown_request
def teardown_request(err):
    db.session.remove()


# 登录接口定义，参数获取
@auth.route('/login', methods=["POST"])
def login():
    data = request.get_json(force=True)
    err, result = login_service(data['username'], data['password'])
    if err:
        return rw(err, {})
    else:
        return rw(Constant.STATUS_OK, result)
