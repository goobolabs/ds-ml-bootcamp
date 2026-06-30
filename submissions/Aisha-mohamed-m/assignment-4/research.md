# Car Price Prediction Using Linear Regression and Random Forest Regression

## Abstract

Predicting the selling price of used cars is an important application of machine learning in the automotive industry. Accurate price prediction helps buyers, sellers, and dealerships make informed decisions. This study compares two supervised machine learning algorithms, Linear Regression and Random Forest Regression, using a cleaned dataset named **cars_clean.csv**. The dataset was preprocessed by selecting appropriate input features and transforming the target variable into a logarithmic scale (logPrice). Both models were trained using 80% of the data and tested using the remaining 20%. Their performance was evaluated using R² (Coefficient of Determination), Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE). The findings indicate that Random Forest Regression significantly outperformed Linear Regression because it captured complex nonlinear relationships within the data and produced more accurate predictions.

## Keywords

Machine Learning, Car Price Prediction, Linear Regression, Random Forest Regression, Supervised Learning, Regression Analysis



# 1. Introduction

Machine learning has become an essential tool for solving prediction problems in many industries. One common regression problem is predicting the selling price of used cars. Since car prices are influenced by many factors such as age, mileage, engine size, fuel type, transmission, and accident history, accurately estimating prices using traditional methods is often difficult.

Regression algorithms learn patterns from historical data and estimate continuous numerical values. Choosing the right regression algorithm directly affects prediction accuracy. This study compares two popular regression techniques—Linear Regression and Random Forest Regression—to determine which model performs better for car price prediction.

The objective of this research is to evaluate both models using the same dataset and identify the most suitable algorithm based on prediction accuracy and error analysis.



# 2. Dataset and Methodology

## 2.1 Dataset

The experiment used the cleaned dataset **cars_clean.csv**, which contains information about used vehicles and their selling prices.

The target variable was **logPrice**, which is the logarithm of the actual selling price. Applying a logarithmic transformation reduces the impact of extreme price values and improves model stability.

## 2.2 Feature Selection

Two columns were removed before training:

* Location_AVg_Price
* Unnamed: 0

These variables were excluded because they either introduced unnecessary information or could potentially leak information into the model.

## 2.3 Data Splitting

The dataset was divided into:

* Training Set: 80%
* Testing Set: 20%

The training data was used to train the models, while the testing data evaluated their ability to predict unseen examples.

## 2.4 Machine Learning Models

### Linear Regression

Linear Regression is one of the simplest supervised learning algorithms. It assumes a linear relationship between the independent variables and the target variable.

Advantages include simplicity, fast computation, and easy interpretation. However, it struggles when relationships between variables are nonlinear.

### Random Forest Regression

Random Forest Regression is an ensemble learning algorithm that combines multiple Decision Trees. Each tree is trained using different random samples of the data, and the final prediction is obtained by averaging the outputs of all trees.

This approach reduces prediction errors and improves model generalization.



# 3. Experimental Results

A sanity check was performed on one testing example (row index 5).

 Model              Predicted Price ($) 

 Actual Price                   3,623
 Linear Regression               $3,308
 Random Forest                   $3,413

The Linear Regression model underestimated the price by approximately $315, while Random Forest underestimated the price by approximately $210 and sometimes Random Forest gives the exact value

These results demonstrate that Random Forest was better able to capture the underlying pricing patterns.



# 4. Performance Evaluation

Three evaluation metrics were used.

## R² Score

The R² score measures how well the model explains the variation in car prices.

Random Forest achieved a higher R² score than Linear Regression, indicating stronger predictive capability.

## Mean Absolute Error (MAE)

MAE measures the average prediction error.

Random Forest produced a lower MAE, meaning its predictions were closer to the actual prices.

## Root Mean Squared Error (RMSE)

RMSE gives greater weight to large prediction errors.

Random Forest achieved a lower RMSE, showing that it made fewer significant mistakes.



# 5. Discussion

The comparison clearly shows that Random Forest Regression performed better than Linear Regression.

Linear Regression assumes that the relationship between the input variables and price is linear. However, used car prices depend on many complex factors that interact in nonlinear ways.

Random Forest successfully models these complex relationships by combining multiple decision trees. This enables it to produce more accurate and stable predictions even when the dataset contains complicated patterns.

Although Random Forest requires more computational resources and training time, the increase in prediction accuracy makes it a better choice for practical applications.



# 6. Conclusion

This research compared Linear Regression and Random Forest Regression for predicting used car prices.

Both algorithms were trained using the same dataset and evaluated using identical testing data. The results showed that Random Forest consistently outperformed Linear Regression across all evaluation metrics.

The higher R² score, lower MAE, lower RMSE, and more realistic predictions demonstrate that Random Forest is the preferred model for car price prediction. Therefore, businesses, online marketplaces, and customers can benefit from using Random Forest Regression to estimate vehicle prices more accurately.
