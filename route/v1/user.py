#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint, request, g
from instance.my_app import db
from service.user import info_service
from tools.pesponse import Constant, resp_wrapper as rw
from flask_jwt_extended import jwt_required, get_jwt_identity

user = Blueprint('user', __name__)


@user.before_request
def before_request():
    g.obj = 'user'


@user.teardown_request
def teardown_request(err):
    db.session.remove()


# 登录接口定义，参数获取
@user.route('/info', methods=["GET"])
@jwt_required()
def info():
    current_user = get_jwt_identity()
    err, result = info_service(current_user)
    if err:
        return rw(err, {})
    else:
        return rw(Constant.STATUS_OK, result)
