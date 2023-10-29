# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager
access_key = 'DU4U0OWWFss8hcy8KmbpaH4u2SnSZUPWEoe5zZTL'
secret_key = '_EfE9zUxccjNSB-ucXL-HLN7ew2tQSAjjAMSScv6'
bucket_name = 'quppt'
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
url = 'https://cdn.dribbble.com/users/1144020/screenshots/3222551/aeroflot_02-03.gif'
# url = "https://mir-s3-cdn-cf.behance.net/projects/202/7a63a457422015.Y3JvcCwyNTA2LDE5NjEsMCwxMTE.jpg"
key = 'xxdddxd.gif'
ret, info = bucket.fetch(url, bucket_name, key)
print(info)
assert ret['key'] == key