# Reflection Paper — Car Price Prediction (Linear Regression vs. Random Forest)

## 1. What did you implement?

In this section, I implemented two types of regression models to predict car prices using the dataset I cleaned in Assignment Three (`clean_car_dataset.csv`).

The target (y) was Price, while the features (X) were all the remaining columns, excluding Price and LogPrice. The dataset was split into 80% for training and 20% for testing using `train_test_split` with `random_state=42`. The training data was used to train both models, while the testing data was used to evaluate how the models performed on new, unseen data.

The two models I trained were Linear Regression and Random Forest Regressor. Linear Regression was used to learn the straight-line relationship between the features and the car price, while Random Forest Regressor used multiple decision trees to learn more complex relationships in the data, which usually produces more accurate predictions.

## 2. Comparison of Models

In the sanity check at row i = 3, the actual car price was $7,009. The Linear Regression model predicted $5,703, while Random Forest predicted $6,941.

Calculating the error, Linear Regression was off by $1,306, while Random Forest was off by only $68. So for this particular row, Random Forest gave a prediction much closer to the actual price and could be considered the model that gave the more realistic result.

However, when evaluating overall performance across the full test dataset, Linear Regression performed better overall. This is shown by its higher R² score (0.436) compared to Random Forest (0.265), as well as a lower RMSE (1,938) and MSE (3,755,299) compared to Random Forest, indicating that it generally produced more accurate and consistent predictions. Although Random Forest had a lower MAE (1,208) compared to Linear Regression (1,428), the overall results show that Linear Regression was the better-performing model on this dataset.

This shows that a single prediction alone cannot determine which model is best. It is important to look at all the evaluation metrics calculated across the overall test data to determine the most suitable model.

## 3. Understanding Random Forest

Random Forest is a machine learning algorithm made up of many decision trees. Instead of relying on just one tree, it creates many trees, each trained on a different subset of the data. Each tree makes its own prediction independently.

When predicting a numeric value (regression), each tree produces its own individual prediction. Random Forest then combines the predictions of all the trees by taking their average, and that average becomes the model's final prediction.

The main advantage of using many trees is that the result does not depend on a single tree alone. If one tree makes a mistake or overfits the data, the other trees can help reduce that error. As a result, Random Forest usually provides more stable and reliable predictions compared to a single Decision Tree.

## 4. Metrics Discussion

Looking at the overall results on the test dataset, Linear Regression achieved a better R² score (0.436) compared to Random Forest (0.265). It also had a lower RMSE (1,938 vs. 2,211), showing that it generally produced more accurate, consistent predictions. Although Random Forest had a lower MAE (1,208 vs. 1,428), the R² and RMSE indicate that Linear Regression was the better-performing model on this dataset.

The main reason for this is that the dataset was small. Random Forest usually needs more data to learn complex relationships between the features. Since the training data was only about 112 rows, it did not have enough data to learn well, which lowered its performance. Linear Regression, on the other hand, performs well on small datasets, especially when the relationship between the features and the target is close to linear.

Overall, Linear Regression's strengths include being a simple model that trains quickly and is easy to interpret. However, its weakness is that it cannot capture non-linear relationships well.

Random Forest, on the other hand, is capable of learning complex, non-linear relationships and usually produces accurate predictions when given a large, high-quality dataset. However, it requires more data and computational resources, and it can sometimes underperform on small datasets or when there isn't enough data for it to learn effectively.

## 5. Your Findings

In general, which model I choose depends on the size of the dataset I have. There are two very different scenarios: working with a large dataset versus a small dataset.

When I have a small dataset, I would prefer Linear Regression, because, as shown in this project, it performed better (R² = 0.436) on the relatively small car dataset (140 rows) compared to Random Forest (R² = 0.265). When my dataset is large, I would choose Random Forest instead, because Random Forest performs well when the dataset contains a large amount of data, since it has enough information across many decision trees to learn complex, non-linear patterns reliably.
