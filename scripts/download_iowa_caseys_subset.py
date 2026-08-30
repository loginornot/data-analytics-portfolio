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
API_URL = f"https://data.iowa.gov/api/v3/views/{DATASET_ID}/query.json"
OUTPUT_PATH = Path("data/iowa_caseys_2012_to_2017_10_31.csv")
PAGE_SIZE = 5_000

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

SELECT_SQL = ", ".join(f"`{column}`" for column in SELECT_COLUMNS)
QUERY = (
    f"SELECT {SELECT_SQL} "
    "WHERE `date` >= '2012-01-01T00:00:00.000' "
    "AND `date` < '2017-11-01T00:00:00.000' "
    "AND upper(`name`) LIKE '%CASEY%' "
    "ORDER BY `date`, `invoice_line_no`"
)


def normalize_response(payload: object) -> list[dict]:
    """Return row dictionaries from the SODA v3 JSON response."""
    if isinstance(payload, list):
        return payload

    if not isinstance(payload, dict):
        raise RuntimeError(f"Unexpected Iowa API response type: {type(payload)!r}")

    for key in ("data", "results", "rows"):
        rows = payload.get(key)
        if isinstance(rows, list):
            if not rows:
                return []
            if isinstance(rows[0], dict):
                return rows

            # Some Socrata responses use positional arrays plus column metadata.
            metadata = payload.get("metadata") or payload.get("meta") or {}
            columns = metadata.get("columns") if isinstance(metadata, dict) else None
            if isinstance(columns, list):
                names = []
                for column in columns:
                    if isinstance(column, dict):
                        names.append(
                            column.get("fieldName")
                            or column.get("field_name")
                            or column.get("name")
                        )
                    else:
                        names.append(str(column))
                if all(names):
                    return [dict(zip(names, row)) for row in rows]

    raise RuntimeError(
        "Unexpected Iowa API JSON shape. Top-level keys: "
        f"{sorted(payload.keys())}"
    )


def fetch_page(page_number: int) -> list[dict]:
    body = {
        "query": QUERY,
        "page": {"pageNumber": page_number, "pageSize": PAGE_SIZE},
        "includeSynthetic": False,
    }
    response = requests.post(
        API_URL,
        json=body,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        timeout=120,
    )
    if not response.ok:
        detail = response.text[:1_500]
        raise RuntimeError(
            f"Iowa API returned HTTP {response.status_code}: {detail}"
        )
    return normalize_response(response.json())


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    frames = []
    page_number = 1
    total_rows = 0

    while True:
        start = total_rows
        print(
            f"Requesting page {page_number} "
            f"(approximately rows {start:,} through {start + PAGE_SIZE - 1:,})..."
        )
        rows = fetch_page(page_number)
        if not rows:
            break

        frame = pd.DataFrame.from_records(rows)
        frames.append(frame)
        total_rows += len(frame)

        if len(rows) < PAGE_SIZE:
            break

        page_number += 1
        time.sleep(0.2)

    if not frames:
        raise RuntimeError("The Iowa API returned no Casey's rows for the historical window.")

    data = pd.concat(frames, ignore_index=True)

    missing = sorted(set(SELECT_COLUMNS) - set(data.columns))
    if missing:
        raise RuntimeError(
            f"Iowa response is missing expected fields: {missing}. "
            f"Returned columns: {list(data.columns)}"
        )

    data = data[SELECT_COLUMNS]
    data.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved {len(data):,} rows to {OUTPUT_PATH}")
    print(f"Date range: {data['date'].min()} through {data['date'].max()}")
    print(f"Unique store names: {data['name'].nunique():,}")


if __name__ == "__main__":
    main()
