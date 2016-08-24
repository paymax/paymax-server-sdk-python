# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import uuid
import time

#生成一次性随机串
def generate_uuid():
    nonce = str(uuid.uuid1()).replace('-','')
    return nonce

def generate_timestamp():
    timestamp = "%d" % (time.time() * 1000)
    return timestamp