#coding:utf8
import logging
from suds.client import Client

def hospital(hospitalName):
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8091/?wsdl', cache=None)
    result = hello_client.service.hospital(hospitalName.decode("utf-8"))
    print result

print hospital("海口观澜湖")