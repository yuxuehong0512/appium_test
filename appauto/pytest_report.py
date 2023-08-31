# author_='Yuxuehong';
# date: 2023/8/24 8:56

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
pytest.main(["--html= reports/report.html", "--self-contained-html"])
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", option)

