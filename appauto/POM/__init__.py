# author_='Yuxuehong';
# date: 2023/8/22 13:22

"""
POM Page Object Model ==>页面对象模型
"""
from appium.webdriver.common.mobileby import MobileBy
from 封装的代码 import *

class PageObject:
    """
    将页面封装的元素全部放进来
    我们定位元素的时候，实际上是通过页面元素的定位方式和元素的值来定位
    所以在脚本里面，页面元的的代表者就是 定位方式 + 定位的值
    """

    city = (MobileBy.ACCESSIBILITY_ID, "书城")  #页面中书城这个元素
    book_list = (MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/rv_book_list"]/android.widget.LinearLayout')
    city_book_name = (MobileBy.ID, "com.zhao.myreader:id/tv_book_name")
    city_book_desc = (MobileBy.ID, "com.zhao.myreader:id/tv_book_desc")
    city_book_author = (MobileBy.ID, "com.zhao.myreader:id/tv_book_author")
    read_book = (MobileBy.ID, 'com.zhao.myreader:id/btn_read_book')
    book_content = (MobileBy.ID, "com.zhao.myreader:id/tv_content")
    chapter_list = (MobileBy.ID, "com.zhao.myreader:id/ll_chapter_list")
    chapter_list_info = (
        MobileBy.XPATH,'//*[@resource-id="com.zhao.myreader:id/lv_chapter_list"]/android.widget.LinearLayout')
    search = (MobileBy.ID, "com.zhao.myreader:id/iv_search")
    search_key = (MobileBy.ID, "com.zhao.myreader:id/et_search_key")
    search_conform = (MobileBy.ID, "com.zhao.myreader:id/tv_search_conform")
    search_books_list = (
        MobileBy.XPATH, '//*[@resource-id="com.zhao.myreader:id/lv_search_books_list"]/android.widget.LinearLayout')


    #上面是封装所有页面元素的数据


    #下面就是对常用的操作进行封装
    #既然是封装操作步骤，所以这里使用的是函数/方法
    #在我们脚本里面只有搜索这个流程是固定的
    #在搜索框输入，点击

    def search_action(self,driver,search_contant):
        """
        搜索这个动作
        :return:
        """
        wait_visibility(d= driver,*self.search_key).send_keys(search_contant) #搜索框输入
        wait_visibility(d=driver,*self.search_conform).click() #点击搜索

        return self #动作之间如果有关联就使用return self


