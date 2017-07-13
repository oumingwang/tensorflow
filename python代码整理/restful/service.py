#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-04 14:03:19
# @Author  : pinghailinfeng (pinghailinfeng79@gmail.com)
# @Link    : http://my.oschina.net/dlpinghailinfeng
# @Version : $Id$

import web
import xml.etree.ElementTree as ET

#tree = ET.parse('users.xml')
#root = tree.getroot()
#print root
urls=(
'/users/hello/city={}'.format("三亚".encode("utf-8")),'hello',
)
app = web.application(urls,globals())


class hello:
	def GET(self):
		return ["hello world"]

'''
	'/users','list_users',
	'/users/(.*)','get_user',
class list_users:
	def GET(self):
		output = 'users:[';
		for child in root:
			print 'child',child.tag,child.attrib
			output +=str(child.attrib)+','
		output += ']';
		print output
		return output
class get_user:
	def GET(self,user):
		for child in root:
		    if child.attrib['id']==user:
		    		return str(child.attrib)
		    		
'''
if __name__ == '__main__':
		app.run()