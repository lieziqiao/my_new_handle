import allure
from selenium.webdriver.common.by import By

import Base_app
# 元素层


class ElementUserCenter(Base_app.base_app.AppUtils):
    def __init__(self):
        super().__init__()
        self.enter_login = By.ID, "com.netease.newsreader.activity:id/a7a"

    #     定位登陆按钮
    @allure.step("点击登陆,跳转去登陆页面")
    def look_for_enter_login(self):
        return self.find_element_by_slide(self.enter_login)


# 操作层
class HandleUserCenter(Base_app.base_app.AppUtils):
    def __init__(self):
        super().__init__()
        # 实例化元素层对象
        self.element = ElementUserCenter()

    #     点击登陆
    def tap_login(self):
        self.tap_element(self.element.look_for_enter_login())


# 业务层
class ProxyUserCenter:
    def __init__(self):
        self.handle = HandleUserCenter()

    #     点击登陆,跳转去登陆页面
    def click_go_login(self):
        self.handle.tap_login()
