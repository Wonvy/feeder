# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# 用户
class Users(models.Model):
    name = models.CharField(max_length=512)
    addDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'用户信息'

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

# 分类
class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u"ID")
    classid = models.IntegerField(null=True, verbose_name=u"分类ID")
    orderid = models.IntegerField(null=True, verbose_name=u"排序ID")
    name = models.CharField(max_length=512, null=True, default="", verbose_name=u"分类名称")
    description = models.TextField(null=True, default="", verbose_name=u"分类描述")
    addDate = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

# 订阅源
class Channel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u"ID")
    categoryid = models.ForeignKey(Category, verbose_name=u"类别")
    orderid = models.IntegerField(null=True, default=0, verbose_name=u"排序")
    favicon = models.CharField(max_length=512, null=True, blank=True, default="", verbose_name=u"图标")
    title = models.CharField(max_length=128, null=True, default="", verbose_name=u"标题")
    atom = models.CharField(max_length=128, null=True, blank=True, default="", verbose_name=u"atom")
    link = models.CharField(max_length=128, null=True, default="", verbose_name=u"链接")
    description = models.TextField(null=True, default="", blank=True, verbose_name=u"描述")
    lastBuildDate = models.DateTimeField(null=True, verbose_name=u"生成日期")
    language = models.CharField(max_length=512, null=True, blank=True, default="", verbose_name=u"语言")
    addDate = models.DateTimeField(auto_now_add=True, verbose_name=u"添加日期")

    class Meta:
        verbose_name = u"订阅"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


# 文章条目
class Item(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u"ID")
    channelid = models.ForeignKey(Channel, default="", verbose_name=u"订阅源")
    reed = models.IntegerField(null=True, default=0,verbose_name=u"是否阅读")
    pic = models.CharField(max_length=512, null=True, default="", verbose_name=u"图片")
    title = models.CharField(max_length=128, null=True, default="", verbose_name=u"标题")
    link = models.CharField(max_length=512, null=True, verbose_name=u"链接")
    # pubDate = models.DateTimeField(auto_now=True)
    pubDate = models.DateTimeField(null=True, verbose_name=u"发布日期")
    category = models.CharField(max_length=128, null=True, default="",verbose_name=u"标签")
    description = models.TextField(null=True, default="", verbose_name=u"描述")
    content = models.TextField(null=True, default="", verbose_name=u"内容")
    addDate = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

# class FriendLinkcategory(models.Model):
#     Id = models.AutoField(primary_key=True)
#     Name = models.CharField("text",max_length=50)


    # username = models.CharField(max_length=16,null=False)
    # password = models.CharField(max_lenght=16,null=False)