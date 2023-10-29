# -*- coding: utf-8 -*-
__author__ = 'wonvy'
__date__ = '10/5/2017 10:41 AM'

import upyun
# SERVICE = os.getenv('UPYUN_SERVICE')
# USERNAME = os.getenv('UPYUN_USERNAME')
# PASSWORD = os.getenv('UPYUN_PASSWORD')

up = upyun.UpYun('wonvyimg', 'admin', 'iamwonvy')
res = up.getlist('/')
# headers = { 'x-gmkerl-rotate': '180' }
#
# with open('xx.png', 'rb') as f:
#     res = up.put('xinu.png', f, checksum=True, headers=headers)

# res = up.put('/ddxx.txt', 'abcdefghijklmnopqrstuvwxyz\n')
# res = up.getlist('/xx.png')
# headers = { 'x-gmkerl-rotate': '180' }

#
# with open('xx.png', 'rb') as f:
#     res = up.put('xx.png', f, checksum=True, headers=headers)

print res