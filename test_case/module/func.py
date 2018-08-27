# coding:utf-8
from selenium import webdriver
import os
import yagmail
import xlrd

# 读取excel数据


# 截图函数
def capture_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    # base_dir = base_dir.replace("\\", "/")
    print(base_dir)
    file_path = base_dir + "/reports/image/" + file_name
    driver.get_screenshot_as_file(file_path)


# 发送邮件函数
def send_mail(receiver, content, attachment):
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="282410983@qq.com", password="bafkcomzsnixcaec", host="smtp.qq.com")
    # 邮件正文 yag.send(接受者，邮件主题，邮件正文，附件)
    yag.send(receiver, "来自dhs的邮件", content, attachment)


# 发送测试报告
def send_report(receiver, content, filename):
    yag = yagmail.SMTP(user="282410983@qq.com", password="bafkcomzsnixcaec", host="smtp.qq.com")
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    attachment = base_dir + "/reports/" + filename
    yag.send(receiver, "来自dhs的邮件", content, attachment)


# 读取excel数据
def get_excel(file):
    rows = []
    data = xlrd.open_workbook(file)
    sheet = data.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row)))
    return rows

if __name__ == "__main__":
    print(get_excel(r'C:\Users\Administrator\Desktop\test.xlsx'))








