# Reflection Paper – Car Price Prediction Using Machine Learning
---

## 1. What Did You Implement?

For this project, I built and compared two Machine Learning models — **Linear Regression** and **Random Forest Regression** — to predict car prices using the cleaned dataset prepared in Assignment Three.

The cleaned dataset contained **140 observations** and **12 variables**, including three engineered features created during preprocessing: **CarAge** (derived from the manufacturing year), **Km_per_year** (average yearly mileage), and **Is_Urban** (whether the vehicle belongs to an urban environment). The target variable (**y**) was **Price**, while the input features (**X**) included all remaining columns except *Price* and *LogPrice*.

I loaded the dataset into **Jupyter Notebook** and split it into training and testing sets using an 80/20 split — **112 samples** for training and **28 samples** for testing — with `random_state = 42` to ensure the split was reproducible.

I then trained the two models on the training data:

- **Linear Regression** was trained as a baseline model, fitting a straight-line relationship between the input features and price.
- **Random Forest Regression** was trained as an ensemble model, building multiple decision trees on different subsets of the data and combining their outputs into a single prediction.

Both models were evaluated on the same 20% test set using four metrics: **R² Score, MAE, MSE, and RMSE**, which allowed for a fair, like-for-like comparison between a simple linear model and a more complex ensemble model.

**Note on a correction made to the Assignment Three notebook:** While revisiting the Assignment Three notebook for this project, I identified a syntax error in the feature-engineering step that creates the `Is_Urban` and `LogPrice` columns. The original code left an opening parenthesis unclosed:

```python
df["Is_Urban"] = (
    df["Location_City"]
    .astype(int)

df["LogPrice"] = np.log(
```

Because the parenthesis after `(int)` was never closed, Python treated the next line as a continuation of the same statement, which produced a `SyntaxError` and, as a downstream consequence, caused the final cell (`df.to_csv(...)`) to fail with a `NameError: name 'df' is not defined` when the notebook was run from a fresh kernel. I corrected this by closing the statement properly:

```python
df["Is_Urban"] = df["Location_City"].astype(int)

df["LogPrice"] = np.log(df["Price"] + 1)
```

I am noting this explicitly because it is a clear, identifiable bug in the data-preparation pipeline itself — separate from the broader data-quality limitations (small sample size, missing pricing factors) discussed later in this report. The dataset used to train the models in this project was generated from a notebook run *before* this bug was introduced; the corrected version of the notebook is included alongside this report so that the full pipeline can be re-run end-to-end without error.

---

## 2. Comparison of Models

### 2.1 How Did Predictions Differ in the Sanity Check?

To sanity-check the models beyond the aggregate metrics, I compared their predictions against one actual test value:

| Actual Price | Linear Regression | Random Forest |
|---|---|---|
| $4,379 | $5,040 | $4,759 |

During this sanity check, the actual car price was **$4,379**. The Linear Regression model predicted a price of **$5,040**, while the Random Forest model predicted **$4,759**. Although both models produced reasonable predictions, the **Random Forest prediction was closer to the actual price** — it overestimated by only about $380, compared to Linear Regression's overestimate of about $661.

The Random Forest model produced a more realistic prediction in this particular sanity check because its prediction differed from the actual price by a smaller amount. This suggests that, for this specific car, Random Forest was able to capture some of the more complex, non-linear relationships between the car's features and its price that a simple linear model may not fully capture.

### 2.2 Which Model Gave More Realistic Results? Why?

This is where the results become genuinely interesting, because the sanity check and the overall evaluation metrics point in **opposite directions** — and reconciling that contradiction is an important part of interpreting the project correctly.

| Metric | Linear Regression | Random Forest |
|---|---|---|
| R² Score | **0.4358** | 0.2748 |
| MAE | 1,428.05 | **1,214.33** |
| MSE | **3,755,299.23** | 4,826,630.55 |
| RMSE | **1,937.86** | 2,196.96 |

Across the **full 28-sample test set**, Linear Regression had the higher R² and the lower MSE/RMSE, meaning it explained more of the overall variance in price (43.58% vs. 27.48%) and made fewer large, heavily-penalized errors overall. Random Forest, by contrast, had the lower MAE, meaning its *typical* error per prediction was somewhat smaller on average.

**Why does R² favor Linear Regression while the sanity check favors Random Forest?** The explanation lies in the difference between a *single observation* and the *full test set*:

- The sanity-check car happened to be one where Random Forest's prediction landed unusually close to the true price. With only **112 training samples**, Random Forest's individual decision trees can become quite sensitive to the specific examples they were trained on, which means its predictions can vary more from car to car — sometimes landing very close, and sometimes landing far off. One favorable example does not represent how the model behaves across all 28 test cases.
- R², on the other hand, is calculated using **every single test observation**, not just one. It reflects how much of the *overall* price variation each model can explain across the whole test set. Linear Regression's higher R² tells us that, taken as a whole, its predictions tracked the true price trend more consistently than Random Forest's did — even though Random Forest happened to "win" on this one example.
- This is also consistent with Random Forest's higher RMSE: RMSE squares errors before averaging them, so it is especially sensitive to a few large mistakes. The fact that Random Forest's RMSE is higher despite its lower MAE suggests it made a small number of sizeable errors elsewhere in the test set that dragged its overall reliability down, even though its prediction on this particular sanity-check car was strong.

**In short:** Random Forest can look more realistic on an individual, case-by-case basis, but Linear Regression is more *consistently* realistic across the dataset as a whole. Since R² and RMSE are calculated over the entire test set rather than a single data point, they give a more complete picture of which model actually generalizes better — which is why **Linear Regression is the more dependable model overall, even though it lost this specific sanity check.**

---

## 3. Understanding Random Forest

In my own words, **Random Forest** is an ensemble learning algorithm built on top of a simpler model: the decision tree. A single decision tree predicts an outcome by repeatedly splitting the data based on feature values (for example, "is CarAge greater than 5?") until it reaches a final prediction. However, one decision tree on its own tends to be unstable — small changes in the training data can produce a very different tree.

Random Forest solves this problem by building **many decision trees instead of just one**, and introducing randomness in two ways:

1. Each tree is trained on a different random sample of the training data (drawn with replacement, a technique called *bagging*).
2. At each split in a tree, only a random subset of features is considered, rather than all of them.

Once all the trees are trained, Random Forest combines their individual predictions. For a regression task like this one, it **averages the predictions of all the trees** to produce the final output. This averaging process is what makes Random Forest more stable and generally less prone to overfitting than a single decision tree, because the errors and quirks of individual trees tend to cancel each other out across the ensemble.

---

## 4. Metrics Discussion

Looking at the two sets of metrics side by side:

- **R²:** Linear Regression scored higher (0.4358 vs. 0.2748), meaning it explained a larger share of the variation in car prices.
- **MAE:** Random Forest scored lower/better (1,214.33 vs. 1,428.05), meaning its typical per-prediction error was smaller.
- **MSE and RMSE:** Linear Regression scored lower/better on both, meaning it had fewer large, heavily-penalized errors across the test set.

This mixed result tells us something meaningful about the **strengths and weaknesses of each model in this specific context**:

- **Linear Regression's strength** is that it found a relatively stable, generalizable linear pattern in the data, which is why it explained more overall variance (higher R²) and avoided large outlier errors (lower RMSE). Its main **weakness** is that it cannot capture any non-linear relationships that might exist between features like mileage, age, and price.

- **Random Forest's strength** is its flexibility — it can model non-linear and more complex interactions between features, which is likely why it was closer on individual predictions. Its main **weakness** in this case was that, with only **112 training samples**, the model likely did not have enough data to build trees that generalized well. Random Forest typically needs more data than Linear Regression to reach its full potential, and with a small dataset it can end up learning noise rather than a true pattern — which would explain its lower R² and higher RMSE here.

Overall, this comparison shows that a more complex algorithm is not automatically a better one. With a small, imperfect dataset, a simpler model like Linear Regression can outperform a more sophisticated ensemble method like Random Forest.

---

## 5. Your Findings

Based on the evaluation metrics from this project, I would prefer **Linear Regression** for predicting car prices on this particular dataset, as it achieved a meaningfully higher R² score (0.4358 vs. 0.2748) and a lower RMSE, indicating that it explained more of the overall price variation and made fewer large, costly errors across the full test set. While Random Forest produced a closer prediction in the single sanity-check example, this advantage did not hold across the dataset as a whole, which makes Linear Regression the more dependable choice between the two.

It is important to stress, however, that **neither model's moderate performance should be blamed primarily on the algorithm itself — it is largely a reflection of the limitations of the underlying data.** An R² of 43.58% is not a high score in absolute terms, but it is a reasonable outcome given that the dataset was small (only 140 total observations, with just 112 used for training) and was missing several variables that are known to strongly influence real-world car prices, such as brand, engine type, fuel type, transmission, vehicle condition, and maintenance history. No regression algorithm, however sophisticated, can learn relationships from information that simply is not present in the dataset; this is a data-quality and data-completeness constraint, not a weakness of Linear Regression as a method. It is also worth clarifying that **changing the train/test split ratio itself would not meaningfully change this outcome.** For example, moving from an 80/20 split to a 90/10 split would only increase the training set from 112 to roughly 126 samples — the same limited set of features and the same overall pool of only 140 records would still be used. R² measures how much of the price variation can be explained by the *available features*, and since those features (and the relationships between them and price) remain unchanged regardless of how the data is split, the core issue is the *number and richness* of available records and features, not the proportion of data allocated to training versus testing.

Random Forest's comparatively weaker performance reinforces this same point: as a more flexible, data-hungry algorithm, Random Forest typically requires a larger volume of training data to build diverse, generalizable decision trees. With only 112 training samples, it is likely that the individual trees in the forest overfit to small idiosyncrasies in the training set rather than learning a robust underlying pattern, which would explain both its lower R² and its higher RMSE. This project therefore taught me an important lesson that goes beyond simply comparing two algorithms: **the success of a Machine Learning model depends first and foremost on the quality, size, and completeness of the dataset.** Even the best-suited algorithm cannot compensate for missing features or an insufficient number of observations, and with a larger and more feature-rich dataset, I would expect both models — and especially Random Forest — to perform considerably better.