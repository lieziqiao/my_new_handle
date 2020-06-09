import time
import allure
from selenium.webdriver.common.by import By
import Base_app
import global_enve
# 元素层


class ElementWangYiFirst(Base_app.base_app.AppUtils):
    # 方法重写, 并定义要用的元素
    def __init__(self):
        super().__init__()
        # 第一个新闻的置顶
        self.zhiding = By.XPATH, "//*[@text='置顶']"
        # 点击新闻后的返回
        self.comeback = By.ID, "com.netease.newsreader.activity:id/aq4"
        # 首页的我
        self.me = By.XPATH, "//*[@text='我']"
        # 首页头部的导航栏
        self.navigation_bar_head = By.ID, "com.netease.newsreader.activity:id/bn9"

    # 定位置顶按钮
    def look_for_zhiding(self):
        return self.find_element_by_slide(self.zhiding)

    # 定位返回按钮
    def look_for_comeback(self):
        return self.find_element_by_slide(self.comeback)

    # 定位首页中的我
    def look_for_me(self):
        return self.find_element_by_slide(self.me)

    # 定位顶部的导航栏
    def look_for_navigation_bar_head(self):
        return self.get_element(self.navigation_bar_head)


# 操作层
class HandleWangYiFirst(Base_app.base_app.AppUtils):
    def __init__(self):
        super().__init__()
        # 实例化元素层对象
        self.element_find = ElementWangYiFirst()

    @allure.step("点击置顶")
    #  点击置顶操作
    def tap_zhiding(self):
        self.tap_element(self.element_find.look_for_zhiding())

    #  点击返回按钮
    @allure.step("点击置顶后返回")
    def tap_comeback(self):
        self.tap_element(self.element_find.look_for_comeback())

    # 点击首页中的我
    @allure.step("点击首页中的我")
    def tap_me(self):
        self.tap_element(self.element_find.look_for_me())

    # 这个方法 可以考虑放到 基类里, 因为app里用的挺多的
    # 寻找顶部导航栏里某个元素, 有的APP页面有轮播图,所以 page_source获取的永远不相同, 这个时候就需要传递导航栏里最尽头的元素
    # @allure.step("去导航栏里选择频道")
    # def find_element_in_navigation_bar_head(self, sub_ele, last_sub=None):
    #     # 当前屏幕的元素
    #     current_page = None
    #     # 上一个屏幕的元素
    #     prev_page = None
    #     # 父类元素
    #     parent = self.element_find.navigation_bar_head
    #     # 导航栏的大小, 限制滑屏的范围就在导航栏的范围内
    #     size = self.element_find.get_element(parent).size
    #     #  导航栏的坐标
    #     location = self.element_find.get_element(parent).location
    #     # 起始点的坐标,  这个乘以0.几是什么?
    #     # 实际上就是拿这个导航栏的尺寸, 把它按比例找到起始点的位置 和终点的位置
    #     start_x = size['width']*0.70 + location['x']
    #     # 滑动的坐标要加上 导航栏的坐标是因为这种导航栏不一定都是全屏的, 所以要加上导航栏的坐标
    #     start_y = size['height']*0.5 + location['y']
    #     #  Y轴不变, 是因为只向左边滑动, 所以 终点 X 轴的位置 比起点的 短
    #     end_x = size['width']*0.4 + location['x']
    #     end_y = size['height']*0.5 + location['y']
    #     sub_ele = By.XPATH, "//*[@text='%s']" % sub_ele
    #     last_sub = By.XPATH, "//*[@text='%s']" % last_sub
    #     while 1:
    #         # 获取当前屏幕的元素
    #         current_page = self.driver.page_source
    #         # 寻找导航栏下面的子类
    #         obj = self.get_element_by_parent(parent, sub_ele)
    #         # 寻找导航栏最后一个元素
    #         last_obj = self.get_element_by_parent(parent, last_sub)
    #         # 如果找到了, 或者滑动屏幕也没有变化了或者 最后一个元素找到了
    #         if obj or (current_page == prev_page) or last_obj:
    #             # 不存在就返回的是空
    #             return obj
    #         else:
    #             # 没有找到就滑屏, 在导航栏的范围里滑屏
    #             self.driver.swipe(start_x, start_y, end_x, end_y)
    #             # global_enve.app_logger.info("滑屏了")
    #             # 把当前屏幕这个变量赋值给上一屏幕
    #             prev_page = current_page

    @allure.step("用基类的新方法从导航栏里找元素")
    def find_element_in_navigation_bar_head_new(self, sub_ele, last_sub):
        # 调用从导航栏里寻找元素的方法
        # result = self.get_element_in_navigation_bar_head(self.element_find.navigation_bar_head, sub_ele, last_sub)
        # return result
        return self.get_element_in_navigation_bar_head(self.element_find.navigation_bar_head, sub_ele, last_sub)


# 业务层
class ProxyWangYiFirst:
    def __init__(self):
        self.handle = HandleWangYiFirst()

    # 在首页点击第一个新闻的置顶并返回首页
    def tap_zhiding_and_comeback(self):
        self.handle.tap_zhiding()
        time.sleep(3)
        self.handle.tap_comeback()
        time.sleep(3)

    # 点击首页中的我
    def click_me(self):
        self.handle.tap_me()

    # 在顶部导航栏中选择频道
    def choose_channel_in_navigation_bar_head(self, channel, last_sub):
        # 选择频道
        # result = self.handle.find_element_in_navigation_bar_head(channel, last_sub)
        result = self.handle.find_element_in_navigation_bar_head_new(channel, last_sub)
        #  pytest框架比unitest框架更方便的地方是可以在PO层做断言
        # if result:
        #     assert True
        # else:
        #     assert False
        # 优化
        return True if result else False

