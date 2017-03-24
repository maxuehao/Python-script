import urllib2
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def get_url():
    html = 'http://www.otureo.com/'
    try:
        num = urllib2.urlopen(html).getcode()
    except urllib2.URLError as e:
        num = e.code
    return num


def send_emali():
    sender = '15624985416@sina.cn'
    receiver = 'maxuehao123@outlook.com'
    subject = 'From Otureo WEB server '
    username = '*****'
    password = '*****'

    message = MIMEText('web server cannot access ', 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.sina.cn')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
    smtp.quit()

if __name__ == '__main__':
    code = get_url()
    if code == 200:
        pass
    else:
        print '404'
        send_emali()

