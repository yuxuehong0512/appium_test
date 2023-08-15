# author_='Yuxuehong';
# date: 2023/8/15 9:15
# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["appium:deviceName"] = "emulator-5554"
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "7.1.2"
caps["appium:appPackage"] = "com.zhao.myreader"
caps["appium:appActivity"] = "com.zhao.myreader.ui.home.MainActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.XPATH, value="//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"华测\"]/android.widget.TextView")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"书架\"]/android.widget.TextView")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"书城\"]/android.widget.TextView")
el3.click()
el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")
el4.click()
el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.zhao.myreader:id/iv_search")
el6.click()
el7 = driver.find_element(by=AppiumBy.ID, value="com.zhao.myreader:id/et_search_key")
el7.click()
el8 = driver.find_element(by=AppiumBy.ID, value="com.zhao.myreader:id/et_search_key")
el8.send_keys("九")
el9 = driver.find_element(by=AppiumBy.ID, value="com.zhao.myreader:id/tv_search_conform")
el9.click()
el10 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]")
el10.click()
el11 = driver.find_element(by=AppiumBy.ID, value="com.zhao.myreader:id/btn_add_bookcase")
el11.click()
el12 = driver.find_element(by=AppiumBy.ID, value="com.zhao.myreader:id/btn_add_bookcase")
el12.click()
el13 = driver.find_element(by=AppiumBy.ID, value="com.zhao.myreader:id/btn_read_book")
el13.click()

driver.quit()