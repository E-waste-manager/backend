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
    gmaps = googlemaps.Client(key=api_key)
    ranked_list = []
    for provider in list_of_providers:
        # provider_location = (provider['latitude'], provider['longitude'])
        provider_location = {'lat': provider['latitude'], 'lng': provider['longitude']}
        print(type(provider_location))
        # dist = connection.bingConnect(origin, provider_location)
        dist_obj = gmaps.distance_matrix(origin, provider_location, mode="driving")
        print(dist_obj)
        if dist_obj['rows'][0]['elements'][0]['status'] != 'ZERO_RESULTS':
            dist = dist_obj['rows'][0]['elements'][0]['distance']['text']
        else:
            dist = -1
        ranked_list.append({'name': provider['name'], 'distance': dist, 'address': provider['address']})
    ranked_list.sort(key=lambda x: x['distance'])
    return ranked_list