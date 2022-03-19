import pytest
from time import sleep
def do_something():
    """
    模拟表示前置接口
    """
    return 3.14

# 定义一个全局变量类

class EnvData:
    pass


class TestCase:
    def setup_class(self):
        # 执行前置操作
        data = do_something()
        # 将data绑定到全局变量类的类属性上
        # EnvData.data = data
        # 将data绑定到当前类的类属性上
        self.data = data
        # self.__class__.res1 = data
        print('用例一')

    def test_something(self):
        print('执行测试')
        # 获取前置方法中产生的数据
        # 从全局变量中获取
        # print(EnvData.data)
        # 从当前用例的类属性中获取
        # print(self.__class__.res1)
        # 如果当前用例对象没有同名对象属性，也可以直接从对象属性中获取
        print(self.data)

if __name__ == '__main__':
    pytest.main(['-sv','test.py'])