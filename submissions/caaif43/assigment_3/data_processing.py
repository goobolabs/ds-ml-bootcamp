```python
import pandas as pd
import numpy as np

```


```python
CSV_PATH = './raw_car_dataset.csv'

df = pd.read_csv(CSV_PATH)
```


```python
# print(df.head())
# print("\n=== INITIAL HEAD ===")
# print(df.info())

```


```python
 # 2) Clean target formatting
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
# print(df.head())
```


```python
 # 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
# print(df.head(10))
```


```python
# 3) Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
```


```python
# 4) Impute missing values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]  = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])

# print(df.head(10))

```


```python
 # 5) Remove duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
# print(f"Dropped duplicates: {before} → {after}")
```


```python
# 6) IQR capping
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_size,  high_size  = iqr_fun(df["Odometer_km"])

df["Price"]  = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_size,  upper=high_size)
print(df.head(10))
```

        Price  Odometer_km  Doors  Accidents  Year  Location_City  Location_Rural  \
    0  1500.0     137830.0    4.0          1  1998              1               0   
    1  4171.0     128548.0    4.0          0  2016              0               1   
    2  5331.0     107302.0    4.0          0  2014              0               0   
    3  1500.0     141838.0    4.0          1  1999              0               0   
    4  1500.0     128548.0    3.0          0  2022              1               0   
    5  1500.0     211171.0    4.0          0  2003              1               0   
    6  1500.0     222235.0    4.0          2  2004              0               1   
    7  1500.0     105068.0    5.0          1  2002              1               0   
    8  2291.0      90015.0    4.0          0  2007              0               1   
    9  1500.0     125976.0    2.0          0  2002              1               0   
    
       Location_Suburb  CarAge   Km_per_Year  
    0                0      28   4922.500000  
    1                0      10  12854.800000  
    2                1      12   8941.833333  
    3                1      27   5253.259259  
    4                0       4  32137.000000  
    5                0      23   9181.347826  
    6                0      22  10101.590909  
    7                0      24   4377.833333  
    8                0      19   4737.631579  
    9                0      24   5249.000000  
    


```python
 # 7) One-hot encode
df = pd.get_dummies(df, columns=["location"], dtype=int)
# print(df.head())
```


```python
 # 8) Feature engineering (no leakage)
CURRENT_YEAR = 2026

df["CarAge"] = CURRENT_YEAR - df["Year"]

df["Km_per_Year"] = (
    df["Odometer_km"] /
    df["CarAge"].replace(0, np.nan))
print(df.head())
```


```python
 # 9) Feature scaling (X only; keep targets & dummies unscaled)
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

# print(df.head())
```


```python
# 9. FINAL CHECK
# ==========================

print("\n===== CLEAN DATA =====")
print(df.head())

print("\n===== FINAL INFO =====")
print(df.info())

print("\n===== FINAL MISSING VALUES =====")
print(df.isnull().sum())

# ==========================
```

    
    ===== CLEAN DATA =====
        Price  Odometer_km  Doors  Accidents  Year  Location_City  Location_Rural  \
    0  1500.0     137830.0    4.0          1  1998              1               0   
    1  4171.0     128548.0    4.0          0  2016              0               1   
    2  5331.0     107302.0    4.0          0  2014              0               0   
    3  1500.0     141838.0    4.0          1  1999              0               0   
    4  1500.0     128548.0    3.0          0  2022              1               0   
    
       Location_Suburb  CarAge   Km_per_Year  
    0                0      28   4922.500000  
    1                0      10  12854.800000  
    2                1      12   8941.833333  
    3                1      27   5253.259259  
    4                0       4  32137.000000  
    
    ===== FINAL INFO =====
    <class 'pandas.core.frame.DataFrame'>
    Index: 140 entries, 0 to 139
    Data columns (total 10 columns):
     #   Column           Non-Null Count  Dtype  
    ---  ------           --------------  -----  
     0   Price            140 non-null    float64
     1   Odometer_km      140 non-null    float64
     2   Doors            140 non-null    float64
     3   Accidents        140 non-null    int64  
     4   Year             140 non-null    int64  
     5   Location_City    140 non-null    int64  
     6   Location_Rural   140 non-null    int64  
     7   Location_Suburb  140 non-null    int64  
     8   CarAge           140 non-null    int64  
     9   Km_per_Year      140 non-null    float64
    dtypes: float64(4), int64(6)
    memory usage: 12.0 KB
    None
    
    ===== FINAL MISSING VALUES =====
    Price              0
    Odometer_km        0
    Doors              0
    Accidents          0
    Year               0
    Location_City      0
    Location_Rural     0
    Location_Suburb    0
    CarAge             0
    Km_per_Year        0
    dtype: int64
    


```python
# 10. SAVE DATASET
# ==========================

OUT_PATH = "clean_car_dataset.csv"

df.to_csv(OUT_PATH, index=False)
```


```python

```


```python

```
