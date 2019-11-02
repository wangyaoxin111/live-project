import requests
import json

for i in range(10):
    url = 'https://restapi.amap.com/v3/place/text?key=891fc6769c45ed042ef6729dde41fb28&keywords=美食&types=&city=福州&children=1&offset=25&page={}&extensions=all'.format(i)
    print(url)
    res = requests.get(url).text
    #print(res)
    res=json.loads(res)
    #print(res['pois'])

    with open('ms0-50.text','a+') as f1:
        with open('ms50-100.text','a+') as f2:
            with open('ms100-200.text', 'a+') as f3:
                with open('ms200-.text', 'a+') as f4:
                    for r in res['pois']:
                        name = r['name']
                        shangquan = r['business_area']
                        rating = r['biz_ext']['rating']
                        cost = r['biz_ext']['cost']
                        print(name)
                        print(shangquan)
                        print(rating)
                        print(cost)
                        if type(cost) == str:
                            print('WRTING')
                            if float(cost) > 200:
                                f4.write(name+' '+rating+'  '+cost+'\n')
                            elif float(cost) >100:
                                f3.write(name +'    ' + rating + '  ' + cost+'\n')
                            elif float(cost)>50:
                                f2.write(name + '   ' + rating + '  ' + cost+'\n')
                            else:
                                f1.write(name + '   '+ rating + '   ' + cost + '\n')

