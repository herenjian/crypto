# -*- coding: utf-8 -*- 

# @File:
# @Time :
# @Author :

class Page():
    def __init__(self):
        #此处应该读取配置文件
        self.addr = 'https://crypto.com/exchange/markets'
        self.token = ''

    def selectCurrency(self,driver,Currency='BTC'):
        # todo 选择币种，此处建议api获取字典
        Currencydict = {
            'All':'2',
            'USDT':'3',
            'USDC':'4',
            'BTC':'5',
            'CRO':'6'
        }
        buttonstr = '//*[@id="app"]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div/div['+Currencydict[Currency]+']'
        print(buttonstr)
        element = driver.find_element_by_xpath(buttonstr)
        return element


    def selectTrade(self,driver,Trade='1'):
        # todo 选择交易入口
        buttonstr = '//*[@id="app"]/div[1]/div[1]/div[3]/div[3]/table/tbody/tr['+str(Trade)+']/td[7]/div/button'
        element=driver.find_element_by_xpath(buttonstr)
        print(buttonstr)
        return element


