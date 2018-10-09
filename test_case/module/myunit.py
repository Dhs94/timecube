# coding:utf-8
from test_case.module.Func import browser
from test_case.module.BasePage import BasePage
import unittest
import time


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = browser("firefox")
        cls. driver.implicitly_wait(10)
        # time.sleep(10)
        cls.driver.maximize_window()
        cls.name = "ricky.liu@zkteco.com"
        cls.pwd = "123456"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

