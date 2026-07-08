# Part C — Reflection Paper

## 1. What Did You Implement?

In this practical assignment, I built two regression models to predict car prices using the cleaned dataset from Assignment Three (`clean_car_dataset.csv`). I first loaded the dataset, selected **Price** as the target variable (`y`), and used all remaining columns except **LogPrice** as the input features (`X`). The dataset was then divided into 80% training data and 20% testing data using `train_test_split()` with `random_state=42`.

After preparing the data, I trained two machine learning models: **Linear Regression** and **Random Forest Regressor**. Once both models were trained, I evaluated their performance using four regression metrics: **R², MAE, MSE, and RMSE**. Finally, I performed a sanity check by comparing the actual price of one test sample with the predictions made by both models.

## 2. Comparison of Models

During the sanity check, the actual car price was **4,379**. The Linear Regression model predicted approximately **5,040.46**, while the Random Forest model predicted approximately **4,594.37**. Both models produced predictions that were reasonably close to the actual value, although neither prediction was exact.

The Random Forest prediction was numerically closer to the actual price in this single example. However, looking at the overall evaluation metrics gives a better understanding of model performance because they are calculated using the entire test dataset rather than one observation.

## 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that combines many decision trees instead of relying on a single tree. Each decision tree is trained using a different random sample of the training data. When making a prediction, every tree produces its own estimate, and the Random Forest calculates the final prediction by averaging the results of all the trees. This approach usually produces more stable predictions and reduces the effect of individual decision tree errors.

## 4. Metrics Discussion

The evaluation results showed different strengths for the two models. The Linear Regression model achieved an **R² of 0.44**, which was higher than the Random Forest model's **R² of 0.24**. It also produced a lower **RMSE (1937.86)** compared to **2244.61** for Random Forest, indicating that its overall prediction errors were smaller.

On the other hand, the Random Forest model obtained a slightly lower **MAE (1238.50)** than the Linear Regression model (**1428.05**). This means that, on average, its absolute prediction error was smaller. However, because its R² was lower and its RMSE was higher, the Linear Regression model performed better overall on this dataset.

## 5. My Findings

Based on the results of this assignment, I prefer the **Linear Regression** model for predicting car prices using this dataset. Although Random Forest gave a slightly smaller MAE and a closer prediction during the sanity check, Linear Regression achieved a higher R² value and a lower RMSE, showing that it explained more variation in the data and produced more consistent predictions overall.

This assignment helped me understand that different evaluation metrics can lead to different conclusions. It also showed the importance of comparing several metrics instead of relying on only one value or one prediction. Selecting the best machine learning model should be based on its overall performance across the testing dataset rather than a single example.
