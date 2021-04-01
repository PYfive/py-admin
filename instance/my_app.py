#!/usr/bin/python
# coding=utf-8
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# create and configure the app
'''
__name__ 是当前 Python 模块的名称。应用需要知道在哪里设置路径， 使用 __name__ 是一个方便的方法。
instance_relative_config=True 告诉应用配置文件是相对于 instance folder 的相对路径。
实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统。
'''
app = Flask(__name__, instance_relative_config=True)

# Flask-SQLAlchemy 的相关配置项  文档地址:http://www.pythondoc.com/flask-sqlalchemy/config.html
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config["JWT_COOKIE_SECURE"] = False  # 生产环境设为因设为True
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in your code!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)
db = SQLAlchemy(app)

