#coding:utf8
import logging
from suds.client import Client

def restSel(hotelName,selNum):
    #hotelname = '海口观澜湖度假酒店'.decode("utf-8")
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8090/?wsdl', cache=None)
    result = hello_client.service.rest(hotelName.decode("utf-8"),selNum)
    print result

print restSel('海口观澜湖度假酒店',3)

