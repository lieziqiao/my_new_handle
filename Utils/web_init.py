import logging
import time
# 给 selenium 的webdriver起个别名, 免得和App的webdriver起冲突
from selenium import webdriver as web_driver
from my_config import get_file_path
# 导入selenium中的option
from selenium.webdriver.chrome.options import Options
import global_enve


# 定义web的工具基类, 获取浏览器驱动对象,关闭浏览器驱动对象, 以及截图操作
class WebTools:
    _driver = None

    @classmethod
    # 暂定是默认使用谷歌浏览器 , 后期有需求可以增进返回其他浏览器的驱动
    def get_driver(cls, browser_name="CHROME"):
        if cls._driver is None and browser_name.upper() == "CHROME":
            options = Options()
            # 更改谷歌的文件默认下载文件的保存路径
            options.add_experimental_option("prefs", {
                # 设置谷歌默认下载文件的保存路径
                "download.default_directory": global_enve.report_address,
                # 为 假 就不会出现提示保存文件位置的弹窗
                "download.prompt_for_download": False
            })
            cls._driver = web_driver.Chrome(chrome_options=options,
                                            executable_path=get_file_path()+'\\chromedriver.exe')
            cls._driver.maximize_window()
            # 加上隐式等待六秒
            cls._driver.implicitly_wait(6)
            # 打开项目地址, 注释掉, 把打开地址和登陆的操作写在Utils的前置类里
            # cls._driver.get(global_enve.project_url)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None

    # 封装截图操作,用时间戳作为分割
    @classmethod
    def take_photo(cls):
        cls._driver.get_screenshot_as_file(str(get_file_path()) + "/Img/{}.png".format(time.strftime("%Y%m%d%H%M%S")))
