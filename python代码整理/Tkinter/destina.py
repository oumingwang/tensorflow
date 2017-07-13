#coding:utf8
import requests
from numpy import *
def viewpoint(origin,destination):
    #str1 = '116.481028,39.989643'
    #str2 = '116.434446,39.90816'
    print type(origin)
    print type(destination)
    print origin
    print destination
    sum = 0
    url = "http://restapi.amap.com/v3/direction/walking?origin=" + origin.encode("utf-8") + "&destination=" + destination +"&key=c912883876e0baa8beb279f31efac462"
    response = requests.request("GET", url)
    print response
    data = response.json()
    #data = {u'status': u'1', u'info': u'ok', u'route': {u'origin': u'116.434307,39.90909', u'paths': [{u'duration': u'149', u'distance': u'208', u'steps': [{u'distance': u'54', u'orientation': [], u'instruction': u'\u6b65\u884c54\u7c73\u53f3\u8f6c', u'action': u'\u53f3\u8f6c', u'polyline': u'116.434319,39.909046;116.434967,39.909046', u'duration': u'39', u'assistant_action': [], u'road': []}, {u'distance': u'84', u'orientation': u'\u5357', u'instruction': u'\u6cbf\u5efa\u56fd\u95e8\u5317\u5927\u8857\u5411\u5357\u6b65\u884c84\u7c73\u5411\u5de6\u524d\u65b9\u884c\u8d70', u'action': u'\u5411\u5de6\u524d\u65b9\u884c\u8d70', u'polyline': u'116.434967,39.909046;116.434967,39.909031;116.434937,39.908932;116.434891,39.908867;116.434891,39.908867;116.43483,39.908726;116.434814,39.908649;116.43483,39.908493;116.43483,39.908428;116.434868,39.908306', u'duration': u'60', u'assistant_action': [], u'road': u'\u5efa\u56fd\u95e8\u5317\u5927\u8857'}, {u'distance': u'23', u'orientation': u'\u4e1c\u5357', u'instruction': u'\u6cbf\u5efa\u56fd\u95e8\u5357\u5927\u8857\u5411\u4e1c\u5357\u6b65\u884c23\u7c73\u53f3\u8f6c', u'action': u'\u53f3\u8f6c', u'polyline': u'116.434868,39.908302;116.434975,39.908195;116.435005,39.908123', u'duration': u'16', u'assistant_action': [], u'road': u'\u5efa\u56fd\u95e8\u5357\u5927\u8857'}, {u'distance': u'47', u'orientation': [], u'instruction': u'\u6b65\u884c47\u7c73\u5230\u8fbe\u76ee\u7684\u5730', u'action': [], u'polyline': u'116.435005,39.908119;116.434456,39.908081', u'duration': u'34', u'assistant_action': u'\u5230\u8fbe\u76ee\u7684\u5730', u'road': []}]}], u'destination': u'116.434446,39.90816'}, u'infocode': u'10000', u'count': u'1'}
    print data
    #print data['route']
    #print data['route']['paths']
    #print data['route']['paths'][0]['steps'][0]['distance']
    for i in range(shape(data['route']['paths'][0]['steps'])[0]):
        sum += int(data['route']['paths'][0]['steps'][i]['distance'].encode('utf-8'))
    print  sum
    #['paths']['steps'][0]
    return sum
