#coding:utf8
import logging
from suds.client import Client

def hospital(hospitalName):
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8091/?wsdl', cache=None)
    result = hello_client.service.hospital(hospitalName)
    #print result
    return result
#print hospital("海口观澜湖")


from flask import Flask, jsonify,abort
import json


app = Flask(__name__)

#result = hello()
#print result

@app.route('/api/hospital/viewpointName=<viewName>', methods=['GET'])
def get_hotel(viewName):
    result = hospital(viewName)
    return json.dumps(result)

app.run(debug=True)