# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.path.append("../../")
from paymax.config import PaymaxConfig
from ApiResource import *
import json

class Charge(object):

    def __init__(self):
        pass

    @classmethod
    def create(cls,body):
        #将body转成json对象
        body = json.dumps(body)

        #请求地址
        uri = str(PaymaxConfig.CREATE_CHARGE)
        return ApiResource.request(uri=uri,body=body)

    @classmethod
    def retrieve(cls,chargeId):
        uri = PaymaxConfig.CREATE_CHARGE + '/' + chargeId
        if not chargeId:
            return 'chargeId can not be blank.'
        return ApiResource.request(uri)