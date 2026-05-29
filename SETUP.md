# Portfolio Environment Setup — Windows

## Marketing Analytics

---

## Step 1 — Install Anaconda

Download from <https://www.anaconda.com/download>  
Choose the **Windows 64-bit** installer. During install:

- ✅ "Add Anaconda to PATH" — check this
- ✅ "Register as default Python" — check this

---

## Step 2 — Create the portfolio environment

Open **Anaconda Prompt** (search in Start menu) and run:

```bash
# Clone the repo
git clone https://github.com/stepanaromanov/python_for_marketing_research_and_analytics
cd python_for_marketing_research_and_analytics

# Create environment from file (this takes 5–10 minutes)
conda env create -f environment.yml

# Activate — do this every time you start work
conda activate marketing-portfolio

# Verify
python --version        # should say 3.12.x
jupyter lab --version   # should say 4.x
```

> **Why conda and not pip?**  
> This portfolio uses both PyMC (PyTensor backend) and Google Meridian (TensorFlow backend).  
> Conda's dependency solver resolves these into a single working environment.  
> Running `pip install` alone will produce conflicts.

---

## Step 3 — Launch JupyterLab

```bash
conda activate marketing-portfolio
cd python_for_marketing_research_and_analytics
jupyter lab
```

Opens JupyterLab in your browser at `http://localhost:8888`

---

## Step 4 — Set up MLflow tracking server (local)

Open a **second** Anaconda Prompt window:

```bash
conda activate marketing-portfolio
cd python_for_marketing_research_and_analytics
mlflow ui
```

Opens the MLflow dashboard at `http://localhost:5000`  
Keep this running while you work — all experiment runs log here automatically.

---

## Step 5 — Professional Certificates notebook

```bash
# Convert the certifications notebook to a clean HTML file (no code cells shown)
jupyter nbconvert --to html 00_professional_development/Certifications.ipynb \
  --no-input --output Certifications.html
```

---

## Recommended folder structure

```
C:\Users\YourName\
  └── portfolio\
      ├── environment.yml
      ├── requirements.txt
      ├── 00_professional_development\
      ├── 01_markov_mta\
      │   ├── 01_markov_chain_mta.ipynb
      │   ├── src\
      │   ├── data\
      │   └── models\
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
| `ModuleNotFoundError: meridian` | `pip install google-meridian==1.6.1` inside activated env |
| JupyterLab opens wrong Python | Kernel → Change Kernel → marketing-portfolio |
| Plotly charts not showing | `pip install ipywidgets` then restart kernel |
| PyMC install fails | Use `conda install -c conda-forge pymc` — do not use pip |
| TensorFlow/Meridian conflict with PyMC | Only occurs with pip. Use conda env create as above |
| `kaleido` static export broken | Downgrade: `pip install kaleido==0.1.0` |
