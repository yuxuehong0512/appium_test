# author_='Yuxuehong';
# date: 2023/8/21 22:40


"""
整个脚本需要
 构建用例    pytest
 执行用例    pytest
 生成测试报告  pytest-html
"""
import random

from 封装的代码 import *
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Options import Options


def test():
    """
    验证通过搜索功能搜索的书籍，与从书城中获取的书籍是相同的；
    """
    print("你好，我们正在运行测试用例")
    # 首先连接设备

    #  第一步封装 driver  会话请求数据 ， 内存 -- 参数/类/函数； 磁盘； 数据库
    # desired_capability = {
    #     "platformName": "android",
    #     "platformVersion": '10.0.0',
    #     "deviceName": 'CUYDU19625011655',
    #     "app": "/Volumes/huace/APP自动化测试课程/class04/课程脚本/pythonProject/dushuwu.apk",
    #     "noReset": True,
    #     # "fullReset": True,
    # }
    desired_capability = Options().app(
        "D://2023-L/python+selenium/app/01app自动化环境的搭建/dushuwu.apk").command_timeout(30).full_reset()
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capability)
    locator = (MobileBy.ACCESSIBILITY_ID, "书城")
    wait_clickable(driver, *locator).click()

    locator = (MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/rv_book_list"]/android.widget.LinearLayout')
    book_elements = wait_visibility_all(driver, *locator)

    # 构建一个随机下标
    rand_index = random.randint(0, len(book_elements) - 1)

    book_element = book_elements[rand_index]

    locator = (MobileBy.ID, "com.zhao.myreader:id/tv_book_name")
    book_name = wait_visibility(book_element, *locator).text

    locator = (MobileBy.ID, "com.zhao.myreader:id/tv_book_desc")
    book_desc = wait_visibility(book_element, *locator).text

    locator = (MobileBy.ID, "com.zhao.myreader:id/tv_book_author")
    book_author = wait_visibility(book_element, *locator).text

    book_element.click()

    locator = (MobileBy.ID, "com.zhao.myreader:id/btn_read_book")
    wait_clickable(driver, *locator).click()

    locator = (MobileBy.ID, "com.zhao.myreader:id/tv_content")
    wait_clickable(driver, *locator).click()

    locator = (MobileBy.ID, "com.zhao.myreader:id/ll_chapter_list")
    wait_clickable(driver, *locator).click()

    locator = (MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/lv_chapter_list"]/android.widget.LinearLayout')
    chapter_elements = wait_visibility_all(driver, *locator)

    book_chapters = dict()

    for index, value in enumerate(chapter_elements):
        locator = (MobileBy.ID, 'com.zhao.myreader:id/tv_chapter_title')

        book_chapters.update({index: wait_visibility(value, *locator).text})

    driver.back()
    driver.back()

    locator = (MobileBy.ID, 'com.zhao.myreader:id/iv_search')

    wait_clickable(driver, *locator).click()

    locator = (MobileBy.ID, 'com.zhao.myreader:id/et_search_key')

    wait_visibility(driver, *locator).send_keys(book_name)

    locator = (MobileBy.ID, 'com.zhao.myreader:id/tv_search_conform')

    wait_clickable(driver, *locator).click()

    locator = (
        MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/lv_search_books_list"]/android.widget.LinearLayout')

    search_books = wait_visibility_all(driver, *locator)

    search_index = None
    for i in search_books:
        locator = (MobileBy.ID, "com.zhao.myreader:id/tv_book_name")
        bn = wait_visibility(i, *locator).text
        if book_name == bn:
            search_index = search_books.index(i)

    if search_index is None:
        raise ValueError(f"没有找到: {book_name} 这本书")

    else:

        search_book = search_books[search_index]

        locator = (MobileBy.ID, "com.zhao.myreader:id/tv_book_name")
        search_book_name = wait_visibility(search_book, *locator).text

        locator = (MobileBy.ID, "com.zhao.myreader:id/tv_book_desc")

        search_book_desc = wait_visibility(search_book, *locator).text

        locator = (MobileBy.ID, "com.zhao.myreader:id/tv_book_author")

        search_book_author = wait_visibility(search_book, *locator).text
        search_book_chapters = dict()

        search_book.click()

        locator = (MobileBy.ID, "com.zhao.myreader:id/btn_read_book")

        wait_clickable(driver, *locator).click()

        locator = (MobileBy.ID, "com.zhao.myreader:id/tv_content")

        wait_clickable(driver, *locator).click()

        locator = (MobileBy.ID, "com.zhao.myreader:id/ll_chapter_list")

        wait_clickable(driver, *locator).click()

        locator = (
            MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/lv_chapter_list"]/android.widget.LinearLayout')

        search_chapter_elements = wait_visibility_all(driver, *locator)

        for index, value in enumerate(search_chapter_elements):
            locator = (MobileBy.ID, "com.zhao.myreader:id/tv_chapter_title")

            search_book_chapters.update(
                {index: wait_visibility(value, *locator).text})

    # assert 接受两个参数 参数1 ： 条件语句； 参数2 ：断言失败的提示语句

    assert book_name == search_book_name and book_desc == search_book_desc and book_author == search_book_author and book_chapters == search_book_chapters, "断言失败，数据不一致"


if __name__ == '__main__':
    import pytest  # pytest 运行测试用例

    # pytest.main(["-vs"])  # 使用它运行测试用例的时候需要注意事项：py 文件的名称需要是 test_ 开头
    # pytest.main(["--html=report1.html"])  # 使用它运行测试用例的时候需要注意事项：py 文件的名称需要是 test_ 开头
    # pytest.main(["-vs", "--html=report2.html"])  # 使用它运行测试用例的时候需要注意事项：py 文件的名称需要是 test_ 开头
    pytest.main(["--html=./reports/report.html", "--self-contained-html"])  # 使用它运行测试用例的时候需要注意事项：py 文件的名称需要是 test_ 开头
