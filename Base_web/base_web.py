import time
import Utils
from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
# 更换新的ActionChains获取方法, 可以看到鼠标在页面上停止时的阴影
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import global_enve


# 对象库层的基类封装
class BaseSou:

    def __init__(self):
        # 获取浏览器驱动
        self.driver = Utils.web_init.WebTools.get_driver()

    # 封装查找元素的方法,继承就可以使用,并且接口的参数是元祖,方法内部对元祖进行了拆分
    def find_element(self, element):
        # noinspection PyBroadException
        try:
            # 服务器和项目都是国外的,所以暂定显式等待十秒钟,超过十秒钟就可以判定是性能上有很大的问题
            wait = WebDriverWait(self.driver, 30, 1)
            # 有*就会把元祖自行拆分
            # ele = wait.until(lambda x: x.find_element(*element))
            # return ele
            return wait.until(lambda x: x.find_element(*element))
        except Exception as e:
            # 把异常信息加入到日志中
            global_enve.my_logger.info(("找不到这个元素", element))
            # 截图,看看是在那个页面执行就出错
            Utils.web_init.WebTools.take_photo()
            return None

    # 查找一组元素的方法,也是用显示等待
    def find_elements(self, element):
        # noinspection PyBroadException
        try:
            # 暂定十秒钟
            wait = WebDriverWait(self.driver, 30, 1)
            # 有*就会把元祖自行拆分
            # ele = wait.until(lambda x: x.find_elements(*element))
            # return ele
            return wait.until(lambda x: x.find_elements(*element))
        except Exception as e:
            # 把异常信息加入到日志中
            global_enve.my_logger.error(("找不到这一组元素", element))
            # 截图,看看是在那个页面执行就出错
            Utils.web_init.WebTools.take_photo()
            return None


# 操作层基类封装,  对元素对象的操作和模拟鼠标键盘的操作以及浏览器的前进后退
# 继承了对象库层可以使用对象库层的属性,不需要实例化对象库层
class BaseTools(BaseSou):
    def __init__(self):
        super().__init__()

    # 封装对输入框的操作, 静态方法可以直接类名.方法名调用(可以不需要实例化,实例化后也可以),静态方法不需要传递self,cls
    @staticmethod
    def input_text(ele, text, sleep_time=0):
        ele.clear()
        ele.send_keys(text)
        if sleep_time != 0:
            time.sleep(sleep_time)

    # 封装点击的操作
    @staticmethod
    def click_element(element):
        element.click()

    # # 模拟回车键, 回车键也要传递一个元素
    # 回车键(要传递元素, 传递输入框的元素, 模拟输入后就按下回车键)
    @staticmethod
    def enter(element):
        element.send_keys(Keys.ENTER)

    # 模拟鼠标左击
    def mouse_left_click(self, element):
        ActionChains(self.driver).click(element).perform()

    # 模拟鼠标右键点击
    def mouse_right_click(self, element):
        ActionChains(self.driver).context_click(element).perform()

    # 模拟鼠标双击
    def mouse_double_click(self, element):
        ActionChains(self.driver).double_click(element).perform()

    # 模拟鼠标悬停
    def mouse_operation_wait(self, element):
        ActionChains(self.driver).move_to_element(element)
        # 设置悬停两秒
        time.sleep(2)
        ActionChains(self.driver).perform()

    # 模拟鼠标拖拽
    def mouse_drag_and_drop(self, drag_element, drop_element):
        ActionChains(self.driver).drag_and_drop(drag_element, drop_element).perform()

    # 模拟鼠标左键点击后,再输入, 有的下拉框必须要点击后才可以输入
    def mouse_click_and_input(self, element, text, clear='no'):
        # 鼠标左键点击
        ActionChains(self.driver).click(element).perform()
        # 等待点击后才可以显示的元素出来
        time.sleep(0.2)
        # 有需要才对输入框进行清空
        if clear == 'yes':
            element.clear()
        # 输入元素
        element.send_keys(text)

    # 把下拉框元素实例化成Select对象
    @staticmethod
    def get_selector(element):
        selector = Select(element)
        return selector

    # 浏览器前进
    def browser_forward(self):
        self.driver.forward()

    # 浏览器后退
    def browser_back(self):
        self.driver.back()

    # 模拟按F5刷新浏览器
    def f5_refresh(self):
        self.driver.refresh()

    # 点击超连接后,直接新窗口打开,就需要切换句柄
    def change_handle(self):
        # 获取windows句柄
        handle = self.driver.window_handles
        # 切换句柄 , -1 是最新的那个句柄
        self.driver.switch_to.window(handle[-1])

    # 切换frame , frame 是有层级结构的, 只有是属于它的下一个层级才可以继续切换, 否则都要回到默认界面,
    # 从最开始的首层一层一层切换下去
    def chang_frame(self, frame_id):
        # 切换frame
        self.driver.switch_to.frame(frame_id)

    # 回到默认界面 , 只有回到默认界面才可以切换到其他iframe的首层
    def chang_default_content(self):
        self.driver.switch_to.default_content()

    # 对数据库进行操作,只需要传入sql语句就可以
    @staticmethod
    def use_sql(sql):
        with Utils.db_mysql.DBUtils() as db:
            # 执行 sql 语句
            db.execute(sql)
            # 获取执行的结果
            # result = db.fetchone()
            # return result
            return db.fetchone()

    # 封装动态下拉选择框里需要滑动鼠标进行选择的方法,
    # 要传递目标下拉框, 定位一组元素的方式去定位下拉框里的元素, 以及要选择的选项
    def auto_choose_channel_item_by_mouse(self, channel_box, channel_items_by_find_elements, selector_by_text):
        #  点击下拉选择框
        self.mouse_left_click(channel_box)
        # channel_items 就是下拉框里所有的选择项, 它们是一组元素, 要用定位一组元素的方法定位
        # 拿着目标值去列表里进行一一对比
        for item in channel_items_by_find_elements:
            # 如果这个item的文本信息和想查找的一样就返回它
            if item.text == selector_by_text:
                return item
            else:
                # 没有找到就滑动鼠标再次查找
                ActionChains(self.driver).move_to_element(item).send_keys(Keys.DOWN).perform()

    # 判断一个元素是否存在,查找由对象层查找
    @staticmethod
    def is_ele_exist(element):
        return True if element else False




