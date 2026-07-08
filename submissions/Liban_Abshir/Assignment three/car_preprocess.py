"""
Car Price Dataset - Lesson 3 Preprocessing Pipeline
Author: Liban Abshir
"""

import numpy as np
import pandas as pd
from scipy.stats import skew

# --- config ---
RAW_PATH = "dataset/raw_car_dataset.csv"
OUTPUT_PATH = "car_l3_clean_ready.csv"
OUTPUT_COPY = "clean_car_dataset.csv"  # same file, second name from brief


def main():
   
    print("\n" + "=" * 60)
    print("STEP 1: Load & Inspect")
    print("=" * 60)

    df = pd.read_csv(RAW_PATH)
    print("\nFirst 10 rows:")
    print(df.head(10))
    print(f"\nShape: {df.shape}")
    print("\nInfo:")
    df.info()
    print("\nMissing counts:")
    print(df.isna().sum())
    print("\nLocation value counts:")
    print(df["Location"].value_counts(dropna=False))

    print("\nKey issues I noticed:")
    print("- Price has $ signs, commas, and some weird high/low values")
    print("- Location has typos (Subrb, Citty) and '??' entries")
    print("- Missing values in almost every column")
    print("- Probably some duplicate rows too")

    print("\n" + "=" * 60)
    print("STEP 2: Clean Target Formatting (Price)")
    print("=" * 60)


    df["Price"] = (
        df["Price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace({"": np.nan, "nan": np.nan})
    )
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    print(f"Price dtype: {df['Price'].dtype}")
    print(f"Price skewness: {skew(df['Price'].dropna()):.3f}")

  
    print("\n" + "=" * 60)
    print("STEP 3: Fix Category Errors (Location)")
    print("=" * 60)

    df["Location"] = df["Location"].astype(str).str.strip().str.lower()
    df["Location"] = df["Location"].replace({"nan": np.nan, "??": np.nan, "": np.nan})

    typo_map = {
        "subrb": "Suburb",
        "suburb": "Suburb",
        "citty": "City",
        "city": "City",
        "rural": "Rural",
    }
    df["Location"] = df["Location"].map(typo_map)

    print("Location counts after cleanup (including missing):")
    print(df["Location"].value_counts(dropna=False))

    # make sure numeric cols are actually numeric before imputation
    for col in ["Odometer_km", "Doors", "Accidents", "Year"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

   
    print("\n" + "=" * 60)
    print("STEP 4: Impute Missing Values")
    print("=" * 60)

    print("My choices:")
    print("- Odometer_km -> median (odometer is continuous, median handles skew)")
    print("- Doors/Accidents -> mode (small integer categories)")
    print("- Location -> mode (most common area type)")

    df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
    df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
    df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
    df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

   
    df["Year"] = df["Year"].fillna(df["Year"].median())

    # price missing -> median price (need target for later steps)
    df["Price"] = df["Price"].fillna(df["Price"].median())

    print("\nMissing counts after imputation:")
    print(df.isna().sum())

 
    print("\n" + "=" * 60)
    print("STEP 5: Remove Duplicates")
    print("=" * 60)

    before = df.shape
    df = df.drop_duplicates()
    after = df.shape
    removed = before[0] - after[0]

    print(f"Shape before: {before}")
    print(f"Shape after:  {after}")
    print(f"Rows removed: {removed}")

   
    print("\n" + "=" * 60)
    print("STEP 6: Outliers - IQR Capping")
    print("=" * 60)

    def iqr_cap(series, name):
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        capped = series.clip(lower, upper)
        n_capped = ((series < lower) | (series > upper)).sum()
        print(f"\n{name}:")
        print(f"  bounds: [{lower:.1f}, {upper:.1f}]  |  values capped: {n_capped}")
        return capped

    df["Price"] = iqr_cap(df["Price"], "Price")
    df["Odometer_km"] = iqr_cap(df["Odometer_km"], "Odometer_km")

    print("\nAfter capping (quick summary):")
    print(df[["Price", "Odometer_km"]].describe().round(2))


    print("\n" + "=" * 60)
    print("STEP 7: One-Hot Encode Location")
    print("=" * 60)

    location_dummies = pd.get_dummies(df["Location"], prefix="Location", dtype=int)
    dummy_cols = list(location_dummies.columns)
    df = pd.concat([df.drop(columns=["Location"]), location_dummies], axis=1)

    print("New dummy columns created:")
    for c in dummy_cols:
        print(f"  - {c}")

  
    print("\n" + "=" * 60)
    print("STEP 8: Feature Engineering")
    print("=" * 60)

    current_year = 2026  


    df["CarAge"] = current_year - df["Year"]


    df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

  
    df["Is_Urban"] = 0
    if "Location_City" in df.columns:
        df["Is_Urban"] = df["Is_Urban"] | df["Location_City"]
    if "Location_Suburb" in df.columns:
        df["Is_Urban"] = df["Is_Urban"] | df["Location_Suburb"]

    # alternative target - not used as a model feature
    df["LogPrice"] = np.log(df["Price"] + 1)

    print("Engineered features added:")
    print("  - CarAge (2026 - Year)")
    print("  - Km_per_year (Odometer_km / CarAge, safe div)")
    print("  - Is_Urban (City or Suburb flag)")
    print("  - LogPrice = log(Price + 1) [target alt, not a feature]")

    # ============================================================
    # STEP 9: Feature Scaling (X only)
    # ============================================================
    print("\n" + "=" * 60)
    print("STEP 9: Feature Scaling")
    print("=" * 60)

    # columns we do NOT scale
    skip_scale = {"Price", "LogPrice", "Is_Urban"} | set(dummy_cols)

    scale_cols = [c for c in df.select_dtypes(include=[np.number]).columns if c not in skip_scale]

    print("Scaling these continuous columns:")
    print(scale_cols)
    print("(Price, LogPrice, dummies, Is_Urban left as-is)")

    for col in scale_cols:
        mu = df[col].mean()
        sigma = df[col].std(ddof=0)  # population std
        if sigma == 0:
            df[col] = 0.0
        else:
            df[col] = (df[col] - mu) / sigma

    print("\nSample of scaled values (first 5 rows, first 4 scaled cols):")
    print(df[scale_cols[:4]].head())

    # quick check means ~0 std ~1
    print("\nScaling sanity (should be ~0 mean, ~1 std):")
    for col in scale_cols[:3]:
        print(f"  {col}: mean={df[col].mean():.4f}, std={df[col].std(ddof=0):.4f}")

    # ============================================================
    # STEP 10: Final Checks & Save
    # ============================================================
    print("\n" + "=" * 60)
    print("STEP 10: Final Checks & Save")
    print("=" * 60)

    print("\nFinal info:")
    df.info()
    print("\nFinal missing counts:")
    print(df.isna().sum())
    print("\nDescribe (selected cols):")
    show_cols = ["Price", "LogPrice", "Odometer_km", "CarAge", "Km_per_year", "Is_Urban"]
    show_cols = [c for c in show_cols if c in df.columns]
    print(df[show_cols].describe().round(3))

    df.to_csv(OUTPUT_PATH, index=False)
    df.to_csv(OUTPUT_COPY, index=False)
    print(f"\nSaved cleaned data to:")
    print(f"  - {OUTPUT_PATH}")
    print(f"  - {OUTPUT_COPY}")

    # --- assertions from assignment ---
    assert df["Price"].dtype in [np.float64, float]
    assert "LogPrice" in df.columns and np.issubdtype(df["LogPrice"].dtype, np.number)
    assert df.isna().sum().sum() == 0
    assert any(c.startswith("Location_") for c in df.columns)

    for col in scale_cols:
        assert abs(df[col].mean()) < 0.01, f"{col} mean not ~0"
        assert abs(df[col].std(ddof=0) - 1.0) < 0.01, f"{col} std not ~1"

    print("\nAll sanity checks passed.")


if __name__ == "__main__":
    main()
