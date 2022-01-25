# -*- coding: utf-8 -*-


from RunTest import *
import datetime
import os
if __name__ == '__main__':
    nowtime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H_%M_%S')
    parent = os.path.dirname(os.path.realpath(__file__))
    garder = os.path.dirname(parent)
    testcase_dir = garder+"/TestCase"
    report_dir = garder+"/TestReport"
    result = br(unittest.defaultTestLoader.discover(testcase_dir, "TestCase_MaketsPages.py"))
    result.report(
        filename="crypto"+nowtime+'自动化测试报告',
        description='cryptoUI自动化测试',
        report_dir=report_dir,
    )
