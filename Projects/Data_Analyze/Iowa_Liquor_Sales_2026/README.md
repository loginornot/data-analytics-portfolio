# Iowa Liquor Sales 2026

## Project goal

Build a modern, reproducible analytics project from the public **Iowa Liquor Sales, 2026** dataset and use it to answer a practical business question:

> **Which stores should a distributor prioritize, and what should it recommend to each store segment to increase sales?**

Rather than beginning with modeling, the project first establishes whether the source data are trustworthy enough for analysis.

## Status

### Completed: Notebook 01 — Data Audit and Cleaning

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

The notebook also identifies a structural **January 2026 precision issue** affecting source cost, retail, liters, and gallons. Rather than inventing missing decimal precision, the workflow flags the affected source price fields, reconstructs volume from bottle count and bottle size, and uses transaction revenue to derive an effective unit sale price when appropriate.

[Open Notebook 01: Data Audit and Cleaning](notebooks/01_data_audit_cleaning.ipynb)

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

## Reproduce the audit

The raw data are not committed because the public dataset is large.

1. Install the repository dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download **Iowa Liquor Sales, 2026** from the Iowa Data Hub:
   https://data.iowa.gov/catalog/dataset/1263
3. Place all CSV file(s) from the export under:
   ```text
   Iowa_Liquor_Sales_2026/data/raw/
   ```
4. Open:
   ```text
   notebooks/01_data_audit_cleaning.ipynb
   ```
5. Run the notebook from the project folder or the `notebooks/` folder.

The notebook filters explicitly to **2026-01-01 through 2026-07-31**, so a later 2026 download can still reproduce the intended analysis window.

## Next stage

### Store Segmentation + Assortment Opportunity Analysis

The next notebook will characterize stores using measures such as:

- sales scale
- order cadence
- category mix
- SKU breadth
- premium-product mix
- growth
- return behavior

The goal is to identify store segments and then find products or categories that under-index within otherwise comparable stores. A later extension may add invoice-level product affinity / market-basket analysis for cross-sell recommendations.

## Historical project

The repository also preserves the original **2019 Thinkful Iowa Liquor Sales A/B Test Proposal**. The 2026 project is new portfolio work and is kept separate so the history of the original coursework remains clear.
