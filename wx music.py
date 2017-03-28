# -*- coding: utf-8 -*-
import urllib, sys
import urllib2
import json
import itchat
import time
import mp3play

#解决网站编码问题
reload(sys)
sys.setdefaultencoding('utf8')

#获取音乐列表
def mp3player(song):
    #get百度音乐api
    url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?format=json&calback=&from=webapp_music&method=baidu.ting.search.catalogSug&query='+ song
    html = urllib2.urlopen(url).read()
    songid = json.loads(html)['song']
    #打印出json数据并格式化输出
    global list
    list = []
    list2 = []
    # 遍历歌曲信息
    for songs in songid:
        list.append(songs['songid'])
        list2.append(songs['songname'] + '————' + songs['artistname'])
    for i in list2:
        print ("歌曲id：%s   %s" % (list2.index(i), i))


#下载音乐
def get_mp3(id):
    print id
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

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    new_list.append(msg['text'])
    if len(new_list) == 1:
        song_name = list[0]
        try:
            news = mp3player(song_name)
        except:
            news = '请输入正确歌曲名...'
            new_list.clear()
        return news
    elif len(new_list) == 2:
        id = list[1]
        get_mp3(id)
        msg = '正在播放音乐：'+ list[0]
        new_list.clear()
        return msg

if __name__ == '__main__':
    new_list = []
    itchat.auto_login(hotReload=True)
    itchat.run()
