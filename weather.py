import requests
import pprint
Key = "&key=" + ""          #input keys
CityName = ""
def Getcity(CityName):
    url_v2 = "https://geoapi.qweather.com/v2/city/lookup?location=" + CityName + Key
    CityArg =  requests.get(url_v2).json()['location'][0]
    return CityArg["id"]
    
    
def GetInfo(location):
    url = "https://devapi.qweather.com/v7/weather/now?" + Key + "&location=" + location
    return requests.get(url).json()

def RetWea():
    CityId = Getcity(CityName)
    return GetInfo(CityId)['now']['temp']

if __name__ == '__main__':
    print("It is: " + WeatherNow['now']['temp'] + " degree")
    
