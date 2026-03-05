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


def get_league_matches(league_id):
    url = f"{BASE_URL}/leagues/{league_id}/matches"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)
    

def get_match_detail(match_id):
    url= f"{BASE_URL}/matches/{match_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def find_league_by_name(keyword, leagues_df):
    result = leagues_df[
        leagues_df["name"].str.contains(keyword, case=False, na=False)
    ]
    return result[["leagueid", "name", "tier"]]

def find_main_event_by_name(keyword, leagues_df):
    result = leagues_df[
        (leagues_df["name"].str.contains(keyword, case=False, na=False)) &
        (~leagues_df["name"].str.contains("qualifier", case=False, na=False)) &
        (leagues_df["tier"] == "professional")
    ]

    return result[["leagueid", "name", "tier"]]

def get_team_info(team_id):
    url= f"{BASE_URL}/teams/{team_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

