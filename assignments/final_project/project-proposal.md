# Final Project Proposal

**Due:** Sunday, July 12, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** Define your capstone ML project before you build it. This is a short planning checkpoint — no code required yet. Your instructor may ask for revisions before the final project deadline.

---

## What You Submit

One file named `project-proposal.md` (or `project-proposal.pdf`) in the submission portal:

```
your_name/final_project/project-proposal.md
```

Length: **1–2 pages**. Write in clear English. Use your own words.

> See [`project-proposal-sample.md`](project-proposal-sample.md) for a worked example. Use it as a **template**, not something to copy.

---

## Required Sections

### 1. Certificate Name

- Your **full name** exactly as you want it written on your **Goobo Labs certificate**.
- Use correct spelling and capitalization (e.g. `Ahmed Hassan Mohamed`, not a nickname or username).
- This is collected once in the proposal — if you need a correction later, contact your instructor before certificates are issued.

### 2. Project Title and Description

- A clear project title.
- One paragraph: what real-world problem you are solving and who benefits from it.

### 3. Problem Type

State whether your project is:

- **Regression** (predict a number), or
- **Classification** (predict a category), or
- **Clustering** (discover groups without labels)

> **Recommendation:** Regression and classification are the easiest to deploy with a `/predict` API. If you choose clustering, explain in this section how your API will accept input and return a segment label or cluster assignment.

### 4. Dataset

- **Source:** Kaggle, UCI, OpenML, government data, or self-collected — include a **link**.
- **Size:** Must have at least **1,000 rows** (state the expected row count).
- **Target column** (if supervised): name and what it represents.
- **Main features:** list the columns you plan to use and what they mean.

### 5. Algorithms You Plan to Train

List **at least three different algorithms** you will train and compare in the final project. For each one, write one sentence on why it fits your problem.

Requirements:

- **Minimum of three** distinct algorithms — you may include more, but three is the required floor.
- At least **two algorithms from the bootcamp** (e.g. Linear/Logistic Regression, Decision Tree, Random Forest, K-Means).
- Any additional algorithms may be ones you **research on your own** (e.g. SVM, Gradient Boosting, XGBoost, DBSCAN, GMM).

All listed algorithms must be **distinct** — do not list the same algorithm twice.

### 6. Evaluation Plan

- Which **metrics** will you use to compare all your models?
- Which **single metric** will you use to pick the best model overall? Explain why that metric fits your problem.

Examples:

- Classification → Accuracy, Precision, Recall, F1; pick best by F1.
- Regression → MAE, RMSE, R²; pick best by lowest MAE or highest R².
- Clustering → Silhouette, Davies–Bouldin; pick best by highest Silhouette.

### 7. Deployment Sketch

- Will you use **Flask** or **FastAPI**?
- What will the `/predict` endpoint **accept** (JSON fields)?
- What will it **return** (prediction label, probability, cluster ID, etc.)?

### 8. Repository Plan

Describe how you will organize your GitHub repo. Example layout:

```
project-repo/
├── dataset/
├── src/
│   ├── preprocess.py
│   └── train.py
├── api/
│   └── app.py
├── models/
├── README.md
└── project_paper.md
```

Adjust folder names to fit your project — the point is to show you have thought about structure before coding.

---

## Evaluation Criteria

Your proposal will be reviewed on:

- **Certificate name provided** — Full name included for certificate printing
- **Problem clarity** — Is the problem real, specific, and feasible before the final deadline?
- **Dataset feasibility** — Is the source credible? Does it meet the 1,000-row minimum?
- **At least three distinct algorithms** — Are they appropriate for the problem type?
- **Realistic metrics** — Do metrics match regression, classification, or clustering?
- **Deployable scope** — Can this reasonably be built, evaluated, and deployed as an API?

---

## What Happens Next

- If approved, build your project following [`final-project.md`](final-project.md).
- **Final due:** Saturday, July 25, 2026 — 12:00 PM (Africa/Mogadishu / EAT).
- You may revise your dataset or algorithms in the final repo — note any changes in your README.

---
