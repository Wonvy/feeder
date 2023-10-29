# -*- coding:utf-8 -*-
import json
import re
import requests
import chardet
import feedparser
import collections
from pyquery import PyQuery as pq
from collections import OrderedDict
from ..models import Users
from ..models import Category
from ..models import Channel
from ..models import Item
import json



def getinfo():
    # 初始化 数据
    json_data = collections.OrderedDict()

    # 返回 源代码
    url= "http://www.zcool.com.cn/"
    r = requests.get(url)
    html = r.text

    # 匹配 html
    html = pq(html)
    div = html('.card-box')
    for index, i in enumerate(div):
        s = pq(pq(i).html())
        json_sub = collections.OrderedDict()
        json_sub['title'] = s('.card-info-title a').text()                      # 名称
        # json_sub['thumbnail'] = s('.card-img a img').attr('srcset')             # 大缩略图
        json_sub['thumbnail'] = s('.card-img a img').attr('src')             # 缩略图
        json_sub['address'] = s('.card-img a').attr('href')                     # 地址
        json_sub['type'] = s('.card-info-type').attr("title")                   # 分类
        json_sub['view'] = s('.statistics-view').text()                         # 人气
        json_sub['comment'] = s('.statistics-comment').text()                   # 评论
        json_sub['upvote'] = s('.statistics-tuijian').text()                    # 推荐
        json_sub['user_name'] = s(".card-item .user-avatar a").text()           # 作者
        json_sub['user_href'] = s(".card-item .user-avatar a").attr("href")     # 作者地址
        json_sub['user_img'] = s(".card-item .user-avatar a img").attr("src")   # 作者头像
        json_sub['posted_time'] = s(".card-item .time").attr("title")           # 作品发表时间
        json_data[index] = json_sub

        # 去重写入数据
        aitem = Item.objects.filter(link=json_sub['address'])
        if not aitem:
            p = Item(channelid=2, reed=0,
                     title=json_sub['title'],
                     pic=json_sub['thumbnail'],
                     link=json_sub['address'],
                     pubDate=json_sub['posted_time'])
            p.save()

        del json_sub
        # print json_data

    # 处理 None对象为 "" 空字符串
    for i in json_data:
        if len(json_data[i]) > 0:
            for s in json_data[i]:
                if json_data[i][s] is None:
                    json_data[i][s] = ""


    # 输出 html文件
    out_html = '<div class="zcool"><ul>'

    for i in json_data:
        out_html = out_html + \
                   '<li><a href="' + json_data[i]["address"] + '" target="_blank">' + \
                    '<div class="z-img"><img src="' + json_data[i]["thumbnail"] + '"></div>' + \
                    '<div class="z-info"><h4>' + json_data[i]["title"] + '</h4>' + \
                    '<img src="' + json_data[i]["user_img"] + \
                    '"><span>' + json_data[i]["user_name"] + '</span></div></a></li>'
    out_html = out_html + "</ul></div>"

    if isinstance(out_html, unicode):
        out_html = out_html.encode('utf8')

    return out_html

# get today
def gettaday(url):
    return "今天数据"

# 更所所有列表
def getalllist():
    for i in Channel.objects.all():
        getlist(i.link)

# 获取列表
def getlist(url,vcategory=""):
    d = feedparser.parse(url)

    # 添加订阅
    if vcategory <> "":
        schannel = Channel.objects.filter(link=url)
        if not schannel:
            t = getattr(d.feed, 'updated_parsed', '2017-09-16 00:00:00')
            if isinstance(t, str):
                apubDate = t
            else:
                apubDate = str(t.tm_year).zfill(2) + r'-' + str(t.tm_mon).zfill(2) + r'-' + str(t.tm_mday).zfill(2) + r' ' + str(t.tm_hour).zfill(2) + r':' + str(t.tm_min).zfill(2) + r':' + str(t.tm_sec).zfill(2)

            dbp = Channel(favicon=d['feed']['link'] + '/favicon.ico',
                          title=d['feed']['title'],
                          link=url,
                          lastBuildDate=apubDate,
                          categoryid = Category.objects.get(name=vcategory))
            # language = d['feed']['language'])
            dbp.save()

    # 添加文章
    classid = Channel.objects.get(link=url).id
    for i in d.entries:
        aitem = Item.objects.filter(link=i['link'])
        if not aitem:
            # get content
            img = ""
            acontent = i.get('content', '')
            if acontent == "":
                acontent = i['description'].encode('utf-8')
                # get bigimg
                result1 = re.search('src="(.+?)"', str(acontent))
                if result1:
                    img = str(result1.group(1))
            else:
                # get bigimg
                result1 = re.search('src="(.+?)"', str(acontent))
                if result1:
                    img = str(result1.group(1))
                # acontent = acontent.decode('unicode-escape')
                if isinstance(acontent, object):
                    acontent = acontent[0].value # 去除base等

            t = getattr(i, 'updated_parsed', '2017-09-16 00:00:00')
            if isinstance(t, str):
                apubDate = t
            else:
                apubDate = str(t.tm_year).zfill(2) + r'-' + str(t.tm_mon).zfill(2) + r'-' + str(t.tm_mday).zfill(
                    2) + r' ' + str(t.tm_hour).zfill(2) + r':' + str(t.tm_min).zfill(2) + r':' + str(t.tm_sec).zfill(2)

            p = Item(channelid=Channel.objects.get(id=classid),
                     reed=0,
                     title=i['title'],
                     pic=img,
                     link=i['link'],
                     pubDate=apubDate,
                     description=i['description'],
                     content=acontent)
            p.save()
    return url

# 获取内容
def getcontent(url):
    try:
        aitem = Item.objects.get(link=url)
    except:
        return "error"
    else:
        aitem.reed=1
        aitem.save()
        o_content = aitem.content
        title =  '<a href="' + url + '" target="_blank">' + "<h1>" + aitem.title + "</h1>" + '</a>'
        date = "<p>" + str(aitem.pubDate) + "</p>"
        link = '<div class="link">' + '<a href="' + url + '" target="_blank">' + u'阅读原文' + '</a></div>'
        o_content = title + date + o_content + link
        # o_content = o_content + u'阅读原文' + '</a></div>'
        # m = pickle.dumps(m)
        # m =str(m)
        # m = m[:-1]
        # m = m[1:]
        # if isinstance(m, object):
        #     m = "是对象"
            # m.value
       # bcontent = aitem.get("content","eee")
        return o_content

# 添加分类
def addCategory(url):
    return 0



