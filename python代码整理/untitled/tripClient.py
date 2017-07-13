#coding:utf8
import logging
from suds.client import Client
def hello(cityName):
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8088/?wsdl', cache=None)
    result = hello_client.service.trip_name(cityName.decode("utf-8"))
    return result


from flask import Flask, jsonify,abort
import json
#from json import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/todo/api/v1.0/cityName=<cityName>', methods=['GET'])
def get_task(cityName):
    result = hello(cityName)
    return json.dumps(result)

app.run(debug=True)