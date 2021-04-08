#!/usr/bin/python
# -*- coding:utf-8 -*-
# 模块引入
from datetime import timedelta, timezone, datetime
from instance.my_app import app, jwt
from route.v1.auth import auth
from route.v1.user import user
from tools.pesponse import resp_wrapper as rw, Constant
from flask_jwt_extended import get_jwt, create_access_token, \
    set_access_cookies, get_jwt_identity

# python2 设置编码格式为utf-8  python3默认是utf-8
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')

app.register_blueprint(auth, url_prefix='/v1/auth')
app.register_blueprint(user, url_prefix='/v1/user')


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now()
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


# 过期令牌
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return rw(Constant.STATUS_TOKEN_EXPIRED, {})


# 无效令牌
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return rw(Constant.STATUS_TOKEN_INVALID, {})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
