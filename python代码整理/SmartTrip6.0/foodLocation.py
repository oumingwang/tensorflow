#coding:utf-8
import requests
from numpy import *

def restaurantData(hotelData):
    url = "http://restapi.amap.com/v3/place/around?key=c912883876e0baa8beb279f31efac462&location=%s&keywords=饭店&types=&offset=&page=&extensions=all" % hotelData
    response = requests.request("GET", url)
    data = response.json()
    return data
