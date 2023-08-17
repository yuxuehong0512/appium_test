# author_='Yuxuehong';
# date: 2023/8/17 11:08

class Test:

    def setup_class(self):
        print("开头")

    def test_001(self):
        print("这是测试用例test001")
    def test_002(self):
        print("这是测试用例test002")
    def test_003(self):
        print("这是测试用例test003")
    def setup(self):
        print("这是测试用例的前置条件")
    def teardown(self):
        print("这是测试用例的后置条件")
    def teardown_class(self):
        print("扫尾")

if __name__ == "__main__":
    pass

