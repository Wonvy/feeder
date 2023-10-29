#coding:utf-8
from django import template
from django.http import HttpResponse
from django.template.defaultfilters import stringfilter
from datetime import date, timedelta
from rss.models import Category
from rss.models import Channel
from rss.models import Item
from django.utils import timezone
import datetime


register = template.Library()

@register.filter
def item_count(value):
    now = timezone.now()
    start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
    citem = Item.objects.filter(channelid=value,pubDate__gt=start,reed=0)
    count = citem.count()
    if count ==0:
        return ""
    return count


@register.filter
def category_count(value):
    citem = Item.objects.filter(channelid=value,reed=0)
    count = citem.count()
    if count ==0:
        return ""
    return count


