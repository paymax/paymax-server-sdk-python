# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64encode,b64decode
from paymax.config import SignConfig

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CERT_DIR = os.path.join(BASE_DIR, "sign")
PRIVATE_KEY = os.path.join(CERT_DIR, SignConfig.PrivateKey)
PUBLIC_KEY = os.path.join(CERT_DIR,SignConfig.PaymaxPublicKey)

class RSASign(object):


    @classmethod
    def rsa_sign(cls,data):
        priKey=open(PRIVATE_KEY,"r").read()
        # print '私钥:\n',priKey
        key = RSA.importKey(priKey)
        h = SHA.new(data)
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(h)
        return b64encode(signature)

    @classmethod
    def rsa_verify(cls,data,sign):
        pubKey = open(PUBLIC_KEY,"r").read()
        key = RSA.importKey(pubKey)
        h = SHA.new(data)
        verifier = PKCS1_v1_5.new(key)
        sign = b64decode(sign)
        return verifier.verify(h,sign)