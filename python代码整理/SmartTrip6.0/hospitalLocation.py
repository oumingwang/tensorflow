#coding:utf-8
import requests
from numpy import *

def hospitalData(hospitalData):
    url = "http://restapi.amap.com/v3/place/around?key=c912883876e0baa8beb279f31efac462&location=%s&keywords=医院&types=&offset=&page=&extensions=all" % hospitalData
    response = requests.request("GET", url)
    data = response.json()
    return data