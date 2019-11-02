#美团美食
# -*- coding:UTF-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import json
import csv


with open(r'福州美食.txt',"w", newline='',encoding='UTF-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['网站名','品类','商家名称','地址','评分','人均消费'])
    target = 'http://fz.meituan.com/meishi/'
    head={}
    head['authorization']='your ClientID'
    head['User-Agent'] = ''
    req = requests.get(url=target,headers=head)
    html=req.text
    bf=BeautifulSoup(html,'lxml')
    texts=bf.find_all('script')
    text=texts[14].get_text().strip()
    text=text[19:-1]
    result=json.loads(text)
    result=result['filters']
    result=result['areas']
    list=[]
    for item in result:
        for i in item['subAreas']:
            if i['name']=='全部':
                list.append(i['id'])
    print(list)
    for item in list:
        for i in range(5):
            if i==0:
                continue
            target='http://fz.meituan.com/meishi/'+'b'+str(item)+'/'+'pn'+str(i)+'/'
            head={}
            head['authorization']='your ClientID'
            head['User-Agent'] = ''
            req = requests.get(url=target,headers=head)
            html=req.text
            bf=BeautifulSoup(html,'lxml')
            texts=bf.find_all('script')
            text=texts[14].get_text().strip()
            text=text[19:-1]
            result=json.loads(text)
            result=result['poiLists']
            result=result['poiInfos']
#            print(result)
            if result:
                print(target)
                for it in result:
                    Info_list=[]
                    Info_list.append('美团')
                    Info_list.append('美食')
                    Info_list.append(it['title'])
                    Info_list.append(it['address'])
                    Info_list.append(it['avgScore'])
                    Info_list.append(it['avgPrice'])
                    writer.writerow(Info_list)
                time.sleep(3)
            else:
                break

print('Done')
