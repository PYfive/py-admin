#!/usr/bin/python
# -*- coding:utf-8 -*-

from model.user import User
from tools.pesponse import Constant


# 登录接口实现
def user_service(username, password):
    users = User.query.filter_by(username=username).first()
    if users.password == password:
        return None, {'nickname': users.nickname}
    else:
        return Constant.STATUS_NO_AUTH, None
