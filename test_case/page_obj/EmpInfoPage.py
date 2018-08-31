from test_case.module.method import Func
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from test_case.page_obj.LoginPage import LoginPage
from test_case.page_obj.HomePage import HomePage
from selenium.common.exceptions import*


class EmpInfoPage(Func):

    Add_btn_loc = ("id", "addEmployeeBtn")
    Edit_btn_loc = ("id", "editEmployeeBtn")
    Del_btn_loc = ("id", "delUserBtn")
    Export_btn_loc = ("id", "exportBtn")

    # Add page
    EmpID_input_loc = ("id", "add_no")
    FirstName_input_loc = ("id", "first_name")
    LastName_input_loc = ("id", "last_name")
    MailBox_input_loc = ("id", "add_email")
    AddPosition_btn_loc = ("xpath", "//*[@id='profile']/form/fieldset[1]/div[6]/div[1]/span/span/span[2]")
    Position_loc = ("xpath", "//*[@id='profile']/form/fieldset[1]/div[6]/div[1]/span/span/input")
    Department_input_loc = ("id", "add_dept")
    HireDate_input_loc = ("id", "add_hiredate")
    Hiredate_btn_loc = ("xpath", "//*[@id='profile']/form/fieldset[2]/div[2]/div[2]/span/span/span")
    Save_btn_loc = ("id", "addEmpSave")
    closeSavePage_loc = ("xpath", "html/body/div[8]/div[1]/div/a")
    # closeSavePage_loc = ("css selector", "div.k-window>div>div>a")

    # add position page
    zkteco_department_loc = ("xpath", "//*[@id='select_tree']/ul/li/div/span[2]")  # zkteco部门
    test_position_loc = ("xpath", "//*[@id='select_tree']/ul/li/ul/li[1]/div/span[2]")  # test职位
    confirmPostion = ("id", "confimPosition")  # OK按键
    clearPosition = ("id", "clearPost")  # clear按键
    selectError = ("id", "select_error")  # select error
    AddError = ("xpath", "html/body/div[24]/div/div")  # add error
    closePostion = ("xpath", "html/body/div[23]/div[1]/div/a/span")  # 关闭add position页面

    # 日历
    today = ("xpath", "//*[@id='33a3a937-00bd-421c-b992-b354dfaaff25']/div[2]/a")
    # today = ("class", "k-nav-today")

    # 点击Add按键
    def click_Add(self):
        self.click(self.Add_btn_loc)

    # 输入EmpID
    def input_EmpID(self, ID):
        self.send_keys(self.EmpID_input_loc, ID)

    # 输入FirstName
    def input_FirstName(self, FirstName):
        self.send_keys(self.FirstName_input_loc, FirstName)

    # 输入LastName
    def input_LastName(self, LastName):
        self.send_keys(self.LastName_input_loc, LastName)

    # 输入mailbox
    def input_Mailbox(self, mailbox):
        self.send_keys(self.MailBox_input_loc, mailbox)

    # 点击选择position按键
    def click_positionBtn(self):
        self.click(self.AddPosition_btn_loc)

    # 选择职位
    def choose_position(self):
        self.click(self.test_position_loc)

    # 选择部门
    def choose_department(self):
        self.click(self.zkteco_department_loc)

    # 点击OK保存
    def click_OK(self):
        self.click(self.confirmPostion)

    # 点击 clear清除
    def click_clear(self):
        self.click(self.clearPosition)

    # 输入雇用日期
    def input_hireday(self, birthday):
        self.send_keys(self.HireDate_input_loc, birthday)

    # 点击雇用日期
    def click_hiredayBtn(self):
        self.click(self.Hiredate_btn_loc)

    # 选择雇佣日期为当前日期
    def click_currentday(self):
        self.click(self.today)

    # 设置position
    def set_position(self):
        self.click_positionBtn()
        self.click(Department_input_loc)
        #try:
        element = self.find_element(self.selectError)
        text = element.text
        return text
        except TimeoutException:
            self.click_OK()
            return True




if __name__ == '__main__':
    driver = webdriver.Firefox()
    EmpInfoPage = EmpInfoPage(driver)
    EmpInfoPage.open('')
    time.sleep(10)
    name = "ricky.liu@zkteco.com"
    pwd = "123456"
    LoginPage(driver).login(name, pwd)
    HomePage(driver).switch_to_EmpInfo()
    EmpInfoPage.click_Add()
    Department_input_loc = ("id", "add_dept")
    text = EmpInfoPage.set_position(Department_input_loc)
    # EmpInfoPage.click_positionBtn()
    # EmpInfoPage.choose_department()
    # selectError = ("id", "select_error")
    # text = EmpInfoPage.find_element(selectError).text
    # Department_input_loc = ("id", "add_dept")
    # t = EmpInfoPage.set_position(Department_input_loc)
    print(text)



