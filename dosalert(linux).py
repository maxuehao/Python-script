# -*- coding: utf-8 -*-
#检测当前连接80端口服务端ip数量，如有同一ip大量连接，可通过邮箱警报
import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def firewall():
    while True:
        frequency = subprocess.check_output(
        "netstat -nat | grep -w 80 |grep -w tcp |awk '{print $5}'|awk -F: '{print $1}'|sort|uniq -c|sort -nr|head -1|awk '{print $1}'",
        shell=True)
        if int(frequency) > 20:
            temp = subprocess.check_output(
            "netstat -nat | grep -w 80 | grep -w tcp |awk '{print $5}'|awk -F: '{print $1}'|sort|uniq -c|sort -nr|head -1",
            shell=True)
            send_emali(temp)
            print 'ok'
            time.sleep(60)
        else:
            time.sleep(5)

def send_emali(temp):
    sender = '15624985416@sina.cn'
    receiver = 'maxuehao123@outlook.com'
    subject = 'From DOS attack warning '
    username = '*****'
    password = '*****'
    message = MIMEText(temp, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.sina.cn')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
    smtp.quit()

if __name__ == "__main__":
    firewall()
