# Analysis of ActBlue contributions to presidential candidates, January-June 2020

This repository contains data and code supporting a [BuzzFeed News article examining donors](TK) on campaign finance. Published August 3, 2019. See below for details.

## Data

This data analyzes ActBlue's [recent mid-year report to the FEC](https://docquery.fec.gov/cgi-bin/forms/C00401224/1344765/), which includes donations made through the organization between January 1, 2019 and June 30, 2019. (Due to its size, the filing itself is not included in this repository, but instructions to download can be found in the 'Reproducibility' section below.)

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

### Contribution totals above legal limit

The FEC prohibits individual donors from giving more than $2,800 to any single committee. ActBlue will prevent a donor from giving greater than the individual limit in a single donation, but it is possible for a donor to give more in aggregate across many donations. Typically, the candidate's committee will refund the difference at a later date which may not be reflected in this filing. Above-legal contributions have no effect on the analyses, which focus on the act of giving rather than how much money the campaigns have raised.

## Analysis

The [`notebooks/codonors.ipynb`](notebooks/codonors.ipynb) notebook contains the main analysis, written in Python. Relevant outputs can be found there, as well as in the [`output/`](output/) directory.

## Output

The [`output/`](output/) directory contains two files that may be of interest to other journalists and researchers:

- [`output/candidate-pair-counts.csv`](output/candidate-pair-counts.csv) counts the number of `donor_id`s that gave to each combination of **two** candidates.
- [`output/candidate-triplet-counts.csv`](output/candidate-triplet-counts.csv) counts the number of `donor_id`s that gave to each combination of **three** candidates.

In both files, combinations are not exclusive. For instance, someone who gave to four candidates will be counted for each permutation (i.e., six pairs and four triplets).

## Reproducibility

The code running the analysis is written in Python 3, and requires the following Python libraries:

- [pandas](https://pandas.pydata.org/) for data loading and analysis
- [fecfile](https://esonderegger.github.io/fecfile/) for parsing the raw FEC filings
- [jupyter](https://jupyter.org/) to run the notebook infrastructure

If you use Pipenv, you can install all required libraries with `pipenv install`.

To download the filing, run `make filings`. **Warning:** this will take several minutes and download a 5+ gb file. 

Run `make load` or execute `notebooks/load_actblue.ipynb` to parse the raw FEC files.

Execute `notebooks/codonors.ipynb` reproduce the findings.


## Licensing

All code in this repository is available under the [MIT License](https://opensource.org/licenses/MIT). Files in the `output/` directory are available under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) license.

## Questions / Feedback

Contact Scott Pham at [scott.pham@buzzfeed.com](mailto:scott.pham@buzzfeed.com).

Looking for more from BuzzFeed News? [Click here for a list of our open-sourced projects, data, and code.](https://github.com/BuzzFeedNews/everything)

