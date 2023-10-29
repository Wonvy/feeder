#!/usr/bin/env python
# coding: utf-8

from django.core.handlers.wsgi import WSGIHandler
import os
import sys

# 将系统的编码设置为UTF8
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fooder.settings")

application = WSGIHandler()
