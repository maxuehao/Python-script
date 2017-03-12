# -*- coding: utf-8 -*-
import urllib
import urllib2
import os
import subprocess
import json
import sys
import mp3play
import time
import webbrowser


def mp3player():
    while True:
        song = raw_input('请输入要查询的歌曲名：')
        try:
            #get百度音乐api
            url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?format=json&calback=&from=webapp_music&method=baidu.ting.search.catalogSug&query='+ song
            html = urllib2.urlopen(url).read()
            songid = json.loads(html)['song']
            break
            #打印出json数据并格式化输出
        except:
            print '亲，请输入正确的歌曲名哦~'
            continue
    list = []
    list2 = []
    #遍历歌曲信息
    for songs in songid:
        #print songs['songname'], songs['artistname'], songs['songid']
        list.append(songs['songid'])
        list2.append(songs['songname']+'————'+ songs['artistname'])
    for i in list2:
        print ("歌曲id：%s   %s" % (list2.index(i),i))
    id = raw_input('输入歌曲id:')

    #get MP3下载
    playurl = 'http://tingapi.ting.baidu.com/v1/restserver/ting?format=json&calback=&from=webapp_music&method=baidu.ting.song.play&songid='+ list[int(id)]
    songhtml = urllib2.urlopen(playurl).read()
    mp3url = json.loads(songhtml)['bitrate']
    urllib.urlretrieve(mp3url['show_link'],"demo.mp3")

    #调用MP3play模块
    mp3 = mp3play.load('demo.mp3')
    mp3.play()
    print ('播放中...')
    times = mp3.seconds()
    time.sleep(int(times))

#解决地理api编码问题
reload(sys)
sys.setdefaultencoding('utf-8')

#检测网络连通性
fnull = open(os.devnull, 'w')
return1 = subprocess.call('ping www.baidu.com', stdout=fnull, stderr=fnull)
if return1:
    print '亲，请检查你的网络哦'
    exit()
else:
    print '连接网络服务器成功...'
fnull.close()

#定位当前使用者位置
apiurl = "https://api.map.baidu.com/location/ip?ak=5qE75i1B1WgsXx7YwGQgQeZwtfRfD3kS&coor=bd09ll"
apidata = urllib2.urlopen(apiurl).read()
place = json.loads(apidata)
city = place['content']
home = city['address_detail']
home1 = home['city']

#定义用户位置
Loc = str(home1)

#定义用户ID
ID = raw_input("请输入你的id:")
print ID ,'你好啊！'

while True:
    temp = raw_input("请输入聊天内容:")
    #物联网接口
    if temp == "开灯":
        print '亲，灯已打开哦'
        continue
    elif temp == "关灯":
        print '亲，灯已关闭啦'
        continue
    elif temp == "打开空调":
        print '亲，空调已打开啦'
        continue
    elif temp == "查看温度":
        print '亲，现在室温13度，空气质量221。'
        continue
    elif temp == "播放歌曲":
        mp3player()
        print '我唱的好不好听啊。'
        continue
    elif temp == "喂狗粮":
        print '自动喂食机已启动...'
        continue
    values = {"key": "e046f1a4f213416d93753e0a985dacc9", "info": temp, "userid": ID, "loc": Loc}
    data = urllib.urlencode(values)
    url = "http://www.tuling123.com/openapi/api"
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    talk = json.loads(response.read())

#检测api返回的信息并格式化输出
    if talk.has_key('url') == False:
        if talk.has_key('list') == False:
            print talk['text']
        else:
            food = talk['list']
            foodurl = food[1]
            print talk['text'], '材料准备：',foodurl['info'], '菜谱连锁：',foodurl['detailurl']
            #打开菜谱网页
            url = foodurl['detailurl']
            webbrowser.open(url)
    else:
        print talk['text'], '网页连锁', talk['url']
        url =  talk['url']
        webbrowser.open(url)