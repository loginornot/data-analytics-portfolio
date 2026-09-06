# Iowa Liquor Sales 2026

## Project goal

Build a modern, reproducible analytics project from the public **Iowa Liquor Sales, 2026** dataset and use it to answer a practical business question:

> **Which stores should a distributor prioritize, and which product categories appear underrepresented relative to similar stores?**

The project starts with source validation and then turns the cleaned transaction data into an account-prioritization and assortment-review framework.

## Completed notebooks

### Notebook 01 — Data Audit and Cleaning

The audit covers **January 1 through July 31, 2026** and processes the snapshot as one analytical table even when the portal export is split across multiple CSV files.

Key results after cleaning:

- **1,402,639 rows**
- **72,456 unique invoices**
- **2,183 stores**
- **4,276 items**
- **44 known category codes**
- **99 Iowa counties**
- **1,088 return/negative rows retained and flagged**
- **0 remaining missing store-geography rows**
- **0 remaining missing category rows**

The audit also identifies a structural **January 2026 precision issue** affecting source cost, retail, liters, and gallons. Rather than inventing missing decimal precision, the workflow flags the affected source price fields, reconstructs defensible volume measures, and preserves the limitation for downstream analysis.

[Open Notebook 01: Data Audit and Cleaning](notebooks/01_data_audit_cleaning.ipynb)

### Notebook 02 — Store Segmentation and Assortment Opportunity

The second notebook builds store-level features and uses K-means clustering to create three interpretable account tiers from **gross sales, ordering days, SKU breadth, and category breadth**.

Verified segment profile:

| Segment | Stores | Median gross sales | Median order days | Median SKUs | Median categories | Share of gross sales |
|---|---:|---:|---:|---:|---:|---:|
| Developing | 274 | $7,497 | 4 | 38 | 13 | 1.1% |
| Core | 1,087 | $29,881 | 17 | 95 | 21 | 15.2% |
| Strategic | 822 | $116,568 | 31 | 321 | 36 | 83.8% |

The Strategic tier contains about **38% of stores but generates roughly 84% of gross sales**, making it the highest-leverage first tier for account review.

The notebook then builds segment-level category benchmarks. A category qualifies only when it represents at least **1% of segment gross sales** and is purchased by at least **50% of stores** in that segment. Core and Strategic stores active in at least five months are screened for categories where actual sales are below **50% of the peer-mix benchmark** and the seven-month benchmark gap is at least **$5,000**.

The resulting gap is explicitly treated as a **prioritization signal, not a forecast of incremental revenue**. Retail format, chain strategy, shelf space, geography, and local demand can all explain intentional deviations from peer mix.

[Open Notebook 02: Store Segmentation and Assortment Opportunity](notebooks/02_store_segmentation_assortment_opportunity.ipynb)

## Cleaning decisions

| Issue | Finding | Decision |
|---|---|---|
| Source-file schema | Downloaded files match | Concatenate |
| Exact duplicates | 13 extra rows | Remove exact duplicates only |
| Repeated invoice-item keys | Legitimate rows with different quantities | Keep |
| Negative sales | 1,088 rows; mostly return invoices | Keep and flag |
| Missing store geography | 680 raw rows | Repair from same-store evidence and documented external verification; 0 remain |
| Missing category | 25 rows for one product | Apply a narrowly documented researched inference; 0 remain |
| Zero source cost | 42 rows for one item | Keep; exclude from cost/margin use |
| January numeric precision | Several source numeric fields largely lose decimals | Flag source prices; reconstruct defensible derived measures |

## Reproduce the project

The raw data are not committed because the public dataset is large.

1. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download **Iowa Liquor Sales, 2026** from the Iowa Data Hub:
   https://data.iowa.gov/catalog/dataset/1263
3. Place all CSV file(s) from the export under:
   ```text
   data/raw/
   ```
4. Run `notebooks/01_data_audit_cleaning.ipynb` to create the processed Parquet file.
5. Run `notebooks/02_store_segmentation_assortment_opportunity.ipynb`.

Notebook 01 filters explicitly to **2026-01-01 through 2026-07-31**, so a later 2026 download can still reproduce the intended analysis window, subject to later corrections by the public data publisher.

## Next extension

A strong next extension would make the peer groups more specific by adding chain or retail-format context, then move from category-level gaps to **specific SKU recommendations** and invoice-level product affinity / market-basket analysis.

## Historical project

The repository also preserves the original **2019 Thinkful Iowa Liquor Sales A/B Test Proposal**. The 2026 project is new portfolio work and is kept separate so the history of the original coursework remains clear.
