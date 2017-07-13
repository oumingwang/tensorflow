import requests
def viewpoint(viewpoint):
    url = "http://restapi.amap.com/v3/place/text?&keywords=%s&city=beijing&output=json&offset=20&page=1&key=5bca02dc6ba1df62e5d370afb0066ec1&extensions=all" % viewpoint
    response = requests.request("GET", url)
    data = response.json()
    print data
    return data['pois'][0]['location']
