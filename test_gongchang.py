import pytest
# pytest中的工厂方法


@pytest.fixture(autouse=False)
def function():
    a = '100'
    return a


class TestGong:
    # 在需要的地方直接调用
    def test_01(self, function):
        an = function
        print("看看是不是返回值 %s" % an)
        # 确认是可以获取返回值的

    # 通过装饰器调用,但是不能获取工厂方法的返回值
    @pytest.mark.usefixtures('function')
    def test_02(self):
        # 获取的是地址
        print("看看获取了什么%s" % function)
        # 拿不到返回值,而且还报错, 要拿到返回值只能用第一种
        # print("能接收返回值嘛%s" %(function()) )
