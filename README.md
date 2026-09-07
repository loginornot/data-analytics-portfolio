# Data Analytics & Machine Learning Portfolio

Selected projects from my Thinkful Data Science training and current portfolio refresh work. This repository demonstrates hands-on work in large-scale data cleaning, statistical analysis, business analytics, clustering, predictive modeling, and natural language processing using Python and Jupyter Notebook.

I also bring five years of U.S. Navy logistics experience and am transitioning into data analytics, with particular interest in data analyst, operations analyst, and business-focused analytics roles.

## Technical Skills Demonstrated

- **Python:** Pandas, NumPy, SciPy
- **Visualization:** Matplotlib, Seaborn
- **Statistics:** descriptive analysis, hypothesis testing, t-tests, A/B test design
- **Machine Learning:** scikit-learn, K-means clustering, supervised and unsupervised workflows
- **Business Analytics:** data-quality auditing, market structure analysis, store segmentation, peer benchmarking, assortment opportunity analysis
- **NLP:** NLTK, spaCy, text cleaning, tokenization, lemmatization, vectorization
- **Tools:** Jupyter Notebook, Git, GitHub

## Featured Projects

### 1. Iowa Liquor Sales 2026 — Market Structure, Store Segmentation & Assortment Opportunity
**Focus:** Large-scale data cleaning, reproducibility, business segmentation, peer benchmarking, recommendation logic

Built a new portfolio analysis around the 2026 Iowa Liquor Sales public dataset. The project begins with a reproducible audit of more than **1.4 million January–July transaction rows**, including multi-file schema validation, exact-duplicate handling, return identification, targeted missing-data enrichment, and detection of a January source-precision issue.

The second notebook converts transaction history into store-level commercial features and evaluates K-means solutions from `k = 2` through `8`. The validated two-segment solution separates **1,354 Focused / Premium-Leaning stores** from **721 High-Volume / Broad-Assortment stores**, while **108 sparse-history stores** are deliberately kept out of clustering rather than forced into a peer group.

The third notebook uses those peer groups to identify category and product whitespace. Recommendation rules require meaningful peer penetration, recent demand, and multi-month support, while filtering specialty packaging and package-size duplicates. The final pipeline produces **671 eligible peer products** and ranks store-level assortment opportunities as transparent peer benchmarks rather than revenue forecasts.

**Skills:** Python, Pandas, NumPy, scikit-learn, Matplotlib, data validation, feature engineering, market concentration, clustering, model evaluation, peer benchmarking, recommendation logic, business analysis

[View the 2026 project](Projects/Data_Analyze/Iowa_Liquor_Sales_2026/README.md)

[Open Notebook 01: Data Audit & Cleaning](Projects/Data_Analyze/Iowa_Liquor_Sales_2026/notebooks/01_data_audit_cleaning.ipynb)

[Open Notebook 02: Market Structure & Store Segmentation](Projects/Data_Analyze/Iowa_Liquor_Sales_2026/notebooks/02_market_structure_store_segmentation.ipynb)

[Open Notebook 03: Assortment Opportunity Analysis](Projects/Data_Analyze/Iowa_Liquor_Sales_2026/notebooks/03_assortment_opportunity_analysis.ipynb)

The [original 2019 Iowa A/B-test proposal](Projects/Data_Analyze/Iowa_Liquor_Store_AB_Test_Proposal.ipynb) is preserved separately as historical coursework.

### 2. Stack Overflow Salary Analysis
**Focus:** Data cleaning, exploratory analysis, statistical testing, compensation analysis

Analyzed the 2018 Stack Overflow Developer Survey to investigate relationships between compensation and factors such as age, professional coding experience, formal education, and work-pattern variables among respondents who reported salary in U.S. dollars. The portfolio-ready version preserves the original 2019 coursework logic while improving reproducibility, documentation, neutral labeling, and statistical interpretation. Selected descriptive charts use medians as a presentation refinement.

**Skills:** Python, Pandas, NumPy, SciPy, Matplotlib, statistical testing

[View the portfolio-ready notebook](Projects/Machine_Learning/Supervised_Learning_Projects/StackOverflow_Salary_Analysis_Portfolio.ipynb)

[View the preserved original 2019 notebook](Projects/Machine_Learning/Supervised_Learning_Projects/Stackoverflow_users_salary_prediction.ipynb)

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
│   │   ├── requirements.txt
│   │   └── notebooks/
│   │       ├── 01_data_audit_cleaning.ipynb
│   │       ├── 02_market_structure_store_segmentation.ipynb
│   │       └── 03_assortment_opportunity_analysis.ipynb
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
