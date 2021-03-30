#!/usr/bin/python
# -*- coding:utf-8 -*-


from model.user import User
from tools.pesponse import Constant
from flask_jwt_extended import create_access_token


# 登录接口实现
def login_service(username, password):
    users = User.query.filter_by(username=username).first()
    if users.password == password:
        access_token = create_access_token(identity=username)
        return None, {'nickname': users.nickname, 'access_token': access_token}
    else:
        return Constant.STATUS_NO_AUTH, None
