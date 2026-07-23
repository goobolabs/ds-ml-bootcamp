from sklearn.ensemble import RandomForestClassifier
import joblib

from preprocess import load_and_prepare_data


X_train, X_test, y_train, y_test = load_and_prepare_data(
    "../dataset/student_performance.csv"
)


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(
    X_train,
    y_train
)


joblib.dump(
    model,
    "../models/random_forest.pkl"
)


print("Model saved successfully!")