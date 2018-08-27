#coding:utf-8
import os
import unittest
import HTMLTestRunner

case_path = os.path.join(os.getcwd(), 'test_case')
report_path = os.path.join(os.getcwd(), 'reports\\report.html')
#fp = open(report_path, 'wb')
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    return discover

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    with open(report_path, 'wb') as fp:
        runner =HTMLTestRunner.HTMLTestRunner(fp, title=u'Timecube测试报告', description=u'用例执行情况')
        runner.run(all_case())


