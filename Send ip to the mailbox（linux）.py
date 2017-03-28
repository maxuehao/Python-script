# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import socket
import os

#检测是否联网
while True:
    return1=os.system('ping -c 2 www.baidu.com')
    if return1 == 0:
        print ('ok')
        break
    else:
        print ('no')

#获取本地ip
def Get_local_ip():
 try:
  csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  csock.connect(('8.8.8.8', 80))
  (addr, port) = csock.getsockname()
  csock.close()
  return addr
 except socket.error:
  return "127.0.0.1"
  
if __name__ == "__main__":
 ip = Get_local_ip() 


#将本机ip地址通过邮件发送给主机邮箱
sender = '15624985416@sina.cn'
receiver = 'maxuehao123@outlook.com'
subject = 'From Raspberry Pi '
smtpserver = 'smtp.sina.cn'
username = '*****'
password = '*****'

message = MIMEText(ip, 'plain', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.sina.cn')
smtp.login(username, password)
smtp.sendmail(sender, receiver, message.as_string())
smtp.quit()
