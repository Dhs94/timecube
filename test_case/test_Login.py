# coding:utf-8
import unittest
from test_case.page_obj.LoginPage import LoginPage
from test_case.module import myunit, method
from ddt import ddt, unpack, data

@ddt
class Login_test(myunit.MyTest):

    def login_case(self, iterm, username, pwd, expect):
        loginpage = LoginPage(self.driver)
        loginpage.open('')
        print("测试项：%s" % iterm)
        result = loginpage.login(username, pwd)
        expect_result = expect
        self.assertEqual(result, expect_result)

    @data(*method.get_excel(r'D:\PycharmProjects\timecube\data\test_login.xlsx'))
    @unpack
    def test_login1(self, iterm, username, pwd, expect):
        self.login_case(iterm, username, pwd, expect)

    # def test_login2(self):
    #     u"""密码或账号错误"""
    #     self.login_case("ricky.liu@zkteco.com", "1234567", "密码不正确")
    #
    # def test_login3(self):
    #     u"""密码或账号未填"""
    #     self.login_case("", "", False)

if __name__ =="__main__":
    unittest.main()



