#coding:utf8
from Tkinter import *
import hotelLocation
from numpy import *
import Trip
import locationRequest
import destina
import foodLocation
import hospitalLocation
import tkMessageBox

root = Tk()
root.title('智能旅游助手')
var = IntVar()
msg = Tk()

hotelDataTotal = {}
hotelDistance = []
hotelRate = []
hotelPrice = []



#选择宾馆按钮
def selHotel(data,viewpoint_location):
    str1 = str(var.get())
    i = int(str1)
    #hotel_location =  '宾馆经纬度：' + data[i]['location'].encode('utf-8')
    restaurant = Tk()
    restaurant.title("选择宾馆周围饭店")
    #estination = destina.viewpoint(data[i]['location'].encode('utf-8'),viewpoint_location)
    restraurantData  = foodLocation.restaurantData(data[i]['location'].encode('utf-8'))
    for restaurant_num in range(shape(restraurantData['pois'])[0]):
        reName =  '饭店名称：' + restraurantData['pois'][restaurant_num]['name'].encode('utf-8')
        if len(restraurantData['pois'][restaurant_num]['tel']):
            reTel =  '饭店电话：' + restraurantData['pois'][restaurant_num]['tel'].encode('utf-8')
        else:
            reTel = '饭店电话：' + '无'
        reAddress =  '饭店地址：' + restraurantData['pois'][restaurant_num]['address'].encode('utf-8')
        reLocation =  '饭店经纬度：' + restraurantData['pois'][restaurant_num]['location'].encode('utf-8')
        if len(restraurantData['pois'][restaurant_num]['biz_ext']['rating']):
            reRate =  '饭店评分：' + restraurantData['pois'][restaurant_num]['biz_ext']['rating'].encode('utf-8')
        else:
            reRate = '饭店评分：' + '0'
        if len(restraurantData['pois'][restaurant_num]['biz_ext']['cost']):
            reMin =  '饭店最低消费：' + restraurantData['pois'][restaurant_num]['biz_ext']['cost'].encode('utf-8')
        else:
            reMin = '饭店最低消费' + '0'

        Radiobutton(restaurant, text=[reName,reAddress,reTel,reRate,reMin,reLocation], variable=var, value=restaurant_num).grid(row=restaurant_num,column=0)
    restaurant.mainloop()


#选择景点按钮
def selViewpoint(tripName):
    str1 = str(var.get())
    i = int(str1)
    name = (tripName['result'][i]['title']).encode('utf-8')
    msg.title(name + '景点介绍')
    viewpoint_name = tripName['result'][i]['title']
    viewpoint_grade = tripName['result'][i]['grade']
    viewpoint_price_min = tripName['result'][i]['price_min']
    viewpoint_address = tripName['result'][i]['address']
    #viewpoint_imgurl = tripName['result'][1]['imgurl']
    viewpoint_location = locationRequest.viewpoint(viewpoint_name)
    '''
    grade = 'grade' +  tripName['result'][i]['grade'].encode('utf-8')
    price_min = 'price_min' + tripName['result'][i]['price_min'].encode('utf-8')
    address = 'address' + tripName['result'][i]['address'].encode('utf-8')
    '''
    titleL1 = Label(msg, text='景区名称：').grid(row=0, column=0)
    titleL2 = Label(msg, text=viewpoint_name).grid(row=0, column=1)
    titleL3 = Label(msg, text='景区星级：').grid(row=1, column=0)
    titleL4 = Label(msg, text=viewpoint_grade).grid(row=1, column=1)
    titleL5 = Label(msg, text='最低票价：').grid(row=2, column=0)
    titleL6 = Label(msg, text=viewpoint_price_min).grid(row=2, column=1)
    titleL7 = Label(msg, text='景区地址：').grid(row=3, column=0)
    titleL8 = Label(msg, text=viewpoint_address).grid(row=3, column=1)
    titleL7 = Label(msg, text='景区经纬度：').grid(row=4, column=0)
    titleL8 = Label(msg, text=viewpoint_location).grid(row=4, column=1)
    hotelButton = Button(msg, text='寻找景点周围饭店', command=lambda: view_hotel(viewpoint_name, viewpoint_location)).grid(
        row=5, column=0)
    hospitalButton = Button(msg, text='寻找景点周围医院',command=lambda: view_hospital(viewpoint_location)).grid(row=5, column=1)
    msg.mainloop()

#寻找景区附近的医院
def view_hospital(viewpoint_location):
    hospitalData = hospitalLocation.hospitalData(viewpoint_location.encode("utf-8"))
    hospital = Tk()
    hospital.title("选择景点周围的医院")
    for hospital_num in range(shape(hospitalData['pois'])[0]):
        hoName = '医院名称：' + hospitalData['pois'][hospital_num]['name'].encode('utf-8')
        if len(hospitalData['pois'][hospital_num]['tel']):
            hoTel = '医院电话：' + hospitalData['pois'][hospital_num]['tel'].encode('utf-8')
        else:
            hoTel = '医院电话：' + '无'
        hoAddress = ''.join(hospitalData['pois'][hospital_num]['address'])
        hoLocation = '医院经纬度：' + hospitalData['pois'][hospital_num]['location'].encode('utf-8')
        hoType = '医院类型：' + hospitalData['pois'][hospital_num]['type'].encode('utf-8')
        Radiobutton(hospital, text=[hoName, hoTel, hoAddress, hoLocation,hoType], variable=var,value=hospital_num).grid(row=hospital_num, column=0)
    hospital.mainloop()



#寻找景区周围宾馆
def view_hotel(viewpoint_name,viewpoint_location):
    #root.destroy()
    hotel_name = viewpoint_name.encode('utf-8') + '宾馆'
    data = hotelLocation.hotel(hotel_name)

    for hotel_data in range(shape(data)[0]):
        hotel_name =  data[hotel_data]['name'].encode('utf-8')
        hotel_location = data[hotel_data]['location'].encode('utf-8')

        #景点与宾馆的距离
        hotel_view_distance = destina.viewpoint(data[hotel_data]['location'].encode('utf-8'),viewpoint_location)

        #hotel_tel = '宾馆电话：' + data[hotel_data]['tel'].encode('utf-8')
        hotel_address = ''.join(data[hotel_data]['address'])
        if len(data[hotel_data]['biz_ext']['rating']):
            hotel_rate = ''.join(data[hotel_data]['biz_ext']['rating'])
            hotelRate = float((data[hotel_data]['biz_ext']['rating']).encode('utf-8')) + 1
        else  :
            hotel_rate = '1'
            hotelRate = 1

        if len(data[hotel_data]['biz_ext']['lowest_price']):
            hotel_minprice =(str(data[hotel_data]['biz_ext']['lowest_price'])).encode('utf-8')
            #hotelMinPrice = (data[hotel_data]['biz_ext']['lowest_price']).encode('utf-8')
        else:
            hotel_minprice = '无'
            #hotelMinPrice = 30000


        Radiobutton(root,text='最短距离推荐',command=lambda : hotel_distance_recom(data,viewpoint_location)).grid(row = 3,column=0)
        Radiobutton(root, text='最低消费推荐',command=lambda : hotel_price_recom(data,viewpoint_location)).grid(row=4, column=0)
        Radiobutton(root, text='最佳评分推荐',command=lambda : hotel_rate_recom(data,viewpoint_location)).grid(row=5, column=0)
        Radiobutton(root, text='性价比推荐', command=lambda: hotel_best_recom(data,viewpoint_location)).grid(row=6, column=0)
        Radiobutton(root, text=["宾馆名称：" + hotel_name,'宾馆经纬度：' + hotel_location,hotel_address,"宾馆评分：" + hotel_rate.encode("utf-8"),"宾馆最低消费：" + hotel_minprice,'距离：'+ str(hotel_view_distance)], variable=var, value=hotel_data,command=lambda : selHotel(data,viewpoint_location)).grid(row=hotel_data+2,column=1)
    #print minDistanceIndex


#宾馆距离排序
def hotel_distance_recom(data,viewpoint_location):
    minDistance = 10000000
    minDistanceIndex = 0
    for hotel_data in range(shape(data)[0]):
        # 景点与宾馆的距离
        hotel_view_distance = destina.viewpoint(data[hotel_data]['location'].encode('utf-8'), viewpoint_location)
        if hotel_view_distance < minDistance:
            minDistance = hotel_view_distance
            minDistanceIndex = hotel_data

    tkMessageBox.showinfo("最短距离酒店为：",[data[minDistanceIndex]['name'].encode('utf-8'),
                                      '宾馆经纬度：' + data[minDistanceIndex]['location'].encode('utf-8'),
                                      '宾馆地址：' + data[minDistanceIndex]['address'].encode('utf-8'),
                                      ])


#宾馆价格排序

def hotel_price_recom(data,viewpoint_location):
    minPrice = inf
    minPriceIndex = 0
    for hotel_data in range(shape(data)[0]):
        if len(''.join(data[hotel_data]['biz_ext']['lowest_price'])):
            hotel_minprice = '宾馆最低消费：' + (data[hotel_data]['biz_ext']['lowest_price']).encode('utf-8')
            hotelPrice = float((data[hotel_data]['biz_ext']['lowest_price']).encode('utf-8')) + 1
        else:
            hotel_minprice = '无最低消费记录无'
            hotelPrice = 100000

        if hotelPrice < minPrice:
            minPrice = hotelPrice
            minPriceIndex = hotel_data
    tkMessageBox.showinfo("消费最低酒店为：", [data[minPriceIndex]['name'].encode('utf-8'),
                                       '宾馆经纬度：' + data[minPriceIndex]['location'].encode('utf-8'),
                                       '宾馆地址：' + data[minPriceIndex]['address'].encode('utf-8'),
                                       ])


#宾馆评价排序
def hotel_rate_recom(data,viewpoint_location):
    minRate = inf
    minRateIndex = 0
    for hotel_data in range(shape(data)[0]):
        if len(data[hotel_data]['biz_ext']['rating']):
            hotel_rate = '宾馆评分：' + (data[hotel_data]['biz_ext']['rating']).encode('utf-8')
            hotelRate = (data[hotel_data]['biz_ext']['rating']).encode('utf-8')
        else:
            hotel_rate = '无'
            hotelRate = 1.0
        if hotelRate > minRate:
            minRate = hotelRate
            minRateIndex = hotel_data

    tkMessageBox.showinfo("评分最好酒店为：", [data[minRateIndex]['name'].encode('utf-8'),
                                       '宾馆经纬度：' + data[minRateIndex]['location'].encode('utf-8'),
                                       '宾馆地址：' + data[minRateIndex]['address'].encode('utf-8'),
                                       ])


#性价比推荐
def hotel_best_recom(data,viewpoint_location):
    listDistance = []
    listRate = []
    listPrice = []

    bestNum = 0
    bestNumIndex = 0
    m = shape(data)[0]

    for hotel_data in range(shape(data)[0]):
        hotel_view_distance = destina.viewpoint(data[hotel_data]['location'].encode('utf-8'), viewpoint_location)
        listDistance.append(float(hotel_view_distance))


        if len(data[hotel_data]['biz_ext']['rating']):
            hotelRate = float((data[hotel_data]['biz_ext']['rating']).encode('utf-8'))
        else:
            hotelRate = 1.0
        listRate.append(hotelRate)

        if len(data[hotel_data]['biz_ext']['lowest_price']):
            hotelPrice = float((data[hotel_data]['biz_ext']['lowest_price']).encode('utf-8')) + 1
        else:
            hotelPrice = 30000
        listPrice.append(hotelPrice)

    maxDist = mat(listDistance).max()
    minDist = mat(listDistance).min()
    maxRate = mat(listRate).max()
    minRate = mat(listRate).min()
    maxPrice = mat(listPrice).max()
    minPrice = mat(listPrice).min()

    rangeRateData = float(maxRate - minRate)
    listRate = mat(listRate)
    normRateData = listRate - tile(minRate,(m,1))
    normRateData = normRateData/tile(rangeRateData,(m,1))
    normRateData = normRateData[0,:]


    rangeDistData = float(maxDist - minDist)
    listDistance = mat(listDistance)
    normDistData = listDistance - tile(minDist, (m, 1))
    normDistData = normDistData / tile(rangeDistData, (m, 1))
    normDistData = normDistData[0, :]


    rangePriceData = float(maxPrice - minPrice)
    listPrice = mat(listPrice)
    normPriceData = listPrice - tile(minPrice, (m, 1))
    normPriceData = normPriceData / tile(rangePriceData, (m, 1))
    normPriceData = normPriceData[0, :]


    for num in range(shape(data)[0]):
        best = normRateData[0,num]/(normDistData[0,num] + normPriceData[0,num]/10)
        if  best > bestNum:
            bestNum = best
            bestNumIndex = num

    tkMessageBox.showinfo("性价比酒店推荐：", [data[bestNumIndex]['name'].encode('utf-8'),
                                           '宾馆经纬度：' + data[bestNumIndex]['location'].encode('utf-8'),
                                           '宾馆地址：' + data[bestNumIndex]['address'].encode('utf-8'),
                                           ])


#主页面确定按钮
def submit():
    #trip = Tk()
    #trip.title('Hello')
    tripName = Trip.tripRecom(cityValue.get().encode('utf-8'))
    for trip_name in range(shape(tripName['result'])[0]):
        name = tripName['result'][trip_name]['title'].encode('utf-8')
        Radiobutton(root, text=[name], variable=var, value=trip_name, command=lambda :selViewpoint(tripName)).grid(row=2+trip_name,column=1)
    #trip.mainloop()

#主页面重置按钮
def reset(cityValue):
    cityValue.set("")


cityValue = StringVar()
L1 = Label(root, text="City Name")
L1.grid(row=0,column=0)
cityEdit = Entry(root, bd=5,textvariable=cityValue)
cityEdit.grid(row=0,column=2)
Button(root, text ='确定', command =submit).grid(row=1,column=1)
Button(root, text ='重置', command = lambda : reset(cityValue) ).grid(row=1,column=2)

root.mainloop()



