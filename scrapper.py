from bs4 import BeautifulSoup
import requests
import time
import re
import json
from datetime import datetime


def getPublicationTime(url):
    req = requests.get(url)
    sup = BeautifulSoup(req.content, 'html.parser')

    raw_time = sup.find('div', {"class": "date_detail"})
    print(raw_time.text)
    try:
        raw_time = raw_time.text.replace('WIB', '')
        raw_time = re.sub(' +', ' ', raw_time)
        raw_time = raw_time.strip()
    except:
        print('errors!')
    finally:
        return raw_time
    return raw_time

print("get republika")
web = requests.get("https://republika.co.id/")
print("done")
soup = BeautifulSoup(web.content, 'html.parser')


def write_json(data, filename='dump.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


lastest = soup.find_all('div', {"class": "teaser_conten1_center"})
lastest_array = []

print('start looping')
for last in lastest:
    if last.find('div', {"class": "clear"}) != None:
        continue

    time_pub = getPublicationTime(last.find('h2').find('a').get('href'))

    x = {
        "categories": str(last.find('h1').find('a').text),
        "title": str(last.find('h2').text),
        "scrapped_time": str(time.strftime("%b %d %Y %H:%M:%S")),
        "published_time": str(time_pub)
    }

    lastest_array.append(x)

print('start dumping')
with open('dump.json') as json_file:
    try:
        data = json.load(json_file)
        data.update(lastest_array)

        write_json(data)
    except:
        write_json(lastest_array)
