import pymongo
import os
from dotenv import load_dotenv
import requests
from xml.etree import ElementTree as ET
import json

from requests import request

load_dotenv()
username = os.getenv("username")
password = os.getenv("password")
bing_key = os.getenv("BING_KEY")

def connect():
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.jvpq2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    return client

def bingConnect(origin, destination):
    routeUrl = f"https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins={origin[0]},{origin[1]}&destinations={destination[0]},{destination[1]}&travelMode=Driving&key={bing_key}"
    request = requests.get(routeUrl)
    response = request.json()
    dist = response['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']
    return dist
    