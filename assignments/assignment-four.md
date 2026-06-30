# Assignment Four: Regression — Theory and Practice

**Due:** Tuesday, June 30, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal:** Demonstrate understanding of regression concepts in Machine Learning and apply them by building and comparing Linear Regression and Random Forest models for car price prediction using the dataset you cleaned in Assignment Three.

---

## Part A — Theory

Write your answers in English using a clear academic style (headings, paragraphs, and references). Length: 2–3 pages. Use your own words — no copy-paste. You may use AI for clarification, but must understand and verify everything you write.

1. **Introduction to Regression**

   - What is regression in Machine Learning?
   - How is it different from classification?
   - Give one real-life example of regression and one of classification.

2. **Types of Regression**

   - Describe and compare the following:
     - Linear Regression
     - Multiple Linear Regression
     - Polynomial Regression
   - For each type, explain: how it works (basic idea), one real-world use case, and its main advantages and limitations.

3. **Regression Metrics**

   - Define and explain what each metric measures:
     - MAE (Mean Absolute Error)
     - MSE (Mean Squared Error)
     - RMSE (Root Mean Squared Error)
     - R² (Coefficient of Determination)
   - Include a comparison table showing their differences (units, sensitivity to large errors, meaning).

4. **Underfitting and Overfitting**

   - Explain what underfitting and overfitting mean in regression models.
   - What causes overfitting, especially in polynomial regression?
   - Give 2–3 methods to prevent overfitting.

5. **Real-World Case Study**

   - Research a real-world project or study that used regression (linear, multiple, or polynomial) in any field such as business, healthcare, education, or transportation.
   - Summarize: the goal, the data used, the type of regression applied, and the key results or insights.

---

## Part B — Practical: Car Price Prediction

**Dataset:** Use the cleaned car dataset you produced in Assignment Three (`clean_car_dataset.csv`).

Create a Jupyter Notebook named `car_price_prediction.ipynb` and implement the following steps:

1. **Load Dataset**

   - Load `clean_car_dataset.csv`.

2. **Prepare Features & Target**

   - Target (`y`) = `Price`
   - Features (`X`) = all columns except `Price` and `LogPrice`.

3. **Split Data**

   - Split into 80% training and 20% testing.
   - Use `random_state=42`.

4. **Train Models**

   - Train a `LinearRegression` model.
   - Train a `RandomForestRegressor` with `n_estimators=100` and `random_state=42`.

5. **Evaluate Performance**

   - Write a helper function to print R², MAE, MSE, and RMSE for a given model.
   - Call it for both models.
   - Expected output format (exact numbers will vary):

     ```
     Linear Regression Performance:
       R²   : 0.84
       MAE  : 3,200
       RMSE : 4,150

     Random Forest Performance:
       R²   : 0.91
       MAE  : 2,100
       RMSE : 3,400
     ```

6. **Sanity Check**

   - Pick one row from the test set (`X_test.iloc[[i]]`) and compare the actual price with predictions from both models.

---

## Part C — Reflection Paper

Write a short paper (1–2 pages, Markdown or PDF) answering the following:

1. **What did you implement?**

   - Briefly describe how you trained Linear Regression and Random Forest to predict car prices using your Assignment Three cleaned dataset.

2. **Comparison of Models**

   - How did predictions differ in your sanity check?
   - Which model gave more realistic results? Why?

3. **Understanding Random Forest**

   - In your own words: what is Random Forest and how does it work (ensemble of decision trees, averaging predictions)?

4. **Metrics Discussion**

   - Which model had better R² and error metrics (MAE, RMSE)?
   - What does that tell you about the strengths and weaknesses of each model?

5. **Your Findings**

   - In 1–2 paragraphs, explain which model you prefer for price prediction and why.

---

## Deliverables

Submit these three files:

- `paper.md` or `paper.pdf` — Part A theory answers.
- `car_price_prediction.ipynb` — Part B notebook with all code and output cells visible.
- `reflection_paper.md` or `reflection_paper.pdf` — Part C reflection.

---
