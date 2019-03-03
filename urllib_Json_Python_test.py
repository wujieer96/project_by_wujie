from urllib import request
import json
def fetch_data(url):
    with request.urlopen(url) as f:
        print('status:',f.status,f.reason)
        res=f.read().decode('utf-8')
        res=json.loads(res)
        return res

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)