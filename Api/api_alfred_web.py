import allure
# 封装一个类, 用来管理Alfred项目的api , 以一个类来管理一个项目的web端的api


class AlfredWebApi:
    def __init__(self):
        self.login_web_url = "http://192.168.0.244/api/user/v1/login"

    @allure.step("调用alfred的web端登陆接口,使用session保持会话")
    #  获取登陆接口并返回响应体
    def get_login_web_api_response(self, session, data, headers=None):
        # 至于接口参数是json还是data ,取决于接口,
        # 如果是 json格式的就传递json , 如果接口要求是form表单就用data(在python中使用dict数据进行传递)
        allure.attach("登陆的用户名%s, 密码%s" % (data.get("username"), data.get("password")))
        # 如果请求头必须要传递
        if headers:
            return session.post(self.login_web_url, json=data, headers=headers)
        # 有一些接口可以不传递请求头,例如这个登陆接口
        else:
            return session.post(self.login_web_url, json=data)

    @allure.step("调用alfred的web端登陆接口,用request发送,成功后就断开和服务器的连接")
    #  获取登陆接口并返回响应体
    def get_login_web_api_response_in_request(self, request, data, headers=None):
        # 至于接口参数是json还是data ,取决于接口,
        # 如果是 json格式的就传递json , 如果接口要求是form表单就用data(在python中都是使用dict数据进行传递)
        allure.attach("登陆的用户名%s, 密码%s" % (data.get("username"), data.get("password")))
        # return request.post(self.login_web_url, json=data)
        # 如果请求头需要传递
        if headers:
            return request.post(self.login_web_url, json=data, headers=headers)
        else:
            return request.post(self.login_web_url, json=data)
