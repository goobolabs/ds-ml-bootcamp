# Part C — Reflection Paper



# Reflection Paper

## Introduction

In this assignment, I implemented two supervised machine learning regression models—**Linear Regression** and **Random Forest Regression**—to predict used car prices. The models were trained using the cleaned and preprocessed dataset from Assignment Three. The goal was to compare a simple linear model with a more advanced ensemble model and evaluate their performance using common regression metrics.

---

# What Did I Implement?

I first loaded the cleaned dataset that I prepared in Assignment Three. The dataset had already been processed by handling missing values, removing or capping outliers, encoding categorical variables, and scaling numerical features where appropriate.

After preprocessing, I separated the dataset into input features (**X**) and the target variable (**Price**). The data was then divided into training and testing sets using an 80/20 split.

Next, I trained two different regression models.

The first model was **Linear Regression**, which learns a straight-line relationship between the input features and the target variable. It estimates coefficients for each feature so that the prediction error is minimized.

The second model was **Random Forest Regression**. This model creates many decision trees using different subsets of the training data and combines their predictions by averaging them. Because of this ensemble approach, Random Forest is able to capture complex and nonlinear relationships between variables.

After training both models, I generated predictions on the test dataset and evaluated them using several regression metrics, including **MAE**, **RMSE**, and **R²**.

---

# Comparison of Models

To compare the models, I performed a simple sanity check by examining a few predicted prices alongside the actual car prices.

The **Linear Regression** model generally produced predictions that followed the overall trend of the data. However, it sometimes underestimated expensive vehicles and overestimated cheaper ones because it assumes a linear relationship between the features and the target.

The **Random Forest** model produced predictions that were usually closer to the actual prices. Since it can model nonlinear relationships and interactions between features, it was able to better capture the complexity of the used car market.

Overall, the predictions from Random Forest appeared more realistic because car prices depend on many factors that do not always have simple linear relationships.

---

# Understanding Random Forest

Random Forest is an **ensemble learning algorithm** that combines many decision trees into a single predictive model.

Instead of relying on one decision tree, Random Forest builds multiple trees using randomly selected samples of the training data and random subsets of the available features. Each decision tree independently predicts the target value. The final prediction is obtained by averaging the predictions from all trees.

This averaging process reduces the effect of errors made by individual trees, making Random Forest more accurate and more resistant to overfitting than a single decision tree.

Because different trees learn different parts of the data, the combined model usually generalizes better to unseen examples.

---

# Metrics Discussion

To evaluate both models, I used four common regression metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Squared Error (MSE)
- Coefficient of Determination (R²)

The Random Forest model achieved a **higher R² score** and **lower MAE and RMSE values** than Linear Regression.

A higher R² indicates that the model explains more of the variation in car prices. Lower MAE and RMSE values indicate that the prediction errors are smaller on average.

These results suggest that Random Forest captured the underlying patterns in the dataset more effectively than Linear Regression.

However, Linear Regression still has important advantages. It is simple, fast to train, computationally efficient, and easy to interpret because each coefficient represents the influence of a feature on the predicted price.

Random Forest, while more accurate, is more computationally expensive and more difficult to interpret because its predictions come from many decision trees rather than a single mathematical equation.

---

# My Findings

Based on the results of this assignment, I prefer **Random Forest Regression** for predicting used car prices. Used car prices are influenced by many factors such as vehicle age, mileage, location, accident history, and their interactions. These relationships are often nonlinear, making Random Forest a better choice because it can model complex patterns without requiring a predefined mathematical equation.

Although Linear Regression is easier to understand and provides a useful baseline model, its assumption of linear relationships limits its predictive performance for real-world datasets. Random Forest consistently produced more accurate predictions and better evaluation metrics, making it the more suitable model for this price prediction task. If interpretability is the main goal, Linear Regression remains valuable; however, if prediction accuracy is the priority, Random Forest is the stronger choice.

---

# Conclusion

This assignment helped me understand both the theoretical and practical aspects of regression models. By implementing Linear Regression and Random Forest on the same dataset, I learned how different algorithms approach prediction problems and how evaluation metrics can be used to compare their performance. Overall, Random Forest demonstrated better predictive ability, while Linear Regression provided a simple and interpretable baseline for comparison.