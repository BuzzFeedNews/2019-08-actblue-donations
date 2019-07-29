# Analysis of contributions to 2020 presidential candidates via ActBlue as of 7/31/2019

This repository contains data and code supporting a [BuzzFeed News article examining donors](TK) on campaign finance. Published August TK, 2019. See below for details.

## Data

All data in this repository comes from the campaigns' committee filings to the [Federal Election Commission](https://www.fec.gov/) (FEC), with assistance from [ProPublica's Campaign Finance API](https://projects.propublica.org/api-docs/campaign-finance/committees/#get-committee-filings).

- [`data/census/zcta_county.csv`](data/census/zcta_county.csv) is a crosswalk that bridges ZIP codes and counties. It is provided by [The US Census](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.html) 

- [`data/candidates.csv`](data/candidates.csv) contains a list of high- and medium-profile Democratic presidential candidates (and primary campaign committees) for whom an "July Quarterly" filing was available on the FEC's website by 6:30am Eastern on July 16, 2019. (The filing deadline was July 15 at midnight.)

- [`data/filings.csv`](data/filings.csv) contains a list of basic metadata for the aforementioned filings.

- The [`data/filings/`](data/filings/) directory contains the raw filing data for each of those filings, in the FEC's `.fec` format.
   
- [`data/census`](`data/census`) contains population estimates for U.S. statesand counties using the 5-year American Community Survey from the Census Bureau.
   
- [`data/states-geojson.json`](`data/states-geojson.json`) is a geojson file of the U.S. states including Alaska and Hawaii. It is generated using [this code](https://github.com/scottpham/us-atlas-geojson).


## Methodology

### Linking donors

The Federal Election Commission filings do not contain any truly-unique identifiers for campaign contributors. So, in order identify donors who have given to multiple campaigns, BuzzFeed News constructed a `donor_id`, created from the following fields:

- First name
- Last name
- 5-digit ZIP code

There are some limitations to this approach:

- If a donor changes their name, or misspells it occasionally, this approach will not cluster all of their contributions together
- If a donor moves to a new ZIP code, this approach will not cluster all of their contributions together
- If two or more donors in the same ZIP code share both a first and last name, this approach will assume (incorrectly) that they are the same person

For these reasons, the results of the analysis should be interpreted as approximations.

### The $200 threshold

The Federal Election Commission does not require campaigns to itemize contributions from donors who have given **$200 or less** during a given campaign cycle. Some campaign committees have included such donors. Some democratic campaign committees seem to have done this because because they received overly large donations and then refunded a portion. For the sake of equal comparison, BuzzFeed News excluded contributions from donors whose aggregate was listed as $200 or less.

### Contribution totals above legal limit

The FEC prohibits individual donors from giving more than $2,800 to any single committee. Even so, the data in the filings appear to indicate that some donors have given more than that amount. In some cases, this may be because the refunds have not yet been processed, or are declared elsewhere. Above-legal contributions have no effect on the analyses, which focus on the act of giving rather than how much money the campaigns have raised.

## Analysis

The [`notebooks/analyze-contributions.ipynb`](notebooks/analyze-contributions.ipynb) notebook contains the main analysis, written in Python. Relevant outputs can be found there, as well as in the [`output/`](output/) directory.

The [`notebooks/geo-analysis.ipynb`](notebooks/geo-analysis.ipynb) notebook contains geographic analysis and exploratory charts. 
## Outputs

The [`output/`](output/) directory contains two files that may be of interest to other journalists and researchers:

- [`output/candidate-pair-counts.csv`](output/candidate-pair-counts.csv) counts the number of `donor_id`s that gave to each combination of **two** candidates.
- [`output/candidate-triplet-counts.csv`](output/candidate-triplet-counts.csv) counts the number of `donor_id`s that gave to each combination of **three** candidates.

In both files, combinations are not exclusive. For instance, someone who gave to four candidates will be counted for each permutation (i.e., six pairs and four triplets).

## Reproducibility

The code running the analysis is written in Python 3, and requires the following Python libraries:

- [pandas](https://pandas.pydata.org/) for data loading and analysis
- [fecfile](https://esonderegger.github.io/fecfile/) for parsing the raw FEC filings
- [jupyter](https://jupyter.org/) to run the notebook infrastructure
- [geopandas](http://geopandas.org/) to run the geo notebook

If you use Pipenv, you can install all required libraries with `pipenv install`.

Execute `notebooks/load_actblue.ipynb` to parse the raw FEC files.

Execute the rest of the notebooks in the `notebooks/` directory to reproduce the findings.

## Licensing

All code in this repository is available under the [MIT License](https://opensource.org/licenses/MIT). Files in the `input/` directory are released into the public domain. Files in the `output/` directory are available under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) license.

## Questions / Feedback

Contact Scott Pham at [scott.pham@buzzfeed.com](mailto:scott.pham@buzzfeed.com).

Looking for more from BuzzFeed News? [Click here for a list of our open-sourced projects, data, and code.](https://github.com/BuzzFeedNews/everything)

