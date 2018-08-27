# coding:utf-8
from test_case.module.method import Func
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

#url = r'http://150.109.56.75:8080/'


class LoginPage(Func):
    username_loc = ('id', 'email')
    password_loc = ('id', 'password')
    submit_loc = ('id', 'loginBtn')
    register_loc = ('class', 'find_rst')
    findpwd_loc = ('class', 'find_pwd')
    experience_loc = ('class', 'experience')
    loginerror_loc = ('xpath', "//*[@id='actions']/div[1]/span/lable")
    loginsucess_loc = ('xpath', "//*[@id='UserAccount']/img")
    account_loc = ('xpath', "//*[@id='modify-user-info-form']/fieldset[1]/div[1]/div/div/div/input")

    def input_username(self, username):
        """输入账号"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密"""
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        """点击登录按钮"""
        if not EC.element_to_be_clickable(self.submit_loc)(self.driver):
            # print("不可点")
            return False
        else:
            self.click(self.submit_loc)
            time.sleep(10)
            # print("点击元素")
            return True

    def register(self):
        """免费注册"""
        self.click(self.register_loc)

    def forget_password(self):
        """忘记密码"""
        self.click(self.findpwd_loc)

    def experience(self):
        """体验"""
        self.click(self.findpwd_loc)

    def login(self, username, password):
        """登录"""
        self.input_username(username)
        self.input_password(password)
        if self.click_submit():
            "登录按键可点"
            if not self.is_located(self.loginsucess_loc):
                "未登录"
                text = self.find_element(self.loginerror_loc).text
                # print(text)
                return text
            else:
                "登录"
                # self.click(self.loginsucess_loc)
                # value = self.get_attribute(self.account_loc, 'value')
                # # print(value)
                return ("login success")
        else:
            """不可点击"""
            # print("按键不可点击")
            return("the button isn't clickable")

if __name__ == '__main__':
    driver = webdriver.Firefox()
    loginpage = LoginPage(driver)
    loginpage.open('')
    time.sleep(10)
    name = "kay.ding@zkteco.com"
    pwd = "123456"
    loginpage.login(name, pwd)
