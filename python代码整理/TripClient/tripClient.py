#coding:utf8
import logging
from suds.client import Client
def  viewpoint(cityName):
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8088/?wsdl', cache=None)
    result = hello_client.service.trip_name(cityName)
    return result

'''
def hotel(viewName,selName):
    print viewName
    print selName
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8089/?wsdl', cache=None)
    result= hello_client.service.hotel("海口观澜湖".decode("utf-8"),4)
    return result
'''


from flask import Flask, jsonify,abort
import json
#from json import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/viewpoint/cityName=<cityName>', methods=['GET'])
def get_viewpoint(cityName):
    result = viewpoint(cityName)
    return json.dumps(result)

'''
@app.route('/api/hotel/viewpointName=<viewName>&&selName=<int:selName>', methods=['GET'])
def get_hotel(viewName,selName):
    result = hotel(viewName,selName)
    return json.dumps(result)
'''
app.run(debug=True)