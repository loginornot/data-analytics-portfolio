# Iowa Liquor Sales A/B Test Proposal — Historical Audit

This document records the audit performed before creating a portfolio-ready version of the original 2019 Thinkful notebook. The original notebook remains unchanged for provenance.

## Historical dataset reconstruction

The original notebook loaded a local pickle (`F:/Thinkful/Datasets/liquor_dataframe.pkl`) created from the State of Iowa Liquor Sales dataset and did not apply a date filter after loading it.

Evidence preserved in the notebook indicates:

- Source dataset: State of Iowa **Iowa Liquor Sales** (`m3tr-qhgy`)
- Historical coverage start: **January 3, 2012**
- Historical snapshot cutoff: **October 31, 2017**
- Historical snapshot size: **approximately 12.59 million rows**
- The final preserved index is `12,590,908`, strongly indicating **12,590,909 rows** in the original zero-indexed snapshot.
- The original schema used the classic 24-column Iowa Liquor Sales layout, including Invoice/Item Number, Date, Store Number, Store Name, Category, Vendor, Item, State Bottle Cost, State Bottle Retail, Bottles Sold, Sale (Dollars), and volume fields.

The live Iowa dataset is still published under dataset identifier `m3tr-qhgy` and currently describes coverage beginning in January 2012. Because the public dataset can receive retrospective corrections, a live query restricted to the same dates should be treated as a **reconstruction of the historical window**, not guaranteed byte-for-byte reproduction of the 2017 snapshot. The original row count and preserved notebook outputs are therefore reference checkpoints rather than strict assertions against the current API.

Official source documentation:

- https://data.iowa.gov/catalog/dataset/1051
- https://dev.socrata.com/foundry/data.iowa.gov/m3tr-qhgy

## Critical semantic correction

The original notebook created:

```python
Total_Cost = State_Bottle_Cost * Bottles_Sold
Profit = Sale_Dollars - Total_Cost
```

This was interpreted as retailer/store profit. That interpretation is incorrect.

According to the Iowa dataset documentation:

- **State Bottle Cost** is the amount the Iowa Alcoholic Beverages Division paid for each bottle.
- **State Bottle Retail** is the amount the store paid for each bottle.
- **Sale (Dollars)** is the total cost of the liquor order paid by the store to the state.
- **Bottles Sold** represents bottles ordered by the store.

Therefore, `Sale_Dollars - State_Bottle_Cost * Bottles_Sold` is closer to a **state wholesale gross-margin proxy**, not Casey's General Store profit. The dataset does not contain Casey's consumer point-of-sale revenue or operating costs, so retailer profit cannot be calculated from this dataset.

This also means the project should describe the Iowa records as **state-to-retailer liquor orders / purchase transactions**, not direct consumer checkout sales.

## Data-quality issues found in the original notebook

The preserved outputs contain rows where `Sale (Dollars)` does not reconcile with `State Bottle Retail × Bottles Sold`. For example, a Casey's row dated October 31, 2017 shows State Bottle Retail of $13.47, 3 bottles sold/ordered, but Sale (Dollars) of $13.47. Other rows show the opposite pattern, with Sale (Dollars) several times larger than the retail-price-times-bottle-count calculation.

These rows can create artificial negative or unusually large values in the original derived `Profit` field. The refreshed notebook therefore validates the arithmetic relationship explicitly and flags non-reconciling rows rather than interpreting them as stores giving products away or losing money.

Zero values in cost, retail, or order dollars are likewise treated as data-quality/correction records unless additional evidence supports a business interpretation.

## Cleaning and reproducibility issues

The original notebook:

- depended on an unavailable local pickle and local CSV path;
- converted currency fields through string replacement without documenting source-version assumptions;
- cast vendor names to strings, which can convert missing values into the literal string `nan`;
- normalized dozens of vendor names through sequential `str.replace` calls;
- contained an encoding artifact in at least one vendor name;
- grouped using display names such as Store Name rather than stable store identifiers in several places;
- did not explicitly validate duplicate invoice-line identifiers or arithmetic consistency.

The portfolio version uses the public source identifier, explicit date boundaries, numeric coercion with validation, stable identifiers where possible, and narrowly scoped normalization only when required.

## Product-ranking audit

The original notebook ranked Casey's products using the derived `Profit` field and grouped by both Item Number and Category Name. Category capitalization changed over time, so the same item could appear more than once in the ranking. Item `11788`, for example, appears under both `CANADIAN WHISKIES` and `Canadian Whiskies` in the preserved output.

The original proposal then hard-coded items `11788`, `11776`, and `35918` as the top three candidates.

The portfolio version ranks products first by stable **Item Number**, using bottles ordered and order dollars as observable demand measures. Descriptions/categories are presentation attributes rather than grouping keys.

## Experiment-design audit

Although the file was titled an A/B Test Proposal, the original design did not define a control group or random assignment. It proposed comparing promoted-store performance with historical values, so the design was closer to a pre/post or historical-baseline study than an A/B test.

Additional issues:

- The intervention was not standardized; shelf placement, flags, and pamphlets were all suggested as possible treatments.
- The unit of assignment and unit of analysis were not defined.
- The success metric mixed `Profit` and `sales` concepts and divided an aggregate historical value by two years even though the loaded snapshot spans substantially more than two years.
- Matching the same season does not by itself remove seasonality, trend, store openings/closures, pricing changes, or other time-varying confounding.
- The proposed two-week decision rule (`continue if >5%`) creates optional-stopping bias without a pre-specified sequential-testing framework.
- No power analysis, alpha level, confidence interval, or minimum detectable effect was defined.
- Selecting treatment stores because they appeared to be the least profitable was based on the incorrect retailer-profit interpretation and also risks regression to the mean.
- Promoting already top-ranked products can cause cannibalization of other products, so total-store/category outcomes need guardrails.

## Portfolio-ready redesign

The refreshed project keeps the original business instinct — test whether targeted merchandising can increase demand — but converts it into a defensible experiment proposal.

Recommended design:

1. **Population:** eligible Casey's stores with stable recent ordering activity and sufficient baseline observations.
2. **Assignment unit:** store, because merchandising is implemented at the store level.
3. **Randomization:** 50/50 treatment and control, stratified or matched on recent baseline order volume (and geography if enough stores are available).
4. **Treatment:** one standardized merchandising treatment applied consistently to a pre-specified set of products.
5. **Pre-period:** approximately 6–8 weeks for baseline measurement and power estimation.
6. **Test period:** approximately 4 weeks, with duration finalized from power analysis and operational constraints.
7. **Primary outcome:** ideally consumer POS units of promoted items per store-week. If only Iowa wholesale data are available, bottles ordered per store-week is explicitly labeled a lagging demand proxy.
8. **Secondary outcomes:** promoted-item order dollars, total liquor bottles/order dollars, order frequency, and non-promoted-item volume to measure cannibalization.
9. **Analysis:** store-level change or difference-in-differences between treatment and control, with inference performed at the store assignment level.
10. **Decision rule:** pre-specified effect threshold, alpha, power, and analysis date; no informal early stopping based on observed uplift.

## Portfolio interpretation

The refreshed notebook is an **experiment proposal and historical data audit**, not a claim that a promotion experiment was actually run. Historical Iowa order data are used for context, candidate-product discovery, store eligibility, baseline variability, and experiment planning. Causal results would require post-randomization treatment/control data, preferably Casey's point-of-sale data.