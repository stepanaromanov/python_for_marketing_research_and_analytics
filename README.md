# Stepan Romanov — Marketing Research & Analytics Portfolio

---

## Projects

**Project 01: Markov Chain Multi-Touch Attribution (MTA)**

**E-commerce channel credit allocation with ground-truth validation and MLOps deployment**

**Stack:** `pandas` · `plotly` · `mlflow` · `dvc` · `numpy`

---

### 📋 Executive Summary

This project implements a **Markov Chain model** for multi-touch attribution to overcome the limitations of last-click models. It fairly credits marketing channels based on their true contribution to conversions by modeling customer journeys as a stochastic process and using removal-effect analysis.

**Key Insight:** Last-click attribution significantly distorts channel performance. The Markov model reveals that **Paid Search** is heavily under-credited (driving far more conversions early in journeys), while **Display** is over-credited.

### 🎯 Business Impact

- **Reallocation recommendation**: Shift budget from over-credited Display to under-credited Paid Search.
- Model validated against **ground-truth causal effects** (+14% lift injected into Paid Search), which the Markov model successfully recovers.

### What You'll Find in the Notebook

- **Synthetic data generation** (200k journeys) with realistic path lengths, and injected causal lifts for validation.
- **Markov Chain implementation** from scratch (transition matrix + removal effects).
- **Comparison**: Last-click vs. Markov attribution shares with clear visualizations.
- **Production SQL query** for aggregating real journey data from a marketing events table.
- **EDA & interactive Plotly visualizations** of journey patterns and channel performance.
- **MLOps practices**: MLflow experiment tracking, DVC pipeline definition, and GitHub Actions CI/CD workflow for weekly retraining.
- Executive summary + technical appendix tailored for CMOs, analysts, data engineers, and hiring managers.

### Skills Demonstrated

- Causal inference & attribution modeling (removal-effect methodology)
- Markov chains & linear algebra in Python
- Reproducible data generation with ground-truth validation
- SQL for production journey reconstruction
- MLOps (DVC + MLflow + CI/CD)
- Clear stakeholder communication (executive + technical sections)

**Folder:** [`01_markov_mta/`](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/tree/main/01_markov_mta)

**Notebook:** [`01_markov_chain_mta.ipynb`](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/blob/main/01_markov_mta/01_markov_chain_mta.ipynb)

---

**Project 02: Shapley Value Attribution for Paid Media** 

**Fair marginal contribution analysis for overlapping B2B channels with ground-truth validation and MLOps** 

**Stack:** `shap` · `pandas` · `plotly` · `mlflow` · `dvc` · `numpy` · `itertools` 

---

### 📋 Executive Summary  
This project implements **Shapley Value decomposition** (from cooperative game theory) for multi-touch attribution. It fairly allocates credit to marketing channels by computing each channel’s average marginal contribution across *all possible coalitions*, solving the overlap problem that plagues heuristic models (last-click, linear, time-decay). 

**Key Insight:** Naive proportional allocation (based on channel frequency) distorts performance. Shapley reveals **Paid Search** is significantly under-credited, while **Webinar** and **Direct** are over-credited. The model exactly recovers the injected ground-truth marginal effects. 

**Shapley is the only attribution method** that satisfies the four core axioms of fairness: Efficiency, Symmetry, Dummy, and Additivity.

### 🎯 Business Impact  
- **Reallocation recommendation**: Increase investment in under-credited **Paid Search** (strong early-funnel driver) and reduce over-reliance on **Webinar** and **Direct**. 
- Model validated against **synthetic ground-truth causal lifts** (+11% incremental revenue per channel in coalitions), which Shapley perfectly recovers. 
- Production-ready for B2B CRM data via SQL cohort aggregation. 

### What You'll Find in the Notebook  
- **Synthetic B2B data generation** (200k deals) with realistic channel overlap, lognormal revenue, and controlled ground-truth marginal contributions. 
- **Shapley implementation** — both exact (all permutations) and Monte-Carlo sampling for scalability, with custom `value_function` based on coalition revenue. 
- **Comparison tables & visualizations**: Naive shares vs. Shapley shares, bias analysis, and interactive Plotly charts. 
- **Production SQL query** for aggregating channel coalitions per closed-won deal within attribution windows. 
- **EDA** of coalition patterns and revenue distributions. 
- **MLOps practices**: MLflow experiment tracking & Model Registry, DVC pipelines, reproducible data generation. 
- Executive summary + technical appendix (math, implementation details, scalability notes). 

### Skills Demonstrated  
- Cooperative game theory & fair credit allocation (Shapley values) 
- Monte-Carlo & exact permutation methods for combinatorial problems 
- Ground-truth validation for attribution models 
- SQL for production journey/coalition reconstruction 
- MLOps (MLflow + DVC) and reproducible experimentation 
- Clear communication for technical and executive audiences 

**Folder:** [`02_shapley_attribution/`](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/tree/main/02_shapley_attribution) 
**Notebook:** [`02_shapley_attribution.ipynb`](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/blob/main/02_shapley_attribution/02_shapley_attribution.ipynb) 

---

## 📦 Legacy Work — `_legacy/`

The [`_legacy/`](./_legacy/) folder contains an earlier collection of **11 Python notebooks** completed in 2023–2024, structured around DataCamp marketing analytics curriculum tracks. They cover the full core stack — pandas, scikit-learn, A/B testing, customer segmentation, churn modelling, and data pipeline engineering — applied to retail, banking, streaming, and education datasets.

They are preserved as a transparent record of foundational skill-building and are fully documented in [`_legacy/README.md`](./_legacy/README.md).

| What you'll find | Details |
|---|---|
| Notebooks | 11 guided case studies |
| Topics | Campaign analysis · Social media · Market basket · ML for marketing · Segmentation · Churn · A/B testing · Data pipelines |
| Stack | Python · pandas · scikit-learn · mlxtend · PostgreSQL · matplotlib · seaborn |
| Period | 2023 – 2024 |

> If you're reviewing this portfolio for the first time, start with the main project list above. Visit `_legacy/` if you want to trace the learning arc or see breadth of topic coverage.
