import requests
# 测试一下接口测试的流程,一个原始的模版


class TestDemo:
    def setup(self):
        #  实例化一个 session 对象
        self.session = requests.session()

    def teardown(self):
        # 关闭 session 回话
        self.session.close()

    #  测试接口能不能连接百度
    def test_01(self):
        #  用 get 进行接口查询, 将 响应内容返回给 response
        response = self.session.get("https://www.baidu.com/")
        text = response.text
        if type(text) == str:
            assert True
        else:
            assert False



