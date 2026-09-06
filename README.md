# Data Analytics & Machine Learning Portfolio

Selected projects from my Thinkful Data Science training and current portfolio refresh work. This repository demonstrates hands-on work in data cleaning, exploratory analysis, statistical testing, experiment design, machine learning, and natural language processing using Python and Jupyter Notebook.

I also bring five years of U.S. Navy logistics experience and am transitioning into data analytics, with particular interest in data analyst, operations analyst, and business-focused analytics roles.

## Technical Skills Demonstrated

- **Python:** Pandas, NumPy, SciPy
- **Visualization:** Matplotlib, Seaborn
- **Statistics:** descriptive analysis, hypothesis testing, t-tests, A/B test design
- **Machine Learning:** scikit-learn, supervised and unsupervised learning workflows
- **NLP:** NLTK, spaCy, text cleaning, tokenization, lemmatization, vectorization
- **Tools:** Jupyter Notebook, Git, GitHub

## Featured Projects

### 1. Stack Overflow Salary Analysis
**Focus:** Data cleaning, exploratory analysis, statistical testing, compensation analysis

Analyzed the 2018 Stack Overflow Developer Survey to investigate relationships between compensation and factors such as age, professional coding experience, formal education, and work-pattern variables among respondents who reported salary in U.S. dollars. The portfolio-ready version preserves the original 2019 coursework logic while improving reproducibility, documentation, neutral labeling, and statistical interpretation. Selected descriptive charts use medians as a presentation refinement.

**Skills:** Python, Pandas, NumPy, SciPy, Matplotlib, statistical testing

[View the portfolio-ready notebook](Projects/Machine_Learning/Supervised_Learning_Projects/StackOverflow_Salary_Analysis_Portfolio.ipynb)

[View the preserved original 2019 notebook](Projects/Machine_Learning/Supervised_Learning_Projects/Stackoverflow_users_salary_prediction.ipynb)

### 2. Iowa Liquor Sales 2026 — Data Audit & Store Opportunity Analysis
**Focus:** Large-scale data cleaning, data quality, reproducibility, business analysis

Rebuilt the Iowa Liquor Sales project around the current 2026 public dataset rather than treating the original 2019 A/B-test proposal as finished portfolio work. The first notebook audits and cleans more than 1.4 million January–July records, validates multi-file ingestion, preserves identifier fields, removes only exact duplicates, investigates returns and missingness, documents targeted enrichments, and detects a January source-precision issue before downstream analysis.

The next stage develops a **store segmentation and assortment opportunity analysis**: characterize retailers by scale, order cadence, category mix, SKU breadth, premium mix, growth, and return behavior, then identify product or category opportunities within comparable stores.

**Skills:** Python, Pandas, NumPy, data validation, reproducible pipelines, data-quality auditing, business analysis

[View the 2026 project](Projects/Data_Analyze/Iowa_Liquor_Sales_2026/README.md)

[Open Notebook 01: Data Audit and Cleaning](Projects/Data_Analyze/Iowa_Liquor_Sales_2026/notebooks/01_data_audit_cleaning.ipynb)

The [original 2019 Iowa A/B-test proposal](Projects/Data_Analyze/Iowa_Liquor_Store_AB_Test_Proposal.ipynb) is preserved separately as historical coursework.

### 3. Zillow Zestimate Kaggle Project
**Focus:** Predictive modeling, supervised machine learning

Worked with Zillow housing data in a Kaggle-style predictive modeling project. This project demonstrates experience preparing data for supervised learning and applying machine learning methods to a real-world prediction problem.

**Skills:** Python, Pandas, scikit-learn, predictive modeling

[View the notebook](Projects/Machine_Learning/Supervised_Learning_Projects/Zillow_Kaggle_Zestimate_Competition.ipynb)

### 4. News NLP Topic Summarization
**Focus:** Natural language processing and text preparation

Built an NLP workflow for news article text, including article collection, regular-expression cleaning, sentence tokenization, lemmatization, and text vectorization using common Python NLP libraries.

**Skills:** Python, NLTK, spaCy, scikit-learn, regular expressions, NLP preprocessing

[View the notebook](Projects/Machine_Learning/Unsupervised_Learning_Projects/NLP_topic_summarization_from_news_data.ipynb)

## Repository Structure

```text
Projects/
├── Data_Analyze/
│   ├── Iowa_Liquor_Sales_2026/
│   │   ├── README.md
│   │   └── notebooks/
│   │       └── 01_data_audit_cleaning.ipynb
│   └── Iowa_Liquor_Store_AB_Test_Proposal.ipynb
└── Machine_Learning/
    ├── Supervised_Learning_Projects/
    │   ├── StackOverflow_Salary_Analysis_Portfolio.ipynb
    │   ├── Stackoverflow_users_salary_prediction.ipynb
    │   └── Zillow_Kaggle_Zestimate_Competition.ipynb
    └── Unsupervised_Learning_Projects/
        └── NLP_topic_summarization_from_news_data.ipynb
```

## Portfolio Note

The older projects in this repository originated in my 2019 Thinkful coursework. Portfolio-ready copies are created separately from preserved originals so the historical work remains intact. Documentation and reproducibility may be modernized, while new analyses are clearly identified as new work rather than presented as part of the original coursework.
