Final Project Proposal
1. Certificate NameSamira Abdirashid Elmi
2. Project Title and DescriptionTitleGym Members Churn Prediction Using Machine Learning
DescriptionThis project aims to predict whether a gym member is likely to cancel their membership (churn) or continue using the gym. Customer churn is a major challenge for fitness centers because losing members reduces revenue and increases the cost of acquiring new customers. By analyzing member information such as age, membership type, workout habits, calories burned, and monthly visits, a machine learning model can identify members who are at risk of leaving. The prediction can help gym managers take preventive actions, such as offering promotions or personalized training plans, to improve customer retention and satisfaction.
3. Problem TypeClassification
The target variable is Churn, which has two categories:
Yes – The member is likely to leave the gym.No – The member is likely to continue their membership.Since the model predicts a category instead of a numerical value, this is a classification problem.
4. DatasetSourceKaggle – Gym Members Churn Prediction Dataset
https://www.kaggle.com/datasets/hassaan2580/churn-prediction-gym-members-dataset
Dataset SizeApproximately 5,000 rows, which satisfies the project requirement of at least 1,000 rows.
Target ColumnChurn
Yes = Member leaves the gym.No = Member stays.Main FeaturesAge – Member's age.Gender – Male or Female.Membership_Type – Basic, Standard, or Premium membership.Favorite_Exercise – The member's preferred exercise.Avg_Workout_Duration_Min – Average workout duration in minutes.Avg_Calories_Burned – Average calories burned during workouts.Total_Weight_Lifted_kg – Total weight lifted.Visits_Per_Month – Number of gym visits each month.5. Algorithms You Plan to Train1. Logistic RegressionA simple and effective baseline classification model that predicts whether a member will churn.
2. Decision Tree ClassifierA tree-based model that can capture non-linear relationships and produce easy-to-understand decision rules.
3. Random Forest ClassifierAn ensemble model that combines multiple decision trees to improve prediction accuracy and reduce overfitting.
6. Evaluation PlanThe models will be evaluated using the following metrics:
AccuracyPrecisionRecallF1-ScoreThe final model will be selected based on the F1-Score, because it balances Precision and Recall and provides a reliable evaluation for customer churn prediction.
7. Deployment SketchThe project will be deployed using Flask.
Input (JSON)
undefined
{
  "Age": 28,
  "Gender": "Female",
  "Membership_Type": "Premium",
  "Favorite_Exercise": "Cardio",
  "Avg_Workout_Duration_Min": 60,
  "Avg_Calories_Burned": 420,
  "Total_Weight_Lifted_kg": 850,
  "Visits_Per_Month": 18
}

Output (JSON)undefined
{
  "Prediction": "No",
  "Probability": 0.94
}

The API will receive member information and return the predicted churn result along with the prediction probability.
8. Repository Planundefined
gym-members-churn-prediction/
├── dataset/
├── notebooks/
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── predict.py
├── api/
│   └── app.py
├── models/
├── requirements.txt
├── README.md
└── project_paper.md


This repository structure keeps the project organized by separating the dataset, preprocessing, model training, deployment, and documentation. It will make the project easier to maintain, understand, and extend in the future.