# -*- coding: utf-8 -*-
'''
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/haite/lvjiapi/scenicnamefindscenicinfo?scenicName=%E6%96%87%E5%8C%96%E9%95%BF%E5%BB%8A'


req = urllib2.Request(url)

req.add_header("apikey", "7b1fafe385f2ce30d02be7e5ea47efb4")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
'''

# !/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode


# ----------------------------------
# 餐饮美食调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/45
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "7b1fafe385f2ce30d02be7e5ea47efb4"

    # 1.按城市检索
    #request1(appkey, "GET")

    # 2.检索周边美食
    request2(appkey, "GET")


# 按城市检索
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/catering/querybycity"
    params = {
        "city": "",  # 城市名称，如：北京 URLencode
        "page": "",  # 当前页数，默认1
        "pagesize": "",  # 每页返回，最大50
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


# 检索周边美食
def request2(appkey, m="GET"):
    url = "http://apis.juhe.cn/catering/query"
    params = {
        "lng": "110.328752",  # 经纬(如:121.538123)，传递的适合google地图的坐标系
        "lat": "20.056739",  # 纬度(如：31.677132)
        "radius": "",  # 搜索范围，单位M，默认3000
        "page": "",  # 当前页数，默认1,最大50.
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


if __name__ == '__main__':
    main()

