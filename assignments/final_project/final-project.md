# Final Project — ML Model Development and Deployment

**Due:** Saturday, July 25, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** Build a complete ML project of your own choice — from dataset preparation, through training and comparing **at least three algorithms**, to deploying the **best model** as an API. This is your capstone: you choose the problem, dataset, and approach.

> You should have submitted an approved [`project-proposal.md`](project-proposal.md) by July 12, 2026. You may revise your dataset or algorithms in the final repo — note any changes in your README.

---

## Overview

This assignment tests your ability to:

- Define a real ML problem
- Collect and process data
- Train and compare **at least three different algorithms**
- Select the **best overall model** with clear justification
- Deploy a working API
- Document your work professionally

---

## Part A — Practical Project (GitHub Repository)

### Objective

Build a complete ML project in your own GitHub repository — from raw data to a deployed `/predict` endpoint using your **best-performing model**.

---

### Instructions

#### 1. Project Setup

- Create a **GitHub repository** for your project (public or private — ensure your instructor can access it).
- Organize code into logical folders, for example: `dataset/`, `src/`, `api/`, `models/`.
- Use meaningful commit messages throughout development.

#### 2. Dataset

- Use a dataset with at least **1,000 samples**.
- Document where you got the dataset (Kaggle, UCI, OpenML, self-collected, etc.) with a link in your README.
- Implement preprocessing in code (cleaning, imputation, encoding, scaling, etc.) — not just described in the paper.

#### 3. Algorithms (At Least Three)

Train **at least three different algorithms** on the same prepared data. These should match your approved proposal (or note any changes in the README). You may train more than three — three is the required minimum.

Requirements:

- All trained algorithms must be **distinct**.
- At least **two** should come from the bootcamp (e.g. Linear/Logistic Regression, Decision Tree, Random Forest, K-Means).
- Any additional algorithms may be ones you researched independently (e.g. SVM, Gradient Boosting, XGBoost, DBSCAN, GMM).
- Use the **same train/test split** (or the same cross-validation strategy) for every model — so the comparison is fair.

For each model, record relevant metrics. Print a **comparison table** with one row per algorithm:

| Algorithm | Metric 1 | Metric 2 | Metric 3 | ... |
| --- | --- | --- | --- | --- |
| Model A | ... | ... | ... | ... |
| Model B | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

**Select the best overall model** using a rule you defined in your proposal (e.g. highest F1, lowest MAE, highest Silhouette). State the rule in your README and paper and explain **why** that metric fits your problem.

- Save and deploy **only the best model** (+ scaler, encoders, or other artifacts needed at inference time).
- Do not deploy a model that was not the winner unless you explain why in the README.

#### 4. Model Evaluation

- Show evaluation results for **every model you trained** in your comparison table.
- Run at least **3 sanity checks** on the **best model** — sample inputs with their predictions printed or logged (show the input features and the model output).
- Include appropriate metrics for your problem type:
  - **Classification:** Accuracy, Precision, Recall, F1, Confusion Matrix
  - **Regression:** MAE, RMSE, R²
  - **Clustering:** Silhouette Score, Davies–Bouldin Index, cluster center interpretation

#### 5. Deployment

- Expose your **best trained model** as an API using **Flask** or **FastAPI**.
- Endpoint **`/predict`** must accept **JSON input** and return **JSON predictions**.
- The API must run locally and respond correctly when tested.

**Optional (extra credit):** Add a simple frontend (HTML form or Streamlit) that calls your API.

Example `curl` test (adjust fields to your project):

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"feature1": 100, "feature2": "Urban", "feature3": 1}'
```

#### 6. Documentation — README.md

Your repo must include a `README.md` with:

- Project title and description
- Dataset details (source, size, link)
- All **algorithms** used (minimum of three)
- Comparison table summary and **which model won**
- Example commands (`python src/train.py`, `uvicorn api.app:app --reload`, etc.)
- Example API usage with `curl`
- Results summary (2–3 sentences on findings)

#### 7. Project Paper

Include `project_paper.md` or `project_paper.pdf` in your repo.

**Length:** 3–5 pages.

**Required sections:**

1. **Problem statement and motivation** — What problem did you solve? Why does it matter?
2. **Dataset and preprocessing** — Source, size, features, cleaning steps.
3. **Algorithms** — Every model you trained (at least three): how each works and why you chose it.
4. **Results and discussion** — Comparison table, sanity checks, which model performed best and why.
5. **Deployment notes** — How the API works; example request and response; frontend if included.
6. **Lessons learned** — Challenges faced, what you would improve, key takeaways.

---

## Part B — Submission (Portal + GitHub)

You submit in **two places**: required files in the portal folder below, and the **full project on your GitHub**.

### 1. GitHub repository (required)

Your complete project must live in a **GitHub repository on your own GitHub account**.

- Create the repo under **your** username (not a zip file, not Google Drive, not a fork of the bootcamp repo).
- Ensure your instructor can access it (public repo, or private repo with instructor invited).
- The repo must contain everything: code, trained model artifacts, API, `project_paper.md` (or PDF), and a **repo `README.md`** with setup instructions, results, and how to run the API.

Example repo URL format:

```
https://github.com/your-username/your-project-name
```

### 2. Portal submission (required)

In the submission portal, create a folder with your own name:

```
your_name/final_project/
├── project-proposal.md      # required
├── project_paper.md         # required (or project_paper.pdf)
└── README.md                # optional
```

| File | Required? | Notes |
| --- | --- | --- |
| `project-proposal.md` | **Yes** | Your project proposal (submitted by July 12; same file stays in the folder for the final deadline). |
| `project_paper.md` | **Yes** | Your 3–5 page report (Markdown or PDF). Upload a copy here — also keep it in your GitHub repo. |
| `README.md` | Optional | Project title, short description, and **link to your GitHub repo**. Recommended but not required. |

Example optional portal `README.md`:

```markdown
# House Price Prediction API

This project predicts house prices from property features using regression.
I trained and compared three models and deployed the best one as a FastAPI service.

**Repository:** https://github.com/ahmed/house-price-api
```

> Do **not** upload code, notebooks, or datasets to the portal. Those live **only** in your GitHub repo. If the repo link is broken or the repo is empty, the submission is incomplete.

---

## Expected Output

A working GitHub repository containing:

- Training and inference code
- All trained models compared (minimum of three)
- Best model saved and deployed via API
- `README.md` with setup and usage instructions
- `project_paper.md` or `project_paper.pdf`

The API must run locally and respond correctly to `/predict`.

---

## Evaluation Criteria

| Criterion | What we look for |
| --- | --- |
| Problem choice and definition | Clear, realistic, well-motivated |
| Data cleaning and preprocessing | Reproducible pipeline in code |
| At least three algorithms trained and compared | Minimum of three required — same split, fair comparison |
| Best model selection | Justified with metrics; winner deployed |
| Model evaluation and sanity checks | Metrics + at least 3 sample predictions on best model |
| Working API deployment | `/predict` accepts JSON, returns JSON, runs locally |
| Documentation | README + 3–5 page paper |
| Code quality and commit history | Organized repo, logical commits |

---

## Tips

- Start from your approved proposal — do not change scope drastically without noting it in the README.
- Train all your models in one script or notebook section so the comparison table is easy to reproduce.
- Test your API with `curl` or Postman before submitting — a broken `/predict` endpoint is the most common failure.
- Supervised projects (regression/classification) are the most straightforward for API deployment. If you chose clustering, make sure `/predict` returns a meaningful segment label for new input rows.

---

## Timeline

| Milestone | Due |
| --- | --- |
| Project proposal | Sunday, July 12, 2026 — 12:00 PM EAT |
| Final project (portal folder + GitHub repo) | Saturday, July 25, 2026 — 12:00 PM EAT |

---
