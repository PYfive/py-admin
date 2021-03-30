#!/usr/bin/python
# -*- coding:utf-8 -*-
# 模块引入
from instance.my_app import app
from route.v1.user import user

# python2 设置编码格式为utf-8  python3默认是utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app.register_blueprint(user, url_prefix='/v1/user')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
