import fecfile
import csv
import sys

MAIN_COLUMNS = [
    "entity_type",
    "filer_committee_id_number",
    "transaction_id",
    "contribution_date",
    "contribution_amount",
    "contribution_aggregate",
    "contributor_organization_name",
    "contributor_first_name",
    "contributor_last_name",
    "contributor_street_1",
    "contributor_street_2",
    "contributor_city", 
    "contributor_zip_code",
    "contributor_state",
    "contributor_employer",
    "contributor_occupation",
    "contribution_purpose_descrip",
    "memo_code",
    "memo_text_description",
]

def schedule_a_to_csv(fec_path):
    src = open(fec_path)
    item_iter = fecfile.fecparser.iter_lines(src, { "as_strings": True })

    writer = csv.DictWriter(
        sys.stdout,
        fieldnames = MAIN_COLUMNS,
        extrasaction = "ignore"
    )
    writer.writeheader()

    for i, item in enumerate(item_iter):
        if i % 10000 == 0:
            sys.stderr.write(f"\r{i:,d}")
        dtype = item.data_type 
        if dtype == "itemization":
            if item.data["form_type"][:2] == "SA":
                form_type = item.data["form_type"]
                writer.writerow(item.data)

    sys.stderr.write(f"\n")

if __name__ == "__main__":
    schedule_a_to_csv(sys.argv[1])
