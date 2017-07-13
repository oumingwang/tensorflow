#coding:utf8
import logging
from suds.client import Client
from flask import Flask, jsonify,abort

def hello():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8089/?wsdl', cache=None)
    result= hello_client.service.hotel("海口观澜湖".decode("utf-8"),4)
    return result




