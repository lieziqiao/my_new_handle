import time
import allure
from selenium.webdriver.common.by import By
import Base_app
import Utils
# 元素层


class ElementLogin(Base_app.base_app.AppUtils):
    def __init__(self):
        super().__init__()
        self.username = By.XPATH, "//*[@text='网易邮箱/手机号']"
        self.password = By.ID, "com.netease.newsreader.activity:id/pn"
        self.login_btn = By.ID, "com.netease.newsreader.activity:id/pp"

    #   定位用户名
    def look_for_username(self):
        return self.find_element_by_slide(self.username)

    #     定位密码
    def look_for_password(self):
        return self.find_element_by_slide(self.password)

    #  定位登陆按钮
    def look_for_login_btn(self):
        return self.find_element_by_slide(self.login_btn)


# 操作层
class HandleLogin(Base_app.base_app.AppUtils):
    def __init__(self):
        super().__init__()
        # 实例化元素层对象
        self.Element = ElementLogin()

    # 输入用户名,需要外部传递
    @allure.step("输入用户名")
    def write_username(self, username):
        allure.attach("用户名", "%s" % username)
        self.input_text(self.Element.look_for_username(), username)
    # 输入密码,外部传递

    @allure.step("输入密码")
    def write_password(self, password):
        allure.attach("密码", "%s" % password)
        self.input_text(self.Element.look_for_password(), password)

    # 点击一下空白的地方, 不然写入的不能保留在对话框
    @allure.step("点击手机空白的地方")
    def click_phone(self):
        self.tap_element((By.CLASS_NAME, "android.widget.EditText"))

    #  点击登陆
    @allure.step("点击登陆")
    def click_login_btn(self):
        self.tap_element(self.Element.look_for_login_btn())

# 业务层


class ProxyLogin:
    def __init__(self):
        # 实例化操作层对象
        self.handle = HandleLogin()

    #  登陆业务,输入后需要点击一下空白的地方
    @allure.step("登陆业务")
    def login(self, username, password):
        self.handle.write_username(username)
        self.handle.click_phone()
        self.handle.write_password(password)
        time.sleep(1)
        # allure添加图片描述
        allure.attach(Utils.app_init.AppTools.get_ne_driver().get_screenshot_as_png(), "输入账号和密码后",
                      allure.attachment_type.PNG)
