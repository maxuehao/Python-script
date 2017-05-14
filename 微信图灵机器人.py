# -*- coding: utf-8 -*-
import urllib,sys
import urllib2
import json
import webbrowser
import itchat

#解决网站编码问题
reload(sys)
sys.setdefaultencoding('utf8')

def robot(msg):
    values = {"key": "e046f1a4f213416d93753e0a985dacc9", "info": msg, "userid": '1'}
    data = urllib.urlencode(values)
    url = "http://www.tuling123.com/openapi/api"
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    talk = json.loads(response.read())
    #检测api返回的信息并格式化输出
    if talk.has_key('url') == False:
        if talk.has_key('list') == False:
            news = talk['text']
        else:
            food = talk['list']
            foodurl = food[1]
            if 'info' not in foodurl:
                for i in food:
                    news = '文章标题：',i['article'],'文章连锁：',i['detailurl'],'文章出处：',i['source']
            else:
                news = talk['text'], '材料准备：',foodurl['info'], '菜谱连锁：',foodurl['detailurl']
                #打开菜谱网页
                url = foodurl['detailurl']
                webbrowser.open(url)
    else:
        news = talk['text'], '网页连锁', talk['url']
        url = talk['url']
        webbrowser.open(url)
    return news

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = '亲，服务器故障...'
    if msg['Text'] == '开灯':
        reply = '亲，灯已打开...'
    elif msg['Text'] == '关灯':
        reply = '亲，灯已关闭...'
    else:
        reply = robot(msg['Text'])
    return reply or defaultReply

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
