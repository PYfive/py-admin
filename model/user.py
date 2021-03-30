#!/usr/bin/python
# -*- coding:utf-8 -*-

from instance.my_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    nickname = db.Column(db.String(255), unique=True)

    def __init__(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname

    def __repr__(self):
        return '<User %r>' % self.username
