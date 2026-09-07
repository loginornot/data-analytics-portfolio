# Data Analysis Projects

This folder contains business-oriented analytical work from my original Thinkful Data Science training and newer portfolio refresh work.

## Iowa Liquor Sales 2026 — Market Structure, Store Segmentation & Assortment Opportunity

This is the current portfolio version of the Iowa project. It uses the public **Iowa Liquor Sales, 2026** dataset and is organized as a three-notebook workflow:

1. **Data Audit & Cleaning**
2. **Market Structure & Store Segmentation**
3. **Assortment Opportunity Analysis**

### Current status

The full three-notebook pipeline is complete for **January 1 through July 31, 2026**.

After cleaning, the dataset contains **1,402,639 rows, 72,456 invoices, 2,183 stores, and 4,276 items**. The audit documents exact duplicates, returns, targeted missing-data repairs, a zero-cost quality flag, and a January source-precision issue.

The segmentation notebook models **2,075 stores** with enough history and selects two commercially interpretable peer groups:

- **Focused / Premium-Leaning Stores** — 1,354 stores
- **High-Volume / Broad-Assortment Stores** — 721 stores

The assortment notebook then benchmarks stores against those peer groups and filters niche, stale, specialty-package, and package-size duplicate recommendations before ranking category and product whitespace.

### Methods demonstrated

- Reproducible multi-file CSV ingestion
- Schema and date-window validation
- Identifier-safe data types
- Duplicate and repeated-key investigation
- Missing-data audit and documented enrichment
- Return/negative-transaction handling
- Source-precision diagnosis
- Store-level feature engineering
- Market concentration analysis
- K-means clustering and model selection
- Peer benchmarking
- Category and product whitespace analysis
- Recommendation filtering and account prioritization

[Open the 2026 project README](Iowa_Liquor_Sales_2026/README.md)

[Open Notebook 01](Iowa_Liquor_Sales_2026/notebooks/01_data_audit_cleaning.ipynb)

[Open Notebook 02](Iowa_Liquor_Sales_2026/notebooks/02_market_structure_store_segmentation.ipynb)

[Open Notebook 03](Iowa_Liquor_Sales_2026/notebooks/03_assortment_opportunity_analysis.ipynb)

## Preserved 2019 Iowa Liquor Sales A/B Test Proposal

The original Thinkful notebook is preserved as historical coursework. It explores Iowa liquor sales and proposes a promotional A/B-test idea. It is no longer presented as the main Iowa portfolio project because the 2026 rebuild provides a stronger, more reproducible business-analysis foundation.

[Open the original 2019 notebook](Iowa_Liquor_Store_AB_Test_Proposal.ipynb)
