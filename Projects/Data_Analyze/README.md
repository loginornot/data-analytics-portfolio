# Data Analysis Projects

This folder contains business-oriented analytical work from my original Thinkful Data Science training and newer portfolio refresh work.

## Iowa Liquor Sales 2026 — Data Audit & Store Opportunity Analysis

This is the current portfolio version of the Iowa project. It uses the public **Iowa Liquor Sales, 2026** dataset and separates reproducible data preparation from the later business analysis.

### Current status

**Notebook 01 is complete:** data audit and cleaning for January 1 through July 31, 2026.

The cleaned snapshot contains **1,402,639 rows** after removing 13 extra exact duplicates. The audit identifies **72,456 invoices, 2,183 stores, 4,276 items, and all 99 Iowa counties**. It also documents returns, targeted missing-data repairs, a zero-cost quality flag, and a January source-precision issue that affects how cost and price fields should be used downstream.

The next notebook will develop a **store segmentation and assortment opportunity analysis**.

### Methods demonstrated

- Reproducible multi-file CSV ingestion
- Schema and date-window validation
- Identifier-safe data types
- Duplicate and repeated-key investigation
- Missing-data audit and documented enrichment
- Return/negative-transaction handling
- Numeric and logical data-quality checks
- Source-precision diagnosis
- Analysis-ready feature creation

[Open the 2026 project README](Iowa_Liquor_Sales_2026/README.md)

[Open Notebook 01](Iowa_Liquor_Sales_2026/notebooks/01_data_audit_cleaning.ipynb)

## Preserved 2019 Iowa Liquor Sales A/B Test Proposal

The original Thinkful notebook is preserved as historical coursework. It explores Iowa liquor sales and proposes a promotional A/B-test idea. It is no longer presented as the main Iowa portfolio project because the 2026 rebuild provides a stronger, more reproducible business-analysis foundation.

[Open the original 2019 notebook](Iowa_Liquor_Store_AB_Test_Proposal.ipynb)
