import requests
import json

for i in range(100):
    url = 'https://restapi.amap.com/v3/place/text?key=891fc6769c45ed042ef6729dde41fb28&keywords=服饰&types=&city=福州&children=1&offset=25&page={}&extensions=all'.format(i)
    print(url)
    res = requests.get(url).text
    #print(res)
    res=json.loads(res)
    #print(res['pois'])

    with open('cloth.txt','a+') as f:
        for r in res['pois']:
            name = r['name']
            shangquan = r['business_area']
            rating = r['biz_ext']['rating']
            cost = r['biz_ext']['cost']
            print(name)
            print(shangquan)
            print(rating)
            print(cost)
            f.write(name+' '+rating+'\n')

