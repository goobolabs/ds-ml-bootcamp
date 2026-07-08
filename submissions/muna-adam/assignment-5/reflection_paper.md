
The dataset was divided into features (X) and the target variable (y), where the target column was Approved. I then split the data into training and testing sets using an 80/20 ratio with stratified sampling to preserve the class distribution.

I trained the following three classification models:

- Logistic Regression
- Random Forest
- XGBoost (Extreme Gradient Boosting) as my additional algorithm

After training, I evaluated each model using four classification metrics:

- Accuracy
- Precision
- Recall
- F1-Score

I also generated confusion matrices for each model and performed a sanity check by comparing how all three models predicted the same loan application.

## Comparison of Models

During the sanity check, all three models predicted the selected applicant as Approved (1), which matched the actual label. Therefore, there was no prediction difference for this individual example. However, Logistic Regression produced more realistic overall results because it achieved the highest **accuracy (75%)**, **recall (92.3%)**, and **F1-score (82.8%)**. It correctly identified more approved loan applications than Random Forest and XGBoost, making it the best-performing model for this dataset.

## Random Forest

Random Forest is an ensemble machine learning algorithm used for both classification and regression problems, instead of building one decision tree, Random Forest builds many decision trees using different random subsets of the training data and different subsets of features. Each tree makes its own prediction, and for classification, the final prediction is determined by majority voting. The class that receives the most votes becomes the model's final prediction.

## XGBoost 

I chose XGBoost as the additional algorithm because it is effective for loan approval classification data. It builds multiple decision trees step by step and improves mistakes from earlier trees.

### Advantage

- Produces very high predictive accuracy.
- Handles complex relationships and feature interactions effectively.

### Limitations

- More computationally expensive than Logistic Regression.
- Requires more hyperparameter tuning to achieve the best performance.

## Metrics Discussion

### Logistic Regression (Best overall performance)

- Accuracy: 0.750 (highest)
- F1-Score: 0.828 (highest)
- 
Strength: Performs best overall on this dataset, meaning it balances precision and recall better than the others.
Weakness: Still a simple linear model, so it may fail on more complex, non-linear patterns in larger datasets.

### Random Forest

- Accuracy: 0.700
- F1-Score: 0.786
  
**Strength**: Good at handling non-linear relationships and reducing overfitting using multiple trees.
**Weakness**: In this case, it did not outperform Logistic Regression, possibly due to small dataset size or weak feature complexity.
  
### XGBoost (same as Random Forest)

- Accuracy: 0.700
- F1-Score: 0.786

**Strength**: Powerful boosting method that usually performs very well on structured data.
**Weakness**: Here it did not improve over Random Forest, meaning it had no extra advantage on this dataset.

I would use Logistic Regression for loan approval prediction because it achieved the best overall performance on this dataset. It had the highest accuracy of 75%, the highest recall of 92.3%, and the highest F1-score of 82.8% compared with Random Forest and XGBoost. This means Logistic Regression correctly identified more applicants who should be approved.