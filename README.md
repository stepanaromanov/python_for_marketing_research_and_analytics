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

**Project 05: Full Multi-Touch Attribution Engine**

**Comprehensive comparison of 8 attribution models with ground-truth validation and production MLOps**

**Stack:** `networkx` · `numpy` · `pandas` · `plotly` · `mlflow` · `dvc`

---

### 📋 Executive Summary

A complete **multi-touch attribution comparison suite** evaluating 8 models (Markov Removal, Exact Shapley, MC Shapley, Hybrid, Time-Decay, Last-Touch, First-Touch, Linear) on 50,000 synthetic customer journeys with injected causal effects.

**Key Result:** Markov Removal model achieves the highest accuracy (MAE **0.003**) against ground truth, significantly outperforming traditional heuristic models.

### 🎯 Business Impact

* **Model ranking validated** against known causal contributions (injected λ effects)
* Identifies clear biases in common models (e.g., Last-Touch heavily over-credits bottom-funnel channels)
* Provides production-ready implementations suitable for real marketing event data
* Includes MLOps practices for scalable, monitored attribution pipelines

### What You'll Find in the Notebook

* **Synthetic data generation** with realistic journey patterns and controllable causal effects
* **Implementation of 8 attribution models** from scratch:
  * Markov Chain (removal effect via fundamental matrix)
  * Exact & Monte Carlo Shapley Value
  * Time-Decay (with λ recovery via OLS)
  * Hybrid Markov-Shapley
  * Classic heuristics (Last/First/Linear)
* **Comprehensive validation** — 90+ sanity checks and statistical tests
* **Advanced extensions**: Online incremental transition matrix updates, CLV decomposition
* **Production SQL** templates for journey aggregation
* **MLOps stack**: DVC pipelines, MLflow tracking, Docker, GitHub Actions CI/CD with drift detection
* Rich interactive Plotly visualizations and performance comparisons

### Skills Demonstrated

* Advanced attribution modeling (Markov chains, Shapley values, hybrid approaches)
* Causal inference & ground-truth validation techniques
* Linear algebra & probabilistic modeling (`networkx`, fundamental matrix)
* Time-decay parameter recovery using OLS
* Production MLOps (DVC + MLflow + CI/CD)
* Comprehensive model evaluation frameworks and sanity testing
* Clear technical + executive communication

**Folder:** [05_multi_touch_attribution_engine/](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/tree/main/05_multi_touch_attribution_engine)

**Notebook:** [5_multi_touch_attribution_engine.ipynb](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/blob/main/05_multi_touch_attribution_engine/5_multi_touch_attribution_engine.ipynb)

---

**Project 06: PyMC MMM with External Regressors**

**Bayesian MMM isolating media effects from macroeconomic and competitive confounders, with parameter-recovery validation and automated retraining**

**Stack:** `pymc` · `arviz` · `scikit-learn` · `plotly` · `mlflow` · `dvc` · `numpy`


---

### 📋 Executive Summary

This project builds a **native PyMC Media Mix Model** that augments standard media variables (**adstock** carry-over + **Hill saturation**) with **external control regressors** — competitor TV pressure, CPI, interest-rate delta, and holidays — so that estimated media ROAS is not contaminated by macroeconomic or competitive swings. The model is fully Bayesian (PyMC 6 / NUTS) and is validated by recovering injected ground-truth coefficients.

**Key Insights:**
- External controls absorb variance that naive models misattribute to paid media, materially shifting estimated channel effects.
- **Sensitivity analysis** (perturbing each driver in real business units) quantifies how sales respond to competitor activity, inflation, and rate moves.
- **Parameter recovery** confirms the sampler reconstructs known media *and* external-regressor coefficients, establishing trust in the inference.

### 🎯 Business Impact

- Produces **defensible ROAS estimates** by separating true media incrementality from confounding macro/competitive effects.
- Enables **scenario stress-testing** of media plans against CPI shifts, rate changes, and competitor spend.
- Posterior **ROAS confidence intervals** give decision-makers uncertainty bounds, not just point estimates.

### What You'll Find in the Notebook

- **Synthetic weekly data generation** with adstock/saturation media transforms and injected ground-truth betas for both media and external regressors.
- **Model ladder for comparison**: naive OLS → adstock-only Ridge → full Bayesian PyMC with controls and Fourier seasonality.
- **PyMC 6 model**: HalfNormal media priors, Normal external/Fourier priors, standardized target, NUTS sampling.
- **MCMC convergence diagnostics** (R-hat, ESS) via `arviz-stats`; PPC, rank, and trace plots via `arviz-plots` (new split-arviz stack alongside Meridian's legacy shim).
- **Parameter-recovery validation** — estimated vs. ground-truth coefficients in raw business units.
- **Sensitivity analysis** perturbing external regressors in real units (competitor TV, CPI, rate delta).
- **Posterior ROAS intervals** via leave-one-channel-out on posterior draws.
- **Backtesting, drift detection, and Shapley-style decomposition** plus production MLOps blocks.
- **Production SQL template** for weekly feature aggregation.

### Skills Demonstrated

- Bayesian media mix modeling in native PyMC (adstock + Hill saturation)
- Control-variable / confounder adjustment with macroeconomic and competitive regressors
- MCMC diagnostics on the modern split-arviz stack (`arviz-base`/`stats`/`plots`)
- Parameter recovery & sensitivity analysis in business units
- Posterior uncertainty quantification for ROAS
- Production MLOps (MLflow + DVC) and reproducible experimentation

**Folder:** [06_pymc_external_regressors/](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/tree/main/06_pymc_external_regressors)

**Notebook:** [06_pymc_external_regressors.ipynb](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/blob/main/06_pymc_external_regressors/06_pymc_external_regressors.ipynb)

---

**Project 07: Customer Segmentation with Causal Uplift Validation**

**Discovering customer segments and proving which ones actually respond to discounts — pairing K-means with a Double-ML causal forest, parameter-recovery checks, and budget-constrained targeting**

**Stack:** `scikit-learn` · `econml` · `dowhy` · `shap` · `umap-learn` · `cvxpy` · `evidently` · `mlflow` · `dvc` · `plotly`

---

### 📋 Executive Summary

This project segments **200,000 customers** on RFM + behavioral features, then uses a **CausalForestDML (Double ML)** model to estimate each segment's true response to a discount — separating genuine promotional incrementality from mere spending level. The segmentation is validated against injected ground-truth labels, and the causal estimates are validated by **recovering known per-segment treatment effects**, including a *negative* one. The result is a targeting policy that earns more incremental revenue than discounting the whole base.

**Key Insights:**
- **All four cluster-validity metrics agree.** The elbow, silhouette, Calinski-Harabasz, and Davies-Bouldin scores unanimously select K=4, and the discovered segments match the injected ground truth at **ARI = 0.98** — the structure is real, not imposed.
- **Discounting loyal big-spenders backfires.** The causal forest recovers a **negative** uplift for high-value loyalists (estimated −14.5% vs injected −15%): they would have purchased anyway, so the coupon only gives away margin.
- **Precision targeting beats blanket discounting.** Because of that one value-destroying segment, targeting only the positive-uplift segments earns more incremental revenue than treating everyone (**USD 19.4M vs 16.8M**), and the budget optimizer correctly sends **~0 spend** to the cannibalizing loyalists.

### 🎯 Business Impact

- Routes discount budget to the customers whose **behavior actually changes**, not just the highest spenders.
- Flags **value-destroying over-discounting** of loyal customers — a common, expensive blind spot.
- **Confidence intervals** on segment-level effects give decision-makers uncertainty bounds, not just point estimates.

### What You'll Find in the Notebook

- **Synthetic 200k-customer DGP** with injected per-segment ground-truth CATEs, soft (Dirichlet) membership, heavy-tailed noise, MAR/MCAR missingness, promo fatigue, and cohort drift.
- **Optimal-K selection** via elbow + silhouette + Calinski-Harabasz + Davies-Bouldin, validated against ground-truth labels (ARI).
- **CausalForestDML** per-customer CATE estimation with a decoupled confounder set; **LinearDML** for influence-function variance.
- **DoWhy DAG identification** (backdoor criterion) with three refutation tests, plus **E-value** sensitivity to unmeasured confounding.
- **Four-approach CATE-recovery comparison** (naive ATE → K-means means → raw forest → hybrid) scored by MAE.
- **Counterfactual targeting policy** and a **CVXPY budget-constrained allocation LP**.
- **T-Learner vs causal-forest uplift baseline** scored by Qini / AUUC.
- IPW balance diagnostics, ANOVA heterogeneity test (η² = 0.91), three CI methods (IF, delta, Politis–Romano).
- **SHAP** feature attribution, **UMAP / t-SNE** projections, holdout backtesting.
- **Evidently** feature + CATE drift monitoring, plus production MLOps (MLflow, DVC, CI/CD heterogeneity gate).
- **Production SQL template** for RFM + behavioral feature aggregation.

### Skills Demonstrated

- Unsupervised segmentation with rigorous K-selection and ground-truth validation (ARI)
- Heterogeneous treatment-effect estimation with Double ML (EconML `CausalForestDML` / `LinearDML`)
- Causal identification and refutation (DoWhy), sensitivity analysis (E-values)
- Cannibalization / negative-uplift detection and budget-constrained targeting (CVXPY)
- Uplift-model evaluation (Qini / AUUC), IPW balancing, posterior uncertainty quantification
- Production MLOps (MLflow + DVC), drift monitoring (Evidently), reproducible experimentation

**Folder:** [07_customer_segmentation_causal/](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/tree/main/07_customer_segmentation_causal)

**Notebook:** [07_customer_segmentation_causal.ipynb](https://github.com/stepanaromanov/python_for_marketing_research_and_analytics/blob/main/07_customer_segmentation_causal/07_customer_segmentation_causal.ipynb)


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
