# author_='Yuxuehong';
# date: 2023/8/21 22:40
"""
封装我们在发起会话过程中的 参数
esired_capability = {
        "platformName": "android",   #  可以使用adb 获取
        "platformVersion": '10.0.0',  #  可以使用adb 获取
        "deviceName": 'CUYDU19625011655',  #  可以使用adb 获取
        "app": "/Volumes/huace/APP自动化测试课程/class04/课程脚本/pythonProject/dushuwu.apk",
        "noReset": True,
        # "fullReset": True,
    }
"""
import os
import warnings


class Options:
    """
    最后要返回的数据是一个 dict
    """

    def __init__(self):
        self.__option = dict()  # 私有属性的写法，为了让外部引用的人无法正大光明的改造

    def __device_name(self, device=str()):

        if device:  # 如果device  不是空字符串
            self.__option.update({"deviceName": device})
        else:
            devices = os.popen("adb devices")  # 使用os.popen 可以获取程序运行完之后的数据，使用os.system 不能获取，不理解去运行试试就OK了
            result = [i for i in devices.read().split("\n") if i != ""]  # 列表推导式里面嵌入if判断，筛选出不为空的数据
            if len(result) > 1:  # 如果 adb devices 运行返回的数据是两行，则认为有返回数据；
                if len(result) > 2:  # 如果adb devices 运行 返回的数据超过两行，怎认为返回的 device name 有多个；所以打印下面的提示；
                    print(f"\033[31m请检查是否同时连接着两台设备，如若连接着两台设备请在任意adb命令中指定设备名；---> -s\033[0m")

                else:
                    for index, value in enumerate(result):  # 通过内置函数enumerate 方法 同时获得 列表中的数据及其数据的下标；其中 index 为下标；value为值
                        if index > 0:  # 如果 index 大于0 ；也就是返回的数据中存在 device name 则过滤掉多余的语句，仅对可以使用的device 进行存贮
                            _device = value.split()[0]
                            self.__option.update({"deviceName": _device})  # 存储 数据 device name
            else:
                raise ValueError(f"无法获取设备信息; 运行了 adb 命令： adb devices  得到结果 ：{devices.read()}")
        return self

    def __platform(self, name=str(), version=str()):
        if name:
            self.__option.update({"platformName": name})
        else:
            shell_result = os.popen("adb shell getprop ro.product.brand").read().strip()
            if shell_result == "Meizu":
                shell_result = "Android"
            self.__option.update({"platformName": shell_result})
        if version:
            self.__option.update({"platformVersion": version})
        else:
            shell_result = os.popen("adb shell getprop ro.build.version.release").read().strip()
            self.__option.update({"platformVersion": shell_result})
        return self

    def no_reset(self, value=True):
        if value:
            self.__option.update({"noReset": value})
        else:
            self.__option.update({"noReset": False})
        return self

    def full_reset(self, value=True):
        """
        因为它是会卸载APP的，所以我们需要它和app 这个参数 一起使用
        :param value:
        :return:
        """

        if value:
            app = self.__option.get("app", "")
            if not app:
                warnings.warn(
                    '使用 fullReset 的时候尽量配合参数 "app" 使用，否则你的被测应用会被卸载，从而影响后面的用例正常执行',
                    FutureWarning,
                    stacklevel=2  # 一般我们设置成2  就好了
                )

                self.__option.update({"fullReset": value})
        else:
            self.__option.update({"fullReset": False})
        return self

    def command_timeout(self, value: int):
        self.__option.update({"newCommandTimeout": value})
        return self

    def options(self, **kwargs):  # 因为整个参数都会是键值对的形式，所以我们使用 **kwargs 解包
        self.__option.update(**kwargs)

        device = kwargs.get("deviceName", "")
        name = kwargs.get("platformName", "")
        version = kwargs.get("platformVersion", "")

        self.__platform(name, version)
        self.__device_name(device)
        return self.__option

    def app(self, value):
        self.__option.update({"app": value})
        return self


if __name__ == '__main__':
    desired_capability = {
        # "platformName": "android",  # 可以使用adb 获取
        # "platformVersion": '10.0.0',  # 可以使用adb 获取
        # "deviceName": 'CUYDU19625011655',  # 可以使用adb 获取
        "app": "D://2023-L/python+selenium/app/01app自动化环境的搭建/dushuwu.apk",
        "noReset": True,
        # "fullReset": True,
    }

    # print(Option().full_reset().command_timeout(30).options(**desired_capability))
    print(Options().full_reset().no_reset().command_timeout(30).options())
