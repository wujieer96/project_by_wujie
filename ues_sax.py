from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherSaxHandler(object):
    weather={}
    forecastArr=[]
    def weather_forecast(self,name,attrs):
        if name=='yweather:location':
            self.weather['city']=attrs['city'] #将城市存入天气对象self.weather中
            print('city:'+self.weather['city'])
        if name=='yweather:forecast':
            iteminfo={}
            for key,val in attrs.items():
                iteminfo[key]=val
            self.forecastArr.append(iteminfo)
            self.weather['forecast']=self.forecastArr #将天气预报存入天气对象中
            print('weather:{},date:{},low:{},high:{}'.format(attrs['text'],attrs['date'],attrs['low'],attrs['high']))

def parseXml(xml_str):
    #print(xml_str)
    handler=WeatherSaxHandler()
    parser=ParserCreate()
    parser.StartElementHandler=handler.weather_forecast
    parser.Parse(xml_str)
    return handler.weather
URL='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL,timeout=4) as f:
    data=f.read()
    print('result[city]:',parseXml(data.decode('utf-8')))