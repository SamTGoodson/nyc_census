import requests 
import pandas as pd
import argparse

import os
from dotenv import load_dotenv

from tqdm import tqdm

load_dotenv()
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

def get_pumas():
    url = 'https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/arcgis/rest/services/NYC_Public_Use_Microdata_Areas_PUMAs_2020/FeatureServer/0/query'
    params = {
    'where': '1=1',
    'outFields': 'PUMA',
    'returnGeometry': 'false',
    'f': 'json'
    }
    response = requests.get(url, params=params)
    pumas = [
    feature['attributes']['PUMA']
    for feature in response.json()['features']
    ]
    return pumas

def fetch_pumas(acs_year,variables):
    pumas = get_pumas()
    all_pumas = []

    for puma in tqdm(pumas, desc="Fetching PUMAs"):
        url = f'https://api.census.gov/data/{acs_year}/acs/acs5/pums'
        params = {
        'get': variables,
        'for': f'public use microdata area:{puma}',
        'in': 'state:36',
        'key': CENSUS_API_KEY
        }
        response = requests.get(url,params)
        puma_results = response.json()
        puma_df = pd.DataFrame(puma_results[1:], columns=puma_results[0])
        all_pumas.append(puma_df)

    all_pumas_df = pd.concat(all_pumas,ignore_index=True)
    return all_pumas_df

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--year", type=int, default=2024)
    parser.add_argument("--vars", type=str, default='NAME,group(B01001)')
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    acs_year = args.year
    variables = args.vars
    output = args.output
    acs_all_pums = fetch_pumas(acs_year, variables)
    acs_all_pums.to_csv(f"{output}.csv", index=False)

if __name__ == "__main__":
    main()