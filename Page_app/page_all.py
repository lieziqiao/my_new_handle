# 用一个类来保存对所有page的业务对象的实例化
import Page_app


# 建立一个统一入口类
class Proxy:
    # 使用property可以直接使用返回的实例对象的属性
    @property
    def get_page_home(self):
        # 返回的是实例化对象, 所以不要忘记()
        return Page_app.page_wangyi_first.ProxyWangYiFirst()

    @property
    #  返回登陆页面的业务对象
    def get_page_login(self):
        return Page_app.page_login.ProxyLogin()

    @property
    # 返回用户个人中心的业务层对象
    def get_page_user_center(self):
        return Page_app.page_user_center.ProxyUserCenter()

