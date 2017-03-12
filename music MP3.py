#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
import mp3play
import urllib
import time
import sys
#解决aciss编码问题
reload(sys)
sys.setdefaultencoding('utf8')

def mp3player():
    song = raw_input('请输入要查询的歌曲名：')
    #get百度音乐api
    url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?format=json&calback=&from=webapp_music&method=baidu.ting.search.catalogSug&query='+ song
    html = urllib2.urlopen(url).read()
    songid = json.loads(html)['song']
    #打印出json数据并格式化输出
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
    time.sleep(times)

mp3player()
