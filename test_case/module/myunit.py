# coding:utf-8
from test_case.module.method import browser
import unittest
import time


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = browser('firefox')
        cls. driver.implicitly_wait(10)
        # time.sleep(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

