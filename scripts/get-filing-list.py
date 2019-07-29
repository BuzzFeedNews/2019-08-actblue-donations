#!/usr/bin/env python
import pandas as pd
import requests
import time
import sys

API_KEY = "AnWOrY6LD2asaGXo7PplU2tHLzN5I6r73fellDHo"
URL_TEMPLATE = "https://api.propublica.org/campaign-finance/v1/{cycle}/committees/{cid}/filings.json"

#ActBlue committee id
actblue_id = "C00401224"

# Calls the filings API, returns json response
# If fail, keep going
def call_api(url, params): 

    retries = 1

    while True:
        try:
            time.sleep(1)
            res = requests.get(
                url,
                params = params,
                headers = {
                    "X-API-Key": API_KEY
                }
            )
            res_json = res.json()
            try:
                status_code = res_json["status"]
            except:
                status_code = res.status_code
            if status_code in [ 200, "OK" ]:
                return res_json
            else:
                sys.stderr.write(f"STATUS CODE: {status_code}; {res_json}\n{url}\n{params}\n")
                sys.stderr.flush()
                time.sleep(15)
                continue
        # On exception retry one time, and then move on
        except Exception as e:
            if retries > 0:
                sys.stderr.write(f"EXCEPTION on {url}: {str(e)}\nRetrying in 15 seconds...\n{retries - 1} retries left\n")
                sys.stderr.flush()
                retries -= 1
                time.sleep(15)
            else:
                sys.stderr.write(f"EXCEPTION on {url}: {str(e)}\nMoving on to next")
                sys.stderr.flush()
                time.sleep(15)
                continue

# call the API for each committee
def get_filings(cid, cycle):
    sys.stderr.write(f"Fetching {cid}\n")
    url = URL_TEMPLATE.format(
        cid = cid,
        cycle = cycle
    )
    res = call_api(url, params = {})
    filings = res["results"]
    sys.stderr.write(f"Found {len(filings)} filing(s)\n")
    # send an empty DF if there are no filings
    if not len(filings):
        return pd.DataFrame(None)
    # else return an empty DF of filings with the committee id in a column
    else:
        return (
            pd.DataFrame(
                filings
            )
            .assign(
                committee_id =  cid,
            )
            [[ "committee_id" ] + list(filings[0].keys())]
            .rename(columns = {
                "id": "filing_id"
            })
        )

# Call get filings for committee id and cycle
def get_all_filings(cid = actblue_id, cycle = 2020):
    filings = pd.concat([ get_filings(cid, cycle)] )

    return filings

if __name__ == "__main__":
    filings = get_filings(cid = actblue_id, cycle = 2016) # CHANGE THIS
    filings.to_csv(sys.stdout, index = False) 
