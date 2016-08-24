# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.path.append("../../")
from paymax.util import HttpUtil
from paymax.config import SignConfig
from paymax.exception import exception



def _validateParams():
    if not SignConfig.PAYRIGHT_SECRET_KEY:
        raise exception.AuthorizationException("Secret key can not be blank.")

    if not SignConfig.PrivateKey:
        raise exception.AuthorizationException("The Path of RSA Private Key can not be blank.")

    if not SignConfig.PaymaxPublicKey:
        raise exception.AuthorizationException("The Path of Paymax Public Key can not be blank.")

class ApiResource(object):

    _validateParams()

    @classmethod
    def request(cls,uri,body=''):

        if not body:
            return HttpUtil.get(uri)
        else:
            return HttpUtil.post(uri,body)

