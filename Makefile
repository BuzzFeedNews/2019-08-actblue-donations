filings:
	mkdir -p data/filings
	python scripts/get-filing-list.py > data/filings.csv
	python scripts/download-filings.py

load:
	nbexec notebooks/load_actblue.ipynb
