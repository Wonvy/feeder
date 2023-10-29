# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from package import home
from package import rssfunc
import requests
import types
import logging
import chardet
from models import Category
from models import Channel
from models import Item
import datetime
import time
from django.utils import timezone
from jparser import PageModel
from models import User
from django import forms
from package import url2io



# 首页
def index(request):
    # rssModel = RssModel(age=26,age3=27)
    # rssModel.save()
    # rssModel = RssModel.objects.get(id=1)
    # rssage = rssModel.age
    # return HttpResponse(rssage)

    # 更新所有订阅
    # home.getalllist()
    item = Item.objects.all()[:9]
    category = Category.objects.all()
    # logging.debug("A log message")
    return render(request,'index.html',context={'itemlist':item,'categorylist':category})

# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

# 注册
def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            cc = User.objects.create(username=username,password=password,email=email)
            cc.save()
            return HttpResponse('注册成功')
    else:
        userform = UserForm()
    return render_to_response('regist.html',{'userform':userform})

# 登陆
def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = User.objects.filter(username__exact=username,password__exact=password)
            if user:
                return render_to_response('index.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')
    else:
        userform = UserForm()
    return render_to_response('login.html',{'userform':userform})

# bootstrap
def bootstrap(request):
    return render_to_response('bootstrap/bootstrap.html')

# 获取 正文
def get_content(request,nid):
    # 从数据库
    wd = home.getcontent(nid)

    if wd == "error" or len(wd) <= 400:

        # url2io
        # http: // www.url2io.com
        # api = url2io.API('j7rFE9MuSYSLlAwL-blmKg')
        # ret = api.article(url=nid)
        # title = '<a href="' + ret["url"] + '" target="_blank">' + "<h1>" + ret["title"] + "</h1>" + '</a>'
        # if ret["date"] == None:
        #     date = "<p>date</p>"
        # else:
        #     date = "<p>" + str(ret["date"]) + "</p>"
        # link = '<div class="link">' + '<a href="' + ret["url"] + '" target="_blank">' + u'阅读原文' + '</a></div>'
        # acontent = title + date + ret["content"] + link
        # return HttpResponse(acontent)

        # 从网站
        r = requests.get(nid)
        html = r.text
        pm = PageModel(html)
        result = pm.extract()
        acontent = "<h1>" + result['title'] + "</h1>"
        for x in result['content']:
            if x['type'] == 'text':
                acontent = acontent + '<p>' + x['data'] + '</p>'
            if x['type'] == 'image':
                acontent = acontent + '<img src="' + x['data']['src'] + '">'
        return HttpResponse(acontent)

    return HttpResponse(wd)


# 获取 订阅列表
def get_list(request,nid):
    # 今天
    if nid == "today":
        now = timezone.now()
        start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
        item = Item.objects.filter(pubDate__gt=start,reed=0).order_by("-pubDate")
        # return HttpResponse(start)
        return render(request, 'today.html', context={'itemlist':item})

    # 最近三天
    if nid == "threedays":
        now = timezone.now()
        start = now - datetime.timedelta(days=3)
        # start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
        # item = Item.objects.filter(pubDate__gt=start,reed=0).order_by()
        item = Item.objects.filter(pubDate__gt=start, reed=0).order_by("-pubDate")
        # return HttpResponse(start)
        return render(request, 'today.html', context={'itemlist':item})

    # 最近一周
    if nid == "week":
        now = timezone.now()
        start = now - datetime.timedelta(days=7)
        # start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
        item = Item.objects.filter(pubDate__gt=start, reed=0).order_by("-pubDate")
        # item = Item.objects.filter(pubDate__gt=start,reed=0)
        # return HttpResponse(start)
        return render(request, 'today.html', context={'itemlist':item})

    # 站酷
    if nid == "zcool":
        wd = rssfunc.Zcool()
        return HttpResponse(wd.getHTML())

    # ui中国
    if nid == "uicn":
        wd = rssfunc.uicn()
        return HttpResponse(wd.getHTML())

    # uehtml
    if nid == "uehtml":
        wd = rssfunc.uehtml()
        return HttpResponse(wd.getHTML())

    # behance
    if nid == "behance":
        return HttpResponse(nid)

    # 综艺节目
    if nid == "zongyi":
        wda = rssfunc.iqiyi()
        wdb = rssfunc.vqq()
        wdc = rssfunc.mgtv()
        wdd = rssfunc.youku()
        ccc = wda.getHTML() + wdb.getHTML() + wdc.getHTML() + wdd.getHTML()
        return HttpResponse(ccc)

    # three dau
    db = Channel.objects.filter(link=nid)
    if db:
        # item = Item.objects.filter(channelid=db[0].id,reed=0).order_by("reed")
        item = Item.objects.filter(channelid=db[0].id).order_by("reed","-pubDate")
        return render(request, 'list.html', context={'itemlist':item})
    else:
        return HttpResponse(nid)

# 添加订阅
def get_feed(request,nid):
    url = request.GET.get('url')
    fenlei = request.GET.get('fenlei')
    if fenlei=='all':
        home.getalllist()
        return HttpResponse("所有列表更新成功")
    else:
        wd = home.getlist(url, fenlei)
        return HttpResponse(wd)

# 添加分类
def add_category(request,nid):
    schannel = Category.objects.filter(name="未分类")
    if not schannel:
        Category(name="未分类", description="未分类", classid=0).save()

    schannel = Category.objects.filter(name=nid)
    if not schannel:
        p = Category(name=nid, description=nid, classid=0)
        p.save()
    return HttpResponse(nid)

# 读取订阅
def get_rss(request):
    rss = rssfunc.mgtv()
    xml = rss.getHTML()
    return HttpResponse(xml)
