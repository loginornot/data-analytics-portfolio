# Data Setup

Raw public datasets are not committed to this repository. Portfolio notebooks document their source, expected local filename, and validation steps.

## Stack Overflow Salary Analysis

The portfolio-ready Stack Overflow Salary Analysis uses the **2018 Stack Overflow Developer Survey**.

Expected path:

```text
data/survey_results_public.csv
```

### Source

- 2018 survey results: https://survey.stackoverflow.co/2018/
- Official survey archive: https://github.com/StackExchange/Survey/tree/main/packages/archive/2018

The public 2018 release contains **98,855 qualified responses**. The refreshed notebook checks this row count before continuing.

### Methodology note

The original coursework annualized monthly salary by multiplying by 12 and weekly salary by multiplying by **52**. Stack Overflow's published 2018 methodology used **50 working weeks**. The portfolio notebook intentionally preserves the original coursework logic and documents the difference. The original notebook also filtered annualized salary to values **above $50,000 and below $195,000**.

### To rerun

1. Obtain the official 2018 public survey response CSV.
2. Save it as `data/survey_results_public.csv`.
3. Run `Projects/Machine_Learning/Supervised_Learning_Projects/StackOverflow_Salary_Analysis_Portfolio.ipynb`.

---

## Iowa Liquor Promotion Experiment Proposal

The original 2019 Thinkful notebook loaded a local pickle created from the historical **Iowa Liquor Sales** dataset. That snapshot contained roughly 12.59 million statewide order lines and extended through **October 31, 2017**.

Downloading today's full statewide dataset is unnecessary for the portfolio refresh. The refreshed notebook analyzes Casey's locations, so the repository includes a downloader that queries only the historical Casey's rows and only the fields required by the project.

### Source

- Iowa Liquor Sales API dataset identifier: `m3tr-qhgy`
- Iowa Data Hub: https://data.iowa.gov/
- Socrata API documentation: https://dev.socrata.com/foundry/data.iowa.gov/m3tr-qhgy

Iowa describes this dataset as liquor **purchase information from Class E licensees by product and order date**. It is not consumer point-of-sale data.

### Create the historical Casey's subset

From the repository root, install dependencies and run:

```text
pip install -r requirements.txt
python scripts/download_iowa_caseys_subset.py
```

The script requests records from 2012 through **2017-10-31** whose store name contains `Casey`, then saves:

```text
data/iowa_caseys_2012_to_2017_10_31.csv
```

The downloader selects the order, store, product, cost, quantity, and order-value fields needed by the portfolio notebook. This avoids downloading the multi-gigabyte statewide archive.

Then run:

```text
Projects/Data_Analyze/Iowa_Liquor_Promotion_Experiment_Portfolio.ipynb
```

### Interpretation note

The original notebook calculated:

```text
Sale (Dollars) - State Bottle Cost × Bottles Sold
```

and called the result `Profit`. Iowa's metadata indicate that `State Bottle Cost` is the amount the Alcoholic Beverages Division paid per bottle and `Sale (Dollars)` is the total amount charged to the licensee for the order. The portfolio refresh therefore does **not** describe this field as Casey's store profit. It preserves the calculation only for provenance and uses direct order measures and product penetration for the refreshed analysis.

## Why these data are not committed

These are external public-source datasets rather than original portfolio code. Keeping large raw files outside the repository reduces repository size while the notebooks and downloader scripts preserve reproducibility.