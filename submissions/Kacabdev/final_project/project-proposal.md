# Final Project Proposal

**Date:** July 2026

---

## 1. Certificate Name

**Abdurahman Aden Mohamed**

---

## 2. Project Title and Description

**Title:** Phishing Website Detection API

Phishing websites trick people into handing over passwords, card numbers, and other personal details by imitating trusted sites like banks or mobile money platforms. Attackers keep changing domain names and page content, but the underlying structure of a phishing URL, things like its length, whether it hides behind an IP address, or how it uses subdomains, tends to follow recognizable patterns. This project builds a model that looks at those structural features of a website and predicts whether it is phishing or legitimate. A browser extension, an email filter, or a security team could use an API like this as an early warning check before a user ever clicks through.

---

## 3. Problem Type

**Classification**: the target is binary, a website is either `phishing` or `legitimate`.

This is supervised learning. The dataset already contains websites that have been manually verified and labeled by security researchers, so the model learns from those confirmed examples.

---

## 4. Dataset

- **Source:** [Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing+websites) (UCI Machine Learning Repository, also mirrored on Kaggle).
- **Size:** the original dataset has 11,055 rows and 32 features. I'll work with a random sample of about **3,000 rows** to keep training and iteration fast, which is still well above the 1,000-row minimum.
- **Target column:** `Result`, whether the website is phishing or legitimate.
- **Main features:**
  - `having_IP_Address`: whether the URL uses a raw IP address instead of a domain name
  - `URL_Length`: whether the URL is unusually long
  - `Shortining_Service`: whether a URL-shortening service was used
  - `having_At_Symbol`: whether the URL contains an `@` symbol
  - `SSLfinal_State`: the state of the site's SSL certificate
  - `having_Sub_Domain`: how many subdomains the URL has
  - `Domain_registeration_length`: how long the domain has been registered for
  - `age_of_domain` and `web_traffic`: how established and how visited the site is

Most features in this dataset are already encoded as small numeric categories (for example -1, 0, 1), which makes it a clean fit for classic classification models.

**Preprocessing plan:** draw a stratified random sample of about 3,000 rows from the original 11,055 so the phishing-to-legitimate ratio stays the same as the full dataset, check for and handle any missing values, confirm all features are in a consistent numeric encoding, scale where needed, and split the sample into an 80/20 train/test set, stratified on `Result`.

---

## 5. Algorithms I Plan to Train

| # | Algorithm | Why it fits |
| --- | --- | --- |
| 1 | **Logistic Regression** | Bootcamp baseline for binary classification. With mostly categorical-style features already encoded numerically, it gives a fast, interpretable starting point. |
| 2 | **Random Forest** | Bootcamp ensemble method. Handles the mix of binary and multi-valued categorical features well, and can highlight which URL characteristics matter most for detecting phishing. |
| 3 | **XGBoost** | I'll research this one on my own. Gradient-boosted trees are widely used in phishing and fraud detection work and are a strong candidate for the best-performing model here. |

That covers the minimum of three. Two come from the bootcamp lessons, and XGBoost is the one I'll dig into through its documentation and a tutorial or two. I may add an SVM as a fourth if time allows.

---

## 6. Evaluation Plan

**Metrics for all three models, measured on the same held-out test set:**

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Best-model rule:** I'll rank the models by **F1-Score**. In phishing detection, missing an actual phishing site (low recall) puts a user at risk, while wrongly flagging a legitimate site (low precision) damages trust in the tool. F1 balances both concerns instead of favoring one. If two models land close on F1, I'll use Recall as the tiebreaker, since letting a phishing site through is generally the more costly mistake.

---

## 7. Deployment Sketch

- **Framework:** FastAPI.
- **Endpoint:** `POST /predict`
- **Input JSON example:**

```json
{
  "having_IP_Address": -1,
  "URL_Length": 1,
  "Shortining_Service": -1,
  "having_At_Symbol": 1,
  "SSLfinal_State": -1,
  "having_Sub_Domain": 0,
  "Domain_registeration_length": -1,
  "age_of_domain": -1,
  "web_traffic": 0
}
```

- **Output JSON example:**

```json
{
  "prediction": "phishing",
  "probability": 0.91
}
```

The API loads the winning model from `models/best_model.pkl`, along with any fitted scaler, so incoming JSON gets preprocessed the same way the training data was before a prediction is returned.

---

## 8. Repository Plan

```
phishing-detection-api/
├── dataset/
│   └── phishing_websites.csv
├── src/
│   ├── preprocess.py      # cleaning, scaling, train/test split
│   └── train.py           # trains all three models, prints comparison table, saves best
├── api/
│   └── app.py              # FastAPI app with /predict
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
├── README.md
├── requirements.txt
└── project_paper.md
```

**Planned run commands:**

```bash
python src/train.py
uvicorn api.app:app --reload
```

---
