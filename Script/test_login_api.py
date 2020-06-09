import requests
# 测试一下接口测试的流程(未封装api之前)


class TestDemoApi:
    def setup(self):
        #  实例化一个 session 对象
        self.session = requests.session()

    def teardown(self):
        # 关闭 session 回话
        self.session.close()

    # 使用session 发送接口请求, 可以维持会话
    def test_01_session(self):
        #  用 post 进行接口查询, 将 响应内容返回给 response
        # cookie = "Cookie: JSESSIONID=F0F3C4398D121A645B6A89D88CBFE176"
        json_data = {"username": "docking", "password": "123456"}
        response = self.session.post("http://192.168.0.244/api/user/v1/login", json=json_data)
        # print(response.text)
        json_1 = response.json()  # type:dict
        if json_1.get("username") == json_data.get("username"):
            assert True
        else:
            assert False

    #  使用
    def test_02_requests(self):
        # 使用 requests 就只需要 requests 就可以了, 不需要实例化session 和 requsts对象,
        # 用requests直接请求会请求结束后就断开连接 , 对服务器不造成负荷
        # 但是使用request 不能保持会话信息,接口断开后,调用下一个接口就需要自行把关联参数传过去
        url1 = "http://192.168.0.244/api/user/v1/login"
        json_data = {"username": "docking", "password": "123456"}
        response = requests.post(url=url1, json=json_data)
        json_1 = response.json()  # type:dict
        if json_1.get("username") == json_data.get("username"):
            assert True
        else:
            assert False

