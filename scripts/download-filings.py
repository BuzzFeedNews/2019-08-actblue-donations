#!/usr/bin/env python
import pandas as pd
import requests
import time
import sys
import os

def fetch_url(url): 
    sys.stderr.write(f"Fetching {url}\n")
    while True:
        try:
            res = requests.get(
                url,
                headers = {
                    "User-Agent": "Mozilla/5.0"
                }
            )

            size = len(res.content)
            status_code = res.status_code
            if status_code in [ 200 ]:
                return res.content
            elif size < 100:
                sys.stderr.write(f"ONLY {size} bytes\n")
            else:
                sys.stderr.write(f"STATUS CODE: {status_code}")
            sys.stderr.flush()
            time.sleep(15)
            continue
        except Exception as e:
            sys.stderr.write(f"EXCEPTION: {str(e)}\n")
            sys.stderr.flush()
            time.sleep(15)
            continue

def download_filings(filing_ids):
    for filing_id in filing_ids:
        dest = f"data/filings/{filing_id}.fec"
        if os.path.isfile(dest):
            continue
        sys.stderr.write(f"Fetching {filing_id}\n")
        url = f"http://docquery.fec.gov/dcdev/posted/{filing_id}.fec"
        content = fetch_url(url)
        with open(dest, "wb") as f:
            f.write(content)

def main():
    #filing_ids = pd.read_csv("data/filings.csv")["filing_id"].tolist()
    filing_ids = pd.read_csv(
        "data/filings.csv"
    ).loc[
        lambda x: x['report_title'].str.contains("MID-YEAR", na=False)
    ]["filing_id"].tolist()

    sys.stderr.write(f"Fetching {filing_ids}...\n")

    download_filings(filing_ids)

if __name__ == "__main__":
    main()
