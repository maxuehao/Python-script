# coding=utf-8
import requests
from lxml import etree
import re
import os

#构造头文件
headers = {'Host':'www.xiaohuar.com',
'User-Agent':'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
}

def html(headers):
   #遍历网站结构
   for i in range(43):
      #content以二进制传输 text以文本传输
      r = requests.get('http://www.xiaohuar.com/list-1-%d.html'% i,headers=headers).content
      #解析xpath
      url = etree.HTML(r)
      #xpath提取名字信息
      name = url.xpath('//div[@class="item_t"]/div/a/img/@alt')
      # xpath提取图片url
      imgurl = url.xpath('//div[@class="item_t"]/div/a/img/@src')
      #遍历提取的信息
      for name, url in zip(name,imgurl):
         #正则表达去除imgurl非法字符
         link = re.findall(r"(.*?).file.(.*)",url)[0][1]
         urllinks = 'http://www.xiaohuar.com/d/file/%s'%link
         #请求图片数据（二进制传输）
         img = requests.get(urllinks,headers=headers).content
         #正则去除文件名非法字符
         p = re.compile('(\/)')
         name = p.sub('.',name)
         #将图片存取本地
         with open('/home/m/Desktop/img/%s' % name,'wb') as f:
            f.write(img)
         print urllinks,"\t","\t""\t",name
      
if __name__ == '__main__':
   html(headers)
   print('OK!!!')
