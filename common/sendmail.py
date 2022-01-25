# -*- coding: utf-8 -*- 

# @Time :
# @Author :

import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

conf = configparser.ConfigParser()
conf.read(rootPath+"/config/settings.ini", encoding='utf-8')

username = conf.get("mail", "chunhuihuang@yitaichang.cn")
password = conf.get("mail", "Huangchunhui520")

def send_email(msg, msg_to,subject):
    smtpserver = 'smtp.163.com'
    sender = "HeyTea <{}>".format("chunhuihuang@yitaichang.cn")
    # subject = 'QApplePay线上运行健康检查'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender.strip('"')
    msgRoot['To'] = ','.join(msg_to)
    msgText = MIMEText('{0}'.format(msg), 'html', 'utf-8')
    msgRoot.attach(msgText)
    smtp = smtplib.SMTP()
    i, j = 1, 1
    while True:
        try:
            smtp.connect(smtpserver)
            smtp.login(username, password)
        except Exception :
            print("第{0}次登陆失败".format(i))
            if i < 3:
                i += 1
                continue
            else:
                return 1000
        try:
            smtp.sendmail(username, msgRoot['To'].split(','), msgRoot.as_string())
        except Exception as msg:
            print("第{0}次发送失败".format(j), msg)
            if j < 3:
                j += 1
                continue
            else:
                return 1001
        print('SUCCESS')
        break
    smtp.quit()
    return 200
