# author_='Yuxuehong';
# date: 2023/8/18 13:46

"""
整个脚本需要
构建用例
执行用例
生成测试报告 pytest——html
"""

from 封装的代码 import *
import time
import random

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from Options import Options


def test():
    """
    验证通过搜索的功能搜索的书籍，与书城中获取的书籍是相同的
    :return:
    """
    """
    a.打开读书屋，进入书城
    """
    # 1.连接方式一：已知活动名和包名
    # caps = {
    #     "appium:deviceName": "emulator-5554",
    #     "platformName": "Android",
    #     "appium:platformVersion": "7.1.2",
    #     "appium:appPackage": "com.zhao.myreader",
    #     "appium:appActivity": "com.zhao.myreader.ui.home.MainActivity"
    # }
    print("你好")
    # 2.连接方式2：不知道活动名和包名
    # 第一步封装driver 会话请求数据
    # caps = {
    #     "appium:deviceName": "emulator-5554",
    #     "platformName": "Android",
    #     "appium:platformVersion": "7.1.2",
    #     "app": "D://2023-L/python+selenium/app/01app自动化环境的搭建/dushuwu.apk",
    #     "fullReset": False, #它会在运行完脚本后帮你卸载掉软件，默认为False不卸载
    # #     "noReset": True,#它在启动app之前，会清除你的app里面的数据，默认为False重置
    # #     #"newCommandTimeout : 20 ", # 服务器等待客户端命令发送的超时时间，超过改时间，如果还没有发送指令，则appium服务器终止会话状态
    #  }
    # {'app': 'D://2023-L/python+selenium/app/01app自动化环境的搭建/dushuwu.apk', 'platformName': 'Android',
    # 'platformVersion': '7.1.2', 'deviceName': 'emulator-5554'}

    caps = Options().app("D://2023-L/python+selenium/app/01app自动化环境的搭建/dushuwu.apk").options()
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=caps)
    # driver.implicitly_wait(10)  # 隐形等待时间
    # driver.wait_activity(activity="",timeout=10) #等待某个avtivity的资源加载完成
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "书城").click()
    locator = (MobileBy.XPATH,
               '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zhao.myreader:id/rv_book_list"]/android.widget.LinearLayout')
    book_elements = wait_visibility_all(driver, *locator)

    """
    b.随机获取一本书,为验证数据点
    """

    # 使用随机数构建方式，获取一个在规定范围内的随机数作为元素的的下标

    rand_index = random.randint(0, len(book_elements) - 1)
    print(rand_index)
    book_element = book_elements[rand_index]

    # c.通过随机指定的书去获取验证数据
    book_name = book_element.find_element(MobileBy.ID, "com.zhao.myreader:id/tv_book_name").text  # 获取书名
    book_desc = book_element.find_element(MobileBy.ID, "com.zhao.myreader:id/tv_book_desc").text  # 获取简介
    book_author = book_element.find_element(MobileBy.ID, "com.zhao.myreader:id/tv_book_author").text  # 获取作者名

    # 获取各章节的名字，并将各章节名字储存到字典中
    book_element.click()
    locator = (MobileBy.ID, 'com.zhao.myreader:id/btn_read_book')
    read_book = wait_clickable(driver, *locator)
    read_book.click()
    locator = (MobileBy.ID, "com.zhao.myreader:id/tv_content")
    content = wait_clickable(driver, *locator)
    content.click()
    locator = (MobileBy.ID, "com.zhao.myreader:id/ll_chapter_list")
    chapter_list = wait_clickable(driver, *locator)
    chapter_list.click()
    locator = (MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/lv_chapter_list"]/android.widget.LinearLayout')
    chapter_lists = wait_visibility_all(driver, *locator)
    book_chapters = dict()
    # for i in chapter_lists:
    #    book_chapter.append(i.find_element(MobileBy.ID,"com.zhao.myreader:id/tv_chapter_title").text)
    for index, element in enumerate(chapter_lists):
        locator = (MobileBy.ID, "com.zhao.myreader:id/tv_chapter_title")
        book_chapters.update({index: wait_visibility(element, *locator).text})

    """
    d、再去搜索里面按照该书名进行搜索
    """
    # 两个返回返回到搜索按钮界面
    driver.back()
    time.sleep(3)
    driver.back()
    time.sleep(2)
    # 进入搜索界面
    locator = (MobileBy.ID, "com.zhao.myreader:id/iv_search")
    search = wait_visibility(driver, *locator)
    search.click()
    # 输入随机获取的书籍名称
    locator = (MobileBy.ID, "com.zhao.myreader:id/et_search_key")
    search_key = wait_visibility(driver, *locator)
    search_key.send_keys(book_name)

    # 搜索书籍
    locator = (MobileBy.ID, "com.zhao.myreader:id/tv_search_conform")
    search_conform = wait_visibility(driver, *locator)
    search_conform.click()

    # 获取所有的章节目录
    search_books_elements = driver.find_elements(
        MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/lv_search_books_list"]/android.widget.LinearLayout')
    search_index = None
    for i in search_books_elements:
        search_book_name = i.find_element(MobileBy.ID, 'com.zhao.myreader:id/tv_book_name').text
        if search_book_name == book_name:
            search_index = search_books_elements.index(i)

    if search_index is None:
        raise ValueError("没有找到 《{}》 这本书".format(book_name))
    else:

        search_book = search_books_elements[search_index]
        # 获取书籍名
        search_book_name = search_book.find_element(MobileBy.ID, 'com.zhao.myreader:id/tv_book_name').text
        # 获取书籍简介
        search_book_desc = search_book.find_element(MobileBy.ID, 'com.zhao.myreader:id/tv_book_desc').text
        # 获取书籍作者
        search_book_author = search_book.find_element(MobileBy.ID, 'com.zhao.myreader:id/tv_book_author').text
        # 打开选中书籍
        search_book.click()
        search_book_chapters = dict()
        # 点击开始阅读
        locator = (MobileBy.ID, 'com.zhao.myreader:id/btn_read_book')
        search_read_book = wait_visibility(driver, *locator)
        search_read_book.click()
        # 点击书籍文字
        locator = (MobileBy.ID, "com.zhao.myreader:id/tv_content")
        search_content = wait_visibility(driver, *locator)
        search_content.click()
        # 点击目录
        locator = (MobileBy.ID, "com.zhao.myreader:id/ll_chapter_list")
        search_chapter_list = wait_clickable(driver, *locator)
        search_chapter_list.click()
        # 将目录中章节顺序和章节内容存储在字典中
        locator = (
        MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/lv_chapter_list"]/android.widget.LinearLayout')
        search_chapter_lists = wait_visibility_all(driver, *locator)
        for index, element in enumerate(search_chapter_lists):
            locator = (MobileBy.ID, "com.zhao.myreader:id/tv_chapter_title")
            search_book_chapters.update(
                {index: wait_visibility(element, *locator).text})

    assert book_name == search_book_name and book_desc == search_book_desc and book_author == search_book_author and book_chapters == search_book_chapters, "断言失败，数据不一致"


if __name__ == "__main__":
    import pytest

    # pytest.main(["-vs"])
    # pytest.main(["--html=report1.html"])
    # pytest.main(["-vs", "--html=report2.html"])
    pytest.main(["--html=./reports/report2.html", "--self-contained-html"])
