# NYC Census
Making some tools for myself to more easily pull census data from just the five boroughs. Right now the two scripts are tract_call.py, which takes a year, a set of variables, and a filepath and returns a .csv with tract-level data and pums_call.py which takes the same arguments and supplies PUMS data. NB: a Census API key needs to be set in an .env file.

## Setup
pip install -r requirements.txt

Add a `.env` file with:
CENSUS_API_KEY=your_key_here

## Examples
python tract_call.py --year 2024 --vars "NAME,group(B01001)" --output tracts_2024
python pums_call.py --year 2024 --vars "JWTRNS,PINCP,POVPIP" --output pums_2024