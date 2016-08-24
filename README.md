# paymax-server-sdk-python

这是Paymax提供的Python语言的Server SDK, 用于帮助用户对接[Paymax API](https://github.com/paymax/paymax-doc/blob/master/API%E6%96%87%E6%A1%A3.md)。

1. 通过以下两个类,分别对接支付和退款。
   - [`Charge`](paymax/model/Charge.py)   用于发起支付订单和查询支付订单信息
   - [`Refund`](paymax/model/Refund.py)  用于发起退款订单和查询退款订单信息
2. 我们为您写好了相应的示例, 参见以下两个类:
   - [`ChargeExample`](paymax/example/ChargeExample.py) 支付
   - [`RefundExample`](paymax/example/RefundExample.py) 退款
3. 为了方便进行测试, 我们已经在[`SignConfig`](paymax/config/SignConfig.py)中做好了一份配置, 您可以直接执行相应的示例进行体验进行体验。
4. 在发起真正的请求之前, 需要在[`SignConfig`](paymax/config/SignConfig.py)中配置自己的私钥、商户SecretKey、Paymax公钥。


访问 [Paymax-doc](http://paymax.github.io/paymax-doc/) 获取更多信息。

Paymax官网: https://paymax.cc/