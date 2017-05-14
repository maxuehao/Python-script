# -*- coding: utf-8 -*-
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    #获取转发到的微信号的id
    kxname = itchat.search_friends(name='***')
    kx_username = kxname[0]
    #获取发送消息者的id
    name = msg['FromUserName']
    user_name = itchat.search_friends(userName=name)
    if user_name['RemarkName'] == '':
        pass
    else:
        #user_name['RemarkName']为发送消息者备注
        news = user_name['RemarkName']+':'+msg['Text']
        itchat.send(news, toUserName=kx_username['UserName'])

itchat.auto_login()
itchat.run()