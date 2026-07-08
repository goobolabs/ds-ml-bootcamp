# Final Project — Capstone Assignments

This folder holds the **bootcamp capstone**: your own ML project from problem definition through model comparison to API deployment. Unlike Assignments 1–6, you choose the dataset, problem, and algorithms.

---

## Files in This Folder

| File | Purpose |
| --- | --- |
| [`project-proposal.md`](project-proposal.md) | **Proposal assignment** — what to submit first (plan only, no code) |
| [`project-proposal-sample.md`](project-proposal-sample.md) | Worked example proposal (Loan Approval API) — use as a template, do not copy |
| [`final-project.md`](final-project.md) | **Final capstone assignment** — full repo, API, paper, and portal submission |

---

## Timeline

| Milestone | Due |
| --- | --- |
| Project proposal | Sunday, **July 12, 2026** — 12:00 PM (Africa/Mogadishu / EAT) |
| Final project | Saturday, **July 25, 2026** — 12:00 PM (Africa/Mogadishu / EAT) |

**Workflow:**

1. Read [`project-proposal.md`](project-proposal.md) and submit your plan (including your **certificate name**) by July 12.
2. Build your project on **your GitHub account** following [`final-project.md`](final-project.md).
3. By July 25, submit your portal folder (see **Portal folder structure** below). All code stays on GitHub.

---

## Portal Folder Structure

In the submission portal, create this folder:

```
your_name/final_project/
├── project-proposal.md      # required
├── project_paper.md         # required (or project_paper.pdf)
└── README.md                # optional
```

| File | Required? | What it is |
| --- | --- | --- |
| `project-proposal.md` | **Yes** | Your approved project plan (certificate name, dataset, algorithms, etc.). Submit by **July 12**; keep the same file in the folder for the final submission. |
| `project_paper.md` | **Yes** | Your 3–5 page report (Markdown or PDF). Same content as the paper in your GitHub repo — upload a copy here for grading. |
| `README.md` | Optional | Short summary of your project + **link to your GitHub repo**. Recommended if you want a quick cover page for instructors. |

**GitHub (required):** Your full project — code, API, trained models, and repo README — must live on **your own GitHub account**. Do not upload code, notebooks, or datasets to the portal.

---

## Dataset Requirements

Your dataset must have at least **1,000 rows**. Document the source in your proposal and repo README.

Pick a dataset that fits a clear ML problem:

- **Classification** — predict a category (e.g. loan approved yes/no, disease present)
- **Regression** — predict a number (e.g. house price, sales amount)
- **Clustering** — discover groups without labels (e.g. customer segments)

> Supervised projects (regression or classification) are the easiest to deploy with a `/predict` API. If you choose clustering, explain how your API will assign new rows to a segment.

---

## Where to Find Datasets

### General repositories

| Source | Link | Notes |
| --- | --- | --- |
| **Kaggle** | [kaggle.com/datasets](https://www.kaggle.com/datasets) | Large catalog; filter by task type and size. Free account required to download. |
| **UCI ML Repository** | [archive.ics.uci.edu/ml](https://archive.ics.uci.edu/ml) | Classic academic datasets; good documentation. |
| **OpenML** | [openml.org](https://www.openml.org/) | Search by task, size, and features; integrates with scikit-learn. |
| **Google Dataset Search** | [datasetsearch.research.google.com](https://datasetsearch.research.google.com/) | Meta-search across many public datasets. |
| **data.gov** | [data.gov](https://data.gov/) | US government open data (also useful for methodology examples). |
| **World Bank Open Data** | [data.worldbank.org](https://data.worldbank.org/) | Global economic and development indicators. |

### Bootcamp-adjacent examples (do not reuse as-is — choose your own project)

These are similar in style to what we covered in class. Use them for **inspiration**, not as your final dataset unless you extend the problem significantly:

- Housing / price prediction (Lesson 4 — regression)
- Loan approval (Lesson 5 — classification)
- Wholesale customers (Lesson 6 — clustering)

---

## Choosing a Good Dataset

- **Size:** At least 1,000 rows — check before you commit in your proposal.
- **License:** Confirm you may use it for a student project (Kaggle and UCI usually allow this; read each dataset’s license).
- **Missing data:** Some missing values are fine — you will handle them in preprocessing.
- **Features:** Prefer tabular data with a mix of numeric and categorical columns — matches what you practiced in Lessons 3–6.
- **Target column:** For supervised learning, make sure the label is clear and documented.

---

## Algorithms (Reminder)

- Train **at least three** distinct algorithms.
- At least **two** from the bootcamp (e.g. Logistic Regression, Random Forest, K-Means).
- Compare on the same train/test split; pick the **best overall** model and deploy that one.

See [`final-project.md`](final-project.md) for full requirements.

---

## How to Submit the Final Project

1. **GitHub** — Host the full project on **your own GitHub account** (code, API, models, repo README).
2. **Portal** — Upload the files in `your_name/final_project/`:
   - `project-proposal.md` — required
   - `project_paper.md` (or `.pdf`) — required
   - `README.md` — optional (project summary + GitHub link)

Do not upload code or datasets to the portal.

---

## Deployment and Documentation Resources

| Topic | Resource |
| --- | --- |
| **FastAPI** | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| **Flask** | [flask.palletsprojects.com](https://flask.palletsprojects.com/) |
| **scikit-learn** | [scikit-learn.org/stable/documentation.html](https://scikit-learn.org/stable/documentation.html) |
| **Saving models** | [scikit-learn model persistence](https://scikit-learn.org/stable/model_persistence.html) (`joblib` / `pickle`) |
| **Testing APIs with curl** | [curl.se/docs/manual.html](https://curl.se/docs/manual.html) |

Lesson 7 covers deployment concepts at a high level. Your final project applies them in your own repo.

---

## Questions?

- Proposal scope or dataset choice → ask **before** July 12.
- Technical blockers during build → use class channel; document what you tried in your paper’s *Lessons learned* section.

---

*Goobo Labs DS/ML Bootcamp — Final capstone folder*
