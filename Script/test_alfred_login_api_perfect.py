import Api
import Utils
import requests
import pytest
# 获取 yaml文件数据, 给登陆接口使用
data = Utils.operation_file.FileTools.operation_file_yaml("/Data/data_api/data_alfred_web_login.yaml",
                                                          key_index="login_successful")
# 测试登陆接口


class TestAlfredLoginApi:
    def setup(self):
        #  实例化 session 对象
        self.session = requests.session()
        # 实例化 接口类对象
        self.api_all = Api.api_alfred_web.AlfredWebApi()
        # # 实例化文件操作对象
        # self.file_handle = Utils.operation_file.FileTools()

    def teardown(self):
        # 关闭 session 对象
        self.session.close()

    # pytest自带的参数化方法, 需要两个参数, 一个是接收的变量, 另一个是从yaml读取的数据,
    @pytest.mark.parametrize("info", data)
    def test_login_yaml_api(self, info):
        response = self.api_all.get_login_web_api_response(self.session, info)
        json_response = response.json()  # type: dict
        # 参数化过来的参数通过键值来获取
        if json_response.get("username") == info.get("username"):
            assert True
        else:
            assert False
