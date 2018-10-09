import unittest
from test_case.page_obj.LoginPage import LoginPage
from test_case.page_obj.EmpInfoPage import EmpInfoPage
from test_case.page_obj.HomePage import HomePage
from test_case.module import myunit, BasePage
from selenium.common.exceptions import *
from test_case.module import Func
from ddt import ddt, unpack, data
from test_case.module.Log import Log

log = Log()
@ddt
class AddEmp_test(myunit.MyTest):

    def isEmpInList(self, ID):
        log.info("--------判断新增人员是否在列表中-------")
        """判断新增人员是否在列表中"""
        list = EmpInfoPage(self.driver).get_allTableContent()  # 获取所有人员列表
        ID_list = [x[4] for x in list]

        log.info("ID list:%s" % ID_list)
        log.info("ID:%s" % ID)
        # print(ID_list)  # 获取Id列表
        # print(ID)
        if ID in ID_list:
            log.info("success")
            return "success"
            # return ("adding emp is success")

    def isRequiredItemFilled(self):
        log.info("--------判断必填项是否填写-------")
        """判断必填项是否填写"""
        EmpID = EmpInfoPage(self.driver).get_attribute(EmpInfoPage.EmpID_input_loc, "value")
        Fname = EmpInfoPage(self.driver).get_attribute(EmpInfoPage.FirstName_input_loc, "value")
        Lname = EmpInfoPage(self.driver).get_attribute(EmpInfoPage.LastName_input_loc, "value")
        mail = EmpInfoPage(self.driver).get_attribute(EmpInfoPage.MailBox_input_loc, "value")
        Hireday = EmpInfoPage(self.driver).get_attribute(EmpInfoPage.HireDate_input_loc, "value")
        if EmpID == "":
            log.info("EmpID is not filled")
            return "EmpID is not filled"
        elif Fname == "":
            log.info("Fname is not filled")
            return "Fname is not filled"
        elif Lname == "":
            log.info("Lname is not filled")
            return "Lnameis not filled"
        elif mail == "":
            log.info("mail is not filled")
            return "mail is not filled"
        elif Hireday == "":
            log.info("Hireday is not filled")
            return "Hireday is not filled"

    def addEmp_case(self, ID, Fname, Lname, Mail, Hireday):

        empinfopage = EmpInfoPage(self.driver)
        empinfopage.open("")
        LoginPage(self.driver).login(self.name, self.pwd)
        HomePage(self.driver).switch_to_EmpInfo()
        empinfopage.add_Emp(ID, Fname, Lname, Mail, Hireday)
        """点击保存后，若弹出报错提示框后，则返回框中信息，若没有报错
        检测是否返回人员列表界面，判断人员列表是否含有新增人员ID"""
        try:
            log.info("--------判断是否弹出错误提示-------")
            text = empinfopage.find_element(empinfopage.Input_error_loc).text
            log.info("message ：%s" % text)
            return text
        except TimeoutException:
            try:
                log.info("--------判断是否还在add emp界面-------")
                e = empinfopage.find_element(empinfopage.Add_page_loc)
                log.info("add emp界面元素：%s" % e)
                r = self.isRequiredItemFilled()
                log.info("message：%s" % r)
                return r
            except TimeoutException:
                log.info("--------判断人员列表中是否有新增的人员-------")
                r = self.isEmpInList(ID)
                log.info("message：%s" % r)
                return r
    @data(*Func.get_excel(r"D:\PycharmProjects\timecube-new\data\Emp.xls"))
    @unpack
    def test_addEmp(self, ID, Fname, Lname, Mail, Hireday, expectresult):
        log.info("--------测试开始-------")
        result = self.addEmp_case(ID, Fname, Lname, Mail, Hireday)
        log.info("result: %s" % result)
        log.info("expect result:%s" % expectresult )
        self.assertEqual(result, expectresult)
        log.info("--------测试结束-------")

    # def testAddSuccess(self):
    #     log.info("--------测试开始-------")
    #     result = self.addEmp_case("201011", "201011", "201011", "201011@q.com", "2018-09-01")
    #     self.assertEqual(result, "Employee ID exists")
    #     log.info("--------测试结束-------")

if __name__ =="__main__":
    unittest.main()


