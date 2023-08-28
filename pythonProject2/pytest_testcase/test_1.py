# author_='Yuxuehong';
# date: 2023/8/24 10:31
import time

import pytest
from appium.webdriver.common.mobileby import MobileBy
import Options
from appium import webdriver
from 封装的代码 import *

"""
添加截图到html中去
"""
from pytest_html import extras  # 由它将截图添加到用例


def test1(extra):
    option = Options.Options().command_timeout(30).options()

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", option)
    print("开始")
    # 将截图添加到pytest测试报告中
    extra.append(extras.png(driver.get_screenshot_as_base64()))
    # driver.get_screenshot_as_file("点击_书城_之前.png")
    location = (MobileBy.ACCESSIBILITY_ID, "书城")
    wait_clickable(driver, *location).click()
    extra.append(extras.png(driver.get_screenshot_as_base64()))
    print("结束")
    # driver.get_screenshot_as_file("点击_书城_之后.png")

