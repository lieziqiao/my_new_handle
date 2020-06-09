import pytest


# pytest中可以参数化的工厂方法
@pytest.fixture(autouse=True,  scope='module', params=["lie", True, None])
def foo(request):
    return request.param


class TestDemo1:
    # 在需要的地方直接传入 函数名,不可以写 function()
    def test_fn1(self, foo):
        # 传入的foo 是告诉 pytest 帮我找到哪个函数直接调用
        print("看看哪里出错 %s" % foo)


