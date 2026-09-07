# Iowa Liquor Sales 2026

## Project overview

This project rebuilds an older Iowa Liquor Sales portfolio idea into a modern, reproducible commercial analytics workflow using the public **Iowa Liquor Sales, 2026** dataset.

The business question is:

> **Which stores should a distributor prioritize, how do stores differ in commercial behavior, and which products appear underrepresented relative to similar stores?**

The analysis is organized as a three-notebook pipeline:

1. **Data Audit & Cleaning** — validate and prepare the transaction data.
2. **Market Structure & Store Segmentation** — understand the store base and create interpretable peer groups.
3. **Assortment Opportunity Analysis** — identify category and product whitespace within those peer groups.

The project covers **January 1 through July 31, 2026**.

---

## Key results

After cleaning, the analytical dataset contains:

- **1,402,639 transaction rows**
- **72,456 invoices**
- **2,183 stores**
- **4,276 items**
- **44 category codes**
- **99 Iowa counties**
- **1,088 return / negative rows retained and flagged**
- **0 remaining missing store-geography rows**
- **0 remaining missing category rows**

The market is relatively dispersed: **643 stores, or 29.5% of stores, account for about 80% of gross sales**.

For store segmentation, **2,075 stores** have enough transaction history to model and **108 stores** are retained as `insufficient_history` rather than forced into a cluster.

The selected two-segment solution has a **silhouette score of 0.323** and produces commercially interpretable peer groups:

| Segment | Stores | Median gross sales | Median order value | Median SKUs | Median categories | Median premium-sales share |
|---|---:|---:|---:|---:|---:|---:|
| Focused / Premium-Leaning Stores | 1,354 | $28,877 | $1,553 | 93 | 21 | 37.0% |
| High-Volume / Broad-Assortment Stores | 721 | $130,265 | $2,855 | 343 | 36 | 16.2% |

Notebook 03 then uses these peer groups to build transparent assortment benchmarks. After filtering niche, stale, specialty-package, and package-size duplicate recommendations, the final recommendation universe contains:

- **671 eligible peer products**
- **749 segment-product benchmarks**
- **271,675 store-product opportunity rows**
- **34 median eligible opportunities per store**

These opportunity values are **peer benchmarks for prioritization, not forecasts of incremental revenue**.

---

## Notebook 01 — Data Audit & Cleaning

[Open Notebook 01](notebooks/01_data_audit_cleaning.ipynb)

The first notebook creates a defensible analytical foundation before any modeling.

### What it does

- Loads one or more Iowa Liquor Sales CSV exports reproducibly.
- Restricts the project to the fixed Jan–Jul 2026 analysis window.
- Preserves identifier fields such as store numbers and ZIP/FIPS codes as text.
- Removes only exact duplicate records.
- Distinguishes legitimate repeated invoice-item lines from duplicates.
- Retains returns and negative transactions as real business activity.
- Repairs missing store geography only when supported by same-store evidence or documented external verification.
- Resolves a narrowly researched missing-category case.
- Identifies a January 2026 source-precision problem affecting several numeric fields.
- Reconstructs defensible volume measures and effective unit price without fabricating cost precision.
- Saves an analysis-ready Parquet dataset for downstream notebooks.

### Important data-quality finding

January source values for `state_bottle_cost`, `state_bottle_retail`, liters, and gallons largely lose decimal precision. The project therefore avoids using January source cost/retail values for precise price or margin analysis. Revenue, bottle counts, reconstructed volume, store/product mix, and invoice behavior remain usable across the full Jan–Jul window.

---

## Notebook 02 — Market Structure & Store Segmentation

[Open Notebook 02](notebooks/02_market_structure_store_segmentation.ipynb)

The second notebook asks:

> **How does the Iowa store base differ in scale, ordering behavior, assortment breadth, price mix, momentum, and returns?**

### Store features

The model uses features representing distinct commercial dimensions:

- gross sales
- average purchase invoice value
- orders per active month
- SKU breadth
- largest-category concentration
- premium-sales mix
- recent sales momentum

Return rate remains a descriptive diagnostic but is **not used to define merchandising peers**. In first-pass testing, including return behavior created a small cluster that otherwise resembled another store group; removing it produced more useful peer groups for downstream assortment analysis.

### Model selection

K-means solutions from `k = 2` through `8` are compared using silhouette and Davies-Bouldin scores. The two-cluster solution performs best on the validated snapshot and is then interpreted using the underlying business metrics rather than treating cluster IDs as meaningful labels by themselves.

---

## Notebook 03 — Assortment Opportunity Analysis

[Open Notebook 03](notebooks/03_assortment_opportunity_analysis.ipynb)

The third notebook turns store segments into decision support for a distributor.

It has three layers:

1. **Category whitespace** — categories that under-index relative to the store's peer segment.
2. **Product whitespace** — products with meaningful, recent peer adoption and no observed positive sales for the target store.
3. **Store prioritization** — accounts with enough commercial scale and credible assortment whitespace to justify attention.

### Recommendation guardrails

This dataset contains transactions, not shelf inventory. Therefore the project deliberately avoids claiming that an item is physically absent from a store.

The recommendation workflow:

- requires minimum peer penetration and peer-store support,
- requires recent peer adoption and multi-month activity,
- excludes `Temporary & Specialty Packages`,
- normalizes obvious packaging descriptions such as PET, mini, flask, and party-bucket variants,
- removes a candidate if the target store already sells the same underlying product family under another item number,
- uses median peer behavior to reduce sensitivity to extreme orders.

The resulting opportunity-dollar metric asks how large the observed gap is relative to comparable peers. It is a **ranking benchmark**, not a causal estimate of what the store would sell after adding the product.

---

## Business interpretation

The workflow can support a distributor in:

- identifying high-leverage accounts,
- benchmarking stores against behaviorally similar peers,
- identifying under-indexed categories,
- surfacing products with broad and recent peer adoption,
- prioritizing sales conversations with transparent evidence.

A production system would ideally add inventory and out-of-stock data, gross margin, promotions, store format and square footage, local demographics, supply constraints, a full seasonal history, and controlled measurement of recommendation lift.

---

## Reproduce the project

The raw transaction files are not committed because the public dataset is large.

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Download **Iowa Liquor Sales, 2026** from the Iowa Data Hub:

   https://data.iowa.gov/catalog/dataset/1263

3. Place all downloaded CSV file(s) under:

   ```text
   data/raw/
   ```

4. Run the notebooks in order:

   ```text
   notebooks/01_data_audit_cleaning.ipynb
   notebooks/02_market_structure_store_segmentation.ipynb
   notebooks/03_assortment_opportunity_analysis.ipynb
   ```

Notebook 01 explicitly filters to **2026-01-01 through 2026-07-31**, allowing the intended analysis window to remain fixed even if the public 2026 dataset later contains additional months.

---

## Skills demonstrated

**Python · Pandas · NumPy · Matplotlib · scikit-learn · data-quality auditing · feature engineering · K-means clustering · model evaluation · peer benchmarking · recommendation logic · business analysis · reproducible analytics**

---

## Historical context

The repository also preserves the original **2019 Thinkful Iowa Liquor Sales A/B Test Proposal** as historical coursework. The 2026 project is a new portfolio rebuild and is kept separate so the original work remains clearly distinguishable from the modern analysis.
