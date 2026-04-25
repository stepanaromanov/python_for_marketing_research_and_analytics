# 📦 _legacy — Python for Marketing Research & Analytics

> **Archive notice:** This folder preserves an earlier body of work completed between 2023–2024.
> The projects here are structured around DataCamp curriculum tracks and guided case studies.
> They demonstrate foundational competency across the core marketing analytics stack in Python.
> For current, original project work see the parent portfolio directory.

---

## Overview

| # | Project | Primary Methods | Business Domain |
|---|---------|----------------|----------------|
| 1 | [Analyzing Marketing Campaigns with pandas](#1-analyzing-marketing-campaigns-with-pandas) | EDA, A/B testing, pandas | Campaign performance |
| 2 | [Analyzing Social Media Data in Python](#2-analyzing-social-media-data-in-python) | API data, NLP, network graphs | Social / community |
| 3 | [Market Basket Analysis in Python](#3-market-basket-analysis-in-python) | Association rules, Apriori | Retail / e-commerce |
| 4 | [Machine Learning for Marketing in Python](#4-machine-learning-for-marketing-in-python) | Churn, CLV, segmentation, scikit-learn | Customer lifecycle |
| 5 | [Customer Segmentation in Python](#5-customer-segmentation-in-python) | Cohort analysis, k-means clustering | Retention / CRM |
| 6 | [Predicting Customer Churn in Python](#6-predicting-customer-churn-in-python) | Logistic regression, Random Forest, EDA | Churn prevention |
| 7 | [Customer Analytics and A/B Testing in Python](#7-customer-analytics-and-ab-testing-in-python) | KPIs, statistical significance, A/B testing | Growth / experimentation |
| 8 | [Combating Subscriber Churn with Targeted Marketing](#8-combating-subscriber-churn-with-targeted-marketing) | ML churn prediction, user segmentation | Streaming / subscriptions |
| 9 | [Cleaning Bank Marketing Campaign Data](#9-cleaning-bank-marketing-campaign-data) | Data cleaning, type validation, PostgreSQL prep | Banking / data engineering |
| 10 | [Building a Retail Data Pipeline](#10-building-a-retail-data-pipeline) | ETL, SQL, parquet, validation | Retail / data engineering |
| 11 | [Private School Student Churn Analysis](#11-private-school-student-churn-analysis) | PostgreSQL, Random Forest, feature importance | Education / retention |

**Stack:** Python 3 · pandas · scikit-learn · matplotlib · seaborn · mlxtend · PostgreSQL · Jupyter Notebook

---

## Projects

### 1. Analyzing Marketing Campaigns with pandas

**Business question:** Which acquisition channels are performing, and are campaign conversion differences statistically real or noise?

This project builds a full marketing analysis workflow from scratch using pandas. It covers importing and cleaning raw campaign data, computing standard marketing metrics (conversion rate, CPA, ROAS), and automating repetitive analysis tasks with reusable custom functions. The A/B testing section applies chi-square and proportion tests to determine whether channel-specific conversion differences are statistically significant — giving a rigorous basis for budget reallocation decisions rather than relying on gut feel.

**Key techniques:** `groupby` aggregations, custom metric functions, A/B test implementation, conversion funnel analysis  
**Tools:** `pandas`, `scipy.stats`, `matplotlib`

---

### 2. Analyzing Social Media Data in Python

**Business question:** What does engagement and community structure look like across a Twitter audience, and what content themes drive interaction?

A comprehensive Twitter/X data project covering the full pipeline from API extraction to insight. The notebook works through JSON parsing of API responses, text preprocessing and keyword frequency analysis, and network graph construction to map follower and mention relationships. The result is a quantified picture of community clusters, influencer nodes, and the content signals most associated with engagement — the kind of analysis that informs both organic content strategy and paid social targeting.

**Key techniques:** Twitter API integration, JSON structure traversal, text tokenisation, network graph analysis, choropleth mapping  
**Tools:** `tweepy`, `json`, `networkx`, `folium`, `matplotlib`

---

### 3. Market Basket Analysis in Python

**Business question:** Which products are bought together, and how can that structure be used to drive cross-sell revenue?

Applies the Apriori association rules algorithm to transaction datasets across multiple retail contexts — grocery stores, libraries, e-book platforms, and general retail. The project works through the full MBA pipeline: encoding transactions, generating frequent itemsets, computing support/confidence/lift metrics, pruning rules by business relevance, and visualising association networks. The output is a prioritised list of cross-sell and bundling opportunities grounded in actual purchase co-occurrence patterns.

**Key techniques:** One-hot transaction encoding, Apriori algorithm, association rule mining, rule pruning by lift/confidence thresholds, visualisation of rule networks  
**Tools:** `mlxtend`, `pandas`, `matplotlib`, `networkx`

---

### 4. Machine Learning for Marketing in Python

**Business question:** Can we predict which customers will churn, what they're worth over their lifetime, and how to segment them for targeted treatment?

A broad survey of ML applications in marketing covering three interconnected problems. The churn section builds classification models with feature engineering and threshold optimisation tuned to business cost of false negatives. The CLV section implements cohort-based and probabilistic models to rank customers by future revenue potential. The segmentation section applies clustering to create actionable audience groups for differentiated marketing. Together they form a playbook for moving from reactive campaign management to predictive customer strategy.

**Key techniques:** Binary classification, CLV modelling (BG/NBD), k-means and hierarchical clustering, feature scaling, model evaluation (ROC, precision-recall)  
**Tools:** `scikit-learn`, `lifetimes`, `pandas`, `seaborn`

---

### 5. Customer Segmentation in Python

**Business question:** How do customer cohorts evolve over time, and what distinct behavioural segments exist within the customer base?

Focuses on two complementary segmentation approaches. Cohort analysis tracks groups of customers acquired in the same period to reveal retention curves, revenue trends, and lifecycle decay — answering when customers disengage, not just whether. The k-means section then clusters customers on behavioural features (recency, frequency, monetary value) to identify well-separated, actionable segments with distinct engagement patterns. Visualisation is central: heatmaps, silhouette plots, and 2D cluster projections make findings shareable with non-technical stakeholders.

**Key techniques:** Cohort construction, retention heatmaps, RFM feature engineering, k-means with elbow and silhouette optimisation, PCA for cluster visualisation  
**Tools:** `pandas`, `scikit-learn`, `matplotlib`, `seaborn`

---

### 6. Predicting Customer Churn in Python

**Business question:** Which customers are most likely to churn, what features drive that risk, and how do we evaluate model performance in a business context?

A focused churn modelling project that follows the full ML workflow. The EDA section uses seaborn to explore the churn dataset — distributions, correlations, and class imbalance — before preprocessing categorical variables and scaling numerics. Multiple scikit-learn classifiers are trained and compared (logistic regression, decision tree, random forest), with evaluation going beyond accuracy to confusion matrices, classification reports, and ROC curves. Feature importance analysis translates model outputs into business-readable risk drivers.

**Key techniques:** Exploratory data analysis, class imbalance handling, multi-model comparison, ROC/AUC, confusion matrix analysis, feature importance ranking  
**Tools:** `pandas`, `scikit-learn`, `seaborn`, `matplotlib`

---

### 7. Customer Analytics and A/B Testing in Python

**Business question:** How do we design, run, and correctly interpret A/B tests — and how do we avoid the common mistakes that lead to wrong decisions?

A rigorous treatment of experimentation methodology applied to customer analytics. The project opens by defining KPIs clearly (the often-skipped prerequisite for any valid test) before building up through test design — sample size calculation, randomisation, control group selection — to execution and analysis. Statistical significance is computed correctly with power analysis, and the notebook explicitly addresses common failure modes: peeking, multiple comparisons, and Simpson's paradox. The final section covers communicating results to non-technical audiences.

**Key techniques:** KPI definition, sample size / power calculation, z-test and t-test implementation, p-value interpretation, multiple comparison correction, results communication  
**Tools:** `scipy.stats`, `statsmodels`, `pandas`, `matplotlib`

---

### 8. Combating Subscriber Churn with Targeted Marketing

**Business question:** For a video streaming platform, which subscribers are most at risk of churning, and what user segments should receive which retention interventions?

An applied ML project framed around a streaming platform's subscriber base. The modelling side builds a churn classifier with engineered engagement features (session frequency, content completion rates, inactivity streaks) and optimises the decision threshold for marketing cost efficiency rather than raw accuracy. The segmentation side uses unsupervised clustering to split the at-risk cohort into sub-groups with distinct behavioural profiles, enabling targeted win-back campaigns rather than a single blunt intervention across all churners.

**Key techniques:** Subscriber engagement feature engineering, churn classification with threshold tuning, at-risk segment clustering, campaign targeting logic  
**Tools:** `scikit-learn`, `pandas`, `matplotlib`, `seaborn`

---

### 9. Cleaning Bank Marketing Campaign Data

**Business question:** How do we prepare raw bank campaign data for reliable downstream analysis and safe loading into a production PostgreSQL database?

A data engineering project centered on the cleaning and validation pipeline for a bank's personal loan marketing campaign dataset. The work covers identifying and resolving type inconsistencies, handling missing and malformed values, standardising categorical encodings, and validating the final schema against PostgreSQL column type requirements. The output is a clean, typed DataFrame ready for `COPY` ingestion — the kind of unglamorous but business-critical work that sits upstream of every analysis.

**Key techniques:** Dtype coercion, missing value imputation strategies, categorical standardisation, schema validation, PostgreSQL-ready export  
**Tools:** `pandas`, `numpy`, `psycopg2`

---

### 10. Building a Retail Data Pipeline

**Business question:** How do we reliably ingest retail data from heterogeneous sources, transform it consistently, and deliver it in a format ready for analysis?

An ETL pipeline project working across two common real-world source formats: SQL tables and parquet files. The extraction stage queries a relational database and reads columnar parquet data, handling schema differences between sources. The transformation stage applies normalisation, joins, and business logic to produce a unified dataset. The load stage writes to a validated output format with row count and schema checks to catch pipeline failures early. The project demonstrates the data engineering competency that makes analytics work reliable at scale.

**Key techniques:** SQL querying from Python, parquet read/write, multi-source join and normalisation, pipeline validation, load verification  
**Tools:** `pandas`, `sqlalchemy`, `pyarrow`, `sqlite3`

---

### 11. Private School Student Churn Analysis

**Business question:** Which students are at risk of leaving a private school, and what academic or demographic factors are most predictive of that decision?

An end-to-end ML project applied to the education sector. Data is pulled directly from a PostgreSQL database using `sqlalchemy`, then processed through a standard ML preparation pipeline: null handling, dummy variable encoding for categorical features, and numeric scaling. A Random Forest classifier is trained and evaluated with a full classification report and confusion matrix. The feature importance output identifies the strongest predictors of student departure — giving school leadership actionable signals for early intervention programmes.

**Key techniques:** PostgreSQL extraction via SQLAlchemy, dummy encoding, feature scaling, Random Forest classification, confusion matrix, feature importance analysis  
**Tools:** `pandas`, `scikit-learn`, `sqlalchemy`, `matplotlib`, `seaborn`

---

## Notes on this archive

These projects were completed as structured learning exercises, primarily following DataCamp course curricula. They demonstrate working knowledge of the core Python marketing analytics stack and the ability to apply standard ML workflows to marketing problems. They are preserved here as a record of foundational skill-building.

For independent, original project work — including custom datasets, novel problem framing, and production-oriented code — see the main portfolio directory.
