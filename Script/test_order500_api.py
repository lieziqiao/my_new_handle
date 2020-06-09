import pytest
import requests
import Api
import my_config
import json
from parameterized import parameterized
path1 = my_config.get_file_path() + "\\Data\\data_api\\order_500.json"
# # 反序列化(提取json文件里的全部数据,不需要拆分,因为要全部作为参数提交)
with open(path1, encoding="UTF-8") as f:
    data = json.load(f)
#  parameterized参数化插件必须要传递元祖或者列表, 如果只有一个数据,就加个逗号或者一个无用的数字也行
data1 = [(data, )]


class TestOrder500:
    def setup_class(self):
        # 实例化接口类对象
        self.api = Api.api_alfred_web.AlfredWebApi()

    def setup(self):
        # 实例化 session, session 要在方法级别的fixture中实例化,
        self.session = requests.session()

    def teardown(self):
        #  关闭会话
        self.session.close()

    # 使用pytest.mark.parameterized就自动拆分要接收的数据,导致本来要一次传递500份的数据会变成每次执行一份,执行500次,
    #  所以数据被拆分以后, 本来是一次要提交500个订单,反而成了发送五百次请求
    # @pytest.mark.parametrize("info", data1)
    # 而且 requests的post请求是允许传递 List嵌套json的,
    # 但是没能恢复到报错传递数据非json类型的异常情况, 应该是数据的问题
    @parameterized.expand(data1)
    def test_commit_order_api(self, info):
        # 提交五百发货订单,不可以使用超管账号, 因为超管账号里运营商的字段是空的
        json_data = {"username": "allan", "password": "888888"}
        # 调用登陆API
        response = self.api.get_login_web_api_response(self.session, data=json_data)
        token = response.json()
        # 获取 token, 作为提交订单参数的请求头
        # json提取数据就和字典是一样的,通过get(key)来获取
        token = token.get("token")
        headers = dict()
        headers["X-USER-TOKEN"] = token
        headers["Content-Type"] = "application/json"
        # print(headers)
        # 登陆成功后就可以继续提交500个订单请求
        url = "http://192.168.0.244:7072/shipments/v1/shipments"
        #  调用接口, 发送五百条订单数据
        # 使用的是session 会话, 不提交token, 是不是也可以提交订单成功, 结果是直接接口就报错了
        response = self.session.post(url, json=info, headers=headers)
        answer = response.json()
        # 提取响应的json数据的字段
        result = answer.get("SUCCEED")
        # result为真的, 说明 "SUCCEED"是有键值的, 说明就是接口请求成功的
        if result:
            assert True



