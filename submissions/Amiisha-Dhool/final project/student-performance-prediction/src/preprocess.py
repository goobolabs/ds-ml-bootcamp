import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_and_prepare_data(path):

    # Load dataset
    df = pd.read_csv(path)

    # Create Pass_Fail target
    df["Pass_Fail"] = df["FinalGrade"].apply(
        lambda x: "Pass" if x >= 50 else "Fail"
    )

    # Separate features and target
    X = df.drop("Pass_Fail", axis=1)
    y = df["Pass_Fail"]

    # Encode categorical columns
    categorical_cols = X.select_dtypes(
        include=["object"]
    ).columns

    encoder = LabelEncoder()

    for col in categorical_cols:
        X[col] = encoder.fit_transform(X[col])

    # Encode target
    y = encoder.fit_transform(y)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test