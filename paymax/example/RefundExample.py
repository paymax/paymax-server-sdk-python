# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.path.append("../../")
from paymax.model.Refund import *

def refund():
    body = {'amount':0.01,'description':u'金龙测试退款'}
    print u'申请退款接口返回', Refund.create('ch_fbf00e5e4df0a8a2d8595915',body)

def retrieve():
    chargeId = 'ch_8a09a6c239481545b56e621c'
    refundId = 're_8f504d26316654d2d549421f'
    print u'退款查询接口返回',Refund.retrieve(chargeId,refundId)

refund()
retrieve()

