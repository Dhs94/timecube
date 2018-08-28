# coding:utf-8
import unittest
from selenium import webdriver
from test_case.page_obj.LoginPage import LoginPage
from test_case.page_obj.HomePage import HomePage
from test_case.module import myunit, method
from ddt import ddt, unpack, data


class Homepage_test(myunit.MyTest):
    name = "ricky.liu@zkteco.com"
    pwd = "123456"
    # 菜单存在
    def menu_search_exist_case(self, info):
        homepage = HomePage(self.driver)
        homepage.open('')
        LoginPage(self.driver).login(self.name, self.pwd)
        results = homepage.search_menu(info)
        print(results)
        info = str.lower(info)
        for result in results:
            result = str.lower(result)
            self.assertIn(info, result)
        # self.assertIn(info, results)

    # 菜单不存在
    def menu_search_not_exist_case(self, info):
        # self.login()
        homepage = HomePage(self.driver)
        homepage.open('')
        # name = "ricky.liu@zkteco.com"
        # pwd = "123456"
        LoginPage(self.driver).login(self.name, self.pwd)
        result = homepage.search_menu(info)
        self.assertFalse(result)

    #登出
    def logout_case(self):
        homepage = HomePage(self.driver)
        homepage.open('')
        LoginPage(self.driver).login(self.name, self.pwd)
        result = homepage.logout()
        self.assertTrue(result)

    # 输入大写
    def test_menu_search_01(self):
        self.menu_search_exist_case('EMP')

    # 输入小写
    def test_menu_search_02(self):
        self.menu_search_exist_case('info')

    # 混合
    def test_menu_search_03(self):
        self.menu_search_exist_case('LeAVe')

    # 输入完整字符
    def test_menu_search_04(self):
        self.menu_search_exist_case('LeAVe records')

    # 输入不存在字符
    def test_menu_search_05(self):
        self.menu_search_not_exist_case('ll')

    # 测试登出
    def test_logout(self):
        self.logout_case()

if __name__ =="__main__":
    unittest.main()