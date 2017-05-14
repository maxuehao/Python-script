# -*- coding: utf-8 -*-
import urllib, urllib2
import json, sys
import mp3play, time

#解决网站编码问题
reload(sys)
sys.setdefaultencoding('utf8')

#获取音乐列表
def mp3player(song):
    while True:
        try:
            #get百度音乐api
            url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?format=json&calback=&from=webapp_music&method=baidu.ting.search.catalogSug&query='+ song
            html = urllib2.urlopen(url).read()
            songid = json.loads(html)['song']
            break
            #打印出json数据并格式化输出
        except:
            print'亲，请输入正确的歌曲名哦~'
            continue
    global list
    list = []
    list2 = []
    #遍历歌曲信息
    for songs in songid:
        list.append(songs['songid'])
        list2.append(songs['songname']+'————'+ songs['artistname'])
    for i in list2:
        print ("歌曲id：%s   %s" % (list2.index(i),i))
    ID = raw_input('请输入歌曲ID：')
    return ID

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

if __name__ == '__main__':
    song = raw_input('输入歌曲名：')
    get_mp3(mp3player(song))
