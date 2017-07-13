#coding:utf8

import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer,Any
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from numpy import *
import requests


def destina(origin,destination):
    sum = 0
    url = "http://restapi.amap.com/v3/direction/walking?origin=" + origin.encode("utf-8") + "&destination=" + destination +"&key=c912883876e0baa8beb279f31efac462"
    response = requests.request("GET", url)
    data = response.json()

    for i in range(shape(data['route']['paths'][0]['steps'])[0]):
        sum += int(data['route']['paths'][0]['steps'][i]['distance'].encode('utf-8'))
    #['paths']['steps'][0]
    return sum


def hospitalPoint(viewpoint):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % viewpoint
    response = requests.request("GET", url)
    data = response.json()
    #print type(data['pois'][0]['location'])
    return data['pois'][0]['location']

def hospitalLocation(hospitalData):
    url = "http://restapi.amap.com/v3/place/around?key=c912883876e0baa8beb279f31efac462&location=%s&keywords=医院&types=&offset=&page=&extensions=all" % hospitalData
    response = requests.request("GET", url)
    data = response.json()
    return data

def view_hospital(viewName):
    viewLocation = hospitalPoint(viewName)
    print viewLocation
    hospitalData = hospitalLocation(viewLocation.encode("utf-8"))
    emptyList = []
    for hospital_num in range(shape(hospitalData['pois'])[0]):
        hospitalList = []
        hoName = '医院名称：' + hospitalData['pois'][hospital_num]['name'].encode('utf-8')
        print hoName
        if len(hospitalData['pois'][hospital_num]['tel']):
            hoTel = '医院电话：' + hospitalData['pois'][hospital_num]['tel'].encode('utf-8')
        else:
            hoTel = '医院电话：' + '无'
        hoAddress = ''.join(hospitalData['pois'][hospital_num]['address'])
        hoLocation = '医院经纬度：' + hospitalData['pois'][hospital_num]['location'].encode('utf-8')
        hoType = '医院类型：' + hospitalData['pois'][hospital_num]['type'].encode('utf-8')
        hospitalList.append(hoName)
        hospitalList.append(hoTel)
        hospitalList.append(hoAddress)
        hospitalList.append(hoLocation)
        hospitalList.append(hoType)
        emptyList.append(hospitalList)

    return emptyList,hospitalData,viewLocation


def hospital_distance_recom(hospitalData,viewLocation):
    minDistance = 10000000
    minDistanceIndex = 0
    distList = []
    for hotel_data in range(shape(hospitalData['pois'])[0]):
        # 景点与宾馆的距离
        hotel_view_distance = destina(hospitalData['pois'][hotel_data]['location'].encode('utf-8'), viewLocation)
        if hotel_view_distance < minDistance:
            minDistance = hotel_view_distance
            minDistanceIndex = hotel_data

    distList.append("距离最短医院为：" + hospitalData['pois'][minDistanceIndex]['name'].encode('utf-8'))
    distList.append(hospitalData['pois'][minDistanceIndex]['location'].encode('utf-8'))
    distList.append(hospitalData['pois'][minDistanceIndex]['address'].encode('utf-8'))
    return distList

class HospitalService(DefinitionBase):
    @soap(String, _returns=Array(Array(String)))
    def hospital(self, hospitalName):
        hospital_list,hospitalData ,viewLocation= view_hospital(hospitalName)
        hospital_distance = hospital_distance_recom(hospitalData,viewLocation)
        hospital_list.append(hospital_distance)
        return hospital_list






if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        soap_application = soaplib.core.Application([HospitalService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 8091, wsgi_application)
        print 'soap server starting......'
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"