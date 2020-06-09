import time
# 有时候会出现元素定位找错的情况, 目前看来, 有可能是打开app的速度太快了,然后里面元素开始定位, 就一直没有找到
# 解决方法是把打开app后的时间进行一个强制等待
import pytest
import Page_app
import Utils
# 数据驱动
data = Utils.operation_file.FileTools.operation_file_yaml("/Data/data_app/data_login_ne.yaml",
                                                          key_index="login_successful")


class TestLogin:
    def setup_class(self):
        # 实例化统一入口类
        self.page = Page_app.page_all.Proxy()

    def setup(self):
        # 获取driver
        self.driver = Utils.app_init.AppTools.get_ne_driver()
        # 实例化Toll工具类对象,用来关闭连接
        self.Tool = Utils.app_init.AppTools()

    # 关闭连接
    def teardown(self):
        time.sleep(3)
        # 退出driver, 关闭app
        self.Tool.quit_ne_driver()

    @pytest.mark.parametrize("info", data)
    def test_login1(self, info):
        time.sleep(2)
        # 点击首页的我
        self.page.get_page_home.click_me()
        time.sleep(1)
        # 点击用户中心的登陆
        self.page.get_page_user_center.click_go_login()
        time.sleep(1)
        # 在登陆页面输入用户名和密码
        self.page.get_page_login.login(info["username"], info["pwd"])
