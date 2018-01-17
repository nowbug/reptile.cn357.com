# /usr/bin
# coding:utf-8
import urllib2
import re
import numpy as np
import pandas as pd
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

f = open('data.txt', 'w')


def listp():
    listinfo = []
    url = 'http://www.cn357.com/notice_list'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 将user_agent写入头信息
    headers = {'User-Agent': user_agent}

    try:
        req = urllib2.Request(url, '', headers)
        response = urllib2.urlopen(req)
        the_page = response.read().decode('gbk')
        content_re = '<a href="/notice_(.*)" target="_blank">(.*)</a> '

        listtemp = re.findall(content_re, the_page)
        for i in listtemp:
            listinfo.append('http://www.cn357.com/notice_' + str(i[0]))
        return listinfo
    except Exception as e:
        print e
        print '被拦截了休息10s并重试'
        time.sleep(15)
        try:
            req = urllib2.Request(url, '', headers)
            response = urllib2.urlopen(req)
            the_page = response.read().decode('gbk')
            content_re = '<a href="/notice_(.*)" target="_blank">(.*)</a> '

            listtemp = re.findall(content_re, the_page)
            for i in listtemp:
                listinfo.append('http://www.cn357.com/notice_' + str(i[0]))
            return listinfo
        except Exception as e:
            print e
            print '被拦截了休息10s并重试'
            time.sleep(10)
            try:
                req = urllib2.Request(url, '', headers)
                response = urllib2.urlopen(req)
                the_page = response.read().decode('gbk')
                content_re = '<a href="/notice_(.*)" target="_blank">(.*)</a> '

                listtemp = re.findall(content_re, the_page)
                for i in listtemp:
                    listinfo.append('http://www.cn357.com/notice_' + str(i[0]))
                return listinfo
            except Exception as e:
                print e
                print '被拦截了休息10s并重试'
                time.sleep(15)


def table(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 将user_agent写入头信息
    headers = {'User-Agent': user_agent}
    try:
        req = urllib2.Request(url, '', headers)
        response = urllib2.urlopen(req)
        the_page = response.read().decode('gbk')
        content_re = u'<div class="r">本批次共 (.*?) 个车型</a></div>'
        listtemp = re.findall(content_re, the_page)
        test = []
        page = 1
        if int(listtemp[0]) > 60:
            page = int(listtemp[0]) / 60
            if int(listtemp[0]) % 60 == 0:
                pass
            else:
                page = page + 1
        for z in range(1, page + 1):
            url1 = url + '_' + str(z)
            test.append(url1)
        return test
    except Exception as e:
        time.sleep(15)
        try:
            req = urllib2.Request(url, '', headers)
            response = urllib2.urlopen(req)
            the_page = response.read().decode('gbk')
            content_re = u'<div class="r">本批次共 (.*?) 个车型</a></div>'
            listtemp = re.findall(content_re, the_page)
            test = []
            page = 1
            if int(listtemp[0]) > 60:
                page = int(listtemp[0]) / 60
                if int(listtemp[0]) % 60 == 0:
                    pass
                else:
                    page = page + 1
            for z in range(1, page + 1):
                url1 = url + '_' + str(z)
                test.append(url1)
            return test
        except Exception as e:
            try:
                req = urllib2.Request(url, '', headers)
                response = urllib2.urlopen(req)
                the_page = response.read().decode('gbk')
                content_re = u'<div class="r">本批次共 (.*?) 个车型</a></div>'
                listtemp = re.findall(content_re, the_page)
                test = []
                page = 1
                if int(listtemp[0]) > 60:
                    page = int(listtemp[0]) / 60
                    if int(listtemp[0]) % 60 == 0:
                        pass
                    else:
                        page = page + 1
                for z in range(1, page + 1):
                    url1 = url + '_' + str(z)
                    test.append(url1)
                return test
            except Exception as e:
                time.sleep(15)


def tableOne(urlone):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 将user_agent写入头信息
    headers = {'User-Agent': user_agent}

    try:
        req = urllib2.Request(urlone, '', headers)
        response = urllib2.urlopen(req)
        the_page = response.read().decode('gbk')
        content_re = '<span class="m"><a href="(.*?)" target="_blank">(.*?)</a></span>'
        listtemp = re.findall(content_re, the_page)
        test = []
        for q in listtemp:
            test.append('http://www.cn357.com' + str(q[0]))
        return test
    except Exception as e:
        print e
        print '被拦截了休息10s并重试'
        time.sleep(15)
        try:
            req = urllib2.Request(urlone, '', headers)
            response = urllib2.urlopen(req)
            the_page = response.read().decode('gbk')
            content_re = '<span class="m"><a href="(.*?)" target="_blank">(.*?)</a></span>'
            listtemp = re.findall(content_re, the_page)
            test = []
            for q in listtemp:
                test.append('http://www.cn357.com' + str(q[0]))
            return test
        except Exception as e:
            try:
                req = urllib2.Request(urlone, '', headers)
                response = urllib2.urlopen(req)
                the_page = response.read().decode('gbk')
                content_re = '<span class="m"><a href="(.*?)" target="_blank">(.*?)</a></span>'
                listtemp = re.findall(content_re, the_page)
                test = []
                for q in listtemp:
                    test.append('http://www.cn357.com' + str(q[0]))
                return test
            except Exception as e:
                print e
                print '被拦截了休息10s并重试'
                time.sleep(15)


def toText(uurl):
    nplist = []
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 将user_agent写入头信息
    headers = {'User-Agent': user_agent}
    try:
        req = urllib2.Request(uurl, '', headers)
        response = urllib2.urlopen(req)
        the_page = response.read().decode('gbk')
        dfs_1 = pd.read_html(the_page)
        test = dfs_1[0].ix[0:20]
        nplist.append(np.array(test[1]).tolist() + np.array(test[3]).tolist())

        f.write('::'.join(map(str, nplist[0])))
        f.write('\n')
        return 'ok+1'
    except Exception as e:
        print e
        print '被拦截了休息10s并重试'
        time.sleep(15)
        try:
            req = urllib2.Request(uurl, '', headers)
            response = urllib2.urlopen(req)
            the_page = response.read().decode('gbk')
            dfs_1 = pd.read_html(the_page)
            test = dfs_1[0].ix[0:20]
            nplist.append(np.array(test[1]).tolist() + np.array(test[3]).tolist())

            f.write('::'.join(map(str, nplist[0])))
            f.write('\n')
            return 'ok+1'
        except Exception as e:
            try:
                req = urllib2.Request(uurl, '', headers)
                response = urllib2.urlopen(req)
                the_page = response.read().decode('gbk')
                dfs_1 = pd.read_html(the_page)
                test = dfs_1[0].ix[0:20]
                nplist.append(np.array(test[1]).tolist() + np.array(test[3]).tolist())

                f.write('::'.join(map(str, nplist[0])))
                f.write('\n')
                return 'ok+1'
            except Exception as e:
                print e
                print '被拦截了休息10s并重试'
                time.sleep(15)


headString = "address::公告型号::品牌::额定质量::整备质量::排放依据标准::轴距::弹簧片数::轮胎规格::前悬后悬::后轮距::整车长::整车高::货厢宽::最高车速::驾驶室准乘人数::准拖挂车总质量::半挂车鞍座最大承载质量::企业地址::传真号码::底盘1::底盘3::公告批次::类型::总质量::燃料种类::轴数::轴荷::轮胎数::接近离去角::前轮距::识别代号::整车宽::货厢长::货厢高::额定载客::转向形式::载质量利用系数::企业名称::电话号码::邮政编码::底盘2::底盘4"
f.write(headString)
f.write('\n')
urlList = listp()
for urll in urlList:
    time.sleep(5)
    print 'sleep 5s'
    for pagelist in table(urll):
        time.sleep(2.5)
        print 'sleep 2.5s'
        for one in tableOne(pagelist):
            time.sleep(0.5)
            f.write(pagelist)
            f.write('::')
            print 'sleep 1s'
            print toText(one)
f.close()
