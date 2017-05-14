# -*- coding: utf-8 -*-
import itchat ,sys

#解决网站编码问题
reload(sys)
sys.setdefaultencoding('utf8')
list = {}

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    name = msg['FromUserName']
    user_name = itchat.search_friends(userName=name)
    user = user_name['RemarkName']
    try:
        if msg['Text'] == 'help':
            text = '本功能实现微信控制门禁开关，实用步骤：1.输入’注册‘ 2.根据提示注册数字ID密码 3.注册成功后可直接输入数字ID控制门禁开关'
            itchat.send(text, toUserName=name)
            print 'ok'
        elif msg['Text'] == '注册':
            itchat.send('请输入4位数字ID密码', toUserName=name)
        else:
            passwd = int(msg['Text'])
            if user not in list:
                list[user] = passwd
                itchat.send('注册成功，直接输入ID可控制门禁', toUserName=name)
            else:
                if list[user] == passwd:
                    itchat.send('门禁已开，欢迎光临' + user, toUserName=name)
                else:
                    itchat.send('密码错误，重新输入，更改密码请联系管理员', toUserName=name)
    except:
        itchat.send('微信智能门禁系统，请输入ID密码，未注册请先注册，帮助请输入help，From ——马雪浩', toUserName=name)
itchat.auto_login()
itchat.run()