# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.path.append("../../")
sys.setdefaultencoding("utf-8")
from paymax.util.HttpUtil import *
from paymax.model.Charge import *
from paymax.config import PaymaxConfig
import json



def changeExample():

    #请求参数
    body = {'order_no':generate_uuid(),
            'amount':0.1,
            'subject':'测试subject',
            'body':'测试body',
            'channel':'alipay_app',
            'app':'%s' % PaymaxConfig.PAYRIGHT_APP_KEY,
            'client_ip':'127.0.0.1',
            'currency':'CNY',
            'description':'description'}

    response = Charge.create(body)
    print u'下单接口返回:\n',response

    global chargeId
    chargeId = json.loads(response)['id']

def retrieve(chargeId = ''):
    print u'查询接口返回',Charge.retrieve(chargeId)

changeExample()
retrieve(chargeId=chargeId)


