# -*- coding: utf-8 -*-


from TestCase import *
from common import logger
from common import CryptoMarkets, Openpage
logs = get_log()
img_path = get_img_path()

class MarketsPages(unittest.TestCase):
    """Markets"""

    _classSetupFailed = True

    _login_status = False

    report_img_path = img_path

    driver = None
    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), "img"))
        im = img.open(img_path + 'img.png')
        x, y = im.size
        out = im.resize((int(x / 4), int(y / 4)), resample=img.ANTIALIAS)
        out.save(img_path + './'+img_name + '.png', quality=100)
        out.close()

    def setUp(cls):
        page = CryptoMarkets.Page()
        driver = Openpage.open_page(page.addr)
        cls.driver = driver
        time.sleep(3)

    def tearDown(cls):
        # logs.info("end run test case: %s" % MarketsPages.__name__)
        cls.driver.quit()

    @BeautifulReport.add_test_img("市场页")
    def test_001_gotoTrade(self):
        try:
            driver = self.driver
            page = CryptoMarkets.Page()
            # 选择币种
            page.selectCurrency(driver,'BTC').click()
            # 断言页面元素是否存在
            #pass
            # 选择交易入口
            page.selectTrade(driver, '2').click()
        except :
            logs.log("出现错误")
            # 抛出异常这个用例就不会pass了
        finally:
            self.save_img("交易页面")




if __name__ == '__main__':
    # unittest.main()

    print(get_img_path())