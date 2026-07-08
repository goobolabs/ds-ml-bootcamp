# Regression in Machine Learning

## Introduction

Regression is one of the most useful methods in supervised Machine Learning. It is used to guess a number (not a category) based on how input data connects to an output value. Regression helps people and companies make good guesses using past data. Some common uses are guessing house prices, sales amounts, medical costs, and weather numbers.

Learning about regression is important because it shows how different factors affect a result. This report talks about what regression is, its main types, how we measure its performance, common problems like overfitting and underfitting, and one real example from the real world.

## 1. What is Regression?

### What is Regression in Machine Learning?

Regression is a supervised Machine Learning method used to guess numbers that can be anything on a scale (continuous values). While training, the model studies how the input data (features) relate to the answer (target). After training, the model can guess new number values for new data.

For example, a regression model can guess a student's final grade, the price of a house, or tomorrow's temperature.

### Regression vs Classification

Both regression and classification are supervised learning types, but they answer different kinds of questions.

- Regression guesses numbers.
- Classification guesses categories or labels.

Examples:

- Regression: Guessing a monthly electric bill based on how much electricity was used.
- Classification: Guessing if an email is Spam or Not Spam.

## 2. Types of Regression

### 2.1 Linear Regression

**Basic Idea**
Linear Regression assumes a straight-line connection between the input and the output. The model finds the best line that makes the smallest errors.

**Formula:**

Y = a + bX

Where:
- Y = the guessed value
- X = the input value
- a = where the line starts (intercept)
- b = how steep the line is (slope)

**Real Example**
Guessing a house price based on its size.

**Good Points**
- Simple to understand and use.
- Trains quickly.
- Easy to explain.
- Works well when the connection is close to a straight line.

**Weak Points**
- Cannot handle complicated, curved connections.
- Affected easily by unusual data points (outliers).
- Works worse when its assumptions are not true.

### 2.2 Multiple Linear Regression

**Basic Idea**
Multiple Linear Regression is like Linear Regression, but it uses two or more inputs to guess one output.

**Formula:**

Y = a + b₁X₁ + b₂X₂ + ... + bₙXₙ

**Real Example**
Guessing an employee's salary using:
- Education level
- Years of work experience
- Age
- Job position

**Good Points**
- Uses many inputs, so guesses can be more accurate.
- Shows more realistic connections.
- Helpful for business and economy predictions.

**Weak Points**
- Can be confused when inputs are too similar to each other (multicollinearity).
- Needs bigger datasets.
- Harder to explain as more inputs are added.

### 2.3 Polynomial Regression

**Basic Idea**
Polynomial Regression handles curved (nonlinear) connections by adding powers like X² and X³.

Instead of a straight line, it draws a curve that fits complicated patterns better.

**Real Example**
Guessing crop harvest amounts using rainfall and temperature, when the connection is curved instead of straight.

**Good Points**
- Handles curved connections well.
- More accurate for curved data.
- More flexible than Linear Regression.

**Weak Points**
- Can overfit the training data easily.
- Hard to choose the right curve level (degree).
- Costs more computer power than Linear Regression.

## 3. How We Measure Regression

Several metrics help us check how good a regression model is.

**Mean Absolute Error (MAE)**
MAE finds the average size of the mistake between the guess and the real answer, ignoring if it's too high or too low.
A lower MAE means better guesses.

**Mean Squared Error (MSE)**
MSE finds the average of the mistakes squared.
Because the mistakes are squared, big mistakes are punished more.

**Root Mean Squared Error (RMSE)**
RMSE is just the square root of MSE.
It's easier to understand because it uses the same units as the target.

**R² (Coefficient of Determination)**
R² tells us how well the model explains the changes in the data.
- R² = 1 means a perfect guess.
- R² = 0 means the model explains nothing.

**Comparing the Metrics**

| Metric | What it Measures | Unit | Sensitive to Big Mistakes | Meaning |
|--------|------------------|------|---------------------------|---------|
| MAE | Average mistake size | Same as target | Low | Lower is better |
| MSE | Average squared mistake | Squared units | Very high | Punishes big mistakes |
| RMSE | Square root of MSE | Same as target | High | Shows average mistake size |
| R² | How much variation is explained | No unit | Not directly | Closer to 1 is better |

## 4. Underfitting and Overfitting

### Underfitting

Underfitting happens when a model is too simple to catch the real pattern in the data.

Signs:
- High error on training data
- High error on testing data
- Bad guesses overall

Example: Using a plain straight line to guess data that is actually very curved.

### Overfitting

Overfitting happens when a model learns the real pattern AND the random noise in the training data.

Signs:
- Very low error on training data
- High error on testing data
- Bad performance on new data

**Reasons for Overfitting (Common in Polynomial Regression)**
- Using too high a polynomial degree.
- Too little training data.
- Too many unneeded features.
- Noisy data.

**Ways to Stop Overfitting**
- Use a simpler model with a lower polynomial degree.
- Use regularization methods like Ridge Regression or Lasso Regression.
- Add more training data or use cross-validation to help the model generalize better.

## 5. Real-World Example

### Healthcare: Guessing Medical Insurance Costs

**Goal**
Researchers built a Multiple Linear Regression model to guess a person's medical insurance cost. Good guesses help insurance companies plan expenses and set fair prices.

**Data Used**
The dataset had:
- Age
- Body Mass Index (BMI)
- Smoking status
- Number of children
- Gender
- Region

**Type of Regression Used**
Multiple Linear Regression

**Main Results**
The study showed that smoking and age were two of the strongest reasons for higher insurance costs. People who smoked usually had much higher costs than people who didn't. BMI also added to higher costs. These results help insurance companies set better prices and help policymakers understand what affects healthcare costs.

## Conclusion

Regression is a strong Machine Learning tool used to guess numbers. Unlike classification, which guesses categories, regression guesses amounts like prices, costs, and temperatures. Linear Regression is good for simple straight-line data, Multiple Linear Regression handles many inputs at once, and Polynomial Regression handles curved data. We check model performance using MAE, MSE, RMSE, and R². Knowing about underfitting and overfitting is key to building good, reliable models. Regression is used in many fields such as business, healthcare, education, and transportation to help make better decisions using data.

## References

Trevor Hastie, Robert Tibshirani, and Jerome Friedman. *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. Springer, 2nd Edition, 2009.

Christopher M. Bishop. *Pattern Recognition and Machine Learning*. Springer, 2006.

Douglas C. Montgomery, Elizabeth A. Peck, and G. Geoffrey Vining. *Introduction to Linear Regression Analysis*. Wiley, 6th Edition, 2021.

IBM. *What is Linear Regression?* IBM Think Topics. https://www.ibm.com/topics/linear-regression
