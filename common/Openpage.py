# -*- coding: utf-8 -*- 

from selenium import webdriver
import sys




def open_page(addr='addr'):
    try:
        print(addr)
        browser = webdriver.Chrome()
        browser.get(addr)
    except:
        sys.exit(0)
    return browser



if __name__ == '__main__':
    pass

