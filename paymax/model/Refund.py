# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.path.append("../../")
from paymax.config import PaymaxConfig
from ApiResource import *
import json



class Refund(object):

    @classmethod
    def create(cls,chargeId,body):
        if not chargeId:
            return 'chargeId can not be blank.'
        #将body转成jon对象
        body = json.dumps(body)
        uri = PaymaxConfig.CREATE_CHARGE + '/' + chargeId + '/refunds'
        return ApiResource.request(uri,body)

    @classmethod
    def retrieve(cls,chargeId,refundId):
        if not chargeId or not refundId:
            return 'chargeId or refundId can not be blank.'
        uri = PaymaxConfig.CREATE_CHARGE + '/' + chargeId + '/refunds/' + refundId
        return ApiResource.request(uri)

