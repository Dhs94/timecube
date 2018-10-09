from test_case.module.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from test_case.page_obj.LoginPage import LoginPage
from test_case.page_obj.HomePage import HomePage

from selenium.common.exceptions import*
import re


class EmpInfoPage(BasePage):

    Add_btn_loc = ("id", "addEmployeeBtn")
    Edit_btn_loc = ("id", "editEmployeeBtn")
    Del_btn_loc = ("id", "delUserBtn")
    Export_btn_loc = ("id", "exportBtn")
    Emp_list_loc = ("css selector", "div#user_grid>div.k-auto-scrollable>table")  # 人员列表
    nextPage_loc = ("xpath", "//*[@id='user_grid']/div[3]/a[3]")
    prePage_loc = ("xpath", "//*[@id='user_grid']/div[3]/a[2]")
    lastPage_loc = ("xpath", "//*[@id='user_grid']/div[3]/a[4]")
    currentPage_loc = ("class name", "k-state-selected")

    """add page元素"""
    Add_page_loc = ("id", "addEmpWindow_wnd_title")
    EmpID_input_loc = ("id", "add_no")
    FirstName_input_loc = ("id", "first_name")
    LastName_input_loc = ("id", "last_name")
    MailBox_input_loc = ("id", "add_email")
    AddPosition_btn_loc = ("xpath", "//*[@id='profile']/form/fieldset[1]/div[6]/div[1]/span/span/span[2]")  # 添加职位按钮
    Position_loc = ("xpath", "//*[@id='profile']/form/fieldset[1]/div[6]/div[1]/span/span/input")
    Department_input_loc = ("id", "add_dept")
    HireDate_input_loc = ("id", "add_hiredate")
    Hiredate_btn_loc = ("xpath", "//*[@id='profile']/form/fieldset[2]/div[2]/div[2]/span/span/span")  # 雇用日期按钮
    Save_btn_loc = ("id", "addEmpSave")  # 保存add界面按钮
    closeSavePage_loc = ("xpath", "html/body/div[8]/div[1]/div/a")  # 关闭add界面按钮
    # closeSavePage_loc = ("css selector", "div.k-window>div>div>a")
    Add_success_loc = ("xpath", "html/body/div[7]/div/div")  # 添加成功提示
    Input_error_loc = ("xpath", "//*[@id='extAlertDialog']/div/div[2]")  # 输入错误提示
    # Add_success_loc = ("class", "k - notification - wrap")

    # add position page
    zkteco_department_loc = ("xpath", "//*[@id='select_tree']/ul/li/div/span[2]")  # zkteco部门
    test_position_loc = ("xpath", "//*[@id='select_tree']/ul/li/ul/li[1]/div/span[2]")  # test职位
    confirmPostion = ("id", "confimPosition")  # OK按键
    clearPosition = ("id", "clearPost")  # clear按键
    selectError = ("id", "select_error")  # select error
    AddError = ("xpath", "html/body/div[24]/div/div")  # add error
    closePostion = ("xpath", "html/body/div[23]/div[1]/div/a/span")  # 关闭add position页面


    def click_Add(self):
        """点击添加人员按钮"""
        self.click(self.Add_btn_loc)

    def input_EmpID(self, ID):
        """输入EmpID"""
        self.send_keys(self.EmpID_input_loc, ID)

    def input_FirstName(self, FirstName):
        """输入FirstName"""
        self.send_keys(self.FirstName_input_loc, FirstName)

    def input_LastName(self, LastName):
        """输入LastName"""
        self.send_keys(self.LastName_input_loc, LastName)

    def input_Mailbox(self, mailbox):
        """输入mailbox"""
        self.send_keys(self.MailBox_input_loc, mailbox)

    def click_positionBtn(self):
        """点击选择position按键"""
        self.click(self.AddPosition_btn_loc)

    def choose_position(self):
        """选择职位"""
        self.click(self.test_position_loc)

    def choose_department(self):
        """选择部门"""
        self.click(self.zkteco_department_loc)

    def click_OK(self):
        """点击OK保存"""
        self.click(self.confirmPostion)

    def click_clear(self):
        """点击 clear清除"""
        self.click(self.clearPosition)

    def input_hireday(self, birthday):
        """输入雇用日期"""
        self.send_keys(self.HireDate_input_loc, birthday)

    def set_position(self, loc):
        """设置position"""
        self.click_positionBtn()
        self.click(loc)
        text = self.find_element(self.selectError).text
        if text == "":
            self.click_OK()
        else:
            return text

    def test_input(self, inputkey):
        """通过关键字调用对应的函数"""
        input_map = {
            "EmpID": self.input_EmpID,
            "FirstName": self.input_FirstName,
            "LastName": self.input_LastName,
            "Mailbox": self.input_Mailbox,
            "hireday": self.input_hireday,
        }
        return input_map[inputkey]

    def nxt_page(self):
        """遍历下一页"""
        self.click(self.nextPage_loc)

    def get_TableContent(self):
        """获取列表人员信息"""
        arr = []
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        loc = ("xpath", "//*[@id='user_grid']/div[2]/table/tbody/tr")
        table_tr_list = self.find_elements(loc)
        for tr in table_tr_list:
            arr1 = (tr.text).split(" ")  # 以空格拆分成若干个(个数与列的个数相同)一维列表
            arr.append(arr1)  # 将表格数据组成二维的列表
        return arr

    def get_allTableContent(self):
        """获取所有页面人员信息"""
        arr = []
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        loc = ("xpath", "//*[@id='user_grid']/div[2]/table/tbody/tr")
        for i in range(5):
            # 获取4页的人员列表
            table_tr_list = self.find_elements(loc)
            for tr in table_tr_list:
                arr1 = (tr.text).split(" ")  # 以空格拆分成若干个(个数与列的个数相同)一维列表
                arr.append(arr1)
            time.sleep(2)
            self.nxt_page()
        return arr





    def add_Emp(self, ID, Fname, Lname, Mail, Hireday):
        """添加人员"""
        self.click_Add()
        self.set_position(loc=("xpath", "//*[@id='select_tree']/ul/li/ul/li[1]/div/span[2]"))  # 设置职位为test
        # 输入值
        # for inputkey, value in input:
            # self.test_input(inputkey)(value)
            # self.click(self.Save_btn_loc)
        self.input_EmpID(ID)
        self.input_FirstName(Fname)
        self.input_LastName(Lname)
        self.input_Mailbox(Mail)
        self.input_hireday(Hireday)
        self.click(self.Save_btn_loc)
        # v = self.get_attribute(self.EmpID_input_loc, "value")
        # print(v)
        # return v

        #     """点击保存后，若弹出报错提示框后，则返回框中信息，若没有报错
        #     检测是否返回人员列表界面，判断人员列表是否含有新增人员ID"""
        # try:
        #     text = self.find_element(self.Input_error_loc).text
        #     print(text)
        #     return text
        # except TimeoutException:
        #     try:
        #         self.find_element(self.Add_page_loc)
        #         print("the require items is blank")
        #         return ("the require items is blank")
        #     except TimeoutException:
        #         list = self.get_allTableContent()  # 获取所有人员列表
        #         ID_list = [x[4] for x in list]
        #         print(ID_list)# 获取Id列表
        #         print(input[0][1])
        #         if input[0][1] in ID_list:
        #             print("success")
        #             return True
        #         else:
        #             print("EMP lost")
        #             return("EMP lost")









if __name__ == '__main__':
    driver = webdriver.Firefox()
    EmpInfoPage = EmpInfoPage(driver)
    EmpInfoPage.open('')
    time.sleep(5)
    name = "ricky.liu@zkteco.com"
    pwd = "123456"
    LoginPage(driver).login(name, pwd)
    HomePage(driver).switch_to_EmpInfo()
    # t = EmpInfoPage.add_Emp([("EmpID", "23331"), ("FirstName", "23331"), ("LastName", "23331"), ("Mailbox", "23331@q.com"),("hireday", "2018-08-10")])

    EmpInfoPage.add_Emp("23342", "", "23342", "23342@q.com", "2018-08-10")
    # if t == "":
    #     print("yes")
    # else:
    #     print("no")








