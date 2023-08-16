# author_='Yuxuehong';
# date: 2023/8/15 14:12
import time
import random

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

"""
目的：
验证通过搜索的功能搜索的书籍，与书城中获取的书籍是相同的：
"""

"""
a.打开读书屋，进入书城
"""
#1.连接方式一：已知活动名和包名
# caps = {
#     "appium:deviceName": "emulator-5554",
#     "platformName": "Android",
#     "appium:platformVersion": "7.1.2",
#     "appium:appPackage": "com.zhao.myreader",
#     "appium:appActivity": "com.zhao.myreader.ui.home.MainActivity"
# }

#2.连接方式2：不知道活动名和包名
caps = {
    "appium:deviceName": "emulator-5554",
    "platformName": "Android",
    "appium:platformVersion": "7.1.2",
    "app": "D://2023-L/python+selenium/app/01app自动化环境的搭建/dushuwu.apk",
    #"fullReset": True, #它会在运行完脚本后帮你卸载掉软件，默认为False不卸载
    "noReset":True #它在启动app之前，会清除你的app里面的数据，默认为False重置
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10) #隐形等待时间
#driver.wait_activity(activity="",timeout=10) #等待某个avtivity的资源加载完成
driver.find_element(AppiumBy.ACCESSIBILITY_ID,"书城").click()
book_elements = driver.find_elements(AppiumBy.XPATH,
                    '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zhao.myreader:id/rv_book_list"]/android.widget.LinearLayout')

"""
b.随机获取一本书,为验证数据点
"""

#使用随机数构建方式，获取一个在规定范围内的随机数作为元素的的下标

rand_index = random.randint(0,len(book_elements)-1)
print(rand_index)
book_element = book_elements[rand_index]


#c.通过随机指定的书去获取验证数据
book_name = book_element.find_element(AppiumBy.ID,"com.zhao.myreader:id/tv_book_name").text #获取书名
book_desc = book_element.find_element(AppiumBy.ID,"com.zhao.myreader:id/tv_book_desc").text #获取简介
book_author = book_element.find_element(AppiumBy.ID,"com.zhao.myreader:id/tv_book_author").text #获取作者名

#获取各章节的名字，并将各章节名字储存到字典中
book_element.click()
read_book_ele = (AppiumBy.ID,'com.zhao.myreader:id/btn_read_book')
read_book = Wait(driver,10).until(EC.visibility_of_element_located(read_book_ele))
read_book.click()
content_ele = (AppiumBy.ID,"com.zhao.myreader:id/tv_content")
content = Wait(driver,10).until(EC.visibility_of_element_located(content_ele))
content.click()
chapter_list_ele = (AppiumBy.ID,"com.zhao.myreader:id/ll_chapter_list")
chapter_list = Wait(driver,10).until(EC.visibility_of_element_located(chapter_list_ele))
chapter_list.click()
chapter_lists = driver.find_elements(AppiumBy.XPATH,'//*[@resource-id="com.zhao.myreader:id/lv_chapter_list"]/android.widget.LinearLayout')
book_chapter = dict()
#for i in chapter_lists:
#    book_chapter.append(i.find_element(AppiumBy.ID,"com.zhao.myreader:id/tv_chapter_title").text)
for index,element in enumerate(chapter_lists):
    book_chapter.update({index:element.find_element(AppiumBy.ID,"com.zhao.myreader:id/tv_chapter_title").text})

"""
d、再去搜索里面按照该书名进行搜索
"""
#两个返回返回到搜索按钮界面
driver.back()
time.sleep(3)
driver.back()
time.sleep(2)
#进入搜索界面
search_ele = (AppiumBy.ID,"com.zhao.myreader:id/iv_search")
search = Wait(driver,10).until(EC.visibility_of_element_located(search_ele))
search.click()

#输入随机获取的书籍名称
search_key_ele = (AppiumBy.ID,"com.zhao.myreader:id/et_search_key")
search_key = Wait(driver,10).until(EC.visibility_of_element_located(search_key_ele))
search_key.send_keys(book_name)

#搜索书籍
search_conform_ele = (AppiumBy.ID,"com.zhao.myreader:id/tv_search_conform")
search_conform = Wait(driver,10).until(EC.visibility_of_element_located(search_conform_ele))
search_conform.click()

#获取所有的章节目录
search_books_elements = driver.find_elements(AppiumBy.XPATH,'//*[@resource-id="com.zhao.myreader:id/lv_search_books_list"]/android.widget.LinearLayout')
search_index = None
for i in search_books_elements:
    search_book_name = i.find_element(AppiumBy.ID,'com.zhao.myreader:id/tv_book_name').text
    if search_book_name == book_name :
        search_index = search_books_elements.index(i)
search_book_chapter = dict()
if search_index is None:
    raise ValueError("没有找到 《{}》 这本书".format(book_name))
else:

    search_book = search_books_elements[search_index]
    #获取书籍名
    search_book_name = search_book.find_element(AppiumBy.ID,'com.zhao.myreader:id/tv_book_name').text
    #获取书籍简介
    search_book_desc = search_book.find_element(AppiumBy.ID,'com.zhao.myreader:id/tv_book_desc').text
    #获取书籍作者
    search_book_author = search_book.find_element(AppiumBy.ID,'com.zhao.myreader:id/tv_book_author').text
    #打开选中书籍
    search_book.click()
    #点击开始阅读
    search_read_book_ele = (AppiumBy.ID, 'com.zhao.myreader:id/btn_read_book')
    search_read_book = Wait(driver, 10).until(EC.visibility_of_element_located(search_read_book_ele))
    search_read_book.click()
    #点击书籍文字
    search_content_ele = (AppiumBy.ID, "com.zhao.myreader:id/tv_content")
    search_content = Wait(driver, 10).until(EC.visibility_of_element_located(search_content_ele))
    search_content.click()
    #点击目录
    search_chapter_list_ele = (AppiumBy.ID, "com.zhao.myreader:id/ll_chapter_list")
    search_chapter_list = Wait(driver, 10).until(EC.visibility_of_element_located(search_chapter_list_ele))
    search_chapter_list.click()
    #将目录中章节顺序和章节内容存储在字典中
    search_chapter_lists = driver.find_elements(AppiumBy.XPATH,
                                         '//*[@resource-id="com.zhao.myreader:id/lv_chapter_list"]/android.widget.LinearLayout')
    for index, element in enumerate(search_chapter_lists):
        search_book_chapter.update({index: element.find_element(AppiumBy.ID, "com.zhao.myreader:id/tv_chapter_title").text})

    if book_name == search_book_name and book_desc == search_book_desc and book_author == search_book_author and book_chapter == search_book_chapter:
        print("通过搜索功能搜索的书籍，与从书城获取的书籍相同")

driver.quit()