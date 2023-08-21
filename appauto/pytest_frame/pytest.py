# author_='Yuxuehong';
# date: 2023/8/17 9:01
"""
在python中，我们要执行一段代码，一定是要调用的

写自动化用例就是用脚本构建有步骤的编程内容

在运行用例的时候可将它放到函数里面或者类方法里面，运行时需要调用
"""
import requests

def test():
    a = "一段代码"
    print(a)
    return a

class Test:
    def test_001(self):
        print("test_001")

    @staticmethod
    def test_002():
        print("test_002")

    @staticmethod
    def test_003():
        print("3")


if __name__ == '__main__':
    pass