## Introduction to Regression

Regression in machine learning is a type of supervised learning used to predict continuous numeric values.

The difference between regression and classification is that regression predict continuous numeric values and classification predicts which class.

examples

regression predicts 1200,1500,100, depends on the use case.

classification predicts 0/1, spam/not spam, male/female, approved/not approved depends on the use case.

### Real use cases

For regression rent prediction,car price prediction, age prediction, bmi prediction.

For classification loan approval, ye/no, spam email prediction,

## Types of Regression

| Linear Regression                                                                       | Multiple Linear Regression                                                                 | Polynomial Regression                                                       |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| The target depends on one feature.                                                      | The target depends on two or more features.                                                | Uses a curve to capture nonlinear relationships.                            |
| Uses a straight line to make predictions.                                               | Uses multiple features to improve prediction instead of relying on one feature.            | Fits a curved line instead of a straight line.                              |
| As the feature increases, the target usually increases or decreases at a constant rate. | Useful in real-world problems where one feature alone is not enough to predict the target. | Useful when the relationship between features and the target is not linear. |
| Best when the target depends mainly on one feature.                                     | Best when several features influence the target.                                           | Best when the data follows a curved pattern.                                |

## Underfitting and Overfitting

Underfitting is when machine learning model confuse to capture and learn from data patterns.

This model performs poor in training and testing

Overfitting is when model memorize training data instead of learning patters.

This model performs well in training and poor in testing

To prevent overfitting flow

- model complexity and dataset enough level
  Decide which model to use complex models needs enough data so based your dataset select model
- feature selection
  Too many features can cause overfitting so select features that determine target value
- Regulation

## Real-World Case Study

| **Category**                   | **Summary**                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Goal**                       | To investigate the relationship between worsening insomnia and the psychological effects of COVID-19, including fear of COVID-19, anxiety, depression, and lifestyle changes.                                                                                                                                                                                     |
| **Data Used**                  | Data from **400 insomnia patients** collected between July 2020 and July 2021 at Wuhan Hospital of Traditional Chinese Medicine. The dataset included demographic information and questionnaire scores from the Spiegel Sleep Questionnaire, Fear of COVID-19 Scale (FCV-19S), Zung Self-Rating Anxiety Scale (SAS), and Zung Self-Rating Depression Scale (SDS). |
| **Type of Regression Applied** | **Linear Regression** was used to determine how strongly fear, anxiety, and depression influenced insomnia and to develop a regression equation.                                                                                                                                                                                                                  |
| **Key Insights**               | Fear of COVID-19, depression, and anxiety were all significantly associated with insomnia. Fear of COVID-19 had the strongest influence on worsening insomnia, followed by depression and anxiety. The study concluded that fear of COVID-19 is a major contributor to increased insomnia.                                                                        |

## Regression Metrics

#### MAE (Mean Absolute Error)

- Measures the average absolute difference between the actual value and the predicted value.
- Lower MAE means better prediction.

#### MSE (Mean Squared Error)

- Measures the average of the squared differences between actual and predicted values.

#### RMSE (Root Mean Squared Error)

- Square root of the Mean Squared Error.
- Measures the average prediction error in the same unit as the target.
- Lower RMSE indicates better model performance.

#### R² (Coefficient of Determination)

- Measures how well the model explains the target variable.
- Higher R² means the model fits the data better.

| Metric | Measures                             | Unit                | Sensitive to Large Errors | Meaning                        |
| ------ | ------------------------------------ | ------------------- | ------------------------- | ------------------------------ |
| MAE    | Average absolute error               | Same as target      | No                        | Lower is better                |
| MSE    | Average squared error                | Squared target unit | Yes                       | Lower is better                |
| RMSE   | Square root of MSE                   | Same as target      | Yes                       | Lower is better                |
| R²     | How well the model explains the data | No unit             | No                        | Higher is better (closer to 1) |

## References

[Linear Regression Analysis of Sleep Quality in People with Insomnia in Wuhan City during the COVID-19 Pandemic](https://pmc.ncbi.nlm.nih.gov/articles/PMC10104741/)
