
import pandas as pd
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "data")
RAIN_FILE = os.path.join(BASE, "rainfall_sample.csv")
CROP_FILE = os.path.join(BASE, "crop_prod_sample.csv")

def load_rainfall():
    df = pd.read_csv(RAIN_FILE, parse_dates=False)
    # ensure types
    df['year'] = df['year'].astype(int)
    return df

def load_crop():
    df = pd.read_csv(CROP_FILE)
    df['year'] = df['year'].astype(int)
    return df

def normalize_state(s):
    # simple normalization
    return s.strip().title()

if __name__ == "__main__":
    print("Rainfall sample:")
    print(load_rainfall().head())
    print("Crop sample:")
    print(load_crop().head())
