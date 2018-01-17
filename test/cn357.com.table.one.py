# /usr/bin
# coding:utf-8
import urllib2
import re


def tableOne(urlone):
    url = urlone
    response = urllib2.urlopen(url)
    the_page = response.read().decode('gbk')
    content_re = '<span class="m"><a href="(.*?)" target="_blank">(.*?)</a></span>'
    listtemp = re.findall(content_re, the_page)
    test = []
    for q in listtemp:
        test.append('http://www.cn357.com' + str(q[0]))
    return test


print tableOne('http://www.cn357.com/notice_2_1')
