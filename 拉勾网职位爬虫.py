# coding=utf-8
import requests
import json
import sys

#解决编码问题
reload(sys)
sys.setdefaultencoding('utf8')

#处理爬取页数
def page(url,headers):
    r = requests.get(url,headers=headers).content
    #解析json
    temp = json.loads(r)
    num_page = temp['content']['positionResult']['totalCount']
    #总岗位数除以每页岗位数
    pages = int(num_page)/14 + 1
    return pages

def html():
    temp = page(url,headers)
    for i in range(temp):
        if i == 0:
            pass
        else:
            urls = 'http://www.lagou.com/jobs/positionAjax.json?city=北京&first=true&kd=%s&pn=%s'%(temp1,i)
            r = requests.get(urls, headers=headers).content
            date = json.loads(r)
            lists =  date['content']['positionResult']['result']
            for i in lists :
                #发布时间
                time = i['createTime']
                #类型
                type = i['firstType']
                type1 =i['secondType']
                name = i['positionName']
                year = i['workYear']
                edu = i['education']
                com = i['companyFullName']
                mon = i['salary']
                #写入文本文件
                with open('testlog.txt', 'a') as f:
                    f.write('发布时间：'+time+'\t'+'岗位:'+name+'\t'+'工资:'+mon+'\t'+'学历:'+edu+'\t'+'公司名称:'+com+'\n')
                print '发布时间：'+time+'\t'+'招聘类型:'+type+'\t'+'技术类型:'+type1+'\t'+'岗位:'+name+'\t'+'经验:'+year+'\t'+'学历:'+edu+'\t'+'公司名称:'+com+'\n'

if __name__=='__main__':
    # 构造请求头文件
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh,zh-CN;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'user_trace_token=20170225094555-6e7b2a7e3aa64609945fc33d0920adee; LGUID=20170225094555-2618ec1d-fafc-11e6-8bf6-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=016e3c0cb010463abeb9a73d65235e0a; _gid=GA1.2.1242677326.1494789972; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1494770451,1494770451,1494789833,1494789836; _ga=GA1.2.454300071.1489908242; JSESSIONID=ABAAABAACDBABJBE031AE5AF1ACBA63F6C567A7886A5E1D',
    'Host':'www.lagou.com',
    'Upgrade-Insecure-Requests':'',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    temp1 = raw_input('请输入爬去岗位：\n')
    url = 'http://www.lagou.com/jobs/positionAjax.json?city=北京&first=true&kd=%s&pn=1'%temp1
    html()