from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
import requests
import time
import re
import json

application = Flask(__name__)


def getPublicationTime(url):
    req = requests.get(url)
    sup = BeautifulSoup(req.content, 'html.parser')

    raw_time = sup.find('div', {"class": "date_detail"})
    raw_time = raw_time.text.replace('WIB', '')
    raw_time = re.sub(' +', ' ', raw_time)
    raw_time = raw_time.strip()
    return raw_time


def getJsonRepublika():
    web = requests.get("https://republika.co.id/")
    soup = BeautifulSoup(web.content, 'html.parser')

    lastest = soup.find_all('div', {"class": "teaser_conten1_center"})
    lastest_array = []

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

    return json.dumps(lastest_array)


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/api")
def getJson():
    return jsonify(getJsonRepublika())


if __name__ == "__main__":
    application.run()
