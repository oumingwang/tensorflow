#coding:utf8
import logging
from suds.client import Client

def hello(cityName):
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8088/?wsdl', cache=None)
    result = hello_client.service.trip_name(cityName.decode('utf-8'))
    return result

def season():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8088/?wsdl', cache=None)
    result = hello_client.service.trip_season()
    return result

print hello('海口')
#print season()