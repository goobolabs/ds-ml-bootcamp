Reflection Paper
1. What did you implement?
I implemented two machine learning regression models, Linear Regression and Random Forest Regressor, to predict used car prices using the cleaned dataset from Assignment Three. The dataset was preprocessed by handling missing values, encoding categorical variables, and selecting relevant features. The data was split into training and testing sets. Both models were trained on the training data and evaluated on the test data using R², MAE, MSE, and RMSE.
⸻
2. Comparison of Models
In the sanity check, the actual car price was $7,009. Linear Regression predicted $5,703, while Random Forest predicted $6,959.
For this single example, Random Forest gave a more realistic prediction because it was much closer to the actual price, with an error of only $50. Linear Regression underestimated the price by $1,306.
⸻
3. Understanding Random Forest
Random Forest is an ensemble machine learning algorithm that combines the predictions of many decision trees. Each tree is trained on a different random sample of the data and considers a random subset of features. For regression problems, the final prediction is the average of all the individual tree predictions. This approach reduces overfitting and usually improves prediction accuracy.
⸻
4. Metrics Discussion
The evaluation results were:
Model	R²	MAE	RMSE
Linear Regression	0.436	1,428	1,938
Random Forest	0.277	1,178	2,193
Linear Regression achieved the higher R² score and lower RMSE, showing that it performed better overall on the test dataset. Random Forest had the lower MAE, meaning its average prediction error was smaller. This indicates that Linear Regression provided more consistent overall performance, while Random Forest could make more accurate predictions for some individual cases.
⸻
5. Your Findings
Overall, I prefer Linear Regression for this car price prediction task because it achieved the best overall evaluation results. It had the highest R² score and the lowest RMSE, indicating that it explained more of the variation in car prices and produced more reliable predictions across the test dataset.
However, the sanity check showed that Random Forest predicted one car price more accurately than Linear Regression. This suggests that Random Forest can perform very well for individual examples, even though its overall performance was lower. Based on the complete evaluation, Linear Regression is the better choice for this dataset, while Random Forest may improve with further parameter tuning and feature engineering.
