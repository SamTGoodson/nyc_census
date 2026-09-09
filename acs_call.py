import requests 
import pandas as pd
import argparse

import os
from dotenv import load_dotenv


COUNTIES = ['005','047','061','081','085']

load_dotenv()
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

def fetch_tracts(acs_year,variables):
    acs_dfs = []

    for county in COUNTIES:
        url = f'http://api.census.gov/data/{acs_year}/acs/acs5'
        params = {
        'get' : variables,
        'for' : 'tract:*',
        'in': f'state:36 county:{county}',
        'key' : CENSUS_API_KEY
        }
        response = requests.get(url,params)
        borough_results = response.json()
        borough_df = pd.DataFrame(borough_results[1:], columns=borough_results[0])
        acs_dfs.append(borough_df)

    acs_all_borough = pd.concat(acs_dfs,ignore_index=True)
    return acs_all_borough

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--year", type=int, default=2024)
    parser.add_argument("--vars", type=str, default='NAME,group(B01001)')
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    acs_year = args.year
    variables = args.vars
    output = args.output
    acs_all_borough = fetch_tracts(acs_year, variables)
    acs_all_borough.to_csv(f"{output}.csv", index=False)

if __name__ == "__main__":
    main()