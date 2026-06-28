# Introduction to Regression

## 1.What is regression in Machine Learning?

Regression is a supervised learning technique that models the relationship between
input features and a continuous numerical output. It is used to forecast or predict specific quantities based on historical data.
---

## 2.How is it different from classification?
Regression predicts continuous, measurable quantities (like temperature or money). 
Classification assigns data into discrete categories or labels (like true/false or red/blue/green).Give one real-life example of regression and classification.
---

Regression: Predicting the future selling price of a house based on its square footage.

Classification: Categorizing an incoming email as either "Spam" or "Not Spam."

## 3.Types of Regression

Linear RegressionFits a single straight line to model the relationship between one input and one output (e.g., predicting exam scores based on hours studied). 

It is highly interpretable but too simplistic for complex, non-linear data.Multiple Linear RegressionUses multiple input variables to predict a single outcome by fitting a multidimensional plane (e.g., predicting a car's price based on its mileage, age, and brand). 

It captures more real-world detail but still assumes all features act linearly.

Polynomial RegressionTransforms features into polynomial terms to fit a curved line to non-linear data (e.g., modeling the early exponential growth of a viral outbreak). 

It is highly flexible but extremely prone to overfitting if the polynomial degree is set too high.
---
## 4.Regression

**MetricsMAE (Mean Absolute Error):** Measures the average absolute distance between predicted and actual values. It is easy to interpret and treats all errors proportionally without exaggerating outliers.

**MSE (Mean Squared Error):** Averages the squared differences between predictions and actuals. By squaring the numbers, it heavily penalizes larger errors, making it highly sensitive to outliers.

**RMSE (Root Mean Squared Error):** The square root of the MSE. This translates the error metric back into the original units of the target variable, making it much easier to understand in context.**$R^2$ (Coefficient of Determination):** Indicates the percentage of variance in the target variable that the model explains. 

A score closer to 1.0 (or 100%) means a perfect fit, while 0 means it performs no better than simply guessing the average.

## 5.Metric Comparison TableMetric
UnitsSensitivity to Large ErrorsMeaningMAESame as targetLowThe average absolute error of the predictions.MSESquared unitsHighThe average squared error of the predictions.RMSESame as targetHighThe standard deviation of the prediction errors.

$R^2$Unitless (Percentage)ModerateThe proportion of variance explained by the model.

## 6.Underfitting and Overfitting

**What do underfitting and overfitting mean?**

Underfitting means the model is too simple to capture the data's true underlying pattern. 

Overfitting means the model is overly complex and memorizes random noise in the training data instead of the general trend.

**What causes overfitting, especially in polynomial regression?**

Overfitting in polynomial regression is caused by choosing a polynomial degree that is too high. The resulting curve wildly contorts to touch every single training data point, ruining its ability to predict new, unseen data accurately.
---
**Give 2–3 methods to prevent overfitting.**
---
**Regularization:** Use techniques like Ridge or Lasso to mathematically penalize overly complex models.

**Cross-Validation:** Evaluate the model across multiple different subsets of the data to ensure it generalizes well to unseen information.
---
## .Real-World Case Study
---
**Goal and Data:**A city bikeshare program wanted to predict hourly bike demand to optimize their inventory using historical temporal data (hour, day) and weather data (temperature, humidity).

**Regression Type and Results:** They applied Polynomial Regression because variables like temperature have a curved, non-linear relationship with ridership (e.g., rentals drop off if it gets too hot). The model successfully predicted daily peak commuting spikes, allowing operators to deploy transport trucks effectively to balance bicycle station levels.