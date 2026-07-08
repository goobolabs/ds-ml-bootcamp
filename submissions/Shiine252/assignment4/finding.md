g

## Findings

In this project, I faced several challenges while building a car price prediction model using both Linear Regression and Random Forest. Initially, when using the original dataset with basic features and feature engineering (such as Year, Odometer, Doors, Accidents, Car_age and Location), the models showed weak predictive performance. The original metrics were low, with Linear Regression achieving an R² of around **0.15** and Random Forest around **0.33**, indicating that the models were not able to explain much of the variation in car prices. This suggested that the original features alone were not sufficient to capture the complexity of the car pricing problem.

To improve performance, I applied feature engineering by creating new variables such as **Km_Per_Accident**, and **Heavy_Use**. These features were designed to better represent real-world car usage patterns and depreciation effects. After feature engineering, the Linear Regression model improved significantly, reaching an R² of about **0.265**, with reduced MAE and RMSE. However, the Random Forest model did not show consistent improvement and remained around **0.31–0.32 R²**, with only minor changes in error metrics.

Despite these improvements, several problems still exist. The dataset is relatively small (140 samples), which limits the ability of the models—especially Random Forest—to generalize well. There is also evidence of overfitting, as seen in the large gap between training and testing R²

```
RandomForest:
Training R²: 0.9637124852609364
Testing R²: 0.32097496969098316
```

```
Training R²: 0.7117011100930808
Testing R²: 0.26526876412487443
```

values. Additionally, some engineered features introduced noise or redundancy, which did not always contribute positively to model performance.

To address these issues, several improvements are recommended. First, collecting more data would significantly improve model generalization and reduce overfitting. Second, hyperparameter tuning (such as limiting tree depth and adjusting minimum samples per leaf in Random Forest) could help improve performance. Third, more meaningful features such as car brand, model type, fuel type, and engine specifications could greatly enhance prediction accuracy. Finally, using cross-validation instead of a single train-test split would provide a more reliable evaluation of model performance.

Overall, while feature engineering improved the Linear Regression model, Random Forest remained the best-performing model. However, the results show that data quality, dataset size, and feature relevance are critical factors in building an effective machine learning model for car price prediction.
