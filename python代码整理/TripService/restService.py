#coding:utf8
import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer,Any
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
import requests
from numpy import *

def destina(origin,destination):
    sum = 0
    url = "http://restapi.amap.com/v3/direction/walking?origin=" + origin.encode("utf-8") + "&destination=" + destination +"&key=c912883876e0baa8beb279f31efac462"
    response = requests.request("GET", url)
    data = response.json()

    for i in range(shape(data['route']['paths'][0]['steps'])[0]):
        sum += int(data['route']['paths'][0]['steps'][i]['distance'].encode('utf-8'))
    #['paths']['steps'][0]
    return sum




def hotel(hotel):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % hotel
    response = requests.request("GET", url)
    data = response.json()
    #print type(data['pois'][0]['location'])
    return data['pois'][0]['location']

def restaurantData(hotelData):

    url = "http://restapi.amap.com/v3/place/around?key=c912883876e0baa8beb279f31efac462&location=%s&keywords=饭店&types=&offset=&page=&extensions=all" % hotelData.encode("utf-8")
    response = requests.request("GET", url)
    data = response.json()
    print data
    return data


from numpy import *

def selHotel(hotelName):
    hotelLocation = hotel(hotelName)
    print hotelLocation
    restraurantData = restaurantData(hotelLocation)
    print restaurantData
    emptyList = []
    for restaurant_num in range(shape(restraurantData['pois'])[0]):
        restList = []
        reName =  '饭店名称：' + restraurantData['pois'][restaurant_num]['name'].encode('utf-8')
        print reName
        if len(restraurantData['pois'][restaurant_num]['tel']):
            reTel =  '饭店电话：' + restraurantData['pois'][restaurant_num]['tel'].encode('utf-8')
        else:
            reTel = '饭店电话：' + '无'
        reAddress =  '饭店地址：' + restraurantData['pois'][restaurant_num]['address'].encode('utf-8')
        reLocation =  '饭店经纬度：' + restraurantData['pois'][restaurant_num]['location'].encode('utf-8')
        if len(restraurantData['pois'][restaurant_num]['biz_ext']['rating']):
            reRate =  '饭店评分：' + restraurantData['pois'][restaurant_num]['biz_ext']['rating'].encode('utf-8')
        else:
            reRate = '饭店评分：' + '0'
        if len(restraurantData['pois'][restaurant_num]['biz_ext']['cost']):
            reMin =  '饭店最低消费：' + restraurantData['pois'][restaurant_num]['biz_ext']['cost'].encode('utf-8')
        else:
            reMin = '饭店最低消费' + '0'
        restList.append(reName)
        restList.append(reTel)
        restList.append(reAddress)
        restList.append(reRate)
        restList.append(reMin)
        emptyList.append(restList)
    print emptyList
    return emptyList,hotelLocation,restraurantData

def rest_distance_recom(restraurantData, hotelLocation):
    minDistance = 10000000
    minDistanceIndex = 0
    distList = []
    for rest_data in range(shape(restraurantData['pois'])[0]):
        # 景点与宾馆的距离
        hotel_view_distance = destina(restraurantData['pois'][rest_data]['location'].encode('utf-8'), hotelLocation)
        if hotel_view_distance < minDistance:
            minDistance = hotel_view_distance
            minDistanceIndex = rest_data

    distList.append("距离最短饭店：" + restraurantData['pois'][minDistanceIndex]['name'].encode('utf-8'))
    distList.append(restraurantData['pois'][minDistanceIndex]['location'].encode('utf-8'))
    distList.append(restraurantData['pois'][minDistanceIndex]['address'].encode('utf-8'))
    return distList

def rest_price_recom(restraurantData, hotelLocation):
    minPrice = inf
    minPriceIndex = 0
    priceList = []
    for rest_data in range(shape(restraurantData['pois'])[0]):
        if len(''.join(restraurantData['pois'][rest_data]['biz_ext']['cost'])):
            hotelPrice = float((restraurantData['pois'][rest_data]['biz_ext']['cost']).encode('utf-8')) + 1
        else:
            hotelPrice = 100000

        if hotelPrice < minPrice:
            minPrice = hotelPrice
            minPriceIndex = rest_data

    priceList.append("消费最低酒店：" + restraurantData['pois'][minPriceIndex]['name'].encode('utf-8'))
    priceList.append(restraurantData['pois'][minPriceIndex]['location'].encode('utf-8'))
    priceList.append(restraurantData['pois'][minPriceIndex]['address'].encode('utf-8'))
    return priceList


def rest_rate_recom(restraurantData, hotelLocation):
    minRate = inf
    minRateIndex = 0
    rateList = []
    for hotel_data in range(shape(restraurantData['pois'])[0]):
        if len(restraurantData['pois'][hotel_data]['biz_ext']['rating']):
            hotelRate = (restraurantData['pois'][hotel_data]['biz_ext']['rating']).encode('utf-8')
        else:
            hotelRate = 1.0
        if hotelRate > minRate:
            minRate = hotelRate
            minRateIndex = hotel_data

    rateList.append("评分最高酒店：" + restraurantData['pois'][minRateIndex]['name'].encode('utf-8'))
    rateList.append(restraurantData['pois'][minRateIndex]['location'].encode('utf-8'))
    rateList.append(restraurantData['pois'][minRateIndex]['address'].encode('utf-8'))
    return rateList


def rest_best_recom(restraurantData, hotelLocation):
    listDistance = []
    listRate = []
    listPrice = []

    bestNum = 0
    bestNumIndex = 0
    m = shape(restraurantData['pois'])[0]

    for rest_data in range(shape(restraurantData['pois'])[0]):
        hotel_view_distance = destina(restraurantData['pois'][rest_data]['location'].encode('utf-8'), hotelLocation)
        listDistance.append(float(hotel_view_distance))

        if len(restraurantData['pois'][rest_data]['biz_ext']['rating']):
            hotelRate = float((restraurantData['pois'][rest_data]['biz_ext']['rating']).encode('utf-8'))
        else:
            hotelRate = 1.0
        listRate.append(hotelRate)

        if len(restraurantData['pois'][rest_data]['biz_ext']['cost']):
            hotelPrice = float((restraurantData['pois'][rest_data]['biz_ext']['cost']).encode('utf-8')) + 1
        else:
            hotelPrice = 30000
        listPrice.append(hotelPrice)

    maxDist = mat(listDistance).max()
    minDist = mat(listDistance).min()
    maxRate = mat(listRate).max()
    minRate = mat(listRate).min()
    maxPrice = mat(listPrice).max()
    minPrice = mat(listPrice).min()

    rangeRateData = float(maxRate - minRate)
    listRate = mat(listRate)
    normRateData = listRate - tile(minRate, (m, 1))
    normRateData = normRateData / tile(rangeRateData, (m, 1))
    normRateData = normRateData[0, :]

    rangeDistData = float(maxDist - minDist)
    listDistance = mat(listDistance)
    normDistData = listDistance - tile(minDist, (m, 1))
    normDistData = normDistData / tile(rangeDistData, (m, 1))
    normDistData = normDistData[0, :]

    rangePriceData = float(maxPrice - minPrice)
    listPrice = mat(listPrice)
    normPriceData = listPrice - tile(minPrice, (m, 1))
    normPriceData = normPriceData / tile(rangePriceData, (m, 1))
    normPriceData = normPriceData[0, :]

    bestList = []
    for num in range(shape(restraurantData['pois'])[0]):
        best = normRateData[0, num] / (normDistData[0, num] + normPriceData[0, num] / 10)
        if best > bestNum:
            bestNum = best
            bestNumIndex = num

    bestList.append("性价比最高酒店：" + restraurantData['pois'][bestNumIndex]['name'].encode('utf-8'))
    bestList.append(restraurantData['pois'][bestNumIndex]['location'].encode('utf-8'))
    bestList.append(restraurantData['pois'][bestNumIndex]['address'].encode('utf-8'))
    return bestList





class RestService(DefinitionBase):

    @soap(String,Integer,_returns=Array(Array(String)))
    def rest(self,hotelName,selNum):
        print hotelName
        restList,hotelLocation,restraurantData = selHotel(hotelName)
        #print restList
        if selNum == 1:
            rest_list = rest_distance_recom(restraurantData, hotelLocation)
        if selNum == 2:
            rest_list = rest_price_recom(restraurantData, hotelLocation)
        if selNum == 3:
            rest_list = rest_rate_recom(restraurantData, hotelLocation)
        if selNum == 4:
            rest_list = rest_best_recom(restraurantData, hotelLocation)
        restList.append(rest_list)
        print restList
        return restList





try:
    from wsgiref.simple_server import make_server

    soap_application = soaplib.core.Application([RestService], 'tns')
    wsgi_application = wsgi.Application(soap_application)
    server = make_server('localhost', 8090, wsgi_application)
    print 'soap server starting......'
    server.serve_forever()
except ImportError:
    print "Error: example server code requires Python >= 2.5"