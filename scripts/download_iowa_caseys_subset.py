"""Download the historical Casey's subset used to reproduce the Iowa liquor project.

This script intentionally queries only the columns and stores needed for the portfolio
refresh. It avoids downloading the multi-gigabyte statewide dataset.

Historical window: 2012-01-01 through 2017-10-31, matching the preserved 2019
notebook snapshot cutoff.
"""

from pathlib import Path
import time

import pandas as pd
import requests

DATASET_ID = "m3tr-qhgy"
API_URL = f"https://data.iowa.gov/resource/{DATASET_ID}.json"
OUTPUT_PATH = Path("data/iowa_caseys_2012_to_2017_10_31.csv")
PAGE_SIZE = 50_000

SELECT_COLUMNS = [
    "invoice_line_no",
    "date",
    "store",
    "name",
    "city",
    "zipcode",
    "county",
    "category",
    "category_name",
    "vendor_no",
    "vendor_name",
    "itemno",
    "im_desc",
    "pack",
    "bottle_volume_ml",
    "state_bottle_cost",
    "state_bottle_retail",
    "sale_bottles",
    "sale_dollars",
    "sale_liters",
]

WHERE_CLAUSE = (
    "date >= '2012-01-01T00:00:00.000' "
    "AND date < '2017-11-01T00:00:00.000' "
    "AND upper(name) like '%CASEY%'"
)


def fetch_page(offset: int) -> list[dict]:
    params = {
        "$select": ",".join(SELECT_COLUMNS),
        "$where": WHERE_CLAUSE,
        "$order": "date, invoice_line_no",
        "$limit": PAGE_SIZE,
        "$offset": offset,
    }
    response = requests.get(API_URL, params=params, timeout=120)
    response.raise_for_status()
    return response.json()


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    frames = []
    offset = 0

    while True:
        print(f"Requesting rows {offset:,} through {offset + PAGE_SIZE - 1:,}...")
        rows = fetch_page(offset)
        if not rows:
            break

        frames.append(pd.DataFrame.from_records(rows))
        offset += len(rows)

        if len(rows) < PAGE_SIZE:
            break

        time.sleep(0.2)

    if not frames:
        raise RuntimeError("The Iowa API returned no Casey's rows for the historical window.")

    data = pd.concat(frames, ignore_index=True)
    data.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved {len(data):,} rows to {OUTPUT_PATH}")
    print(f"Date range: {data['date'].min()} through {data['date'].max()}")
    print(f"Unique store names: {data['name'].nunique():,}")


if __name__ == "__main__":
    main()
