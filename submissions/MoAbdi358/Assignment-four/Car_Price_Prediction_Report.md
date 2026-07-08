# Car Price Prediction Using Linear Regression and Random Forest Regression

## Abstract

Predicting the selling price of vehicles is an important application of machine learning in the automotive industry. Accurate price prediction helps buyers, sellers, and dealerships make informed decisions. This study compares two supervised machine learning algorithms, Linear Regression and Random Forest Regression, using a cleaned dataset named `clean_car_dataset.csv`. The dataset was preprocessed with engineered numerical and location-based features, and the target variable used for prediction was `Price`. Both models were trained using 80% of the data and tested using the remaining 20%. Their performance was evaluated using R² (Coefficient of Determination), Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). The findings show that Linear Regression achieved a slightly higher R² and lower RMSE than Random Forest, while Random Forest achieved a lower MAE, suggesting the two models have different error patterns on this dataset.

## Keywords

Machine Learning, Car Price Prediction, Linear Regression, Random Forest Regression, Supervised Learning, Regression Analysis

## 1. Introduction

Machine learning has become an essential tool for solving prediction problems in many industries. One common regression problem is predicting the selling price of vehicles. Since prices are influenced by many factors such as size, age, condition, and location, accurately estimating prices using traditional methods is often difficult.

Regression algorithms learn patterns from historical data and estimate continuous numerical values. Choosing the right regression algorithm directly affects prediction accuracy. This study compares two popular regression techniques — Linear Regression and Random Forest Regression — to determine which model performs better for car price prediction.

The objective of this research is to evaluate both models using the same dataset and identify the most suitable algorithm based on prediction accuracy and error analysis.

## 2. Dataset and Methodology

### 2.1 Dataset

The experiment used the cleaned dataset `clean_car_dataset.csv`, which contains 99 records with engineered numerical features and location indicators related to vehicles and their selling prices.

The target variable was `Price`, the actual selling price of the vehicle.

### 2.2 Feature Selection

One column was removed before training:

- `LogPrice`

This column was excluded because it is a logarithmic transformation of the target variable itself, and keeping it in the input features would leak information about the answer directly into the model.

### 2.3 Data Splitting

The dataset was divided into:

- **Training Set:** 80% (79 records)
- **Testing Set:** 20% (20 records)

The training data was used to train the models, while the testing data evaluated their ability to predict unseen examples. A fixed `random_state=42` was used to make the split reproducible.

### 2.4 Machine Learning Models

**Linear Regression**

Linear Regression is one of the simplest supervised learning algorithms. It assumes a linear relationship between the independent variables and the target variable.

Advantages include simplicity, fast computation, and easy interpretation. However, it can struggle when relationships between variables are nonlinear.

**Random Forest Regression**

Random Forest Regression is an ensemble learning algorithm that combines multiple Decision Trees (100 trees were used in this experiment). Each tree is trained using different random samples of the data, and the final prediction is obtained by averaging the outputs of all trees.

This approach can reduce prediction errors and improve model generalization, though it depends on having enough data for the trees to learn stable patterns.

## 3. Experimental Results

A sanity check was performed on one testing example (row index 3).

| Model | Predicted Price ($) |
|---|---|
| Actual Price | 554,800 |
| Linear Regression | 583,076 |
| Random Forest | 554,827 |

The Linear Regression model overestimated the price by approximately $28,276, while Random Forest overestimated the price by only about $27 — essentially matching the actual value on this particular example.

This single result shows Random Forest can be extremely precise on individual cases, even though its overall error across the full test set was higher than Linear Regression's, as shown in the next section.

## 4. Performance Evaluation

Three main evaluation metrics were used.

| Metric | Linear Regression | Random Forest |
|---|---|---|
| R² | 0.875 | 0.865 |
| MAE | 57,059 | 52,643 |
| MSE | 4,692,253,234 | 5,065,281,448 |
| RMSE | 68,500 | 71,171 |

**R² Score**

The R² score measures how well the model explains the variation in car prices. Linear Regression achieved a slightly higher R² (0.875) than Random Forest (0.865), meaning it explained a marginally larger share of the price variation on this test set.

**Mean Absolute Error (MAE)**

MAE measures the average prediction error. Random Forest produced a lower MAE (52,643 vs. 57,059), meaning its predictions were, on average, closer to the actual prices in absolute terms.

**Root Mean Squared Error (RMSE)**

RMSE gives greater weight to large prediction errors. Linear Regression achieved a lower RMSE (68,500 vs. 71,171), suggesting it made fewer very large mistakes than Random Forest on this dataset.

## 5. Discussion

Unlike many larger-scale car price studies where Random Forest clearly outperforms Linear Regression, this experiment shows a mixed result: Linear Regression slightly outperformed Random Forest on R² and RMSE, while Random Forest slightly outperformed Linear Regression on MAE.

A likely explanation is the small size of the dataset. With only 99 total records (79 used for training), Random Forest's 100 decision trees have very little data per tree to learn from, which can lead to less stable predictions and occasional larger errors — raising its RMSE even though its typical (average) error stayed low. Linear Regression, being a simpler model with fewer parameters to estimate, can perform more consistently on small datasets because it is less prone to overfitting.

The single-row sanity check also illustrates this: Random Forest predicted almost the exact price for that one example, while Linear Regression was off by about $28,000 — yet across the full test set, Linear Regression's overall error was more consistent.

This highlights an important lesson in regression analysis: no single metric tells the whole story, and a more complex model (like Random Forest) is not automatically better, especially on small datasets. Model choice should depend on the size and nature of the data, not just the algorithm's reputation for handling complexity.

## 6. Conclusion

This research compared Linear Regression and Random Forest Regression for predicting car prices using an engineered feature dataset of 99 records.

Both algorithms were trained using the same 80/20 split and evaluated using identical testing data. The results showed a mixed outcome: Linear Regression achieved a higher R² and lower RMSE, while Random Forest achieved a lower MAE and a near-perfect prediction on the single-row sanity check.

These findings suggest that, on smaller datasets, simpler models like Linear Regression can be just as competitive as more complex ensemble models like Random Forest. Future work with a larger dataset would help clarify whether Random Forest's advantages become more apparent as more training data becomes available.
