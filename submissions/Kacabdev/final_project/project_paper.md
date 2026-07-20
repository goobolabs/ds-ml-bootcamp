# Phishing Website Detection API — Project Paper

**Author:** Abdurahman Aden Mohamed
**Date:** July 2026

---

## 1. Problem Statement and Motivation

Phishing websites impersonate trusted services — banks, mobile money
platforms, email providers — to trick people into handing over passwords,
card numbers, and other sensitive information. Attackers constantly
change domain names and page content to evade blocklists, but the
underlying *structure* of a phishing URL and page tends to follow
recognizable patterns: unusually long URLs, IP addresses used in place of
domain names, missing or mismatched SSL certificates, very young domains,
excessive subdomains, forms that submit to a different domain than they
were served from, and so on.

This project builds a binary classifier that looks at 30 such structural
features and predicts whether a website is `phishing` or `legitimate`,
then deploys the best-performing model behind a `POST /predict` API. A
small web frontend ("PhishGuard AI") lets a user fill in a website's
structural features through a grouped, dropdown-based form and get an
instant verdict — it does not crawl the live URL itself, it packages the
same 30 UCI-style features the model was trained on. A tool like this
could sit in front of a browser extension, an email link filter, or a
security operations dashboard as an early warning check *before* a user
ever clicks through to a site.

## 2. Dataset and Preprocessing

**Source.** The [UCI Machine Learning Repository "Phishing Websites"
dataset](https://archive.ics.uci.edu/dataset/327/phishing+websites)
(Mohammad & McCluskey, 2012), collected from PhishTank, MillerSmiles, and
Google search operators (fetched via the `ucimlrepo` package and saved to
`dataset/phishing_websites.csv`). It contains 11,055 labeled websites —
6,157 legitimate and 4,898 phishing — each described by 30 integer-coded
features plus the target column `result`. All features are encoded on a
`{-1, 0, 1}` scale, where `-1` generally signals a phishing-like trait,
`1` a legitimate-like trait, and `0` a suspicious/intermediate state for
features that aren't strictly binary (e.g. `sslfinal_state`,
`url_of_anchor`, `having_sub_domain`).

**Feature groups.** The 30 features fall into four broad categories:
address-bar-based (e.g. `having_ip_address`, `url_length`,
`having_at_symbol`, `prefix_suffix`), abnormal-based (`request_url`,
`url_of_anchor`, `sfh`, `abnormal_url`), HTML/JavaScript-based
(`redirect`, `on_mouseover`, `popupwindow`, `iframe`), and domain-based
(`age_of_domain`, `dnsrecord`, `web_traffic`, `page_rank`,
`google_index`).

**Cleaning and preprocessing pipeline** (`backend/src/preprocess.py`),
implemented in code rather than described only in prose:

1. Load the CSV and check for missing values — none found, the dataset
   ships fully pre-encoded with no nulls.
2. Check for duplicate rows — **5,206 of the 11,055 rows (about 47%) were
   exact duplicates** and were dropped before splitting, leaving 5,849
   unique rows. This was caught by an explicit `duplicated()` check before
   the split rather than assumed away; skipping it would have let
   near-identical rows land on both sides of the train/test split and
   inflate the reported metrics.
3. Confirm every remaining column's values fall within `{-1, 0, 1}` —
   raises an error otherwise, rather than silently trusting the source
   file.
4. Recode the target from the dataset's native `{-1 = phishing, 1 =
   legitimate}` to the more conventional `{1 = phishing, 0 = legitimate}`
   so precision/recall/F1 read the way "catching phishing" implies.
5. Stratified 80/20 train/test split (`random_state=42`) on the
   deduplicated data — 4,679 train rows (~51.6% phishing / 48.4%
   legitimate) and 1,170 test rows (604 phishing / 566 legitimate).
6. Fit a `StandardScaler` on the training features only, then transform
   both train and test — this benefits Logistic Regression the most and
   is harmless for the tree-based models.

## 3. Algorithms

Three algorithms were trained on the identical scaled train/test split
(`backend/src/train.py`) so the comparison in Section 4 is fair.

**Logistic Regression** (bootcamp). A linear model that estimates the
log-odds of "phishing" as a weighted sum of the 30 features. Chosen as
the baseline: with mostly small-integer categorical-style features, a
linear decision boundary is fast to train, easy to interpret via its
coefficients, and a reasonable first guess for whether the relationship
between features and label is close to linear.

**Random Forest** (bootcamp). An ensemble of decision trees, each trained
on a bootstrap sample with a random subset of features considered at each
split, with predictions combined by majority vote. Chosen because it
naturally handles the mix of binary (`{-1,1}`) and ternary (`{-1,0,1}`)
categorical-style features without needing one-hot encoding, captures
non-linear interactions (e.g. "long URL *and* no HTTPS" being riskier
than either alone), and exposes feature importances that are useful for
understanding which URL characteristics matter most.

**XGBoost** (independently researched). Gradient-boosted decision trees
built sequentially, where each new tree focuses on correcting the errors
of the previous ensemble, regularized to reduce overfitting. Chosen
because gradient-boosted trees are widely reported as strong or
state-of-the-art performers in phishing- and fraud-detection literature,
and were a natural fourth-hour research target beyond what the bootcamp
covered directly (studied via the XGBoost documentation and
introductory tutorials).

All three use `random_state=42` for reproducibility. Hyperparameters were
kept close to sensible defaults (Random Forest and XGBoost both use 300
trees, Logistic Regression uses `max_iter=1000`) rather than exhaustively
tuned, since the project's emphasis was on a correct, fair, end-to-end
comparison rather than squeezing out the last percentage point of
accuracy.

## 4. Results and Discussion

Comparison table produced by `backend/src/train.py` (also saved to
`backend/models/comparison_table.csv`), on the real, deduplicated UCI
dataset described in Section 2:

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| **XGBoost** | **0.9479** | **0.9594** | **0.9387** | **0.9490** |
| Random Forest | 0.9402 | 0.9572 | 0.9255 | 0.9411 |
| Logistic Regression | 0.9179 | 0.9247 | 0.9156 | 0.9201 |

**Best-model rule.** Models are ranked by F1-Score, with Recall as a
tiebreaker if two models land close together. In phishing detection,
missing an actual phishing site (low recall) directly puts a user at
risk, while wrongly flagging a legitimate site (low precision) mainly
costs user trust in the tool — a real but generally less severe failure
mode. F1 balances both concerns instead of over-favoring one, and the
Recall tiebreaker reflects that letting a phishing site through is the
costlier mistake when two models are otherwise close.

**Winner: XGBoost**, with the highest F1-Score (0.9490) and also the
highest Accuracy, Precision, and Recall of the three — it wins outright
on every metric, no tiebreaker needed. Its confusion matrix on the test
set (rows = actual, columns = predicted, order `[legitimate, phishing]`):

```
[[542  24]
 [ 37 567]]
```

i.e. of 566 actual legitimate sites, 542 were correctly passed through
and 24 were incorrectly flagged as phishing; of 604 actual phishing
sites, 567 were caught and only 37 were missed.

**Sanity checks.** `train.py` runs 3 sample predictions from the held-out
test set through the winning model and prints the input features, actual
label, predicted label, and predicted class probability for each. All
three sampled rows were predicted correctly, two with near-zero phishing
probability (0.0001, 0.0009 — confidently legitimate) and one with 0.9985
phishing probability (confidently phishing) — the model is not just
correct but decisively confident on these samples.

**Discussion.** On the real, deduplicated dataset, the gradient-boosted
model outperforms both the linear model and the bagged-tree ensemble on
every metric, with Random Forest a close second and Logistic Regression
clearly behind. This lines up with what the phishing-detection literature
generally reports (e.g. Georgetown Analytics' coefficient analysis:
`sslfinal_state` and `url_of_anchor` are consistently the two strongest
single predictors) — real feature interactions in this dataset are
non-linear enough that boosting's sequential error-correction gives it a
real edge over a single linear boundary. Random Forest remains valuable
even though it didn't win: its feature importances corroborate XGBoost's
and give a second, more interpretable signal for which URL
characteristics deserve the most scrutiny in a real deployment.

## 5. Deployment Notes

The winning model (XGBoost) and its `StandardScaler` are serialized with
`joblib` to `backend/models/best_model.pkl` and
`backend/models/scaler.pkl`; `backend/models/feature_columns.json`
records the exact feature order the scaler expects, and
`backend/models/model_info.json` records which algorithm won and its
metrics, so the API can report them back to the caller.

**Framework:** FastAPI (`backend/api/app.py`), served with `uvicorn`.

**Endpoint:** `POST /predict`, accepting a JSON body with all 30 feature
values — validated with a Pydantic model constraining every field to
`{-1, 0, 1}`, so out-of-range values are rejected with a clear 422 error
— and returning the predicted label and both class probabilities:

```json
// request (excerpt)
{"having_ip_address": -1, "url_length": 1, "sslfinal_state": -1, "...": "..."}

// response
{"prediction": "phishing", "phishing_probability": 0.91, "legitimate_probability": 0.09, "model": "XGBoost"}
```

Internally, `/predict` orders the incoming JSON fields to match
`feature_columns.json`, applies the same `StandardScaler` fitted during
training, and calls `model.predict_proba`. A `GET /health` route reports
which model is currently loaded and its training metrics.
`CORSMiddleware` is configured with `allow_origins=["*"]` so the frontend
can call the API from a different origin.

**Split deployment.** The backend (FastAPI + model) is deployed to
**Render** as its own service. The frontend — `index.html`, `style.css`,
and `script.js` at the repo root, a plain HTML/CSS/vanilla-JS form
grouping the 30 features into the four categories from Section 2, with
quick-fill "load phishing example" / "load legitimate example" buttons
and a dark-mode toggle — is deployed separately to **GitHub Pages**
(served straight from the `main` branch root, no build step). Because the
two live on different origins, `script.js` calls the API through an
explicit `API_BASE_URL` constant pointed at the Render service URL rather
than a same-origin relative path.

## 6. Lessons Learned

The dataset held a real data-quality trap: 47% of the raw rows were exact
duplicates. Left undetected, some of those duplicates would have landed
on both sides of the train/test split, letting the model "memorize" test
rows it had technically already seen in training and inflating every
reported metric. Checking `df.duplicated().sum()` and dropping before the
split — rather than assuming a published academic dataset is
split-ready — is now a standing habit for any tabular dataset going
forward.

On the modeling side, choosing F1 with a Recall tiebreaker *before*
looking at results avoided the temptation to justify whichever model
happened to "look best" after the fact. It also turned out to be a moot
point here: XGBoost won on every single metric, not just F1, so there was
no close call to break. Random Forest and XGBoost weren't wasted effort
even so — their feature-importance rankings corroborate each other and
give an interpretable signal for which URL characteristics matter most,
which the linear model's coefficients alone don't surface as clearly.

Splitting the deployment across two hosts (Render for the API, GitHub
Pages for the static frontend) surfaced a cross-origin lesson: a frontend
that calls its API via a same-origin relative path (`fetch("/predict")`)
silently breaks the moment the two are hosted separately, since the
request goes to the frontend's own origin instead of the API. Keeping the
API base URL as one explicit constant in `script.js`, backed by a
permissive CORS policy on the FastAPI side, made the two-host setup a
one-line change instead of a rewrite.

If extended further, the next steps would be: (1) add a small calibration
check (e.g. a reliability diagram) since the API returns a probability
that downstream systems may threshold on; (2) tune XGBoost and Random
Forest's hyperparameters now that a fair baseline comparison exists,
rather than relying on near-default settings; and (3) fix
`backend/src/preprocess.py` and `backend/src/train.py`'s relative paths
(`./dataset/...`, `models`), which still assume the pre-restructuring flat
layout — run from the repo root today, they'd read the dataset correctly
but write a fresh `models/` at the repo root instead of into
`backend/models` where `app.py` actually looks, so a rerun currently needs
a manual move of the output folder into place.


# project Repo ⬇

https://github.com/Kacabdev/pishing-detection-api2