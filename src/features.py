import pandas as pd
import time
import os

def categorize_game_speed(duration):
    if duration < 30:
        return "Fast"
    elif duration <= 40:
        return "Normal"
    else:
        return "Late"
    
def add_game_features(df):
    df["game_speed_categorize"] = df["duration"].apply(categorize_game_speed)
    return df