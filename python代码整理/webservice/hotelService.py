
#coding:utf8
import requests
from numpy import *

def hotel(hotelName):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % hotelName
    #data = {u'status': u'1', u'count': u'204', u'infocode': u'10000', u'pois': [{u'tel': u'0898-88827081;13136084777', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.1', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'28888.00'}, u'business_area': [], u'id': u'B0FFGQHA9A', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727585,18.274079', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100000', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/6452685ef6cbd4b29757d71ef9dbebbb', u'title': u'\u516c\u5171\u533a\u57df'}, {u'url': u'http://store.is.autonavi.com/showpic/2d1c7f3399927d0e7cd9b06b8ba0729b', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/6a323ae8da853f83a239764da84204a2', u'title': []}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u8708\u652f\u6d32\u5c9b\u85e4\u6d77\u897f\u6751110-3\u53f7', u'distance': u'17', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u8708\u652f\u6d32\u5c9b\u6c99\u6ee9\u65c5\u9986', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'13687562991', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': [], u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': []}, u'business_area': [], u'id': u'B0FFF6PUMZ', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.726660,18.274291', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100000', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/c1c323639635571d5c94150b51bc6091', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/d6ddd514f8b9839dc36192ecdbe5b2af', u'title': u'\u5176\u4ed6'}, {u'url': u'http://store.is.autonavi.com/showpic/13c046cfbf54125545167630d94cdd5d', u'title': u'\u5176\u4ed6'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u6d77\u68e0\u6e7e\u9547106\u4e61\u9053\u5317200\u7c73', u'distance': u'82', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u68a6\u84dd\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88601515;18189858727', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.6', u'cost': [], u'star': [], u'hotel_ordering': u'0', u'lowest_price': []}, u'business_area': [], u'id': u'B03830NFDR', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727587,18.274324', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u5bbe\u9986\u9152\u5e97;\u5bbe\u9986\u9152\u5e97', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100100', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/b107f1e11f19e00b96890ca9c0f1f537', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/7ba37c2fa33c78d6cac9052850756820', u'title': u'\u9ad8\u7ea7\u6d77\u666f\u53cc\u6807\u623f'}, {u'url': u'http://store.is.autonavi.com/showpic/c43c1572452b7ecc3df480cdb30f3282', u'title': u'\u9ad8\u7ea7\u6d77\u666f\u5927\u5e8a\u623f'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u4e09\u4e9a\u65c5\u6e38\u533a\u4e09\u4e9a\u6d77\u68e0\u6e7e\u9547\u540e\u6d77\u4e1c\u675115\u53f7(\u8708\u652f\u6d32\u5c9b\u65c1)', u'distance': u'26', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u83e0\u841d\u871c\u6d77\u666f\u516c\u9986', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88757720', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.4', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'128.00'}, u'business_area': [], u'id': u'B03830NS2W', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.728600,18.273921', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/108016ddaa0c14affadde42306b122f8', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/543907968ddf0437169872ef2a0a3123', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/796ca3c2e7eb53a5632f53cfcb63ce75', u'title': u'\u9152\u5e97\u5916\u89c2'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u6797\u65fa\u9547\u540e\u6d77\u6751\u897f3\u53f7(\u8fd1\u8708\u652f\u6d32\u5c9b\u7801\u5934)', u'distance': u'126', u'navi_poiid': [], u'name': u'\u5b8c\u7f8e\u5927\u6d77\u5ba2\u6808(\u8708\u652f\u6d32\u5e97)', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'18976805182;13363286888', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.3', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'108.00'}, u'business_area': [], u'id': u'B03830NS30', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.729133,18.274013', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/ac26795b4fbc9f4aa269dd9a58afd288', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/635a03ae8a507c70d8c1e032a5fb11f2', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/57bbc83d17dceb4e36fd6aa02d550a7a', u'title': u'\u5916\u89c2'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u6d77\u68e0\u6e7e\u85e4\u6d77\u6e14\u6751\u540e\u6d77\u7801\u5934(\u8708\u652f\u6d32\u5c9b\u7801\u5934\u65c1)', u'distance': u'180', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u84dd\u8272\u7406\u60f3\u6d77\u666f\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88751161;13876663763', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.4', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'138.00'}, u'business_area': [], u'id': u'B0FFGGYBTD', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727637,18.273210', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100000', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/c4b5e8ce48a88d50c9cd936472b3df1b', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/4d72e503dac58c75d53b45aa86ca2020', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/96569050d0647f6c0fa4c888d7722c5f', u'title': []}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u6d77\u68e0\u6e7e\u9547\u85e4\u6d77\u793e\u533a(\u85e4\u6d77\u5c0f\u5b66\u76f4\u8d7030\u7c73)', u'distance': u'105', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u6d77\u68e0\u6e7e\u81ea\u7531\u8005\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88812040;18689705981', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.4', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'285.00'}, u'business_area': [], u'id': u'B0FFGBHL03', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727554,18.272528', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/cfa3f1f0334047267b39feddd7c14351', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/a9d3806da30bfd6f1a3292137be389ca', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/f3f3a3cead5efabb0ba7142fec5152f2', u'title': []}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u8708\u652f\u6d32\u5c9b\u85e4\u6d77\u897f\u6751144\u53f7', u'distance': u'179', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u54c6\u5566A\u68a6\u6d77\u8fb9\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88753766;13647511574', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'2.6', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'131.00'}, u'business_area': [], u'id': u'B0FFFGZYKH', u'gridcode': u'2709352810', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727005,18.271792', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u5bbe\u9986\u9152\u5e97;\u5bbe\u9986\u9152\u5e97', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100100', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/f5b7d7b54243b9fd995db841225ca0fc', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/07c1efd018b538ddc57c01d929aebec2', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/c668531d4765684afd31970ba5514898', u'title': []}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u817e\u6d77\u793e\u533a\u897f3\u53f7\u817e\u6d77\u5c0f\u5b66\u897f100\u7c73', u'distance': u'264', u'navi_poiid': u'E49F021014_562', u'name': u'\u540e\u6d773\u53f7\u5ea6\u5047\u9152\u5e97', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88751319;13807513018', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'3.9', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'108.00'}, u'business_area': [], u'id': u'B0FFH7Q9C3', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727518,18.272468', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/deae1a895be12ee6474d7454f70f068a', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/467abd9ddd2215cb283b9b3f4c6d393b', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/2d316589efda286741c9d46895d8197e', u'title': u'\u5ba2\u623f'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u85e4\u6d77\u5c45\u59d4\u4f1a\u897f\u6751118\u53f7', u'distance': u'186', u'navi_poiid': [], u'name': u'\u6d77\u4e4b\u89d2\u65c5\u79df', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88813569;13697075959', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.4', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'45.00'}, u'business_area': [], u'id': u'B0FFH011JN', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727857,18.272892', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100000', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/7641dbba76228f8f0f6b0b6e3a24c37d', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/6183d19e3cb25e5c80beb0227b29b7ad', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/e2b6c8fdb5434850522cd76bcbfbbd22', u'title': u'\u5916\u89c2'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'106\u4e61\u9053\u5317100\u7c73', u'distance': u'145', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u89c2\u6f6e\u97f3\u9752\u5e74\u65c5\u820d(\u8708\u652f\u6d32\u5c9b\u5e97)', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'13379937930', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.8', u'cost': [], u'star': [], u'hotel_ordering': u'0', u'lowest_price': u'133.00'}, u'business_area': [], u'id': u'B0FFH6LCRH', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.728444,18.273889', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/5ee0970af77a426690a4f8db59c8eb1e', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/758d6c0c55970e411836ea39e7a48bce', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/24f9616cce4248bdf76ade0647ea7893', u'title': []}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u8708\u652f\u6d32\u5c9b\u7801\u5934\u540e\u6d77\u6751\u897f\u67513\u5c0f\u7ec43-2', u'distance': u'110', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u843d\u5b89\u6d77\u666f\u5ba2\u6808(\u8708\u652f\u6d32\u5c9b\u5e97)', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'18608959536;13098981067', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'3.8', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'87.00'}, u'business_area': [], u'id': u'B0FFF3IV8T', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727317,18.272579', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/5fb2b941c59df9cddb789acae75ea9cc', u'title': u'\u516c\u5171\u533a\u57df'}, {u'url': u'http://store.is.autonavi.com/showpic/f8331b00ebbc9f1f758d1c519d0a0cd8', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/bf21b84d1b6bd805654230f52f86b902', u'title': u'\u516c\u5171\u533a\u57df'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u6d77\u68e0\u6e7e\u8708\u652f\u6d32\u5c9b\u666f\u533a\u95e8\u53e3', u'distance': u'173', u'navi_poiid': u'E49F021014_576', u'name': u'\u540e\u6d77\u6e14\u5bb6\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'13215866079;18876790275', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.3', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'128.00'}, u'business_area': [], u'id': u'B0FFG2N6L6', u'gridcode': u'2709352821', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.729569,18.274252', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/4795b933b84c168aafda426ce6f53939', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/54c875f5df064cab4f062f28cdc70cac', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/5b4180e95f6f910eb134057a566179c1', u'title': u'\u5927\u5802/\u63a5\u5f85\u53f0'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'106\u4e61\u9053\u897f100\u7c73', u'distance': u'226', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u5bb9\u5bb9\u6c11\u5bbf', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88590735;18851616662', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.4', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'108.00'}, u'business_area': [], u'id': u'B0FFFAF94N', u'gridcode': u'2709352810', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727052,18.272035', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/8d1468d4bcb7052e7458accf56311393', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/3a4a487896b6bac6f83d074e560b09af', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/a2e536e9d34b28457cb8e92c761afa6f', u'title': []}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u6d77\u68e0\u6e7e\u6797\u65fa\u9547\u8708\u652f\u6d32\u5c9b\u7801\u5934\u95e8\u53e3\u659c\u5bf9\u976250\u7c73', u'distance': u'237', u'navi_poiid': [], u'name': u'\u7ea2\u8272\u6c34\u6676\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88757727', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'5.0', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'68.00'}, u'business_area': [], u'id': u'B0FFFTITR1', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.726461,18.272705', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100000', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/896442aa6ed8d9ce05b1bad54ba38cec', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/a3b849fb9dd67d972d7b45fcd8b418e3', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/b357188e42ffe24c2ac620a02bcd96e2', u'title': u'\u5916\u89c2'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u6d77\u6ee8\u6d77\u68e0\u6e7e\u85e4\u6d77\u793e\u533a\u897f\u675171\u53f7(\u8708\u652f\u6d32\u7801\u5934)\u8fd1106\u4e61\u9053', u'distance': u'189', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u6d77\u68e0\u6e7e\u8def\u6613\u9152\u5e97', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88812040;13648306767', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.2', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'280.00'}, u'business_area': [], u'id': u'B0FFHL6RCZ', u'gridcode': u'2709352820', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.728216,18.272255', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173;\u4f4f\u5bbf\u670d\u52a1\u76f8\u5173', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100000', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/6d7f51e3cfe03bfd753cc0825fb7c0d1', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/7393d9506501843b855b8aaaa7443002', u'title': u'\u5ba2\u623f'}, {u'url': u'http://store.is.autonavi.com/showpic/8bdaf67c6cf16d0844ff8918836e4f68', u'title': u'\u5ba2\u623f'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u540e\u6d77\u6751\u8708\u652f\u6d32\u5c9b\u85e4\u6d77\u897f\u6751144\u53f7', u'distance': u'225', u'navi_poiid': [], u'name': u'\u4e09\u4e9a\u6d77\u68e0\u6e7e\u4f0a\u6c34\u6e90\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'18083822222', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.8', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'112.00'}, u'business_area': [], u'id': u'B0FFGE76L9', u'gridcode': u'2709352810', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727207,18.271957', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u5bbe\u9986\u9152\u5e97;\u5bbe\u9986\u9152\u5e97', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100100', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/fecc020b4f43de0e9093f94e6c97b1a6', u'title': []}, {u'url': u'http://store.is.autonavi.com/showpic/e6b2d7e985b6dc4777892b3cdb3a17c3', u'title': u'\u5ba2\u623f'}, {u'url': u'http://store.is.autonavi.com/showpic/8bb0f798cf0cd4095bebae29828ce8f2', u'title': u'\u5ba2\u623f'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u540e\u6d77\u897f\u6751143-10\u53f7', u'distance': u'243', u'navi_poiid': [], u'name': u'\u666f\u516e\u9601\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'13876556575;15707825035;13501704750', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.5', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'138.00'}, u'business_area': [], u'id': u'B0FFFSRLC3', u'gridcode': u'2709352810', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.727026,18.271904', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/af09df0a3f08f52f42d612190a0a1c06', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/cfe8131991008b24725779e1f441fc3a', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/a8b2836f5fc3ae81ccd9c3433d78630e', u'title': u'\u9152\u5e97\u5916\u89c2'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'\u540e\u6d773\u53f7\u9644\u8fd1', u'distance': u'252', u'navi_poiid': [], u'name': u'\u540e\u6d77\u9a7f\u7ad9(\u8708\u652f\u6d32\u5c9b\u5e97)', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88829053;18907608342', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.0', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'141.00'}, u'business_area': [], u'id': u'B0FFFGZYK3', u'gridcode': u'2709352810', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.726999,18.271763', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/8497efa5c023d94391f5c2db32d8be51', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/9d3f958baaf5583b5800e5b4c4e8723d', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/905c719cf640decf4ad66e0d9cc9828f', u'title': u'\u9152\u5e97\u5916\u89c2'}], u'pname': u'\u6d77\u5357\u7701', u'address': u'106\u4e61\u9053\u5357100\u7c73', u'distance': u'268', u'navi_poiid': u'E49F021014_559', u'name': u'\u91d1\u6c99\u6e7e\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': []}, {u'tel': u'0898-88753611;17789797610', u'shopid': [], u'tag': [], u'postcode': [], u'exit_location': [], u'biz_ext': {u'rating': u'4.8', u'cost': [], u'star': [], u'hotel_ordering': u'1', u'lowest_price': u'28.00'}, u'business_area': [], u'id': u'B0FFG9ILRV', u'gridcode': u'2709352821', u'citycode': u'0899', u'indoor_data': {u'truefloor': [], u'cpid': [], u'floor': []}, u'discount_num': u'0', u'entr_location': [], u'biz_type': u'hotel', u'event': [], u'indoor_map': u'0', u'shopinfo': u'0', u'pcode': u'460000', u'adname': u'\u6d77\u68e0\u533a', u'location': u'109.729640,18.273950', u'recommend': u'0', u'type': u'\u4f4f\u5bbf\u670d\u52a1;\u65c5\u9986\u62db\u5f85\u6240;\u65c5\u9986\u62db\u5f85\u6240', u'email': [], u'match': u'0', u'website': [], u'typecode': u'100200', u'importance': [], u'timestamp': [], u'groupbuy_num': u'0', u'cityname': u'\u4e09\u4e9a\u5e02', u'photos': [{u'url': u'http://store.is.autonavi.com/showpic/5494885d2a2fbc6ecfbe923134578339', u'title': u'\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/1a32e327f628c8bdb7fcbdb1887d77e9', u'title': u'\u9152\u5e97\u5916\u89c2'}, {u'url': u'http://store.is.autonavi.com/showpic/e0c77c19b939320d615e511a284431f0', u'title': []}], u'pname': u'\u6d77\u5357\u7701', u'address': u'106\u4e61\u9053\u9644\u8fd1', u'distance': u'234', u'navi_poiid': [], u'name': u'\u7c73\u5947\u4e3b\u9898\u5ba2\u6808', u'adcode': u'460202', u'children': [], u'poiweight': [], u'alias': u'\u6728\u9e1f\u77ed\u79df'}], u'info': u'OK', u'suggestion': {u'keywords': [], u'cities': []}}
    response = requests.request("GET", url)
    data = response.json()
    return data['pois']

def viewpoint(viewpoint):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % viewpoint
    response = requests.request("GET", url)
    data = response.json()
    #print type(data['pois'][0]['location'])
    return data['pois'][0]['location']

def destina(origin,destination):
    #str1 = '116.481028,39.989643'
    #str2 = '116.434446,39.90816'
    #print type(origin)
    #print type(destination)
    #print origin
    #print destination
    sum = 0
    url = "http://restapi.amap.com/v3/direction/walking?origin=" + origin.encode("utf-8") + "&destination=" + destination +"&key=c912883876e0baa8beb279f31efac462"
    response = requests.request("GET", url)
    #print response
    data = response.json()
    #data = {u'status': u'1', u'info': u'ok', u'route': {u'origin': u'116.434307,39.90909', u'paths': [{u'duration': u'149', u'distance': u'208', u'steps': [{u'distance': u'54', u'orientation': [], u'instruction': u'\u6b65\u884c54\u7c73\u53f3\u8f6c', u'action': u'\u53f3\u8f6c', u'polyline': u'116.434319,39.909046;116.434967,39.909046', u'duration': u'39', u'assistant_action': [], u'road': []}, {u'distance': u'84', u'orientation': u'\u5357', u'instruction': u'\u6cbf\u5efa\u56fd\u95e8\u5317\u5927\u8857\u5411\u5357\u6b65\u884c84\u7c73\u5411\u5de6\u524d\u65b9\u884c\u8d70', u'action': u'\u5411\u5de6\u524d\u65b9\u884c\u8d70', u'polyline': u'116.434967,39.909046;116.434967,39.909031;116.434937,39.908932;116.434891,39.908867;116.434891,39.908867;116.43483,39.908726;116.434814,39.908649;116.43483,39.908493;116.43483,39.908428;116.434868,39.908306', u'duration': u'60', u'assistant_action': [], u'road': u'\u5efa\u56fd\u95e8\u5317\u5927\u8857'}, {u'distance': u'23', u'orientation': u'\u4e1c\u5357', u'instruction': u'\u6cbf\u5efa\u56fd\u95e8\u5357\u5927\u8857\u5411\u4e1c\u5357\u6b65\u884c23\u7c73\u53f3\u8f6c', u'action': u'\u53f3\u8f6c', u'polyline': u'116.434868,39.908302;116.434975,39.908195;116.435005,39.908123', u'duration': u'16', u'assistant_action': [], u'road': u'\u5efa\u56fd\u95e8\u5357\u5927\u8857'}, {u'distance': u'47', u'orientation': [], u'instruction': u'\u6b65\u884c47\u7c73\u5230\u8fbe\u76ee\u7684\u5730', u'action': [], u'polyline': u'116.435005,39.908119;116.434456,39.908081', u'duration': u'34', u'assistant_action': u'\u5230\u8fbe\u76ee\u7684\u5730', u'road': []}]}], u'destination': u'116.434446,39.90816'}, u'infocode': u'10000', u'count': u'1'}
    #print data
    #print data['route']
    #print data['route']['paths']
    #print data['route']['paths'][0]['steps'][0]['distance']
    for i in range(shape(data['route']['paths'][0]['steps'])[0]):
        sum += int(data['route']['paths'][0]['steps'][i]['distance'].encode('utf-8'))
    #['paths']['steps'][0]
    return sum


def view_hotel(viewpoint_name):
    hotel_name = viewpoint_name.encode('utf-8') + '宾馆'
    data = hotel(hotel_name)
    viewpoint_location = viewpoint(viewpoint_name)
    emptyList = []
    for hotel_data in range(shape(data)[0]):
        hotelList = []
        hotel_name =  data[hotel_data]['name'].encode('utf-8')
        hotel_location = data[hotel_data]['location'].encode('utf-8')
        #景点与宾馆的距离
        hotel_view_distance = destina(data[hotel_data]['location'].encode('utf-8'),viewpoint_location)
        hotel_address = ''.join(data[hotel_data]['address'])
        if len(data[hotel_data]['biz_ext']['rating']):
            hotel_rate = ''.join(data[hotel_data]['biz_ext']['rating'])
        else  :
            hotel_rate = '1'

        if len(data[hotel_data]['biz_ext']['lowest_price']):
            hotel_minprice =(str(data[hotel_data]['biz_ext']['lowest_price'])).encode('utf-8')
        else:
            hotel_minprice = '无'
        hotelList.append("宾馆名称：" + hotel_name)
        hotelList.append("宾馆地理位置：" + hotel_location)
        hotelList.append("宾馆与景点距离：" + str(hotel_view_distance))
        hotelList.append(hotel_address)
        hotelList.append("宾馆评分：" + (str(hotel_rate)))
        hotelList.append("宾馆最低消费：" + hotel_minprice)
        emptyList.append(hotelList)
    print emptyList
    return data,emptyList,viewpoint_location


#宾馆距离排序
def hotel_distance_recom(data,viewpoint_location):
    minDistance = 10000000
    minDistanceIndex = 0
    distList = []
    for hotel_data in range(shape(data)[0]):
        # 景点与宾馆的距离
        hotel_view_distance = destina(data[hotel_data]['location'].encode('utf-8'), viewpoint_location)
        if hotel_view_distance < minDistance:
            minDistance = hotel_view_distance
            minDistanceIndex = hotel_data

    distList.append("距离最短酒店：" + data[minDistanceIndex]['name'].encode('utf-8'))
    distList.append(data[minDistanceIndex]['location'].encode('utf-8'))
    distList.append(data[minDistanceIndex]['address'].encode('utf-8'))
    return distList




#宾馆价格排序

def hotel_price_recom(data,viewpoint_location):
    minPrice = inf
    minPriceIndex = 0
    priceList = []
    for hotel_data in range(shape(data)[0]):
        if len(''.join(data[hotel_data]['biz_ext']['lowest_price'])):
            hotelPrice = float((data[hotel_data]['biz_ext']['lowest_price']).encode('utf-8')) + 1
        else:
            hotelPrice = 100000

        if hotelPrice < minPrice:
            minPrice = hotelPrice
            minPriceIndex = hotel_data

    priceList.append("消费最低酒店：" + data[minPriceIndex]['name'].encode('utf-8'))
    priceList.append(data[minPriceIndex]['location'].encode('utf-8'))
    priceList.append(data[minPriceIndex]['address'].encode('utf-8'))
    return priceList


#宾馆评价排序
def hotel_rate_recom(data,viewpoint_location):
    minRate = inf
    minRateIndex = 0
    rateList = []
    for hotel_data in range(shape(data)[0]):
        if len(data[hotel_data]['biz_ext']['rating']):
            hotelRate = (data[hotel_data]['biz_ext']['rating']).encode('utf-8')
        else:
            hotelRate = 1.0
        if hotelRate > minRate:
            minRate = hotelRate
            minRateIndex = hotel_data

    rateList.append("评分最高酒店：" + data[minRateIndex]['name'].encode('utf-8'))
    rateList.append(data[minRateIndex]['location'].encode('utf-8'))
    rateList.append(data[minRateIndex]['address'].encode('utf-8'))
    return rateList


#性价比推荐
def hotel_best_recom(data,viewpoint_location):
    listDistance = []
    listRate = []
    listPrice = []

    bestNum = 0
    bestNumIndex = 0
    m = shape(data)[0]

    for hotel_data in range(shape(data)[0]):
        hotel_view_distance = destina(data[hotel_data]['location'].encode('utf-8'), viewpoint_location)
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

    bestList = []
    for num in range(shape(data)[0]):
        best = normRateData[0,num]/(normDistData[0,num] + normPriceData[0,num]/10)
        if  best > bestNum:
            bestNum = best
            bestNumIndex = num

    bestList.append("性价比最高酒店：" + data[bestNumIndex]['name'].encode('utf-8'))
    bestList.append(data[bestNumIndex]['location'].encode('utf-8'))
    bestList.append(data[bestNumIndex]['address'].encode('utf-8'))
    return bestList



import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array



class HotelService(DefinitionBase):
    @soap(String,Integer,_returns=Array(Array(String)))
    def hotel(self,hotelName,selNum):
        dataHotel,hotelList,viewpoint_location = view_hotel(hotelName)
        if selNum == 1:
            hotel_list = hotel_distance_recom(dataHotel, viewpoint_location)
        if selNum == 2:
            hotel_list = hotel_price_recom(dataHotel, viewpoint_location)
        if selNum == 3:
            hotel_list = hotel_rate_recom(dataHotel, viewpoint_location)
        if selNum == 4:
            hotel_list = hotel_best_recom(dataHotel, viewpoint_location)
        hotelList.append(hotel_list)
        return hotelList

    '''
    @soap(Integer,Inreturns=Array(String))
    def selectBest(self,selNum):
        #if selNum == 1:
        return hotel_distance_recom(dataHotel,viewpoint_location_1)
    '''


try:
    from wsgiref.simple_server import make_server
    soap_application = soaplib.core.Application([HotelService], 'tns')
    wsgi_application = wsgi.Application(soap_application)
    server = make_server('localhost', 8089, wsgi_application)
    print 'soap server starting......'
    server.serve_forever()
except ImportError:
    print "Error: example server code requires Python >= 2.5"