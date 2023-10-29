# -*- coding:utf-8 -*-
import json
import re
import requests
import collections
from pyquery import PyQuery as pq
from collections import OrderedDict
import time
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree
from xml.dom import minidom

# 活动行
class huodongxing:
    def __init__(self):
        self.siteURL = "http://www.huodongxing.com/eventlist?orderby=o&city=%E5%8E%A6%E9%97%A8"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')    # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('.event-horizontal-list-new > li')

        for index, i in enumerate(div):
            json_sub = collections.OrderedDict()

            json_sub['title'] = pq(i).children('h3 a').attr('title')  # 活动名称
            json_sub['thumbnail'] = pq(i).children('a img').attr('src')    # 活动图片
            json_sub['href'] = pq(i).children('h3 a').attr('href') # 活动链接
            json_sub['date'] = pq(i).children('.event-info div span.icon-event-time').text()  # 活动日期
            json_sub['address'] = pq(i).children('.event-info div span.icon-event-location').text()  # 活动地址
            json_sub['organizer'] = pq(i).children('div.apply a span').text()  # 活动发起人

            json_data[index] = json_sub
        return json_data

    # 输出 HTML
    def getHTML(self, file=0):
        out_html = '<div class="zcool"><ul>'
        dict = self.getData()
        for i in dict:
            out_html = out_html + \
                       '<li><a href="' + dict[i]["href"] + '" target="_blank">' + \
                        '<div class="z-img"><img src="' + dict[i]["img"] + '" />' + \
                        '</div><div class="z-info"><h4>'+ dict[i]['title'] + \
                       '</h4></div></a></li>'
        out_html = out_html + "</ul></div>"
        if isinstance(out_html, unicode):
            out_html = out_html.encode('utf8')

        if file == 1:
            json_file = open('zcool.html', 'w')
            json_file.writelines(out_html)
            json_file.close()
            return u'输出html文件'
        else:
            return out_html

# 大麦网
class damai:
    def __init__(self):
        self.siteURL = "https://search.damai.cn/search.html?spm=a2o6e.home_xiamen.0.0.5b4dc0d9ecyIOp&cty=%E5%8E%A6%E9%97%A8&order=1"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')    # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('#content_list > li')

        for index, i in enumerate(div):
            json_sub = collections.OrderedDict()

            json_sub['title'] = pq(i).children('div.search_txt h3 a').text()  # 活动名称
            json_sub['thumbnail'] = pq(i).children('div.search_img a img').attr('src')    # 活动图片
            json_sub['href'] =  pq(i).children('div.search_txt h3 a').attr('href') # 活动链接
            json_sub['date'] = pq(i).children('div.search_txt_time p.search_txt_time a').text()  # 活动日期
            json_sub['address'] = pq(i).children('div.search_txt p.c1 a').text()  # 活动地址
            json_sub['organizer'] = "大麦网"

            json_data[index] = json_sub
        return json_data

    # 输出 HTML
    def getHTML(self, file=0):
        out_html = '<div class="zcool"><ul>'
        dict = self.getData()
        for i in dict:
            out_html = out_html + \
                       '<li><a href="' + dict[i]["href"] + '" target="_blank">' + \
                        '<div class="z-img"><img src="' + dict[i]["img"] + '" />' + \
                        '</div><div class="z-info"><h4>'+ dict[i]['title'] + \
                       '</h4></div></a></li>'
        out_html = out_html + "</ul></div>"
        if isinstance(out_html, unicode):
            out_html = out_html.encode('utf8')

        if file == 1:
            json_file = open('zcool.html', 'w')
            json_file.writelines(out_html)
            json_file.close()
            return u'输出html文件'
        else:
            return out_html

# 豆瓣同城
class douban:
    def __init__(self):
        self.siteURL = "https://www.douban.com/location/xiamen/events/future-all"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')    # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('#db-events-list ul > li')

        for index, i in enumerate(div):
            json_sub = collections.OrderedDict()

            json_sub['thumbnail'] = pq(i).children('div.pic a img').attr('src')  # 活动图片
            json_sub['title'] = pq(i).children('div.info .title a span').text()  # 活动名称
            json_sub['href'] =  pq(i).children('div.info .title a').attr('href') # 活动链接
            # json_sub['date'] = pq(i).children('div.info ul.event-meta li.event-time time').attr('datetime')  # 活动日期
            # json_sub['address'] = pq(i).children('div.search_txt p.c1 a').text()  # 活动地址
            # json_sub['organizer'] = "大麦网"

            json_data[index] = json_sub
        return json_data

    # 输出 HTML
    def getHTML(self, file=0):
        out_html = '<div class="zcool"><ul>'
        dict = self.getData()
        for i in dict:
            out_html = out_html + \
                       '<li><a href="' + dict[i]["href"] + '" target="_blank">' + \
                        '<div class="z-img"><img src="' + dict[i]["img"] + '" />' + \
                        '</div><div class="z-info"><h4>'+ dict[i]['title'] + \
                       '</h4></div></a></li>'
        out_html = out_html + "</ul></div>"
        if isinstance(out_html, unicode):
            out_html = out_html.encode('utf8')

        if file == 1:
            json_file = open('zcool.html', 'w')
            json_file.writelines(out_html)
            json_file.close()
            return u'输出html文件'
        else:
            return out_html

# 秀动网
class showstart:
    def __init__(self):
        self.siteURL = "http://www.showstart.com/event/list?keyword=%E5%8E%A6%E9%97%A8"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')    # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('#db-events-list ul > li')

        for index, i in enumerate(div):
            json_sub = collections.OrderedDict()

            json_sub['thumbnail'] = pq(i).children('div.pic a img').attr('src')  # 活动图片
            json_sub['title'] = pq(i).children('div.info .title a span').text()  # 活动名称
            json_sub['href'] =  pq(i).children('div.info .title a').attr('href') # 活动链接
            # json_sub['date'] = pq(i).children('div.info ul.event-meta li.event-time time').attr('datetime')  # 活动日期
            # json_sub['address'] = pq(i).children('div.search_txt p.c1 a').text()  # 活动地址
            # json_sub['organizer'] = "大麦网"

            json_data[index] = json_sub
        return json_data

    # 输出 HTML
    def getHTML(self, file=0):
        out_html = '<div class="zcool"><ul>'
        dict = self.getData()
        for i in dict:
            out_html = out_html + \
                       '<li><a href="' + dict[i]["href"] + '" target="_blank">' + \
                        '<div class="z-img"><img src="' + dict[i]["img"] + '" />' + \
                        '</div><div class="z-info"><h4>'+ dict[i]['title'] + \
                       '</h4></div></a></li>'
        out_html = out_html + "</ul></div>"
        if isinstance(out_html, unicode):
            out_html = out_html.encode('utf8')

        if file == 1:
            json_file = open('zcool.html', 'w')
            json_file.writelines(out_html)
            json_file.close()
            return u'输出html文件'
        else:
            return out_html

# 懒人周末 小日子
class xiaorizi:
    def __init__(self):
        self.siteURL = "http://xiaorizi.me/event/xiamen/"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')    # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('#db-events-list ul > li')

        for index, i in enumerate(div):
            json_sub = collections.OrderedDict()

            json_sub['thumbnail'] = pq(i).children('div.pic a img').attr('src')  # 活动图片
            json_sub['title'] = pq(i).children('div.info .title a span').text()  # 活动名称
            json_sub['href'] =  pq(i).children('div.info .title a').attr('href') # 活动链接
            # json_sub['date'] = pq(i).children('div.info ul.event-meta li.event-time time').attr('datetime')  # 活动日期
            # json_sub['address'] = pq(i).children('div.search_txt p.c1 a').text()  # 活动地址
            # json_sub['organizer'] = "大麦网"

            json_data[index] = json_sub
        return json_data

    # 输出 HTML
    def getHTML(self, file=0):
        out_html = '<div class="zcool"><ul>'
        dict = self.getData()
        for i in dict:
            out_html = out_html + \
                       '<li><a href="' + dict[i]["href"] + '" target="_blank">' + \
                        '<div class="z-img"><img src="' + dict[i]["img"] + '" />' + \
                        '</div><div class="z-info"><h4>'+ dict[i]['title'] + \
                       '</h4></div></a></li>'
        out_html = out_html + "</ul></div>"
        if isinstance(out_html, unicode):
            out_html = out_html.encode('utf8')

        if file == 1:
            json_file = open('zcool.html', 'w')
            json_file.writelines(out_html)
            json_file.close()
            return u'输出html文件'
        else:
            return out_html

c = damai()
print c.getData()
