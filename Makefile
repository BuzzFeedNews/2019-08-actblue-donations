filings:
	mkdir -p data/filings
	curl https://docquery.fec.gov/dcdev/posted/1344765.fec > data/filings/1344765.fec
	python scripts/extract-schedule-a.py "data/filings/1344765.fec" > data/filings/1344765-schedule-a.csv

load:
	nbexec notebooks/load_actblue.ipynb
