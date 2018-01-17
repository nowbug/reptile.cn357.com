# /usr/bin
# coding:utf-8
import urllib2
import re


def table(url):
    '''
    '''
    url = url

    response = urllib2.urlopen(url)
    the_page = response.read().decode('gbk')
    content_re = u'<div class="r">本批次共 (.*?) 个车型</a></div>'
    listtemp = re.findall(content_re, the_page)
    print int(listtemp[0])
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


print table('http://www.cn357.com/notice_56')
