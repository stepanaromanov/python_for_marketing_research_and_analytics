# Portfolio Environment Setup — Windows
## Marketing Analytics

---

## Step 1 — Install Anaconda

Download from https://www.anaconda.com/download  
Choose the **Windows 64-bit** installer. During install:
- ✅ "Add Anaconda to PATH" — check this
- ✅ "Register as default Python" — check this

---

## Step 2 — Create the portfolio environment

Open **Anaconda Prompt** (search in Start menu) and run:

```bash
# Clone your repo first
git clone https://github.com/stepanaromanov/python_for_marketing_research_and_analytics
cd python_for_marketing_research_and_analytics

# Create environment from file
conda env create -f environment.yml

# Activate it — do this every time you start work
conda activate marketing-portfolio

# Verify
python --version        # should say 3.12.x
jupyter lab --version   # should say 4.x
```

---

## Step 3 — Install heavy optional packages (when needed)

Install these **one project at a time** — they are large and slow:

```bash
conda activate marketing-portfolio

# PyMC — needed for Projects 03, 06, 07, 08, 10
conda install -c conda-forge pymc

# Meridian (Google MMM) — needed for Projects 03, 06, 07, 08, 09
pip install meridian

# MLflow (if pip install failed)
pip install mlflow

# DVC
pip install dvc
```

---

## Step 4 — Launch JupyterLab

```bash
conda activate marketing-portfolio
cd python_for_marketing_research_and_analytics
jupyter lab
```

This opens JupyterLab in your browser at `http://localhost:8888`

---

## Step 5 — Set up MLflow tracking server (local)

In a **second** Anaconda Prompt window:

```bash
conda activate marketing-portfolio
cd python_for_marketing_research_and_analytics
mlflow ui
```

Opens MLflow dashboard at `http://localhost:5000`  
Keep this running while you work — all experiment runs log here automatically.

---

## Step 6 — Set up DVC

```bash
conda activate marketing-portfolio
cd python_for_marketing_research_and_analytics

# Initialise DVC in your repo (one time only)
dvc init
git add .dvc .dvcignore
git commit -m "init: add DVC"

# Run a pipeline
dvc repro
```

---

## Professional Certificates Notebook

```bash
# Run the Jupyter nbconvert tool to convert 00_professional_development/certifications.ipynb notebook (professional development path) into an HTML file named certifications.html, while --no-input hides the code cells so only outputs/markdown appear.
jupyter nbconvert --to html certifications.ipynb --no-input --output certifications.html
```

---

## Recommended Windows folder structure

```
C:\Users\YourName\
  └── portfolio\
      ├── environment.yml          ← this file
      ├── requirements.txt
      ├── 00_professional_development\
      ├── 01_markov_mta\
      │   ├── 01_markov_chain_mta.ipynb
      │   ├── src\
      │   ├── data\
      │   ├── models\
      │   └── dvc.yaml
      ├── 02_shapley_attribution\
      ├── 03_meridian_mmm\
      └── ...
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `conda: command not found` | Restart terminal after Anaconda install |
| `ModuleNotFoundError: mlflow` | `pip install mlflow` inside activated env |
| JupyterLab opens wrong Python | Kernel → Change Kernel → marketing-portfolio |
| DVC `No such command` | `pip install dvc` in activated env |
| Plotly charts not showing | `pip install ipywidgets` then restart kernel |
| PyMC install fails | Use `conda install -c conda-forge pymc` not pip |
