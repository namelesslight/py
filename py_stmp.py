#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py_stmp.py
# @Time      :2021/10/14 09:37:40
# @Author    :ZCL
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

mail_host=""  #设置smtp服务器
mail_user=""    #发送者邮箱
mail_pass=""   #密码口令 

sender = ''#发送者
receivers = ['']#接收者
subject = '这是标题'# 邮件标题

#此处取标题
message = MIMEMultipart()
message['From'] = ''#发送者邮箱
message['To'] = ''#接收者邮箱
message['Subject'] = Header(subject, 'utf-8')

message.attach(MIMEText('Python 邮件发送测试...', 'plain', 'utf-8'))
att1=MIMEText(open('a.txt','rb',encoding='utf-8').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.txt"'#此处的test.txt是发送后的文件名，任意取名，但文件后缀名不能改，如此处的.txt
message.attach(att1)

smtpObj = smtplib.SMTP() 
smtpObj.connect(mail_host)    # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print ("邮件发送成功")
("Error: 无法发送邮件")
smtpObj.quit()