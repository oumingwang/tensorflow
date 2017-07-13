#coding:utf8
import requests
import locationRequest
import hotelLocation
import destina
from numpy import *
tripName ={u'reason': u'\u6210\u529f', u'error_code': 0, u'result': [{u'cityId': u'133', u'title': u'\u4e9a\u9f99\u6e7e\u70ed\u5e26\u5929\u5802\u68ee\u6797\u516c\u56ed\uff08\u975e\u8bda\u52ff\u6270\u2161\u62cd\u6444\u5730\uff09', u'grade': u'AAAA', u'sid': u'26358', u'price_min': u'80', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_26358.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u4e9a\u9f99\u6e7e\u56fd\u5bb6\u65c5\u6e38\u5ea6\u5047\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/05/17/PxL6ZO_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u8708\u652f\u6d32\u5c9b', u'grade': u'AAAAA', u'sid': u'8078', u'price_min': u'60', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_8078.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u6797\u65fa\u9547\u6d77\u68e0\u6e7e\u8708\u652f\u6d32\u5c9b\u5ea6\u5047\u4e2d\u5fc3', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/07/18/dI7lpU_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u9e7f\u56de\u5934\u98ce\u666f\u533a', u'grade': u'AAA', u'sid': u'9724', u'price_min': u'32', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9724.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u9e7f\u5cad\u8def\u9e7f\u56de\u5934\u516c\u56ed', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/08/17/ddXZ8m_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5929\u6daf\u6d77\u89d2', u'grade': u'AAAA', u'sid': u'1370', u'price_min': u'60', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_1370.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5929\u6daf\u9547\u9a6c\u5cad\u5c71\u9e93\u5929\u6daf\u6d77\u89d2\u6e38\u89c8\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/07/09/7hemXP_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u4e09\u4e9a\u5927\u5c0f\u6d1e\u5929', u'grade': u'AAAAA', u'sid': u'6651', u'price_min': u'116', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_6651.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5d16\u57ce\u5927\u5c0f\u6d1e\u5929\u65c5\u6e38\u533a', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/08/19/HStAFU_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u73e0\u6c5f\u5357\u7530\u6e29\u6cc9', u'grade': u'', u'sid': u'9739', u'price_min': u'150', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9739.html', u'address': u'\u6d77\u5357\u4e09\u4e9a\u6d77\u68e0\u6e7e\u5357\u7530\u65c5\u6e38\u57ce\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/11/02/16/1J0a9T_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5357\u5c71\u5bfa', u'grade': u'AAAAA', u'sid': u'9738', u'price_min': u'138', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9738.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5d16\u57ce\u9547\u5357\u5c71\u6587\u5316\u65c5\u6e38\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/06/17/M2UcTE_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u4e09\u4e9a\u5947\u5e7b\u827a\u672f\u4f53\u9a8c\u9986', u'grade': u'', u'sid': u'28723', u'price_min': u'68', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_28723.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u91d1\u9e21\u5cad\u6021\u548c\u8c6a\u5ead1-2\u5c42\uff08\u65b0\u4e00\u4e2d\u5bf9\u9762\uff09', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/12/14/lzbWUf_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5440\u8bfa\u8fbe\u96e8\u6797\uff08hold\u4f4f\u7231\u62cd\u6444\u5730\uff09', u'grade': u'AAAAA', u'sid': u'21294', u'price_min': u'138', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_21294.html', u'address': u'\u6d77\u5357\u7701\u4fdd\u4ead\u53bf\u56fd\u8425\u4e09\u9053\u519c\u573a\u5440\u8bfa\u8fbe\u96e8\u6797\u666f\u533a', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/05/19/qFmw1C_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u897f\u5c9b\u6d77\u6d0b\u6587\u5316\u65c5\u6e38\u533a', u'grade': u'AAAA', u'sid': u'9750', u'price_min': u'118', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9750.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u4e09\u4e9a\u6e7e\u8def\u8096\u65d7\u6e2f\u7801\u5934', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/12/11/FYDc4B_240x135_00.jpg'}]}

viewpoint_name =  tripName['result'][1]['title']
viewpoint_grade =  tripName['result'][1]['grade']
viewpoint_price_min =  tripName['result'][1]['price_min']
viewpoint_address = tripName['result'][1]['address']
viewpoint_imgurl = tripName['result'][1]['imgurl']
viewpoint_location = locationRequest.viewpoint(viewpoint_name)

# encoding: utf-8
# !/usr/bin/python

'''''Tkinter教程之Frame篇'''
# Frame就是屏幕上的一块矩形区域，多是用来作为容器（container）来布局窗体。
'''''1.创建Frame'''
# -*- coding: cp936 -*-
from Tkinter import *
import tkMessageBox
root = Tk()
hotelMSG = {}
#hotel = Tk()
#hotel.title("宾馆信息")
var = IntVar()

def sel(data,viewpoint_location):
    str1 = str(var.get())
    i = int(str1)
    hotel_location =  '宾馆经纬度：' + data[i]['location'].encode('utf-8')
    destination = destina.viewpoint(data[i]['location'].encode('utf-8'),viewpoint_location)
    tkMessageBox.showinfo('距离景区步行距离','距离景区步行距离：' + str(destination).encode("utf-8")+"米")

def view_hotel(viewpoint_name,viewpoint_location):
    #root.destroy()

    hotel_name = viewpoint_name.encode('utf-8') + '宾馆'
    hotelMSG['hotel_name'] = hotel_name
    #print hotel_name
    data = hotelLocation.hotel(hotel_name)
    #print hotel_location
    for hotel_data in range(shape(data)[0]):
        hotel_name =  '宾馆名称：' + data[hotel_data]['name'].encode('utf-8')
        hotel_location = '宾馆经纬度：' + data[hotel_data]['location'].encode('utf-8')
        hotel_tel = '宾馆电话：' + data[hotel_data]['tel'].encode('utf-8')
        hotel_address = '宾馆地址：' + data[hotel_data]['address'].encode('utf-8')
        if len(data[hotel_data]['biz_ext']['rating']):
            hotel_rate = '宾馆评分：' + (data[hotel_data]['biz_ext']['rating']).encode('utf-8')
        else  :
            hotel_rate = '无'
        if len(data[hotel_data]['biz_ext']['lowest_price']):
            hotel_minprice = '宾馆最低消费：' + (data[hotel_data]['biz_ext']['lowest_price']).encode('utf-8')
        else:
            hotel_minprice = '无'
        Radiobutton(root, text=[hotel_name,hotel_location,hotel_tel,hotel_address,hotel_rate,hotel_minprice], variable=var, value=hotel_data,command=lambda : sel(data,viewpoint_location)).grid(row=hotel_data+6,column=0)



titleL1 = Label(root,text = '景区名称：').grid(row=0,column=0)
titleL2 = Label(root,text = viewpoint_name).grid(row=0,column=1)
titleL3 = Label(root,text = '景区星级：').grid(row=1,column=0)
titleL4 = Label(root,text = viewpoint_grade).grid(row=1,column=1)
titleL5 = Label(root,text = '最低票价：').grid(row=2,column=0)
titleL6 = Label(root,text = viewpoint_price_min).grid(row=2,column=1)
titleL7 = Label(root,text = '景区地址：').grid(row=3,column=0)
titleL8 = Label(root,text = viewpoint_address).grid(row=3,column=1)
titleL7 = Label(root,text = '景区经纬度：').grid(row=4,column=0)
titleL8 = Label(root,text = viewpoint_location).grid(row=4,column=1)
hotelButton = Button(root,text='寻找景点周围宾馆',command = lambda : view_hotel(viewpoint_name,viewpoint_location)).grid(row=5,column=0)
doctButton = Button(root,text='寻找景点周围医院').grid(row=5,column=1)

#hotel.mainloop()
root.mainloop()



