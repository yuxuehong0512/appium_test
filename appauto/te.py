# author_='Yuxuehong';
# date: 2023/8/16 9:43

# class Tesr():
#     name = "rengy"
#     desc_1 = "1"
#     desc_2 = "2"
#     desc_3 = "3"
#
#     def __init__(self,desc_1,desc_2,desc_3):
#         self.name = dict()
#         self.desc_1 = desc_1
#         self.desc_2 = desc_2
#         self.desc_3 = desc_3
#
#     def jineng_1(self):
#         print("{}释放{}".format(self.name,self.desc_1))
#         return self
#
#     def jineng_2(self):
#         print("{}释放{}".format(self.name,self.desc_2))
#
#
#     def jineng_3(self):
#         print("{}释放{}".format(self.name,self.desc_3))
#
#
# tesr = Tesr("12","23","34")
# tesr.name = "xiaoyu"
# tesr.jineng_1().jineng_2()

class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('Hello, my name is', self.name)
        return self

person = Person('Alice')
person.say_hello()
