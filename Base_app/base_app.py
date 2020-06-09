import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Utils
import global_enve
# APP的基类,和web自动化不一样,APP的PO模式,元素层和操作层都继承同一个类,继承这个直接使用即可,
# 考虑到app有时候有的元素需要进行滑屏之后才可以看到, 所以查找元素的方法统一使用找不到就会递归调用滑屏再查找的方法


class AppUtils:
    # 获取APP的driver
    def __init__(self):
        # 当前获取的是网易新闻这个app的driver
        self.driver = Utils.app_init.AppTools.get_ne_driver()
        # 设定获取 driver 建立连接后进行等待响应
        time.sleep(2)

    # 获取元素的方法, 用显式等待
    def get_element(self, element, tm=1):
        # 加上这个就可以消除捕获异常范围太宽广的警告
        # noinspection PyBroadException
        try:
            wait = WebDriverWait(self.driver, 5, tm)
            # 有*就会把元祖自行拆分,x代表是它自己本身
            # ele = wait.until(lambda x: x.find_element(*element))
            # return ele
            return wait.until(lambda x: x.find_element(*element))

        except Exception as e:
            #  记录在日志器
            global_enve.my_logger.info("没有找到这个元素")
            return None

    #  定位一组元素
    def get_elements(self, element, tm=1):
        # noinspection PyBroadException
        try:
            wait = WebDriverWait(self.driver, 5, tm)
            # 有*就会把元祖自行拆分,x代表是它自己本身
            # ele = wait.until(lambda x: x.find_elements(*element))
            # return ele
            return wait.until(lambda x: x.find_elements(*element))

        except Exception as e:
            #  记录在日志
            global_enve.my_logger.info("没有找到这组元素")
            return None

    #  封装一个通过父类元素定位它的下属元素的方法
    #  除了 driver.find_element, 其实 obj.find_element 也是可以的, 常用于app的导航栏中
    def get_element_by_parent(self, hub_element, sub_element, tm=1):
        hub_element = self.get_element(hub_element)
        # noinspection PyBroadException
        try:
            # 用父类元素替换掉 driver
            wait = WebDriverWait(hub_element, 5, tm)
            # 通过父类寻找子类, selenium自带的寻找元素方式是需要传递元祖的
            # ele = wait.until(lambda x: x.find_element(*sub_element))
            # return ele
            return wait.until(lambda x: x.find_element(*sub_element))
        except Exception as e:
            #  记录在日志
            global_enve.my_logger.info("父类下面没找到这个子类元素,请重新查找")
            return None

    # 封装点击手机屏幕
    def tap_element(self, element):
        # 实例化一个TouchAction对象
        action = TouchAction(self.driver)
        # isinstance用来比较 两个数据的类型
        if isinstance(element, tuple):
            # 如果传递进来的元素是元祖就先去定位它
            element = self.get_element(element)
        # 点击
        action.tap(element).perform()

    # 封装输入方法
    def input_text(self, element, text):
        if isinstance(element, tuple):
            element = self.get_element(element)
        element.clear()
        element.send_keys(text)

    #  封转滑屏的方法,默认向上滑屏一次,一般APP都是向上滑屏比较多
    def phone_slide(self, direction="up", duration=3000, count=1):
        # 获取屏幕分辨率
        phone_windows = self.driver.get_window_size()
        # 用一个列表作为容器存储屏幕分辨率
        distance = list()
        # 返回的是字典,所以拆解屏幕分辨率
        for i in phone_windows.values():
            distance.append(i)
        # 设置滑屏的次数,默认是1
        for i in range(count):
            # driver.swipe需要传递两个参数, 一个起始点坐标, 一个是终点坐标, 根据坐标来实现滑动

            # 向上滑屏
            if direction == "up":
                # 向上滑屏, X轴不变, Y 轴的数值变大
                self.driver.swipe(distance[0] * 0.5, distance[1] * 0.5,
                                  distance[0] * 0.5, distance[1] * 0.7, duration=duration)
            # 向下滑屏
            elif direction == "down":
                # 向下滑屏, X轴不变, Y 轴数值变小
                self.driver.swipe(distance[0] * 0.5, distance[1] * 0.6,
                                  distance[0] * 0.5, distance[1] * 0.5, duration=duration)
            # 向左滑屏
            elif direction == "left":
                # 向左滑屏, y轴不变, x轴数值变小
                self.driver.swipe(distance[0] * 0.6, distance[1] * 0.5,
                                  distance[0] * 0.5, distance[1] * 0.5, duration=duration)
            # 向右滑屏
            elif direction == "right":
                # 向左滑屏, y轴不变, x轴数值变大
                self.driver.swipe(distance[0] * 0.5, distance[1] * 0.5,
                                  distance[0] * 0.6, distance[1] * 0.5, duration=duration)
            time.sleep(0.2)

    # 滑屏递归查找元素的方法, 默认向上滑屏五次重新查找元素(在app中适用于多数情景)
    def find_element_by_slide(self, element, loop=5):
        # 先假设做一个死循环,
        while 1:
            # 查找元素
            obj = self.get_element(element)
            # 返回为空,说明查找的元素没有找到, 限定滑屏次数,未超过次数限制就可以继续滑屏
            if obj is None and global_enve.repeat <= loop+1:
                # 找不到就滑屏
                self.phone_slide()
                # 计数加一
                global_enve.repeat += 1
                # 结束本次循环
                continue
            else:
                #  计数清零
                global_enve.repeat = 0
                #  return 就会中断函数 , 所以就会跳出这个死循环
                return obj

    # 定义工具方法用于获取元素的 enabled 属性 ,定义为静态方法是为了去掉函数名下面的波浪线,
    # 因为它提示这是个静态方法, 因为这个方法不涉及自己所在的类的属性, 所以pycharm认为这是个静态方法
    # 类方法里不需要self, cls , 也不需要实例化,调用即可, 可以类.方法名调用, 也可以实例对象.方法名调用
    @staticmethod
    def get_ele_enabled(element):
        obj_enabled = element.get_attribute("enabled")
        return False if obj_enabled == 'false' else True

    # 判断一个元素是否存在
    @staticmethod
    def is_ele_exist(element):
        return True if element else False

    #  封装一个从导航栏中寻找元素的方法
    def get_element_in_navigation_bar_head(self, hub_ele, sub_ele, last_sub):
        # global_enve.my_logger.info("看看基类库里参数" + str(hub_ele) + str(sub_ele) + str(last_sub))
        # 当前屏幕的元素
        current_page = None
        # 上一个屏幕的元素
        prev_page = None
        # 找到父类元素
        parent = hub_ele
        # 导航栏的大小, 限制滑屏的范围就在导航栏的范围内
        size = self.get_element(parent).size
        # 导航栏的坐标
        location = self.get_element(parent).location
        # 起始点的坐标,  这个乘以0.几是什么?
        # 实际上就是拿这个导航栏的尺寸, 把它按比例找到起始点的位置 和终点的位置
        start_x = size['width']*0.7 + location['x']
        # 滑动的坐标要加上 导航栏的坐标是因为这种导航栏不一定都是全屏的, 所以要加上导航栏的坐标
        start_y = size['height']*0.5 + location['y']
        #  Y轴不变, 是因为只向左边滑动, 所以 终点 X 轴的位置 比起点的 短
        end_x = size['width']*0.55 + location['x']
        end_y = size['height']*0.5 + location['y']
        # 子类元素
        sub_ele = By.XPATH, "//*[@text='%s']" % sub_ele
        # 导航栏最后一个元素
        last_sub = By.XPATH, "//*[@text='%s']" % last_sub
        last_obj = None
        while 1:
            # 获取当前屏幕的元素
            current_page = self.driver.page_source
            # 寻找导航栏下面的子类
            obj = self.get_element_by_parent(parent, sub_ele)
            # 寻找导航栏最后一个元素
            last_obj = self.get_element_by_parent(parent, last_sub)
            # 如果找到了, 或者滑动屏幕也没有变化了或者 最后一个元素找到了
            if obj or (current_page == prev_page) or last_obj:
                # 不存在就返回空,
                return obj
            else:
                # 没有找到就滑屏, 在导航栏的范围里滑屏
                self.driver.swipe(start_x, start_y, end_x, end_y)
                # global_enve.app_logger.info("滑屏了")
                # 把当前屏幕这个变量赋值给上一屏幕
                prev_page = current_page

