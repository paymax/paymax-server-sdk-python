# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.path.append("../../")
from paymax.config import PaymaxConfig
from paymax.config import SignConfig
from PaymaxUtil import *
from paymax.sign import RSASign
from paymax.exception import exception
import requests




#设置需要发送的HTTP头信息
def setHeader():
    nonce = generate_uuid()
    timestamp = generate_timestamp()
    header = {
        "Host":"www.paymax.cc",
        "ContentType":"application/json;charset=utf-8",
        "nonce":nonce,
        "timestamp":timestamp,
        "Authorization":SignConfig.PAYRIGHT_SECRET_KEY
    }
    return header


#签名数据
def to_sign_data(header,method,uri,body=''):

    #组装签名数据，顺序必须一致
    nonce = header['nonce']
    timestamp = header['timestamp']
    Authorization = header['Authorization']
    #query目前4个接口都未空，预留参数
    query_string = ''
    sign_data = method+'\n'+uri+'\n'+query_string+'\n'+nonce+'\n'+timestamp+'\n'+Authorization+'\n'+ body

    #通过私钥签名
    sign_data = RSASign.RSASign.rsa_sign(data=sign_data)
    return sign_data

#验签数据
def to_verify_data(header,response_data):

    #验签的sign
    sign = header['sign']

    #验签的各个字段，顺序要一致
    nonce = header['nonce']
    timestamp = header['timestamp']
    Authorization = header['authorization']
    verify_data = nonce+'\n'+timestamp+'\n'+Authorization+'\n'+response_data

    verify_result = RSASign.RSASign.rsa_verify(verify_data,sign)
    print '验签结果》》 ',verify_result
    if not verify_result:
        raise exception.InvalidResponseException("Invalid Response.[Response Data And Sign Verify Failure.]")

    if SignConfig.PAYRIGHT_SECRET_KEY != Authorization:
        raise exception.InvalidResponseException("Invalid Response.[Secret Key Is Invalid.]")

    if float(generate_timestamp()) - float(timestamp) >= 2*60*1000:
        raise exception.InvalidResponseException("Invalid Response.[Response Time Is Invalid.]")


#get请求方法
def get(uri):
    header = setHeader()
    #签名数据
    sign_data = to_sign_data(header=header,method='get',uri=uri)

    #组装HTTP Header
    request_header = {'Host':header['Host'],
                      "Content-Type":"application/json;charset=utf-8",
                      'Authorization':header['Authorization'],
                      'nonce':header['nonce'],
                      'timestamp':header['timestamp'],
                      'sign':sign_data}

    url = PaymaxConfig.PAYRIGHT_SERVER_URL + uri

    try:
        r = requests.get(url=url,headers=request_header)
        print u'请求地址：',r.url
    except Exception as e:
        print u'请求失败：',e

    #验签
    if r.status_code < 400:
        to_verify_data(r.headers,r.text)
    return r.text

#post请求方法
def post(uri,body):

    if uri == '':
        raise exception.AuthorizationException("Access url is empty")

    #初始化header
    header = setHeader()

    #签名数据
    sign_data = to_sign_data(header=header,method='post',uri=uri,body=body,)

    #组装HTTP Header
    request_header = {'Host':header['Host'],
                      "Content-Type":"application/json;charset=utf-8",
                      'Authorization':header['Authorization'],
                      'nonce':header['nonce'],
                      'timestamp':header['timestamp'],
                      'sign':sign_data}

    url = PaymaxConfig.PAYRIGHT_SERVER_URL + uri

    try:
        #发送HTTP请求
        r = requests.post(url=url,data=body,headers=request_header)
        print u'请求地址：',r.url
    except Exception as e:
        print u'请求失败：',e

    #验签
    if r.status_code < 400:
        to_verify_data(r.headers,r.text)
    return r.text



