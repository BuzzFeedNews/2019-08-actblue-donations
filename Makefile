filings:
	mkdir -p data/filings
	python scripts/get-filing-list.py > data/filings.csv
	python scripts/download-filings.py

zcta_shape:
	curl https://www2.census.gov/geo/tiger/TIGER2018/ZCTA5/tl_2018_us_zcta510.zip -o data/census/tl_2018_us_zcta510.zip
	unzip data/census/tl_2018_us_zcta510.zip -d data/census/tl_2018_us_zcta510
	rm data/census/tl_2018_us_zcta510.zip

tl_state:
	curl https://www2.census.gov/geo/tiger/TIGER2018/STATE/tl_2018_us_state.zip -o data/census/tl_2018_us_state.zip
	unzip data/census/tl_2018_us_state.zip -d data/census/tl_2018_us_state
	rm data/census/tl_2018_us_state.zip

load:
	nbexec notebooks/load_actblue.ipynb
