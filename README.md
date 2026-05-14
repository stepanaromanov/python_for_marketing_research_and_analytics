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
**Project 03: Meridian Media Mix Modeling (MMM)**

**Digital + TV spend with geo-level Bayesian inference and automated retraining**

**Stack:** `meridian` · `tensorflow_probability` · `arviz` · `mlflow` · `dvc`

---

### 📋 Executive Summary

This project builds a **full Bayesian Media Mix Model** using Google's Meridian framework. It estimates true channel ROAS while accounting for **saturation (Hill function)**, **carry-over (adstock)**, **seasonality**, and **geo-level heterogeneity**.

**Key Insights:**
- **Display** is loss-making at current spend (effective ROAS 0.9×).
- **TV** is heavily saturated (87% of max response).
- **Paid Search** has the highest growth potential (Max ROAS 3.8× with significant headroom).
- Geo variation: ±18% ROAS multiplier across regions.

**Business Impact:** Recommended reallocation of **$180k** from Display to Paid Search → projected **+$43k** incremental revenue.

### What You'll Find in the Notebook

- Synthetic multi-geo panel data generation (104 weeks × 5 regions) with injected ground-truth effects.
- Full Meridian model setup: priors, hierarchical partial pooling, and posterior diagnostics (R-hat, ESS, LOO).
- Response curves, saturation analysis, and carry-over estimation.
- Budget optimizer integration using Meridian’s built-in tools.
- Production SQL template for weekly geo-level aggregation.
- MLOps: MLflow tracking, DVC pipelines, and drift detection for automated retraining.

### Skills Demonstrated

- Bayesian hierarchical modeling & MCMC diagnostics
- Media mix modeling (saturation + adstock)
- Geo-level partial pooling
- Production-grade MMM deployment
- Clear executive communication of complex Bayesian results

**Folder:** [03_meridian_mmm/](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/tree/main/03_meridian_mmm)  
**Notebook:** [03_meridian_mmm_portfolio.ipynb](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/blob/main/03_meridian_mmm/03_meridian_mmm_portfolio.ipynb)

---

**Project 04: Shapley-Based Budget Optimizer**

**MLOps-optimised budget reallocation with PuLP linear programming and canary rollout**

**Stack:** `pulp` · `mlflow` · `dvc` · `scipy` · `statsmodels`

---

### 📋 Executive Summary

This notebook takes **Shapley-attributed ROAS** as input and solves a **constrained linear program** to find the optimal budget split across channels that maximises projected revenue **without increasing total spend**.

**Optimisation Result (example):**
- +19% projected revenue lift from reallocation alone.
- Paid Search gains +$38k, Display reduced by $38k, etc.
- Hard constraints: min/max spend per channel respected.

**Key Features:**
- PuLP exact solver (<0.1s).
- Stochastic simulation using ROAS volatility.
- Executive HTML KPI card.
- Full MLflow logging + canary deployment guardrails.

### What You'll Find in the Notebook

- Shapley ROAS ingestion and validation.
- Linear programming formulation (objective + constraints).
- Sensitivity analysis and what-if scenarios.
- Production SQL for rolling 90-day ROAS calculation.
- Executive one-pager renderer + audit-ready MLflow artifacts.

### Skills Demonstrated

- Mathematical optimization (PuLP linear programming)
- Budget allocation under constraints
- Integration of attribution models into downstream optimisation
- Production MLOps serving patterns
- Stochastic simulation for risk assessment

**Folder:** [04_budget_optimizer/](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/tree/main/04_budget_optimizer)  
**Notebook:** [04_budget_optimizer.ipynb](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/blob/main/04_budget_optimizer/04_budget_optimizer.ipynb)

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
