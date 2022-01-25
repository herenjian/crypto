# -*- coding:utf-8 -*-
import os
import time
from selenium.common.exceptions import NoSuchElementException



# 判断元素是否存在
def element_exist(driver, element):
    try:
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(element)
        driver.implicitly_wait(10)
        return True
    except NoSuchElementException:
        driver.implicitly_wait(10)
        return False


# 判断元素对象是否存在
def element_object_exist(func, driver):
    try:
        func(driver)
        return True
    except:
        return False




# 错误页面截图
def ErrorImage(driver):
    NowDate = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    NowTime = time.strftime("%H_%M_%S", time.localtime(time.time()))
    # UrlFrode = "D:\\AppAutomation\\AppData\\Results\\Android\\ErrorImage\\"
    UrlFrode = os.path.join(os.getcwd(), "../TestFile/ErrorImage/")
    FoldURL = UrlFrode + NowDate
    FileURL = UrlFrode + NowDate + "\\" + NowTime
    if not os.path.isdir(FoldURL) and not os.path.exists(FoldURL):
        os.mkdir(FoldURL)
    else:
        print("The fold is exist on list")
    ImageURL = FileURL + "Error_png.png"
    driver.d.screenshot(ImageURL)


# 判断对象是否存在当前页面
def ObjDisplay(driver, Objects):
    if Objects.is_displayed() == True:
        print("Passed: The page display object")
    else:
        print("Failed: The page does not displayed object")
        ErrorImage(driver)
        # exit()
    return Objects


