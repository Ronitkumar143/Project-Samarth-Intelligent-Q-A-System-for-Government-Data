
import re
from .etl import load_rainfall, load_crop, normalize_state
import pandas as pd

def avg_annual_rainfall(state, years):
    df = load_rainfall()
    state = normalize_state(state)
    sub = df[df['state'].str.lower() == state.lower()]
    if sub.empty:
        return None
    # compute annual totals per year
    totals = sub.groupby('year')['rainfall_mm'].sum().reset_index()
    recent = totals[totals['year'].isin(years)]
    return recent['rainfall_mm'].mean()

def top_crops_by_volume(state, years, top_m=3):
    df = load_crop()
    state = normalize_state(state)
    sub = df[(df['state'].str.lower()==state.lower()) & (df['year'].isin(years))]
    if sub.empty:
        return []
    agg = sub.groupby('crop')['production_tonnes'].sum().reset_index().sort_values('production_tonnes', ascending=False)
    return agg.head(top_m).to_dict(orient='records')

def answer_question(question):
    # Very small rule-based parser for demo purposes
    q = question.lower()
    # match compare avg rainfall in X and Y for last N years
    m = re.search(r"compare .*rainfall in (\w+) and (\w+) for the last (\d+) years", q)
    if m:
        s1, s2, n = m.group(1).title(), m.group(2).title(), int(m.group(3))
        # determine years (use available in sample)
        df = load_rainfall()
        years = sorted(df['year'].unique())[-n:]
        r1 = avg_annual_rainfall(s1, years)
        r2 = avg_annual_rainfall(s2, years)
        crops1 = top_crops_by_volume(s1, years, top_m=3)
        crops2 = top_crops_by_volume(s2, years, top_m=3)
        ans = {
            "query": question,
            "years_analyzed": list(years),
            "state_1": {"name": s1, "avg_annual_rainfall_mm": r1, "top_crops": crops1},
            "state_2": {"name": s2, "avg_annual_rainfall_mm": r2, "top_crops": crops2},
            "sources": [
                {"dataset": "rainfall_sample.csv", "path": "data/rainfall_sample.csv"},
                {"dataset": "crop_prod_sample.csv", "path": "data/crop_prod_sample.csv"}
            ]
        }
        return ans

    # match highest production district for crop in state (recent year)
    m2 = re.search(r"identify the district in (\w+) with the highest production of (\w+)", q)
    if m2:
        state, crop = m2.group(1).title(), m2.group(2).title()
        df = load_crop()
        sub = df[(df['state'].str.lower()==state.lower()) & (df['crop'].str.lower()==crop.lower())]
        if sub.empty:
            return {"error":"no data"}
        latest_year = sub['year'].max()
        recent = sub[sub['year']==latest_year]
        top = recent.sort_values('production_tonnes', ascending=False).iloc[0]
        bottom = recent.sort_values('production_tonnes', ascending=True).iloc[0]
        return {
            "state": state,
            "crop": crop,
            "year": int(latest_year),
            "highest_district": top['district'],
            "highest_production_tonnes": float(top['production_tonnes']),
            "lowest_district": bottom['district'],
            "lowest_production_tonnes": float(bottom['production_tonnes']),
            "sources": [{"dataset":"crop_prod_sample.csv","path":"data/crop_prod_sample.csv"}]
        }

    return {"error":"question not recognized by demo parser. Try a supported template."}

if __name__ == "__main__":
    print(answer_question("Compare average rainfall in Bihar and Jharkhand for the last 2 years"))
