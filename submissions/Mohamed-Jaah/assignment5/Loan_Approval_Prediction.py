# =====================================
# Loan Classification code
# =====================================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler  # <--- Halkan waxaan ka beddelay StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Loading the dataset
df = pd.read_csv("Cleaned_Loan_Dataset.csv")

# Defining x and y
y = df["Approved"]
X = df.drop("Approved", axis=1)

# Spliting the dataset into training and testing 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

#  Scaling the Data
scaler = RobustScaler()  # <--- Halkan waxaa laga beddelay StandardScaler()
# Fit only on training data, then transform both training and testing data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# ---------------------------

# Initializing the model
logistic = LogisticRegression(max_iter=1000, random_state=42)
forest = RandomForestClassifier(n_estimators=100, random_state=42)
tree = DecisionTreeClassifier(random_state=42)

# Training the model using previous scaled data
logistic.fit(X_train_scaled, y_train)
forest.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

# Evaluating as function
def evaluate(model, name, X_data):
    # Predict using the appropriately scaled data
    pred = model.predict(X_data)
    
    print("\n" + name)
    print("Accuracy:", round(accuracy_score(y_test, pred), 3))
    print("Precision:", round(precision_score(y_test, pred), 3))
    print("Recall:", round(recall_score(y_test, pred), 3))
    print("F1:", round(f1_score(y_test, pred), 3))
    
    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, pred))

# Print Evaluations
evaluate(logistic, "Logistic Regression Performance", X_test_scaled)
evaluate(forest, "Random Forest Performance", X_test_scaled)
evaluate(tree, "Decision Tree Performance", X_test_scaled)

# Sanity Checking
sample = X_test.iloc[[3]]

# Scaling single sample 
sample_scaled = scaler.transform(sample)

# Last Printing
print("\nActual")
print(y_test.iloc[3])
print("\nLogistic:", logistic.predict(sample_scaled)[0])
print("\nRandom Forest:", forest.predict(sample_scaled)[0])
print("\nDecision Tree:", tree.predict(sample_scaled)[0])