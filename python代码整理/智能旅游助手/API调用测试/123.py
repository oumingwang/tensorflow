#coding:utf-8
#print u'\u67e5\u8be2\u6210\u529f'\

'''
    viewpoint_name = {u'reason': u'\u6210\u529f', u'error_code': 0, u'result': [{u'cityId': u'133', u'title': u'\u4e9a\u9f99\u6e7e\u70ed\u5e26\u5929\u5802\u68ee\u6797\u516c\u56ed\uff08\u975e\u8bda\u52ff\u6270\u2161\u62cd\u6444\u5730\uff09', u'grade': u'AAAA', u'sid': u'26358', u'price_min': u'80', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_26358.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u4e9a\u9f99\u6e7e\u56fd\u5bb6\u65c5\u6e38\u5ea6\u5047\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/05/17/PxL6ZO_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u8708\u652f\u6d32\u5c9b', u'grade': u'AAAAA', u'sid': u'8078', u'price_min': u'60', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_8078.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u6797\u65fa\u9547\u6d77\u68e0\u6e7e\u8708\u652f\u6d32\u5c9b\u5ea6\u5047\u4e2d\u5fc3', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/07/18/dI7lpU_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u9e7f\u56de\u5934\u98ce\u666f\u533a', u'grade': u'AAA', u'sid': u'9724', u'price_min': u'32', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9724.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u9e7f\u5cad\u8def\u9e7f\u56de\u5934\u516c\u56ed', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/08/17/ddXZ8m_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5929\u6daf\u6d77\u89d2', u'grade': u'AAAA', u'sid': u'1370', u'price_min': u'60', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_1370.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5929\u6daf\u9547\u9a6c\u5cad\u5c71\u9e93\u5929\u6daf\u6d77\u89d2\u6e38\u89c8\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/07/09/7hemXP_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u4e09\u4e9a\u5927\u5c0f\u6d1e\u5929', u'grade': u'AAAAA', u'sid': u'6651', u'price_min': u'116', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_6651.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5d16\u57ce\u5927\u5c0f\u6d1e\u5929\u65c5\u6e38\u533a', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/08/19/HStAFU_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u73e0\u6c5f\u5357\u7530\u6e29\u6cc9', u'grade': u'', u'sid': u'9739', u'price_min': u'150', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9739.html', u'address': u'\u6d77\u5357\u4e09\u4e9a\u6d77\u68e0\u6e7e\u5357\u7530\u65c5\u6e38\u57ce\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/11/02/16/1J0a9T_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5357\u5c71\u5bfa', u'grade': u'AAAAA', u'sid': u'9738', u'price_min': u'138', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9738.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5d16\u57ce\u9547\u5357\u5c71\u6587\u5316\u65c5\u6e38\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/06/17/M2UcTE_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u4e09\u4e9a\u5947\u5e7b\u827a\u672f\u4f53\u9a8c\u9986', u'grade': u'', u'sid': u'28723', u'price_min': u'68', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_28723.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u91d1\u9e21\u5cad\u6021\u548c\u8c6a\u5ead1-2\u5c42\uff08\u65b0\u4e00\u4e2d\u5bf9\u9762\uff09', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/12/14/lzbWUf_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5440\u8bfa\u8fbe\u96e8\u6797\uff08hold\u4f4f\u7231\u62cd\u6444\u5730\uff09', u'grade': u'AAAAA', u'sid': u'21294', u'price_min': u'138', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_21294.html', u'address': u'\u6d77\u5357\u7701\u4fdd\u4ead\u53bf\u56fd\u8425\u4e09\u9053\u519c\u573a\u5440\u8bfa\u8fbe\u96e8\u6797\u666f\u533a', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/05/19/qFmw1C_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u897f\u5c9b\u6d77\u6d0b\u6587\u5316\u65c5\u6e38\u533a', u'grade': u'AAAA', u'sid': u'9750', u'price_min': u'118', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9750.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u4e09\u4e9a\u6e7e\u8def\u8096\u65d7\u6e2f\u7801\u5934', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/12/11/FYDc4B_240x135_00.jpg'}]}
s = u'109.334090,18.302638'
s = s.split(',')
print type(s)
print type (s)
print type(float(s[0].encode("utf-8")))
'''

'''
foodLocation = {u'resultcode': u'200', u'error_code': 0, u'reason': u'\u67e5\u8be2\u6210\u529f', u'result': [
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'0',
     u'address': u'\u4e8c\u4e8c\u4e94\u56fd\u9053\u5929\u6daf\u9547\u653f\u5e9c\u5bf9\u9762', u'phone': u'15008992698',
     u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'1', u'stars': u'0.0',
     u'latitude': u'18.30687', u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i2.dpfile.com/pc/5a48e56f448ddc36bb85da5b1744cd69/29514370_m.jpg', u'avg_price': u'0',
     u'product_rating': u'', u'very_bad_remarks': u'0', u'name': u'\u99a8\u7f18\u95e8\u524d\u996d\u5e97',
     u'common_remarks': u'0', u'bad_remarks': u'0', u'longitude': u'109.32785', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'1',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u99a8\u7f18\u95e8\u524d\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'',
     u'address': u'\u4e8c\u4e8c\u4e94\u56fd\u9053\u4e0e\u9752\u9f99\u8857\u4ea4\u754c\u5904', u'phone': u'13111950628',
     u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'', u'stars': u'0.0',
     u'latitude': u'18.30619', u'tags': u'\u5c0f\u5403\u9762\u98df,\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u5929\u9a6c\u98df\u5e97',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33153', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5c0f\u5403\u9762\u98df>>\u5929\u9a6c\u98df\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'',
     u'address': u'\u5929\u6daf\u9547\u9a6c\u5cad\u5c71(\u6d77\u6ee8\u897f\u4fa7)', u'phone': u'',
     u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'', u'stars': u'0.0',
     u'latitude': u'18.30694', u'tags': u'\u5c0f\u5403\u9762\u98df,\u6cb3\u4e1c\u533a',
     u'photos': u'http://i3.dpfile.com/ci/20111104/8203326.143141.893.jpg/17928059_m.jpg', u'avg_price': u'0',
     u'product_rating': u'', u'very_bad_remarks': u'',
     u'name': u'\u5929\u6daf\u6d77\u89d2\u6e38\u89c8\u533a\u4f11\u95f2\u5427', u'common_remarks': u'',
     u'bad_remarks': u'', u'longitude': u'109.3319', u'nearby_shops': u'', u'environment_rating': u'',
     u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u6cb3\u4e1c\u533a>>\u5c0f\u5403\u5feb\u9910>>\u5c0f\u5403\u9762\u98df>>\u5929\u6daf\u6d77\u89d2\u6e38\u89c8\u533a\u4f11\u95f2\u5427'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'',
     u'stars': u'0.0', u'latitude': u'18.30608', u'tags': u'\u9762\u5305\u751c\u70b9,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u907f\u98ce\u5858',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33199', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u9762\u5305\u751c\u70b9>>\u907f\u98ce\u5858'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u5e02\u533a', u'very_good_remarks': u'',
     u'stars': u'0.0', u'latitude': u'18.30613', u'tags': u'\u66f4\u591a\u9152\u5e97\u4f4f\u5bbf,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'',
     u'name': u'\u6ee1\u5c4b\u751c\u54c1\u86cb\u7cd5', u'common_remarks': u'', u'bad_remarks': u'',
     u'longitude': u'109.33222', u'nearby_shops': u'', u'environment_rating': u'', u'recommended_products': u'',
     u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u5e02\u533a>>\u4e09\u4e9a\u6e7e>>\u9762\u5305\u751c\u70b9>>\u6ee1\u5c4b\u751c\u54c1\u86cb\u7cd5'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u5e02\u533a', u'very_good_remarks': u'',
     u'stars': u'0.0', u'latitude': u'18.30573', u'tags': u'\u9762\u5305\u751c\u70b9,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u725b\u725b\u86cb\u7cd5\u574a',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33231', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u5e02\u533a>>\u4e09\u4e9a\u6e7e>>\u9762\u5305\u751c\u70b9>>\u725b\u725b\u86cb\u7cd5\u574a'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'0',
     u'address': u'\u5929\u6daf\u9547\u4e2d\u5fc3\u5b66\u6821\u5bf9\u9762', u'phone': u'', u'city': u'\u4e09\u4e9a',
     u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'1', u'stars': u'0.0', u'latitude': u'18.30584',
     u'tags': u'\u5176\u4ed6\u4e2d\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i1.dpfile.com/pc/e75c04fa7ef9de8e75399b66698fabe7/37568823_m.jpg', u'avg_price': u'0',
     u'product_rating': u'', u'very_bad_remarks': u'0', u'name': u'\u65b0\u519c\u6751\u996d\u5e84',
     u'common_remarks': u'0', u'bad_remarks': u'0', u'longitude': u'109.33277', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'1',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5176\u4ed6>>\u5176\u4ed6\u4e2d\u9910>>\u65b0\u519c\u6751\u996d\u5e84'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u5e02\u533a', u'very_good_remarks': u'',
     u'stars': u'0.0', u'latitude': u'18.30558', u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u6d3b\u4e30\u996d\u5e97',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33285', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u5e02\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u6d3b\u4e30\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'314\u7701\u9053',
     u'phone': u'0898-88911948', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'', u'stars': u'0.0', u'latitude': u'18.30608',
     u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'',
     u'name': u'\u9ea6\u5ba2\u4ed5\u70b8\u9e21\u6c49\u5821', u'common_remarks': u'', u'bad_remarks': u'',
     u'longitude': u'109.3331', u'nearby_shops': u'', u'environment_rating': u'', u'recommended_products': u'',
     u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u9ea6\u5ba2\u4ed5\u70b8\u9e21\u6c49\u5821'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'',
     u'address': u'\u4e8c\u4e8c\u4e94\u56fd\u9053\u5929\u6daf\u9547\u9a6c\u5cad\u5c45\u59d4\u4f1a\u5bf9\u9762',
     u'phone': u'0898-88910003', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'', u'stars': u'0.0', u'latitude': u'18.30543', u'tags': u'\u5ddd\u83dc,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i2.dpfile.com/pc/07d2e098efe0df01dac02237be1dbf0e/41231884_m.jpg', u'avg_price': u'0',
     u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u8001\u743c\u6d77\u996d\u5e97',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33362', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5ddd\u83dc>>\u8001\u743c\u6d77\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'\u5929\u6daf\u90ae\u653f',
     u'phone': u'0898-88910231', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'', u'stars': u'0.0', u'latitude': u'18.30538',
     u'tags': u'\u6d77\u5357\u83dc,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u5929\u6daf\u996d\u5e97',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33372', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u5929\u6daf\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'0898-88910923', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'', u'stars': u'0.0', u'latitude': u'18.30534',
     u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u5409\u7965\u996d\u5e97',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33379', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u5409\u7965\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'0', u'address': u'225\u56fd\u9053',
     u'phone': u'0898-88910002', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'0', u'stars': u'0.0', u'latitude': u'18.30528',
     u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'0',
     u'name': u'\u4e09\u59d0\u59b9\u987a\u53d1\u996d\u5e97', u'common_remarks': u'1', u'bad_remarks': u'0',
     u'longitude': u'109.33384', u'nearby_shops': u'', u'environment_rating': u'', u'recommended_products': u'',
     u'all_remarks': u'1',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u4e09\u59d0\u59b9\u987a\u53d1\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'',
     u'stars': u'0.0', u'latitude': u'18.30525',
     u'tags': u'\u5c0f\u5403\u9762\u98df,\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u743c\u6d77\u98df\u5e97',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.3339', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5c0f\u5403\u9762\u98df>>\u743c\u6d77\u98df\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'0898-88858088', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'', u'stars': u'0.0', u'latitude': u'18.30522',
     u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'',
     u'name': u'\u6d77\u5929\u4e00\u54c1\u996d\u5e97', u'common_remarks': u'', u'bad_remarks': u'',
     u'longitude': u'109.33397', u'nearby_shops': u'', u'environment_rating': u'', u'recommended_products': u'',
     u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u6d77\u5929\u4e00\u54c1\u996d\u5e97'},
    {u'service_rating': u'7.2', u'recommended_dishes': u'\u7092\u672c\u5730\u571f\u9e21', u'good_remarks': u'0',
     u'address': u'\u5929\u6daf\u9547(\u8fd1\u5929\u6daf\u9547\u4e2d\u5fc3\u5b66\u6821)', u'phone': u'0898-88911085',
     u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'0', u'stars': u'3.0',
     u'latitude': u'18.30488', u'tags': u'\u6d77\u5357\u83dc,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/pc/3f7c82ae52e0545307332bdbdf2c5e7a/41328212_m.jpg', u'avg_price': u'44',
     u'product_rating': u'6.4', u'very_bad_remarks': u'0', u'name': u'\u6daf\u5cad\u996d\u5e97',
     u'common_remarks': u'1', u'bad_remarks': u'0', u'longitude': u'109.33404', u'nearby_shops': u'',
     u'environment_rating': u'5.7', u'recommended_products': u'', u'all_remarks': u'14',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u6d77\u5357\u83dc>>\u6daf\u5cad\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'13198976216', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'', u'stars': u'0.0', u'latitude': u'18.30512',
     u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'',
     u'name': u'\u5929\u6daf\u597d\u8fd0\u996d\u5e97', u'common_remarks': u'', u'bad_remarks': u'',
     u'longitude': u'109.33424', u'nearby_shops': u'', u'environment_rating': u'', u'recommended_products': u'',
     u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u5929\u6daf\u597d\u8fd0\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'18876082878', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a',
     u'very_good_remarks': u'', u'stars': u'0.0', u'latitude': u'18.30503',
     u'tags': u'\u5feb\u9910\u7b80\u9910,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'',
     u'name': u'\u8001\u9e2d\u6d77\u6d6a\u996d\u5e97', u'common_remarks': u'', u'bad_remarks': u'',
     u'longitude': u'109.33427', u'nearby_shops': u'', u'environment_rating': u'', u'recommended_products': u'',
     u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5c0f\u5403\u5feb\u9910>>\u5feb\u9910\u7b80\u9910>>\u8001\u9e2d\u6d77\u6d6a\u996d\u5e97'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'',
     u'address': u'\u4e8c\u4e8c\u4e94\u56fd\u9053\u5929\u6daf\u4e4b\u6625\u519c\u5bb6\u996d\u5e97\u65c1', u'phone': u'',
     u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u65c5\u6e38\u533a', u'very_good_remarks': u'', u'stars': u'0.0',
     u'latitude': u'18.30341', u'tags': u'\u5176\u4ed6\u4e2d\u9910,\u4e1c\u5317\u83dc,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u5b9d\u5c9b\u519c\u5bb6\u83dc',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33932', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u65c5\u6e38\u533a>>\u4e09\u4e9a\u6e7e>>\u5176\u4ed6>>\u5176\u4ed6\u4e2d\u9910>>\u5b9d\u5c9b\u519c\u5bb6\u83dc'},
    {u'service_rating': u'', u'recommended_dishes': u'', u'good_remarks': u'', u'address': u'225\u56fd\u9053',
     u'phone': u'', u'city': u'\u4e09\u4e9a', u'area': u'\u4e09\u4e9a\u5e02\u533a', u'very_good_remarks': u'',
     u'stars': u'0.0', u'latitude': u'18.30313',
     u'tags': u'\u5176\u4ed6\u4e2d\u9910,\u4e1c\u5317\u83dc,\u4e09\u4e9a\u6e7e',
     u'photos': u'http://i3.dpfile.com/s/c/app/shop/i/shop/no-photo.2ee36d9fa3e22353370b4c54124d2e22.png',
     u'avg_price': u'0', u'product_rating': u'', u'very_bad_remarks': u'', u'name': u'\u5929\u6daf\u4e4b\u6625',
     u'common_remarks': u'', u'bad_remarks': u'', u'longitude': u'109.33938', u'nearby_shops': u'',
     u'environment_rating': u'', u'recommended_products': u'', u'all_remarks': u'',
     u'navigation': u'\u4e09\u4e9a\u9910\u5385>>\u4e09\u4e9a\u5e02\u533a>>\u4e09\u4e9a\u6e7e>>\u5176\u4ed6>>\u5176\u4ed6\u4e2d\u9910>>\u5929\u6daf\u4e4b\u6625'}]}
from Tkinter import *
from numpy import *

restaurant = Tk()
var = IntVar()
for food_message in range(shape(foodLocation['result'])[0]):

    reName =  "饭店名称：" + foodLocation['result'][food_message]['name'].encode("utf-8")
    reAddress = "饭店地址：" + foodLocation['result'][food_message]['address'].encode("utf-8")
    rePhone = "联系方式：" + foodLocation['result'][food_message]['phone'].encode("utf-8")
    reArea = "饭店区域：" + foodLocation['result'][food_message]['area'].encode("utf-8")
    reStars = "平均评分：" + foodLocation['result'][food_message]['stars'].encode("utf-8")
    reLon =  "经度：" + foodLocation['result'][food_message]['longitude'].encode("utf-8")
    reLat = "维度：" + foodLocation['result'][food_message]['latitude'].encode("utf-8")
    s1 = float(foodLocation['result'][food_message]['longitude'].encode("utf-8"))
    s2 = float(foodLocation['result'][food_message]['latitude'].encode("utf-8"))
    #reLocation = reLocation.split(",")
    s = (s1,s2)


    print foodLocation['result'][food_message]['name'].encode("utf-8")
    Radiobutton(restaurant, text=[reName,reAddress,rePhone,reStars], variable=var,
                value=food_message).grid(row=food_message, column=0)
restaurant.mainloop()
'''
'''
import requests
from numpy import *
url = "http://apis.haoservice.com/lifeservice/travel/scenery?pid=0&cid=133&page=2&key=760f02c0930b4c9a9b45460c5ed453a6"
response = requests.request("GET", url)
viewpoint_name =  response.json()
print viewpoint_name
for i in range(shape(viewpoint_name['result'])[0]):
'''
'''
import datetime
now_time = datetime.datetime.now()
dictSeason = {"wangji":['06','07','08'],"danji":['01','02','03','04','05','09','10','11','12']}
dataMonth = datetime.datetime.now().strftime('%m')
for i in dictSeason.keys():
    if dataMonth in dictSeason[i]:
        print i
'''

'''
import random
tripNum = random.randint(1, 2)
print tripNum
(stringArray){
         string[] =
            "景点名称:海口火山口地质公园",
            "景点评级：AAAA",
            "景点最低价格：48",
            "景点地址：海南省海口市西南石山镇",
            "景点名称:海口观澜湖",
            "景点评级：",
            "景点最低价格：98",
            "景点地址：海南省海口市观澜湖大道1号",
            "景点名称:海口观澜湖反弹蹦床公园",
            "景点评级：",
            "景点最低价格：78",
            "景点地址：海南省海口市龙华区观澜湖新城9栋三楼2304、2305号",
      },
      (stringArray){
         string[] =
            "景点名称:海口火山口地质公园",
            "景点评级：AAAA",
            "景点最低价格：48",
            "景点地址：海南省海口市西南石山镇",
            "景点名称:海口观澜湖",
            "景点评级：",
            "景点最低价格：98",
            "景点地址：海南省海口市观澜湖大道1号",
            "景点名称:海口观澜湖反弹蹦床公园",
            "景点评级：",
            "景点最低价格：78",
            "景点地址：海南省海口市龙华区观澜湖新城9栋三楼2304、2305号",
      },
 }

Process finished with exit code 0

'''
'''
import requests
from numpy import *

def viewpoint(viewpoint):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % viewpoint
    response = requests.request("GET", url)
    data = response.json()
    #print type(data['pois'][0]['location'])
    return data['pois'][0]['location']

def restaurantData(hotelData):

    url = "http://restapi.amap.com/v3/place/around?key=c912883876e0baa8beb279f31efac462&location=%s&keywords=饭店&types=&offset=&page=&extensions=all" % hotelData.encode("utf-8")
    response = requests.request("GET", url)
    data = response.json()
    print data
    return data



from numpy import *

def selHotel():
    hotelData = viewpoint('海口观澜湖')
    print hotelData
    restraurantData  = restaurantData(hotelData)
    print restaurantData
    for restaurant_num in range(shape(restraurantData['pois'])[0]):
        reName =  '饭店名称：' + restraurantData['pois'][restaurant_num]['name'].encode('utf-8')
        print reName
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


selHotel()
'''


import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer,Any
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from numpy import *
import requests
def hospitalPoint(viewpoint):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % viewpoint
    response = requests.request("GET", url)
    data = response.json()
    #print type(data['pois'][0]['location'])
    return data['pois'][0]['location']

def hospitalLocation(hospitalData):
    url = "http://restapi.amap.com/v3/place/around?key=c912883876e0baa8beb279f31efac462&location=%s&keywords=医院&types=&offset=&page=&extensions=all" % hospitalData
    response = requests.request("GET", url)
    data = response.json()
    return data

def view_hospital(viewName):
    viewLocation = hospitalPoint(viewName)
    print viewLocation
    hospitalData = hospitalLocation(viewLocation.encode("utf-8"))
    emptyList = []
    for hospital_num in range(shape(hospitalData['pois'])[0]):
        hospitalList = []
        hoName = '医院名称：' + hospitalData['pois'][hospital_num]['name'].encode('utf-8')
        print hoName
        if len(hospitalData['pois'][hospital_num]['tel']):
            hoTel = '医院电话：' + hospitalData['pois'][hospital_num]['tel'].encode('utf-8')
        else:
            hoTel = '医院电话：' + '无'
        hoAddress = ''.join(hospitalData['pois'][hospital_num]['address'])
        hoLocation = '医院经纬度：' + hospitalData['pois'][hospital_num]['location'].encode('utf-8')
        hoType = '医院类型：' + hospitalData['pois'][hospital_num]['type'].encode('utf-8')
        hospitalList.append(hoName)
        hospitalList.append(hoTel)
        hospitalList.append(hoAddress)
        hospitalList.append(hoLocation)
        hospitalList.append(hoType)
        emptyList.append(hospitalList)
    return emptyList

print view_hospital("海口观澜湖")