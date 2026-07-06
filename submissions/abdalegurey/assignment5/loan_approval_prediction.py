import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# --------------------------------
# 1) Load Dataset

CSV_PATH = "dataset/clean_loan_dataset.csv"
df = pd.read_csv(CSV_PATH)

# 2)Prepare Features & Target

X = df.drop("Approved", axis=1)
y = df["Approved"]



# 3)Split Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

# 4) Train Models (Reproduce Lesson)

lr = LogisticRegression(
    max_iter=1000,
    random_state=42
)

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)


#random forest 

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

#5) Research & Train a Third Classifier

# ## Third Classifier: Decision Tree

# I chose Decision Tree because it is simple, easy to interpret, and works well for classification problems such as loan approval prediction. Decision Trees can capture non-linear relationships between applicant features and the approval decision.


dt = DecisionTreeClassifier(
    random_state=42
)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

# 6) Evaluate Performance

def evaluate_model(name, y_true, y_pred):

    print("=" * 45)
    print(name)
    print("=" * 45)

    print(f"Accuracy : {accuracy_score(y_true, y_pred):.3f}")
    print(f"Precision: {precision_score(y_true, y_pred):.3f}")
    print(f"Recall   : {recall_score(y_true, y_pred):.3f}")
    print(f"F1-Score : {f1_score(y_true, y_pred):.3f}")

    print("\nConfusion Matrix")

    print(confusion_matrix(y_true, y_pred))

    print()


evaluate_model(
    "Logistic Regression Performance",
    y_test,
    lr_pred
)

evaluate_model(
    "Random Forest Performance",
    y_test,
    rf_pred
)

evaluate_model(
    "Decision Tree Performance",
    y_test,
    dt_pred
)

# 7) Sanity Check


i = 0

sample = X_test.iloc[[i]]

actual = y_test.iloc[i]

lr_prediction = lr.predict(sample)[0]

rf_prediction = rf.predict(sample)[0]

dt_prediction = dt.predict(sample)[0]

print("Actual Label :", actual)

print("Logistic Regression :", lr_prediction)

print("Random Forest :", rf_prediction)

print("Decision Tree :", dt_prediction)





