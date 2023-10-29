# -*- coding: utf-8 -*-
__author__ = 'wonvy'
__date__ = '10/4/2017 12:08 PM'
# http://blog.csdn.net/spch2008/article/details/9343207


def catcher():
    try:
        c = 55
    except:
        print "got exception"
    else:
        print "not exception"
c = catcher()
