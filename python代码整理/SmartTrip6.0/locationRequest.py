import requests
def viewpoint(viewpoint):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=c912883876e0baa8beb279f31efac462&extensions=all" % viewpoint
    response = requests.request("GET", url)
    data = response.json()
    #print type(data['pois'][0]['location'])
    return data['pois'][0]['location']