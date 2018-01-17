# /usr/bin
# coding:utf-8
import pandas as pd
import requests
import numpy as np
import urllib2
import urllib

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

f = open('data.txt', 'w')


def toText():
    nplist = []
    url = 'http://www.cn357.com/notice143993_YH5122TQZ01P'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 将user_agent写入头信息
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python'}
    headers = {'User-Agent': user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    the_page = response.read().decode('gbk')
    dfs_1 = pd.read_html(the_page)
    test = dfs_1[0].ix[0:20]
    nplist.append(np.array(test[1]).tolist() + np.array(test[3]).tolist())

    f.write('::'.join(map(str, nplist[0])))
    return 'ok+1'


print toText()
f.close()
