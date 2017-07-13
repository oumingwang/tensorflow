#coding:utf8
import requests
from numpy import *
import destina


def hotel(hotelName):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % hotelName
    response = requests.request("GET", url)
    data = response.json()
    return data['pois']
    '''
    print data['pois']
    print '宾馆名称：' + data['pois'][0]['name'].encode('utf-8')
    print '宾馆电话：' + data['pois'][0]['tel'].encode('utf-8')
    print '宾馆地址：' + data['pois'][0]['address'].encode('utf-8')
    print '所在城市：' + data['pois'][0]['cityname'].encode('utf-8')
    print '所在省份：' + data['pois'][0]['pname'].encode('utf-8')
    if len(data['pois'][0]['biz_ext']['rating']):
        print ''.join(data['pois'][0]['biz_ext']['rating'])
    else:
        print "无评价"
    print '宾馆最低消费：' + data['pois'][0]['biz_ext']['lowest_price'].encode('utf-8')
    '''

def hotelRequest(hotelName,viewpoint_location):
    hotelData = hotel(hotelName)
    hotelDict = {}
    for hotel_data in range(shape(hotelData)[0]):
        hotelList = []
        hotelList.append(hotelData[hotel_data]['name'].encode('utf-8'))
        hotelList.append(hotelData[hotel_data]['location'].encode('utf-8'))
        hotelList.append(destina.viewpoint(hotelData[hotel_data]['location'].encode('utf-8'),viewpoint_location))
        hotelList.append(''.join(hotelData[hotel_data]['address']))
        if len(hotelData[hotel_data]['biz_ext']['rating']):
            hotel_rate = ''.join(hotelData[hotel_data]['biz_ext']['rating'])
        else  :
            hotel_rate = '1'
        hotelList.append(hotel_rate)

        if len(hotelData[hotel_data]['biz_ext']['lowest_price']):
            hotel_minprice =(str(hotelData[hotel_data]['biz_ext']['lowest_price'])).encode('utf-8')
        else:
            hotel_minprice = '无'
        hotelList.append(hotel_minprice)
        hotelDict[hotel_data] = hotelList

    return hotelDict