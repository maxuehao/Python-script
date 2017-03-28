# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib

def login():
    filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    # 声明一个MozillaCookieJar对象实例来保存cookie，并写入文件
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    values = {"USERNAME": '*****', "PASSWORD": '*****'}
    # 将提交表单的用户名密码打包成字典values
    data = urllib.urlencode(values)
    # 将values字典利用urlencode编码
    url = "http://10.0.40.216/xk/LoginToXk"
    # 确定登陆界面url
    opener.open(url, data)
    # 模拟登录，并把cookie保存到变量
    cookie.save(ignore_discard=True, ignore_expires=True)
    # 保存cookie到cookie.txt中
    while True:
        data = raw_input("请输入选课代码：\n 1,专业选修课 \n 2,文学与艺术审美 \n 3,经法与社会分析 \n 4,素养与个体成长 \n 5,历史与文化传承 \n 6,自然与科学文明: \n")
        if data.isdigit():
            temp = int(data)
            if temp == 1:
                gradeUrl = "http://10.0.40.216/xk/getXkInfo?jx0502zbid=173&jx0502id=72"
                break
            elif temp == 2:
                gradeUrl = "http://10.0.40.216/xk/getXkInfo?jx0502zbid=170&jx0502id=75"
                break
            elif temp == 3 :
                gradeUrl = "http://10.0.40.216/xk/getXkInfo?jx0502zbid=174&jx0502id=73"
                break
            elif temp == 4 :
                gradeUrl = "http://10.0.40.216/xk/getXkInfo?jx0502zbid=169&jx0502id=74"
                break
            elif temp == 5 :
                gradeUrl = "http://10.0.40.216/xk/getXkInfo?jx0502zbid=171&jx0502id=76"
                break
            elif temp == 6 :
                gradeUrl = "http://10.0.40.216/xk/getXkInfo?jx0502zbid=172&jx0502id=77"
                break
            else:
                print ('请输入有正确课程代码！')
        else:
            print('非法输入！')
    result = opener.open(gradeUrl)
    # 利用cookie请求访问另一个网址，此网址登陆后的网址
    print result.read()
login()