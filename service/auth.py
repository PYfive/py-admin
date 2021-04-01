#!/usr/bin/python
# -*- coding:utf-8 -*-


from model.user import User
from tools.pesponse import Constant
from flask_jwt_extended import create_access_token


# 登录接口实现
def login_service(username, password):
    try:
        users = User.query.filter_by(username=username).first()
        if users is not None and users.password == password:
            token = create_access_token(identity=username)
            return None, {'token': token}
        else:
            return Constant.STATUS_NO_AUTH, None
    except BaseException as e:
        return Constant.STATUS_SERVER_ERROR, None
