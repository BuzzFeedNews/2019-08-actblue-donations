filings:
	mkdir -p data/filings
	python scripts/get-filing-list.py > data/filings.csv
	python scripts/download-filings.py

zcta_shape:
	curl https://www2.census.gov/geo/tiger/TIGER2010/ZCTA5/2010/tl_2010_us_zcta510.zip -o data/census/tl_2010_us_zcta510.zip
	unzip data/census/tl_2010_us_zcta510.zip -d data/census/tl_2010_us_zcta510

load:
	nbexec notebooks/load_actblue.ipynb
