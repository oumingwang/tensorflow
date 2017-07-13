#coding:utf8
import logging
from suds.client import Client

def restSel(hotelName,selNum):
    #hotelname = '海口观澜湖度假酒店'.decode("utf-8")
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8090/?wsdl', cache=None)
    result = hello_client.service.rest(hotelName,selNum)
    #print result
    return result

#print restSel('海口观澜湖度假酒店',4)

from flask import Flask, jsonify,abort
import json


app = Flask(__name__)

#result = hello()
#print result

@app.route('/api/rest/hotelName=<hotelName>&&selName=<selName>', methods=['GET'])
def get_rest(hotelName,selName):
    result = restSel(hotelName,selName)
    #print result
    return json.dumps(result)

app.run(debug=True)