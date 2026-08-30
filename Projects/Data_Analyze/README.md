# Data Analysis Projects

This folder contains business-oriented analytical work completed during Thinkful Data Science training.

## Featured: Iowa Liquor Sales Merchandising Experiment Proposal

This project revisits a 2019 Thinkful A/B test proposal using Iowa liquor transaction data. The portfolio refresh preserves the original business idea while correcting the interpretation of the source data and redesigning the experiment as a true randomized store-level test.

[Open the portfolio-ready Iowa Liquor experiment proposal](Iowa_Liquor_AB_Test_Portfolio.ipynb)

[Read the historical audit](Iowa_Liquor_Store_AB_Test_Audit.md)

[View the preserved original 2019 notebook](Iowa_Liquor_Store_AB_Test_Proposal.ipynb)

### Business / Analytical Question

Can standardized in-store merchandising for selected liquor products increase demand at Casey's stores relative to comparable stores without the treatment?

### Historical data context

The original notebook used a local historical snapshot of the State of Iowa Liquor Sales dataset. Preserved output indicates approximately **12.59 million rows**, covering **January 3, 2012 through October 31, 2017**.

The Iowa dataset records spirits purchases by licensed retailers from the state. It does not contain consumer point-of-sale revenue or retailer operating costs. The portfolio refresh therefore replaces the original retailer-profit interpretation with observable wholesale demand measures such as bottles ordered and order dollars.

### What the refresh demonstrates

- Historical dataset provenance and reproducibility auditing
- Large-dataset loading and column normalization with Pandas
- Numeric cleaning and transaction-level validation
- Distinguishing source semantics from misleading derived metrics
- Stable-identifier product and store analysis
- Exploratory analysis of wholesale demand
- A/B test design with treatment, control, and store-level randomization
- Difference-in-differences thinking for a pre/post randomized design
- Metric selection, guardrails, power-planning considerations, and causal limitations
- Clear separation between observational historical analysis and causal experiment results

### Tools

Python, Pandas, NumPy, Matplotlib, Jupyter Notebook

### Portfolio context

The original 2019 notebook remains unchanged for provenance. The portfolio-ready notebook corrects a central semantic issue in the original analysis: `Sale (Dollars) - State Bottle Cost × Bottles Sold` cannot be interpreted as Casey's profit because the Iowa records describe state-to-retailer liquor purchases. It also fixes product grouping, adds data-quality validation, documents the reconstructed historical window, and converts the original historical-comparison plan into a defensible randomized store-level merchandising experiment proposal.
