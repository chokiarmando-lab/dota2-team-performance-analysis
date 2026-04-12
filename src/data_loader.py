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

def get_picks_bans(match_id):
    data = get_match_detail(match_id)
    picks_bans = data.get("picks_bans", [])
    
    result = []
    for pb in picks_bans:
        if pb.get("is_pick"):
            result.append({
                "match_id": match_id,
                "hero_id": pb.get("hero_id"),
                "team": "radiant" if pb.get("team") == 0 else "dire",
                "radiant_win": data.get("radiant_win"),
                "radiant_team_id": data.get("radiant_team_id"),
                "dire_team_id": data.get("dire_team_id")
            })
    return result

def get_hero_list():
    url = f"{BASE_URL}/heroes"
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())[["id", "localized_name", "primary_attr"]]   
    
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

