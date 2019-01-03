import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import time
import BSTestRunner
import unittest

def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    #发送邮箱服务器
    smtpserver='smtp.163.com'

    #发送邮箱及授权密码
    user='lihh0727@163.com'
    password='mxr870828'

    #发送邮箱和接收邮箱
    sender='lihh0727@163.com'
    receives=['463836190@qq.com']

    #邮件主题和内容
    subject='Web Selenium 自动化测试报告'
    # content='<html><h1 style="color:red">我要自学网，自学成才</h1></html>'
    #邮件正文
    msg=MIMEText(mail_content,'html','utf-8')
    msg['Subject'] = subject
    msg['From']=sender
    msg['To']=','.join(receives)

    #SSL协议端口号,不同邮箱端口不同
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    #向服务器标识用户身份
    smtp.helo(smtpserver)
    #服务器返回结果确认
    smtp.ehlo(smtpserver)
    #登录邮箱服务器用户名密码
    smtp.login(user,password)

    print("Start send Email...")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("Send success")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对文件排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\'))
    print(lists)
    print("latest report is:" + lists[-1])

    # 输出最新报告路径
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    #存放报告的文件夹
    report_dir = './testreport'
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    #报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #报告文件完整路径
    report_name = report_dir + '/' + now + 'result.html'

    #打开文件在报告文件写入测试结果
    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title="Test Report",description="test case result")
        runner.run(discover)
    f.close()

    latest_report = latest_report(report_dir)
    send_mail(latest_report)