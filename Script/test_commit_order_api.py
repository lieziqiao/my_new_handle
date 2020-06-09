import pytest
import requests
import Api


class TestCommitOrder:
    def setup_class(self):
        # 实例化接口类对象
        self.api = Api.api_alfred_web.AlfredWebApi()

    def setup(self):
        # 实例化 session
        self.session = requests.session()

    def teardown(self):
        #  关闭会话
        self.session.close()

    #  提交订单得到接口,这里就跑通了提交单条订单
    def test_commit_order_api(self):
        json_data = {"username": "allan", "password": "888888"}
        # 调用登陆API
        response = self.api.get_login_web_api_response(self.session, data=json_data)
        token = response.json()
        # 获取 token, 作为提交订单参数的请求头
        token = token.get("token")
        headers = dict()
        headers["X-USER-TOKEN"] = token
        headers["Content-Type"] = "application/json"
        # print(headers)
        # 登陆成功后就可以继续提交500个订单请求
        url = "http://192.168.0.244:7072/shipments/v1/shipments"
        json_data = [
            {
                "serviceType": "RETURN",
                "trackingNumber": "R202006021000",
                "additionalTrackingNumber": "",
                "referenceNumber": "",
                "locationId": "",
                "accessCode": 12345556,
                "recipientPhone": 13590274675,
                "recipientEmail": "allan.yan@pakpobox.com",
                "recipientAddress": "",
                "recipientName": "",
                "note": "",
                "charge": 0,
                "weight": "2.25 kg",
                "senderPhone": 0,
                "senderEmail": "",
                "senderAddress": "",
                "senderName": "allan",
                "companyId": ""
            }
        ]
        response = self.session.post(url, json=json_data, headers=headers)
        answer = response.json()
        # print(answer)
        # 提取响应的json数据的字段
        result = answer.get("SUCCEED")
        # result为真的, 说明 "SUCCEED"是有键值的, 说明就是接口请求成功的
        if result:
            assert True
