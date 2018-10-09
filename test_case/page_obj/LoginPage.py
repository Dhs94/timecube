# coding:utf-8
from test_case.module.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import*

#url = r'http://150.109.56.75:8080/'


class LoginPage(BasePage):
    username_loc = ('id', 'email')  # 用户名输入框
    password_loc = ('id', 'password')  # 密码输入框
    submit_loc = ('id', 'loginBtn')  # 登录按钮
    register_loc = ('class', 'find_rst')  # 注册按钮
    findpwd_loc = ('class', 'find_pwd')  # 找回密码按钮
    loginerror_loc = ('xpath', "//*[@id='actions']/div[1]/span/lable")  # 错误信息
    loginsucess_loc = ('xpath', "//*[@id='UserAccount']/img")  # 用户信息图标
    account_loc = ('xpath', "//*[@id='modify-user-info-form']/fieldset[1]/div[1]/div/div/div/input")  # 账号信息

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
            time.sleep(5)
            # print("点击元素")
            return True

    def register(self):
        """免费注册"""
        self.click(self.register_loc)

    def forget_password(self):
        """忘记密码"""
        self.click(self.findpwd_loc)


    def is_login(self):
        """点击用户信息"""
        self.click(self.loginsucess_loc)
        value = self.get_attribute(self.account_loc, 'value')
        return value

    def login(self, username, password):
        """登录"""
        """判断是否跳转到登录界面"""
        try:
            self.find_element(self.username_loc)
            self.input_username(username)
            self.input_password(password)
            if self.find_element(self.submit_loc).is_enabled():
                self.click_submit()
            else:
                print("登录按键不可点")
                return("the button isn't clickable")
        except TimeoutException:
            print("页面不存在")

if __name__ == '__main__':
    driver = webdriver.Firefox()
    loginpage = LoginPage(driver)
    loginpage.open('')
    time.sleep(10)
    name = "kay.ding@zkteco.com"
    pwd = "123456"
    loginpage.login(name, pwd)
