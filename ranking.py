import connection
import numpy as np
import pandas as pd
import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def ranking(origin):
    client = connection.connect()
    db = client.ewaste
    providers = db.Waste
    list_of_providers = providers.find({})
    ranked_list = []
    for provider in list_of_providers:
        provider_location = (provider['latitude'], provider['longitude'])
        dist = connection.bingConnect(origin, provider_location)
        ranked_list.append({'name': provider['name'], 'distance': dist, 'address': provider['address']})
    ranked_list.sort(key=lambda x: x['distance'])
    return ranked_list