from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from preprocess import load_and_prepare_data
import joblib


X_train, X_test, y_train, y_test = load_and_prepare_data(
    "../dataset/student_performance.csv"
)


model = joblib.load(
    "../models/random_forest.pkl"
)


prediction = model.predict(X_test)


print("Accuracy:",
      accuracy_score(y_test, prediction))

print("Precision:",
      precision_score(y_test, prediction))

print("Recall:",
      recall_score(y_test, prediction))

print("F1 Score:",
      f1_score(y_test, prediction))