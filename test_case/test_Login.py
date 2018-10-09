# coding:utf-8
import unittest
from test_case.page_obj.LoginPage import LoginPage
from test_case.module import myunit, BasePage
from test_case.module import Func
from ddt import ddt, unpack, data

@ddt
class Login_test(myunit.MyTest):

    def login_case(self, iterm, username, pwd, expect):
        """
            若登录按键不可点输出button isn't clickable
            否则点击登录后，若找不到登录用户信息即未登录，输出错误信息
            如果找得到则打印用户信息，返回success
        """
        loginpage = LoginPage(self.driver)
        loginpage.open('')
        print("测试项：%s" % iterm)
        if loginpage.login(username, pwd) =="the button isn't clickable":
            return ("the button isn't clickable")
        else:
            if not loginpage.is_located(loginpage.loginsucess_loc):
                "未登录"
                text = loginpage.find_element(loginpage.loginerror_loc).text
                # print(text)
                result = text
            else:
                "登录"
                print(loginpage.is_login())
                result = "login success"
        expect_result = expect
        self.assertEqual(result, expect_result)

    @data(*Func.get_excel(r'D:\PycharmProjects\timecube-new\data\test_login.xlsx'))
    @unpack
    def test_login1(self, iterm, username, pwd, expect):
        self.login_case(iterm, username, pwd, expect)


    # def test_login2(self):
    #     u"""密码或账号错误"""
    #     self.login_case("ricky.liu@zkteco.com", "123456", "login success")
    #
    # def test_login3(self):
    #     u"""密码或账号未填"""
    #     self.login_case("", "", False)

if __name__ =="__main__":
    unittest.main()




