import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
smtpserver='smtp.163.com'

#发送邮箱及授权密码
user='lihh0727@163.com'
password='mxr870828'

sender='lihh0727@163.com'
receives=['lihh@glodon.com']

#邮件主题和内容
subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:res">我要自学网，自学成才</h1></html>'

#获取最新报告
#报告存放位置
report_dir = r'C:\Users\Yuexl\Documents\GitHub\SeleniumLesson\trunk\unittestlihh\testreport'
#返回指定的文件夹中的文件列表
lists = os.listdir(report_dir)
#按时间顺序对文件排序
lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'))
print(lists)
print("latest report is:"+lists[-1])

#输出最新报告路径
file = os.path.join(report_dir,lists[-1])
print(file)
send_file = open(file,'rb').read()
# send_file=open(r'C:\Users\Yuexl\Documents\GitHub\SeleniumLesson\trunk\beijing.jpg','rb').read()
att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']="attachment;filename=aa.html"

msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)



#SSL协议端口号
smtp=smtplib.SMTP_SSL(smtpserver,465)
#进行认证
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send Email...")
smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print("Send success")
