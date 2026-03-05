import requests
import pandas as pd
import time
import os

BASE_URL = "https://api.opendota.com/api"

def get_all_leagues():
    url = f"{BASE_URL}/leagues"
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())


def get_league_matches(league_id, limit=100):
    url = f"{BASE_URL}/leagues/{league_id}/matches"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    return df.head(limit)

def get_match_detail(match_id):
    url= f"{BASE_URL}/matches/{match_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
