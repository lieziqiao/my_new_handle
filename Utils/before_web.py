# 前置类
import time
from selenium.webdriver.common.by import By
import Utils
import global_enve
# 封装一些前置操作, 方便调用,这样就不需要规定执行顺序, 任意执行哪条先都无所谓,降低耦合度
# 因为web和app的driver容易产出冲突, 所以这个模块用于封装web端的前置操作,接口的不需要是因为使用的是session会话可以保持着


class PrepositionOperationWeb:
    def __init__(self):
        pass
