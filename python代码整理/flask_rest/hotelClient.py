#coding:utf8
import logging
from suds.client import Client
def hotel(viewName,selName):
    print viewName
    print type(selName)
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8089/?wsdl', cache=None)
    result= hello_client.service.hotel(viewName,selName)
    return result



from flask import Flask, jsonify,abort
import json


app = Flask(__name__)

#result = hello()
#print result

@app.route('/api/hotel/viewpointName=<viewName>&&selName=<selName>', methods=['GET'])
def get_hotel(viewName,selName):
    result = hotel(viewName,selName)
    return json.dumps(result)

app.run(debug=True)

