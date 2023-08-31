# author_='Yuxuehong';
# date: 2023/8/24 9:17

"""
生成测试报告：
需要pytest-html
"""

import pytest

import Options
from appium import webdriver

"""
app功能测试+操作截图

出现异常也要截图
"""
option = Options.Options().no_reset().command_timeout(30).options()

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", option)
#pytest.main(["--html= reports/report.html", "--self-contained-html"])

#1、driver的截图是关于整个界面的截图

driver.get_screenshot_as_file("需要你添加截图报错的位置.png") #会将报错图片保存在相对路径下

#base64_img = driver.get_screenshot_as_base64() #将图片转化为一个文件流

#print(base64_img)

#2、对于元素的截图

from appium.webdriver.common.mobileby import MobileBy

ele = driver.find_element(MobileBy.ACCESSIBILITY_ID,"书城")

ele.screenshot("书城.png") #将元素保存为图片

base64_ele_img = ele.screenshot_as_base64
print(base64_ele_img)