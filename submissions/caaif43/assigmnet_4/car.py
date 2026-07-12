{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "968499a1-cc07-4d5c-9784-1c085130420d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "55a15979-f0ba-4d9f-ab1d-d367ccd745c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "CSV_PATH = './clean_car_dataset.csv'\n",
    "df = pd.read_csv(CSV_PATH)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "06d507e8-6781-4fca-9d82-dc89baa90fd8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2) Split features (X) and target (y)\n",
    "# Target variable (Price)\n",
    "y = df[\"Price\"]\n",
    "X = df.drop(columns=[\"Price\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "62b68d2f-17ab-4a86-9bc7-7c0f7e2ad810",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Keep 20% of data for testing generalization. random_state for reproducibility.\n",
    "# Target variable (Price)\n",
    "y = df[\"Price\"]\n",
    "\n",
    "# Features (all columns except Price)\n",
    "X = df.drop(columns=[\"Price\"])\n",
    "\n",
    "# print(\"Features Shape:\", X.shape)\n",
    "# print(\"Target Shape:\", y.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bd712242-a124-4dc3-a7cc-f4f13ad38c10",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4) Train Linear Regression\n",
    "# --------------------------------\n",
    "# Linear model is simple and interpretable; good baseline.\n",
    "lr = LinearRegression()\n",
    "lr.fit(X_train, y_train)\n",
    "lr_pred = lr.predict(X_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "276a00d0-65b0-461c-8eac-738049b7fd6f",
   "metadata": {},
   "outputs": [],
   "source": [
    " # 5) Train Random Forest\n",
    "# Ensemble model captures non-linear relationships; often stronger than linear.\n",
    "rf = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "rf.fit(X_train, y_train)\n",
    "rf_pred = rf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b167809f-5398-486d-a38a-c80ab60ef863",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_metrics(name, y_true, y_pred):\n",
    "    \"\"\"Print R², MAE, MSE, RMSE for a model's predictions.\"\"\"\n",
    "    r2  = r2_score(y_true, y_pred)\n",
    "    mae = mean_absolute_error(y_true, y_pred)\n",
    "    mse = mean_squared_error(y_true, y_pred)\n",
    "    rmse = np.sqrt(mse)\n",
    "    print(f\"\\n{name} Performance:\")\n",
    "    print(f\"  R²   : {r2:.3f}\")          \n",
    "    print(f\"  MAE  : {mae:,.0f}\")        \n",
    "    print(f\"  MSE  : {mse:,.0f}\")        \n",
    "    print(f\"  RMSE : {rmse:,.0f}\")       \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5138dcfb-3da2-4907-9c2b-4251668c7fd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Linear Regression Performance:\n",
      "  R²   : 0.436\n",
      "  MAE  : 1,428\n",
      "  MSE  : 3,755,299\n",
      "  RMSE : 1,938\n",
      "\n",
      "Random Forest Performance:\n",
      "  R²   : 0.291\n",
      "  MAE  : 1,163\n",
      "  MSE  : 4,720,916\n",
      "  RMSE : 2,173\n"
     ]
    }
   ],
   "source": [
    "# 7) Show results for both models\n",
    "print_metrics(\"Linear Regression\", y_test, lr_pred)\n",
    "print_metrics(\"Random Forest\",   y_test, rf_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "16837d71-e4e9-4c41-b2b3-3758d392e169",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Single-row sanity check:\n",
      "  Actual Price: $7,009\n",
      "  LR Pred     : $5,703\n",
      "  RF Pred     : $6,989\n"
     ]
    }
   ],
   "source": [
    " # 8) Single-row prediction (sanity check)\n",
    "# --------------------------------\n",
    "# Pick one unseen row from X_test and predict both models.\n",
    "# Use iloc[[i]] (double brackets) to keep it as a DataFrame with column names\n",
    "i = 3\n",
    "x_one_df = X_test.iloc[[i]]   # 1-row DataFrame (keeps feature names)\n",
    "y_true   = y_test.iloc[i]     # scalar\n",
    "\n",
    "p_lr_one = float(lr.predict(x_one_df)[0])\n",
    "p_rf_one = float(rf.predict(x_one_df)[0])\n",
    "\n",
    "print(\"\\nSingle-row sanity check:\")\n",
    "print(f\"  Actual Price: ${y_true:,.0f}\")\n",
    "print(f\"  LR Pred     : ${p_lr_one:,.0f}\")\n",
    "print(f\"  RF Pred     : ${p_rf_one:,.0f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f2f8b74-f301-40a2-8416-98f984e81f42",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
