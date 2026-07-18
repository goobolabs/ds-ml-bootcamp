# Process Reflection: Cleaning & Engineering the Car Dataset

**Project Details:** Data Preprocessing & Feature Engineering Pipeline  
**Name:** Ali-Salad  
**Date:** July 2026  

---

## The Core Strategy

When I first opened `car_dataset.csv`, it had all the classic issues of a messy, real-world dataset: inconsistent text formatting, string types mixed into numerical columns, weird placeholders like `??`, missing values, and massive price spikes (like a couple of cars sitting at $\$120,000+$ while most were around $\$1,500$). 

Instead of just dropping messy rows and losing valuable data, I built an end-to-end pipeline that standardizes the formatting, fixes missing blocks using domain-specific statistics, caps extreme values, and engineers fresh features to give future machine learning models more signal to work with.

---

## Behind the Decisions: Step-by-Step

### 1. Cleaning the Target and Text Errors
Before doing any math, I had to fix the data types. The `Price` column was a mix of strings with `$` and commas. I stripped those out using regex and forced it into a float. 

For the `Location` column, I caught a couple of issues. "Subrb" was clearly a typo for "Suburb", so I merged them. I also noticed some entries used `??` for unknown locations. I replaced those with actual null values (`pd.NA`) so pandas could track them properly before I handled imputation.

### 2. Strategic Imputation: Why Median vs. Mode?
When filling in missing data, a blanket approach doesn't work. I split my strategy based on how the columns were distributed:
* **Odometer (Median):** Mileage data is heavily right-skewed. A few cars have massive mileage numbers that would pull the average (mean) way too high, making it unrepresentative for a normal used car. The median cuts through that skew perfectly.
* **Doors, Accidents, Location (Mode):** These are discrete or categorical categories. You can't have 3.7 doors or 0.4 accidents. Using the mode (the most frequent value, like 4 doors or 0 accidents) keeps the dataset realistic and clean.

### 3. Dropping Duplicates
I checked for and dropped exact duplicate rows. Keeping duplicate data in a dataset this small can cause data leakage later on, which tricks you into thinking your model is performing better during validation than it actually would in the real world.

### 4. Handling Outliers with IQR Capping
The price column had some extreme outliers that would have completely warped a gradient-based model. Instead of deleting these records entirely, I used the Interquartile Range (IQR) method with a $1.5 \times \text{IQR}$ threshold. I capped (clipped) the extreme values at the upper and lower boundaries. This keeps the data size intact while stopping massive numbers from throwing off the model's loss functions.

### 5. Smart Feature Engineering
I built five new features to extract hidden context from the raw data:
* **`CarAge`:** Subtracting the car's manufacture year from our current year (2026) turns a static date into a highly useful linear age metric.
* **`Km_per_year`:** Dividing total mileage by the car's age tells us how hard the car was driven. I made sure to map any 0-year ages to `np.nan` first to prevent zero-division crashes.
* **`Accident_per_door` & `Is_Urban`:** These extract structural risk. `Is_Urban` isolates the city variable into a quick binary flag, which is a great proxy for stop-and-go wear and tear.
* **`LogPrice`:** I applied a $\log(1+x)$ transform to the price. This stabilizes the target variance and pulls high outliers closer to a normal distribution, which linear algorithms love.

### 6. Isolation-Aware Scaling
Finally, I applied a `StandardScaler` to the continuous features so they all share a mean of 0 and a variance of 1. However, I explicitly wrote the code to skip the target metrics (`Price` and `LogPrice`) to keep them interpretable. I also kept the scaler away from the one-hot encoded variables and binary flags, as scaling 0/1 indicator columns completely ruins their meaning.

---

## finaly
The end result is a highly structured, clean feature matrix saved to `clean_car_dataset.csv`. 