from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
import requests
import time
import re
import json

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/api")
def getJson():
    json = open('dump.json')
    return jsonify(json)


if __name__ == "__main__":
    application.run()
