#coding:utf8
import requests
import json
#import xml.etree.cElementTree as ET
import xml.sax

url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=5bca02dc6ba1df62e5d370afb0066ec1&extensions=all" % viewpoint

response = requests.request("GET", url)

data = response.json()
print data['pois'][0]
print data['pois'][0]['tel']
print data['pois'][0]['location']
print data['pois'][0]['name']
print data['pois'][0]['address']
print data['pois'][0]['cityname']
print data['pois'][0]['pname']
