import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.163.com'

#发送邮箱及授权密码
user='lihh0727@163.com'
password='mxr870828'

sender='lihh0727@163.com'
receive='lihh@glodon.com'

subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:res">我要自学网，自学成才</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='lihh0727@163.com'
msg['To']='lihh@glodon.com'

smtp=smtplib.SMTP_SSL(smtpserver,465)
#进行认证
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send Email...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("Send success")

