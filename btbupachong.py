# coding=utf-8
import requests
from lxml import etree
import os 
import sys  

#解决编码问题
reload(sys)  
sys.setdefaultencoding('utf8')   

#定义头文件
headers = {'Host':'www.btbu.edu.cn',
'User-Agent':'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
}


def html(headers):
   r = requests.get('http://www.btbu.edu.cn/news/mtgs/index.htm',headers=headers).content.decode('utf-8')
   #Xpath解析
   url = etree.HTML(r)
   links = url.xpath('//option/@value')
   for i in links:
      #迭代爬取
      r = requests.get('http://www.btbu.edu.cn/news/mtgs/%s'% i,headers=headers).content.decode('utf-8')
      url = etree.HTML(r)
      time = url.xpath('//div[@class="box02_con02 box_list"]/ul/li/span/text()') 
      title = url.xpath('//div[@class="box02_con02 box_list"]/ul/li/a/text()')
      links = url.xpath('//div[@class="box02_con02 box_list"]/ul/li/a/@href')
      for a, b, c in zip(time, title,links):
         with open('testlog.txt', 'a') as f:
            #写日志文件TXT
            f.write(a+'\t'+'http://www.btbu.edu.cn/news/mtgs/%s'% c+'\t'+b.strip()+'\n')
         print a,'\t','http://www.btbu.edu.cn/news/mtgs/%s'% c,'\t',b.strip()
      

if __name__ == '__main__':
   html(headers)
   print('OK!!!')
