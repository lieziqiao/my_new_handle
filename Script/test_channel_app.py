import time
# 有时候会出现元素定位找错的情况, 目前看来, 有可能是打开app的速度太快了,然后里面元素开始定位, 就一直没有找到
# 解决方法是把打开app后的时间进行一个强制等待
# 用上allure做测试报告
# import allure
import pytest
import Page_app
import Utils


class TestChannel:
    def setup_class(self):
        # 实例化统一入口类
        self.page = Page_app.page_all.Proxy()

    def setup(self):
        # 获取 网易app的driver
        self.driver = Utils.app_init.AppTools.get_ne_driver()
        # 实例化Toll工具类对象,用来关闭连接
        self.app_tools = Utils.app_init.AppTools()

    # 关闭连接
    def teardown(self):
        time.sleep(3)
        self.app_tools.quit_ne_driver()

    # 测试导航栏
    def test_channel(self):
        self.page.get_page_home.choose_channel_in_navigation_bar_head("财经", "小说")
