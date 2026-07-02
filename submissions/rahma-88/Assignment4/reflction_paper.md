
Reflection Paper
Q1
After the dataset was ready, it was split into two sections: one for model training and another for performance evaluation.Typically, 20% of the data was utilized for testing and 80% was used for training. To determine how automotive attributes like year, mileage, engine size, fuel type, and transmission relate to the car's pricing, a Linear Regression model was constructed using the training data after the required categorical variables were prepared and converted. Prices for the test data were then predicted using the trained model.
The same preprocessed training and testing datasets were used to train a Random Forest Regressor. Using various portions of the training data, this model generates numerous decision trees. The results are then combined by averaging all of the predictions. Random Forest is superior to a simple straight-line model because it can identify intricate, curved relationships between automotive attributes and their costs.

Q2
Both models produced rather accurate price forecasts throughout the sanity check, but there were some obvious discrepancies.
The forecasts demonstrated a clear relationship in which the input features caused the price to fluctuate in a straight line. Although the model was functional, it occasionally produced costs that were either too high or too low, particularly for expensive or unusual vehicles. This is due to the assumption made by linear regression that there is a straight-line relationship between the features and the price.
Based on market pricing, the Random Forest Regression forecasts were largely in line with expectations. The model addressed the interdependence of various elements, including age, mileage, engine size, and fuel type, which improved the accuracy and dependability of the forecasts. Additionally, the complex patterns in the data had less of an impact.
A more accurate model
Because car prices are influenced by complex, non-linear elements that a simple linear model cannot fully describe, the Random Forest Regression model produced more realistic findings. Compared to Linear Regression, Random Forest's pricing forecasts are more reliable because it uses predictions from several decision trees to reduce prediction mistakes and better handle various types of data.

Q3
A machine learning technique called Random Forest combines several decision trees to get a prediction that is more accurate. By utilizing various data sets and feature sets each time, it generates multiple decision trees rather than just one. It is referred to as a "forest of decision trees" for this reason.

Q4 -

Metric	Linear Regression	Random Forest	Better Model
MAE	1,428.05	1,204.81	Random Forest
RMSE	1,937.86	2,198.01	Linear Regression
R² Score	43.58%	27.42%	Linear Regression

Linear Regression
Strengths:
Achieved the highest R² Score (43.58%), explaining more variation in car prices.
Produced the lowest RMSE (1,937.86), meaning it made fewer large prediction errors.
Performed better overall on this dataset.
Weaknesses:
Had a higher MAE than Random Forest, meaning its average prediction error was slightly larger.
Random Forest Regression
Strengths:
Achieved the lowest MAE (1,204.81), meaning its predictions were closer to the actual prices on average.
Weaknesses:
Had a lower R² Score (27.42%), indicating it explained less variation in the data.
Had the highest RMSE (2,198.01), showing that it made some large prediction errors that negatively affected its overall performance.

Q5
Overall, the findings indicate that Linear Regression offers a higher overall fit and more consistent predictions, making it a better fit for this cleaned dataset. Although Random Forest typically does well on complicated datasets, its larger RMSE (2,198.01) and lower R² score (27.42%) suggest that it had trouble grasping some observations in this instance. Because it generated more accurate and consistent predictions on this dataset, I would thus select Linear Regression as the best model for forecasting automobile prices.