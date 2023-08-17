# author_='Yuxuehong';
# date: 2023/8/17 13:20
class Test:
    def setup(self):
        print("前置处理")
    def test_001(self):
        print("001")
    def test_002(self):
        print("002")
    def test_003(self):
        print("003")
    def teardown(self):
        print("后置")