import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


# 1. LOAD DATASET
PATH = "clean_loan_dataset.csv"
df = pd.read_csv(PATH)
print("=============INITIAL DATASET==========")
print(df.head())

# 2. PREPARE FEATURES AND TARGET
X = df.drop("Approved", axis=1)
y = df["Approved"]


# 3. SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)



# 4. TRAIN MODELS
Log_reg = LogisticRegression(max_iter=1000, random_state=42)
Random_fc = RandomForestClassifier(n_estimators=100, random_state=42)



Log_reg.fit(X_train, y_train)
Random_fc.fit(X_train, y_train)



# 5. RESEARCH AND TRAIN THIRD CLASSIFIER
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# I used my third model or classifier in Decision Tree Classifier because it is simple, easy to understand, and works well for classification problems like loan approval. It can handle both numerical and categorical data without much preprocessing. It also captures complex patterns in the data better than linear models.


# 6. EVALUATE PERFORMANCE
def classification_metrics(name, y_true, y_pred, pos_label=1):
    print(f"Model: {name}")
    print(f"Accurancy: {accuracy_score(y_true, y_pred): .3f}")
    print(f"Precission: {precision_score(y_true, y_pred, pos_label=pos_label): .3f}")
    print(f"Recall: {recall_score(y_true, y_pred, pos_label=pos_label): .3f}")
    print(f"F1_Score: {f1_score(y_true, y_pred, pos_label=pos_label): .3f}")



def show_confMatr(name, y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    cm_df = pd.DataFrame(cm, index=["Actual No", "Actual Yes"], columns=["Pred No", "Pred Yes"])
    print(f"\n=== {name} ===")
    print(cm_df)




log_r_pred = Log_reg.predict(X_test)
classification_metrics("LogisticRegression", y_test, log_r_pred, pos_label=1)
show_confMatr("Logistic Regression", y_test, log_r_pred)

rfc_pred = Random_fc.predict(X_test)
classification_metrics("ٌRandomForestClassifier", y_test, rfc_pred, pos_label=1)
show_confMatr("Random Forest", y_test, rfc_pred)

dt_pred = dt.predict(X_test)
classification_metrics("Decision Tree", y_test, rfc_pred, pos_label=1)
show_confMatr("Decision Tree", y_test, dt_pred)



# FINAL SANITY CHECK
i = 3
x_one_df = X_test.iloc[[i]]
y_true = y_test.iloc[i]

print("\n ==========SANITY CHECK==========")
print(f"Actual Label: {y_true}")
print(f"Logistic Regression: {Log_reg.predict(x_one_df)[0]}")
print(f"Random Forest Lable: {Random_fc.predict(x_one_df)[0]}")
print(f"Decision Tree Label: {dt.predict(x_one_df)[0]}")


