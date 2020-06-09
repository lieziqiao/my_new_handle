import Page_web


class ProxyWeb:
    @property
    def get_baidu_proxy(self):
        return Page_web.page_baidu.NewProxy()
