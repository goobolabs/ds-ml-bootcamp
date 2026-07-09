# 📄 Loan Approval Classification — A+ Final Report

## 📌 1. Introduction

In this project, I built a machine learning system to predict loan approval outcomes using a cleaned dataset (`clean_loan_dataset.csv`). The goal was to apply classification algorithms learned in Lesson 5 and extend them with an additional model to compare performance and understand real-world prediction behavior.

---

## 📌 2. What I Implemented

I reproduced the Lesson 5 machine learning pipeline, which included:
- Loading and exploring the cleaned dataset
- Splitting data into training (80%) and testing (20%) sets using stratification
- Separating features (X) and target variable (Approved)

I trained three classification models:
- Logistic Regression (from Lesson 5)
- Random Forest (from Lesson 5)
- K-Nearest Neighbors (KNN) as an additional researched algorithm

All models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

I also performed a sanity check using a single test sample to compare actual vs predicted outcomes.

---

## 📌 3. Comparison of Models

In the sanity check, all three models predicted **"Approved (1)"** for a case that was actually **"Rejected (0)"**, resulting in a false positive across all models.

However, this does not reflect overall model performance, but rather a single borderline case.

From full evaluation metrics:
- Logistic Regression showed the highest overall accuracy and stable performance
- Random Forest performed slightly lower but remained balanced
- KNN showed strong recall but lower accuracy

### 📊 Most realistic model:
Logistic Regression gave the most realistic and consistent predictions overall because it balanced accuracy and generalization better than the other models.

---

## 📌 4. Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve classification performance.

- Each decision tree is trained on a random subset of data and features
- Each tree makes its own prediction
- The final output is determined by majority voting

This method reduces overfitting and improves generalization, making it suitable for complex datasets like loan approval prediction.

---

## 📌 5. Third Algorithm: K-Nearest Neighbors (KNN)

I selected KNN because it is a simple, intuitive classification algorithm that predicts labels based on the majority class of nearby data points.

### 📌 How it works:
- Calculates distance between data points
- Finds the nearest neighbors (K)
- Assigns the most common class among neighbors

### 📊 Advantages:
- Easy to understand and implement
- Works well on small structured datasets

### ⚠️ Limitations:
- Sensitive to feature scaling
- Can be slow on large datasets

### 📊 Performance comparison:
- Higher recall than Random Forest in some cases
- Lower accuracy than Logistic Regression
- Less stable overall predictions

---

## 📌 6. Metrics Discussion

### 📊 Model Performance Summary:
- **Logistic Regression**: Best Accuracy (0.700), balanced performance
- **Random Forest**: Moderate performance, slightly lower accuracy (0.650)
- **KNN**: High Recall (0.846), but lower accuracy (0.650)

### 📌 Interpretation:
- Logistic Regression is stable and consistent
- KNN is strong at identifying positive cases (approvals)
- Random Forest needs tuning to improve performance

This shows that different models have different strengths depending on the metric being optimized.

---

## 📌 7. Final Findings

Based on all evaluations, I would choose **Logistic Regression** as the final model for loan approval prediction.

### 📌 Reasons:
- Highest and most stable accuracy
- Balanced precision and recall
- More interpretable compared to complex models
- Less sensitive to noise compared to KNN

However, all models showed some false positives, meaning they incorrectly predicted approval for rejected applications. This suggests that further improvements such as feature engineering, class balancing, or hyperparameter tuning could enhance performance.

---

## 📌 8. Conclusion

This project demonstrated how different classification models behave on the same dataset. While all models performed reasonably well, Logistic Regression provided the best balance between simplicity, accuracy, and interpretability, making it the most suitable choice for loan approval prediction in this case.