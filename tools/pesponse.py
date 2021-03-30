#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
import decimal
from flask import Response, json


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime.time):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        '''
        elif isinstance(obj,ObjectId):
            return str(obj)
        '''
        return json.JSONEncoder.default(self, obj)


class Constant(object):
    STATUS_OK = ('1000', '成功')
    STATUS_SERVER_ERROR = ('1001', '服务器开小差了,请稍后重试')
    STATUS_ARGUMENT_ERROR = ('1002', '参数错误')
    STATUS_NO_AUTH = ('1004', '登录失败,用户名秘密错误')


def json_ify(data):
    """flask default jsonify function not surport datetime serialize
    """
    return Response(json.dumps(data, cls=APIEncoder), mimetype='application/json')


def resp_wrapper(cs_status, rval=None):
    return json_ify({'code': cs_status[0], 'msg': cs_status[1], 'data': rval})
