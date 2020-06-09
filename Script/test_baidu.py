import Page_web
import Utils
import global_enve


class TestBaidu:
    def setup(self):
        self.web = Page_web.page_init.ProxyWeb()
        # 获取浏览器驱动
        self.driver = Utils.web_init.WebTools.get_driver()
        # 打开项目地址
        self.driver.get(global_enve.project_url)

    def teardown(self):
        # 关闭浏览器
        Utils.web_init.WebTools.quit_driver()

    def test_open_baidu(self):
        baidu = self.web.get_baidu_proxy
        baidu.only_input("可以了")
