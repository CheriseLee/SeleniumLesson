import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail():
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
    content='<html><h1 style="color:red">我要自学网，自学成才</h1></html>'
    #邮件正文
    msg=MIMEText(content,'html','utf-8')
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
