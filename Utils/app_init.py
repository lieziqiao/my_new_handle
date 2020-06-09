from appium import webdriver
# 封装的工具类, 用来获取APP 的 driver , 当前的APP设置,ID, 版本等都是写死的, 后面可以在config中获取
# 当前就设定是安卓7.1.2, 设备ID是XXX, 包名和启动名是网易新闻这个APP的,
# 如果要测试多个APP, 可以返回多个APP的driver, 但是 PO层中就要更改获取的是哪个driver,只是可以保留旧的项目的driver配置,方便移植


class AppTools:
    __ne_driver = None

    @classmethod
    def get_ne_driver(cls):
        #  网易新闻这个driver的标志位
        if cls.__ne_driver is None:
            des_cap = {
                "platformName": "android",
                "platformVersion": "7.1.2",
                "deviceName": "emulator-5554",
                "appPackage": "com.netease.newsreader.activity",
                "appActivity": "com.netease.nr.phone.main.MainActivity ",
                "resetKeyboard": True,
                "unicodeKeyboard": True,
                'noReset': True,
                #  加上UI2 就能定位到toast 框,但是执行速度会很慢
                'automationName': 'Uiautomator2'

            }
            # 获取对应的连接
            cls.__ne_driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
        # 返回 driver
        return cls.__ne_driver

    @classmethod
    def quit_ne_driver(cls):
        if cls.__ne_driver:
            # 关闭app,这样看起来有效果
            cls.__ne_driver.close_app()
            # 退出连接
            cls.__ne_driver.quit()
            # 释放__driver
            cls.__ne_driver = None
