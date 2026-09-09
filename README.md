# NYC Census
Making some tools for myself to more easily pull Census data from just the five boroughs. Right now the only script is acs_call.py, which takes a year, a set of variables, and a filepath and returns a .csv with tract-level data. Will hopefully add more for other files and for PUMA data. NB: a Census API key needs to be set in an .env file.

## Setup
pip install -r requirements.txt

Add a `.env` file with:
CENSUS_API_KEY=your_key_here

## Example
python acs_call.py --year 2024 --vars "NAME,group(B01001)" --output tracts_2024