from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
import requests
import time
import re
import json
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/api")
def getJson():
    with open("dump.json") as json_file:
        return jsonify(json_file)

if __name__ == "__main__":
    application.run()
