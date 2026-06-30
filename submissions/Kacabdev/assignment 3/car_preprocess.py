import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# STEP ONE
# 1. Data Loading 
CSV_PATH = "raw_car_dataset.csv"

df = pd.read_csv(CSV_PATH)


# 2. Showing head(10), shape, info, missing counts & location value counts
print("\n=== Head ===")
print(df.head(10))

print("\n=== Shape ===")
print(df.shape)

print("\n=== INFO ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Location counts ===")
print(df["Location"].value_counts(dropna=False))


# STEP TWO 

# 1. Price cleaning
print("\n=== Price Cleaning ===")
df["Price"] = (df["Price"].replace(r"[\$,]", "", regex=True).astype(float))

print("\n Price Skewness: ")
print(df["Price"].skew())



# Step Three
# Fix category errors before imputation
#sidan ayan hore u aragnay 
#subrb = typo error. ?? = unknown value, NaN = missing


print("\n=== Step 3: Fix catergoty Erros")

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": np.nan})

print("\n Location Counts After fixing:")
print(df["Location"].value_counts(dropna=False))

#Step 4 Impute Missing values
#inako adegsanyna sidan hose
#odometer_km = median, Doors = mode, Accidents = mode, locatin = mode

print("\n=== Step 4: Imputation ===")

print("\n Missing Before: ")
print(df.isnull().sum())

#values ka an buxino maraka
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("\n Missing After:")
print(df.isnull().sum())

#Step 5 REMOVING DUPLICATES

before_rows = len(df)
df = df.drop_duplicates()

after_rows = len(df)

rows_removed = before_rows - after_rows

print("Rows Before: ", before_rows)
print("Rows After: ", after_rows)
print("Duplicates Removed: ", rows_removed)


#Step 6 Price IQR capping

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lowe_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["Price"] = df["Price"].clip(lower=lowe_bound, upper=upper_bound)


print("\nPrice Outlier Bounds")
print("Lower: ", lowe_bound)
print("Upper: ", upper_bound)

print(df["Price"].describe())


#Odoometer IQR capping

Q1 = df["Odometer_km"].quantile(0.25)
Q3 = df["Odometer_km"].quantile(0.75)

IQR = Q3 - Q1

lowe_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["Odometer_km"] = df["Odometer_km"].clip(lower=lowe_bound, upper=upper_bound)

print("\nOdometer Outlier Bounds")
print("Lower: ", lowe_bound)
print("Upper: ", upper_bound)

print(df["Odometer_km"].describe())


#Step 7: One hot encoding location

print("\n=== Step 7: One hot encoding location ===")

#before encoding
print("Shape before encoding: ", df.shape)
print("Location unique values: ", df["Location"].unique())

#One hot encodeing location
df = pd.get_dummies(df, columns=["Location"], prefix="Location", drop_first=False)

#After encoding
print("Shape after encoding: ", df.shape)


#here are the new columns created
location_cols = [col for col in df.columns if col.startswith("Location_")]
dummy_cols = [c for c in df.columns if c.startswith("Location_")]
df[dummy_cols] = df[dummy_cols].astype(int)
print("New location columns: ", location_cols)


print(df[location_cols].head())


#Step 8 featuring / feature engineerin 
print("\n===== STEP 8: FEATURE ENGINEERING =====")


     # 1. CarAge (assumes Year column exists; if not tell me)
if "Year" in df.columns:
    df["CarAge"] = 2026 - df["Year"]
    print("CarAge created using Year column.")
else:  #Waa hadii uuna year column kenu jiri lahayn lacala wyan
    print("WARNING: No Year column found. CarAge skipped.")

      # 2. Km per year (safe division)
if "CarAge" in df.columns:
    df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
    df["Km_per_year"] = df["Km_per_year"].fillna(df["Odometer_km"])
else:
    print("Km_per_year skipped (no CarAge).")

     # 3. Is_Urban (City or Suburb = 1, Rural = 0)
df["Is_Urban"] = ((df.get("Location_City", 0) == 1) | 
                  (df.get("Location_Suburb", 0) == 1)).astype(int)

     # 4. Log target (NOT feature leakage for X later)
df["LogPrice"] = np.log(df["Price"] + 1)

print("\nNew feature sample:")
cols_to_show = [c for c in ["CarAge", "Km_per_year", "Is_Urban", "LogPrice"] if c in df.columns]
print(df[cols_to_show].head())

print("\nCurrent shape:", df.shape)

#Step 9: featuer scalling
print("\n===== STEP 9: FEATURE SCALLING =====")

scale_cols = []
for col in ["Odometer_km", "CarAge", "Km_per_year"]:
    if col in df.columns:
        scale_cols.append(col)

print("Columns to scale:", scale_cols)

scaler = StandardScaler()

df_scaled = df.copy()
df_scaled[scale_cols] = scaler.fit_transform(df_scaled[scale_cols])

print("\nSample after scaling:")
print(df_scaled[scale_cols].head())

print("\nCheck mean (should be ~0):")
print(df_scaled[scale_cols].mean())

print("\nCheck std (should be ~1):")
print(df_scaled[scale_cols].std())



#Step 10:  Final checks and Save

    # 1. Missing values checking
missing = df.isnull().sum()
print("\nMissing values per column:")
print(missing)

print("\nTotal missing values:", missing.sum())
  #Asserting weye
assert missing.sum() == 0, "ERROR: Missing values still exist!"


    # 2. Basic structure checking 
print("\nFinal shape:", df.shape)
print("\nData types:\n", df.dtypes)

    # 3. Check required columns exist
assert "LogPrice" in df.columns, "LogPrice missing!"
assert any(col.startswith("Location_") for col in df.columns), "Location encoding missing!"

    # 4. Small describe summary
print("\nDescribe (numeric):")
print(df.describe())

  # 5. Save files
df.to_csv("car_l3_clean_ready.csv", index=False)

print("\nFiles saved:")
print("- car_l3_clean_ready.csv")
print("\nHawshu way dhantahay ✔")
