 # coding=utf-8
import requests
from lxml import etree
import os
import sys

#解决网站编码
reload(sys)
sys.setdefaultencoding('utf-8')

#构造请求头文件
headers = {'Host':'www.autohome.com.cn',
'User-Agent':'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
}

#下载图片
def download(urls,n,p):
   rs = requests.get(urls).text
   r = etree.HTML(rs)
   imgurl = r.xpath('//div[@class="column grid-16"]/div[@class="uibox"]/div[2]/ul/li/a/img/@src')
   imgname = r.xpath('//div[@class="column grid-16"]/div[@class="uibox"]/div[2]/ul/li/a/img/@alt')
   for a,b in zip(imgurl,imgname):
      img = requests.get(a).content
      with open('/home/m/Desktop/imgcar/%s%s' % (n,b),'wb') as f:
         print p+"\t"+n+"\n"
         f.write(img)

#返回抓取图片的网页URL
def html(headers):
   r = requests.get('http://www.autohome.com.cn/car/?pvareaid=101452',headers=headers).text
   url = etree.HTML(r)
   name = url.xpath('//ul[@class="rank-list-ul"]/li[@id]/h4/a/text()')
   price = url.xpath('//a[@class="red"]/text()')
   img = url.xpath('//ul[@class="rank-list-ul"]/li/div[2]/a[@id]/@href')
   for n,i,p in zip(name,img,price):
      download(i,n,p)
      #打印日志
      #with open('log.text','a') as f:
         #f.write(i+"\t"+p+"\t"+n+"\n")
      
if __name__ == '__main__':   
   html(headers)
