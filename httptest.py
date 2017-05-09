# coding=utf-8
import requests
from time import ctime
from multiprocessing import Pool

url = ['http://www.baidu.com',
       'http://www.btbu.edu.cn',
       'http://www.google.com',
       'http://www.btbu.edu.cn/1',
       'http://www.otureo.com'
]
#测试网页状态码
def test(url1):
    r = requests.get(url1)
    # 判断网站状态码
    if r.status_code != 200:
        #创建日志文件
        with open('testlog.txt', 'a') as f:
            f.write("Datetime: %s , Url: %s , Code: %d .\n" % (ctime(), url1, r.status_code))
    print ("Datetime: %s , Url: %s , Code: %d " % (ctime(), url1, r.status_code))

def log(i):
    try:
        test(i)
    except:
        with open('testlog.txt', 'a') as f:
            f.write("Datetime: %s , Url: %s , Code: Internet Erro" % (ctime(), i))
        print ("Datetime: %s , Url: %s , Code: Internet Erro" % (ctime(), i))

if __name__ == '__main__':
    #创建进程池
    p = Pool(4)
    for i in url:
        p.apply_async(log, args=(i,))
    p.close()
    p.join()
    print ("Test OK!!!")