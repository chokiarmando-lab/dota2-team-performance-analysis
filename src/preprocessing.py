import pandas as pd
import time
import os

def preprocess_matches(df):
    df["start_time"] = pd.to_datetime(df["start_time"], unit="s")
    df["duration"] = (df["duration"] / 60).round(2)
    df["total_kills"] = df["radiant_score"] + df["dire_score"]
    
    return df