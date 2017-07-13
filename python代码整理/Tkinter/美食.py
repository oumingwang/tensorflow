# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode
appkey = "7b1fafe385f2ce30d02be7e5ea47efb4"
m="GET"
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