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


# 站酷
class Zcool:
    def __init__(self):
        self.siteURL = "http://www.zcool.com.cn/"

    # 获取 当前日期
    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 获取 当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('.card-box')
        for index, i in enumerate(div):
            s = pq(pq(i).html())
            json_sub = collections.OrderedDict()
            json_sub['title'] = s('.card-info-title a').text()  # 名称
            # json_sub['thumbnail'] = s('.card-img a img').attr('srcset')             # 大缩略图
            json_sub['thumbnail'] = s('.card-img a img').attr('src')  # 缩略图
            json_sub['address'] = s('.card-img a').attr('href')  # 地址
            json_sub['type'] = s('.card-info-type').attr("title")  # 分类
            json_sub['view'] = s('.statistics-view').text()  # 人气
            json_sub['comment'] = s('.statistics-comment').text()  # 评论
            json_sub['upvote'] = s('.statistics-tuijian').text()  # 推荐
            json_sub['user_name'] = s(".card-item .user-avatar a").text()  # 作者
            json_sub['user_href'] = s(".card-item .user-avatar a").attr("href")  # 作者地址
            json_sub['user_img'] = s(".card-item .user-avatar a img").attr("src")  # 作者头像
            json_sub['posted_time'] = s(".card-item .time").attr("title")  # 作品发表时间
            json_data[index] = json_sub
            del json_sub
            # print json_data

        # 处理 None对象为 "" 空字符串
        for i in json_data:
            if len(json_data[i]) > 0:
                for s in json_data[i]:
                    if json_data[i][s] is None:
                        json_data[i][s] = ""
        # 转换 缩略图转行为大图
        # for i in json_data:
        #     if len(json_data[i]) > 0:
        #         for s in json_data[i]:
        #             # 切换 大图
        #             str3 = re.search(".+\.(jpg|gif|png|jpeg)", str(json_data[i]["thumbnail"]) )
        #             if str3:
        #                 json_data[i]["thumbnail"] = str3.group()
        #             # else:
        #                 # print json_data[i]["thumbnail"]
        return json_data

    # 输出 JSON
    def getJSON(self, file=0):
        dict = self.getData()
        out_json = json.dumps(dict, indent=4, separators=(',', ': '))
        if file == 1:
            json_file = open('zcool.json', 'w')
            json_file.write(out_json)
            json_file.close()
            return u'输出json文件'
        else:
            return out_json

    # 输出 XML
    def getXML(self, file=0):
        dict = self.getData()
        chanel = Element('chanel')
        title = SubElement(chanel, 'title')
        title.text = u'站酷'

        link = SubElement(chanel, 'link')
        link.text = 'http://www.zcool.com.cn'

        description = SubElement(chanel, 'description')
        description.text = u'站酷 (ZCOOL) - 设计师互动平台 - 打开站酷，发现更好的设计！'

        lastBuildDate = SubElement(chanel, 'lastBuildDate')
        lastBuildDate.text = u'Mon, 25 Sep 2017 03:39:51 +0000'

        language = SubElement(chanel, 'language')
        language.text = u'zh-CN'


        for i in dict:
            item = SubElement(chanel, "item")
            title = SubElement(item, "title")
            title.text = dict[i]["title"]
            link = SubElement(item, "link")
            link.text = dict[i]["address"]
            pubDate = SubElement(item, "pubDate")
            pubDate.text = dict[i]["posted_time"]
            description = SubElement(item, "description")
            description.text = dict[i]["title"]

        # 输出xml文件1
        tree = ElementTree(chanel)
        # tree.write('result.xml', encoding='utf-8')

        xml_string = etree.tostring(chanel)
        tree = minidom.parseString(xml_string)
        xml_string = tree.toxml()
        print xml_string

    # 输出 HTML
    def getHTML(self, file=0):
        out_html = '<div class="zcool"><ul>'
        dict = self.getData()
        for i in dict:
            out_html = out_html + \
                       '<li><a href="' + dict[i]["address"] + '" target="_blank">' + \
                        '<div class="z-img"><img src="' + dict[i]["thumbnail"] + '"></div>' + \
                        '<div class="z-info"><h4>' + dict[i]["title"] + '</h4>' + \
                        '<img src="' + dict[i]["user_img"] + \
                        '"><span>' + dict[i]["user_name"] + '</span></div></a></li>'
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

# UI中国
class uicn:
    def __init__(self):
        self.siteURL = "http://www.ui.cn/"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('.post-works > li > div.cover a')

        for index, i in enumerate(div):
            json_sub = collections.OrderedDict()
            json_sub['title'] = pq(i).attr('title')
            json_sub['href'] = self.siteURL + pq(i).attr('href')
            json_sub['img'] = pq(i).children('img').attr('data-original')

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

# uehtml
class uehtml:
    def __init__(self):
        self.siteURL = "http://www.uehtml.com/"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')  # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('.citem .citemtop')

        for index, i in enumerate(div):
            json_sub = collections.OrderedDict()
            json_sub['title'] = pq(i).children('div.citemtxt a').text()
            # json_sub['title'] = json_sub['title'].encode('utf8')
            json_sub['href'] = pq(i).children('div.citemtxt a').attr('href')
            json_sub['img'] = pq(i).children('a img').attr('data-src')

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
                       '</div><div class="z-info"><h4>' + dict[i]['title'] + \
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



# 爱奇艺
class iqiyi:
    def __init__(self):
        self.siteURL = "http://www.iqiyi.com/"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')  # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('ul.mod_focus-index_list li')
        for index, i in enumerate(div):
            # b = pq(i).attr('data-jpg')  # 图片

            # print s('a').attr('alt')  # 名称
            # print s('a').attr('href')  # 链接
            s = pq(pq(i).html())
            json_sub = collections.OrderedDict()
            json_sub['title'] = s('a').attr('alt')
            json_sub['href'] = s('a').attr('href')
            json_sub['img'] = pq(i).attr('data-jpg')
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

# 腾讯视频
class vqq:
    def __init__(self):
        self.siteURL = "http://v.qq.com/"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')  # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('.slider_nav > a')

        for index, i in enumerate(div):
            # print pq(i).attr('href')                # 链接
            # print pq(i).attr('data-bgimage')        # 图片
            # print pq(i).children('div.tit').text()  # 大标题
            # print pq(i).children('div.txt').text() # 小标题
            json_sub = collections.OrderedDict()
            json_sub['title'] = pq(i).children('div.tit').text() + ':' + pq(i).children('div.txt').text()
            json_sub['href'] = pq(i).attr('href')
            json_sub['img'] = pq(i).attr('data-bgimage')
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

# 芒果TV
class mgtv:
    def __init__(self):
        self.siteURL = "http://www.mgtv.com/"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')    # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('#honey-focus-list > li > a')

        for index, i in enumerate(div):
            # print pq(i).attr('href')                # 链接
            # print pq(i).attr('data-img')             # 图片
            # print pq(i).children('p.til').text()    # 大标题
            # print pq(i).children('p.txt').text()    # 小标题
            json_sub = collections.OrderedDict()
            json_sub['title'] = pq(i).children('p.til').text() + ':' + pq(i).children('p.txt').text()
            json_sub['href'] = pq(i).attr('href')
            json_sub['img'] = pq(i).attr('data-img')
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

# 优酷
class youku:
    def __init__(self):
        self.siteURL = "http://www.youku.com/"

    # 获取 html
    def getSource(self):
        r = requests.get(self.siteURL)
        return r.text.encode(r.encoding).decode('utf-8')    # 编码

    # 获取 列表
    def getData(self):
        json_data = collections.OrderedDict()
        html = self.getSource()
        html = pq(html)
        div = html('.focus-list li')

        for index, i in enumerate(div):
            # print pq(i).attr('href')                # 链接
            # print pq(i).attr('data-img')             # 图片
            # print pq(i).children('p.til').text()    # 大标题
            # print pq(i).children('p.txt').text()    # 小标题
            json_sub = collections.OrderedDict()
            json_sub['title'] = pq(i).children('a').attr('alt')
            json_sub['href'] = pq(i).children('a').attr('href')

            str3 = re.search("url\('//([^']+?)'\)", pq(i).attr('style'))
            if str3:
                json_sub['img'] = str3.group(1)
            else:
                json_sub['img'] = ""


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

# c = uehtml()
# print c.getData()
