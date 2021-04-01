#!/usr/bin/python
# -*- coding:utf-8 -*-

from model.user import User


# 登录接口实现
def info_service(current_user):
    users = User.query.filter_by(username=current_user).first()
    return None, {
        'username': users.username,
        'nickname': users.nickname,
    }
