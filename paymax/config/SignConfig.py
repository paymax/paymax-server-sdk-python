# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Paymax提供给商户的SecretKey
# 登录网站后查看
PAYRIGHT_SECRET_KEY="55970fdbbf10459f966a8e276afa86fa"

# 商户自己的私钥
# 样例 见 rsa_private_key.pem
PrivateKey = 'rsa_private_key.pem'

# Paymax提供给商户的公钥路径
# 登录网站后查看,把它保存到一个pem文件中
# 样例 见 paymax_rsa_public_key.pem
PaymaxPublicKey = 'rsa_public_key.pem'