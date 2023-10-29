# -*- coding: utf-8 -*-
__author__ = 'wonvy'
__date__ = '10/6/2017 9:07 AM'

# 买一台服务器 vpn


import urllib2
import random
import time
import re
from lxml import etree


def get_proxy(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36 '
    }
    req = urllib2.Request('http://www.xicidaili.com/nn/{}'.format(page), headers=headers)
    response = urllib2.urlopen(req)
    html = response.read()
    # proxy_list = []

    ip_port_list = re.findall(r'<tr class[\s\S]*?</tr>', html)
    # ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', html)
    # port_list = re.findall(r'<td>(\d+)</td>', html)
    # for i,j in zip(ip_list, port_list):
    #     print i,j
    # print ip_port_list
    for i in ip_port_list:
       pass

    print ip_port_list[0]

    # print port_list


if __name__ == '__main__':
    get_proxy(1)
