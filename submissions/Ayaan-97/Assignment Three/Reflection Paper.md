# Reflection: Data Preprocessing for Car Price Dataset
## 1. For missing values, I used a strategy based on the distribution of each feature:
* **Odometer_km (Median):** I chose the median because odometer readings often contain extreme outliers. The median is more robust than the mean, ensuring the center isn't pulled by a few high-mileage cars.
* **Doors & Accidents (Mode):** These are discrete numerical values (categories). Using the most frequent value (mode) ensures we keep the data realistic (e.g., you can't have 3.4 doors).
* **Location (Mode):** Since Location is a categorical feature, the mode was used to fill unknowns with the most common area type.
  
## 2. Outlier Handling (IQR)
I used the Interquartile Range (IQR) method to identify and cap outliers for Price and Odometer_km. 
* **Calculation:** I computed the bounds as $Q1 - 1.5 \times IQR$ and $Q3 + 1.5 \times IQR$.
* **Capping Logic:** To solve the "minus" problem where the lower bound mathematically drops below zero, I implemented a `max(0, lower)` constraint. This ensures that features like Price and Odometer remain physically possible (non-negative) while still removing extreme high-end outliers that could skew the model.
  
## 3. Feature Engineering
I added four new features to improve the predictive power of the dataset:
* **CarAge:** Calculated as `2026 - Year`. This converts the year into a direct measure of age, which usually has a linear relationship with price.
* **Km_per_year:** Created by dividing `Odometer_km` by `CarAge`. I added a `+1` constant to the denominator to prevent division-by-zero errors for brand-new cars.
* **Is_Urban:** A binary flag derived from the `Location_city` dummy variable to simplify location into a binary urban/non-urban feature.
* **Log_price:** Created as a log-transformed version of the target. This helps normalize the price distribution, making it easier for linear models to process.
  
## 4. Scaling Decisions
I used `StandardScaler` to standardize continuous features (Age, Odometer, etc.) so they have a mean of 0 and a standard deviation of 1.
* **Exclusions:** I intentionally excluded the target variables (`Price`, `Log_price`) and binary dummy variables (`Is_Urban`, `Location_*`) from scaling to maintain their interpretability and avoid distorting the 0/1 meaning of encoded categories.