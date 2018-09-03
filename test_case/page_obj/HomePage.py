from test_case.module.method import Func
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from test_case.page_obj.LoginPage import LoginPage
from selenium.common.exceptions import*


class HomePage(Func):

    # 导航栏
    logo_loc = ('xpath', 'html/body/header/a')  # timecube logo
    MenuSearch_input_loc = ('id', 'search')  # 菜单搜索输入框
    MenuSearch_btn_loc = ('xpath', 'html/body/header/nav/div[2]/div')  # 搜索按钮
    SwitchLanguage_loc = ('class', 'earth')  # 切换语言
    SwitchRole_loc = ('class', 'team')  # 切换角色
    UserAccount_loc = ('id', 'UserAccount')  # 用户账号
    logOff_loc = ('id', 'logout')  # 登出

    #菜单栏
    Personnel_loc = ('xpath', "//*[@id='side']/li[1]/a")  # personnel模块
    Attedance_loc = ('xpath', "//*[@id='side']/li[2]/a")  # attenda模块
    Data_loc = ('xpath', "//*[@id='side']/li[3]/a")  # data模块
    Leave_loc = ('xpath', "//*[@id='side']/li[4]/a")  # leave模块
    Report_loc = ('xpath', "//*[@id='side']/li[5]/a")  # report 模块
    System_loc = ('xpath', "//*[@id='side']/li[6]/a")  # sysstem 模块

    # personnel子项
    Emp_info_loc = ('xpath', "//*[@id='side']/li[1]/ul/li[1]/a")  # personnel模块下的employee information
    Import_emp_loc = ('xpath', "//*[@id='side']/li[1]/ul/li[2]/a")  # personnel模块下的import employee
    structure_loc = ('xpath', "//*[@id='side']/li[1]/ul/li[3]/a")  # personnel模块下的structure
    menu_search_result_loc = ('xpath', "//span[@class='ng-binding']")  # 菜单栏搜搜结果
    # menu_search_result_loc = ('css selector', 'li.ng-scope>a>span')


    # 页面标题
    # page_title_loc = ('xpath', "//*[@id='navcontent']/div/span")
    page_title_loc = ('css selector', 'div#navcontent>div>span')

    def input_search_menu(self, info):
        self.send_keys(self.MenuSearch_input_loc, info)

    def click_search_btn(self):
        self.click(self.MenuSearch_btn_loc)
        time.sleep(10)

    # 导航栏搜索结果
    def get_menu_search_result(self):
        try:
            result = self.find_elements(self.menu_search_result_loc)
            results = []
            for i in result:
                results.append(i.text)
            return results
        except TimeoutException:
            # text = "don't exist"
            return False

    # 导航栏搜索
    def search_menu(self, info):
        self.input_search_menu(info)
        self.click_search_btn()
        result = self.get_menu_search_result()
        return result

    def click_logout(self):
        self.click(self.logOff_loc)

    # 登出
    def logout(self):
        self.click_logout()
        try:
            element = self.find_element(self.logOff_loc)
            return element
        except TimeoutException:
            return True

    # 跳转到主界面
    def switch_to_homepage(self):
        self.click(self.logo_loc)
        text = self.find_element(self.page_title_loc).text
        return text

    # 跳转到employee information界面
    def switch_to_EmpInfo(self):
        self.click(self.Personnel_loc)
        self.click(self.Emp_info_loc)
        time.sleep(5)
        text = self.find_element(self.page_title_loc).text
        return text

if __name__ == '__main__':
    driver = webdriver.Firefox()
    homepage = HomePage(driver)
    homepage.open('')
    time.sleep(10)
    name = "ricky.liu@zkteco.com"
    pwd = "123456"
    LoginPage(driver).login(name, pwd)
    # homepage.input_search_menu('emp')
    # homepage.click_search_btn()
    # print(homepage.search_menu('leave'))
    # print(homepage.logout())
    print(homepage.switch_to_EmpInfo())


