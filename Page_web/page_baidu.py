
import time
from selenium.webdriver.common.by import By
# 封装对象库层
from Base_web.base_web import BaseSou, BaseTools


class Element(BaseSou):
    def __init__(self):
        super().__init__()
        # 百度首页输入框的元素
        self.text_input = (By.ID, "kw")

    #     百度首页的搜索按钮
        self.look_for_btn = (By.ID, "su")

    # 找到输入框元素
    def look_for_text_input(self):
        return self.find_element(self.text_input)
    # 找到 搜索按钮
    def look_for_lookfor_btn(self):
        return self.find_element(self.look_for_btn)


# 操作层
class Handle(BaseTools):
    def __init__(self):
        super().__init__()
        self.Element1 = Element()
    # 在百度输入框输入
    def input_baidu(self,word):
       self.input_text(self.Element1.look_for_text_input(), word)
    # 点击搜索按钮
    def go_lookfor(self):
        self.click_element(self.Element1.look_for_lookfor_btn())

#     用鼠标点击搜索按钮
    def use_mouse_click_search_btn(self):
        self.mouse_left_click(self.Element1.look_for_lookfor_btn())


# 业务层
class NewProxy:
    def __init__(self):
        self.Handle1 = Handle()

    #  在百度首页进行输入内容并点击去搜索
    def only_input(self, word):
        self.Handle1.input_baidu(word)
        # 为了视觉效果
        time.sleep(1)
        # 点击去搜索
        # self.Handle1.go_lookfor()
#         用鼠标去点击
        self.Handle1.use_mouse_click_search_btn()
        time.sleep(1)



