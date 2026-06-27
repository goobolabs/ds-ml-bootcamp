# Data Preprocessing Reflection

## 1. Handling Missing Values

For numerical columns such as **Odometer_km**, I used the **median** instead of the mean.  
This is because median is more robust to outliers and skewed distributions, which are common in real-world car datasets. Mean could be heavily affected by extreme values like very high mileage vehicles.

For categorical columns such as **Location**, I used the **mode**.  
This is because categorical variables do not have numerical meaning, and the most frequent category is the most reasonable replacement for missing values.

For discrete integer-like columns such as **Doors**, mode was also used because these values represent fixed categories (e.g., 2, 3, 4, 5 doors) rather than continuous numbers.

---

## 2. Outlier Handling (IQR Capping)

I used the **IQR (Interquartile Range) method** with k = 1.5 to cap outliers in columns like **Price** and **Odometer_km**.

IQR was chosen because it does not assume a normal distribution and works well for skewed data. Instead of removing rows, I used **capping (winsorization)** to preserve data while reducing the effect of extreme values.

This approach helps maintain dataset size while controlling extreme influence on the model.

---

## 3. Feature Engineering

Several new features were created to improve model performance:

- **Car_Age**: calculated from `Year` to represent vehicle age. Older cars generally have lower value.
- **Km_per_Year**: derived from `Odometer_km / (Car_Age + 1)` to measure usage intensity over time.
- **IS_City**: binary encoding of city location to capture urban vs non-urban pricing differences.
- **LogPrice**: applied `log1p` transformation to reduce skewness in price distribution and improve regression stability.

These features were designed to help the model capture more meaningful patterns beyond raw values.

---

## 4. Feature Scaling

StandardScaler was applied to numerical features (excluding target variables and dummy variables).

Scaling was necessary because many machine learning models (e.g., linear regression, KNN, SVM) are sensitive to feature magnitude. Standardization ensures all features contribute equally during model training.

---

## Conclusion

Overall, the preprocessing pipeline focused on:
- Robust missing value handling (median/mode)
- Outlier control using IQR capping
- Feature engineering for better predictive signals
- Proper scaling for model stability

These steps improve data quality and increase the likelihood of better model performance.