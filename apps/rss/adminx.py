# -*- coding: utf-8 -*-
__author__ = 'wonvy'
__date__ = '10/2/2017 8:45 AM'

import xadmin

from xadmin import  views

from .models import Channel, Category, Item

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "小顽的后台"
    site_footer = "小顽"
    menu_style = "accordion"

class CategoryAdmin(object):
    list_display = ['id', 'name', 'classid']

class ChannelAdmin(object):
    list_display = ['id','categoryid', 'title', 'link']

class ItemAdmin(object):
    list_display = ['id', 'title', 'pubDate']
    # data_charts = {
    #         "user_count": {'title': u"course_num", "x-field": "pubDate", "y-field": ("course_num"),
    #                        "order": ('addtime',)
    #                        }
    #     }

xadmin.site.register(Channel, ChannelAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Item, ItemAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

