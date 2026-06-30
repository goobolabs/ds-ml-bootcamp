# Definition of Regression

Regression is a method that predicts continuous numerical values.

Regression predicts numbers, while classification predicts categories.

---

## Real-life examples

### Regression
- Car price prediction  
- Sales forecast  
- Salary prediction  

### Classification
- Spam detection  
- Vehicle type classification  
- Image classification (Cat vs Dog)  

---

## Linear Regression

Linear Regression uses a line to predict numbers based on data.

- How it works: Uses a straight line to predict values  
- Use case: Predict house price from size  
- Advantages: Simple, fast  
- Limitations: Only works for linear (straight-line) data  

---

## Multiple Linear Regression

A regression method that predicts a number (output) using two or more input variables (features).

- How it works: Uses multiple inputs to predict one value  
- Use case: Predict car price using mileage, age, engine size  
- Advantages: More accurate with many features  
- Limitations: Still assumes linear relationship  

---

## Polynomial Regression

A type of regression where the relationship between input and output is modeled using a curved line.

- How it works: Uses curved relationships (x², x³) for prediction  
- Use case: Predict growth or non-linear trends  
- Advantages: Handles complex patterns  
- Limitations: Can overfit easily  

---

## Error Metrics

### MAE (Mean Absolute Error)
Measures the average prediction error.

### MSE (Mean Squared Error)
Measures the average of squared prediction errors.

### RMSE (Root Mean Squared Error)
Square root of MSE.  
It measures average error in the same unit as the target value.

### R² (R-squared)
Measures how well the regression model explains the variation in the data.

---

| Metric   | What it Measures                     | Unit                               | Sensitive to Large Errors? |
|----------|--------------------------------------|------------------------------------|----------------------------|
| MAE      | Average absolute error              | Same as target (e.g., dollars, kg) | No                         |
| MSE      | Average squared error               | Squared units                      | Yes                        |
| RMSE     | Square root of MSE                  | Same as target                     | Yes                        |
| R²       | Model performance / explanation     | No unit                            | No                         |

---

## Underfitting and Overfitting

### Underfitting
Happens when the model is too simple to learn the pattern in the data.

### Overfitting
Happens when the model learns the training data too well (including noise), so it performs well on training data but poorly on new data.

---

## Causes of Overfitting (Polynomial Regression)

- Model is too complex (high-degree polynomial)
- Fits noise instead of real pattern
- Not enough data compared to model complexity  

---

## Methods to Prevent Overfitting

- Use a simpler model (avoid very high-degree polynomials)  
- Use more data (helps learn real patterns)  


## Real-World Case Study: Diabetes Prediction

### Goal  
The goal of this project was to predict how much a person’s diabetes will progress after one year.  
Doctors use this to understand whether a patient’s condition is getting better or worse.

### Data Used  
The dataset included real patient information such as:
- Age  
- Gender  
- BMI
- Blood pressure  
- Blood sugar levels  
- Other medical test results  

Each row represents one patient.  
The target value is the diabetes progression score after 1 year.

### Type of Regression Used  
Multiple Linear Regression was used.

This model uses many input features to predict one number (the outcome).  
It learns how each factor (like BMI or blood pressure) affects diabetes progression.

### Key Results  
- BMI and blood pressure were the strongest predictors of diabetes progression  
- Some features had very little impact on the final prediction  
- The model gave useful estimates, but not perfect ones  
- It helped identify which health factors are most important  

