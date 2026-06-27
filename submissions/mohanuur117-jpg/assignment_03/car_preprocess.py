import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def run_pipeline():
    print("="*60)
    print("STEP 1: Load & Inspect")
    print("="*60)
    # Load dataset
    df = pd.read_csv("raw_car_dataset (1).csv")
    
    print("\n--- First 10 Rows ---")
    print(df.head(10))
    print(f"\nShape of dataset: {df.shape}")
    
    print("\n--- Info ---")
    df.info()
    
    print("\n--- Missing Values Count ---")
    print(df.isnull().sum())
    
    print("\n--- Raw Location Value Counts ---")
    print(df['Location'].value_counts(dropna=False))
    
    print("\n[Data Quality Assessment]:")
    print("- 'Price' has a mixed format with string representations ($ signs and commas) and a potential severe right skew.")
    print("- 'Odometer_km' contains missing values.")
    print("- 'Doors' contains missing values.")
    print("- 'Location' has typos ('Subrb'), placeholders ('??'), and missing entries.")
    print("- Duplicate records are highly probable given the frequency of identical rows.")

    print("\n" + "="*60)
    print("STEP 2: Clean Target Formatting (Price)")
    print("="*60)
    # String manipulation to strip structural noise
    df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False)
    df['Price'] = df['Price'].str.replace(',', '', regex=False)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    
    print(f"Price column data type: {df['Price'].dtype}")
    print(f"Price column skewness: {df['Price'].skew():.4f}")

    print("\n" + "="*60)
    print("STEP 3: Fix Category Errors before Imputation")
    print("="*60)
    # Standardize spaces and text case
    df['Location'] = df['Location'].astype(str).str.strip()
    
    # Correct typographical errors mapping
    typo_map = {'Subrb': 'Suburb', 'Rurl': 'Rural', 'Cty': 'City'}
    df['Location'] = df['Location'].replace(typo_map)
    
    # Standardize semantic blanks/placeholders to true NaNs
    missing_placeholders = ['??', 'unknown', 'blank strings', 'N/A', '', 'nan', 'None']
    df['Location'] = df['Location'].replace(missing_placeholders, np.nan)
    
    print("--- Updated Location Value Counts (incl. NaN) ---")
    print(df['Location'].value_counts(dropna=False))

    print("\n" + "="*60)
    print("STEP 4: Impute Missing Values")
    print("="*60)
    # Continuous variable imputation
    odo_median = df['Odometer_km'].median()
    df['Odometer_km'] = df['Odometer_km'].fillna(odo_median)
    
    # Categorical and discrete variable imputation
    doors_mode = df['Doors'].mode()[0]
    df['Doors'] = df['Doors'].fillna(doors_mode)
    
    accidents_mode = df['Accidents'].mode()[0]
    df['Accidents'] = df['Accidents'].fillna(accidents_mode)
    
    location_mode = df['Location'].mode()[0]
    df['Location'] = df['Location'].fillna(location_mode)
    
    print("--- Missing Values After Imputation ---")
    print(df.isnull().sum())
    print("\n[Imputation Rationale]:")
    print(f"- Odometer_km: Imputed using Median ({odo_median}) to remain robust against extreme mileage outliers.")
    print(f"- Doors & Accidents: Discrete structural metrics imputed using Mode ({doors_mode}, {accidents_mode}).")
    print(f"- Location: Categorical feature imputed using Mode ('{location_mode}') to reflect the most frequent structural class.")

    print("\n" + "="*60)
    print("STEP 5: Remove Duplicates")
    print("="*60)
    shape_before = df.shape
    df = df.drop_duplicates().reset_index(drop=True)
    shape_after = df.shape
    
    print(f"Dataset shape before deduplication: {shape_before}")
    print(f"Dataset shape after deduplication:  {shape_after}")
    print(f"Total duplicate rows removed:       {shape_before[0] - shape_after[0]}")

    print("\n" + "="*60)
    print("STEP 6: Outlier Treatment (IQR Capping)")
    print("="*60)
    # Outlier threshold determination logic
    def get_iqr_bounds(series):
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return lower_bound, upper_bound

    price_lower, price_upper = get_iqr_bounds(df['Price'])
    odo_lower, odo_upper = get_iqr_bounds(df['Odometer_km'])
    
    print(f"Price Limits:       Lower = {price_lower:.2f} | Upper = {price_upper:.2f}")
    print(f"Odometer_km Limits: Lower = {odo_lower:.2f} | Upper = {odo_upper:.2f}")
    
    # Apply soft capping transformation bounds
    df['Price'] = df['Price'].clip(lower=price_lower, upper=price_upper)
    df['Odometer_km'] = df['Odometer_km'].clip(lower=odo_lower, upper=odo_upper)
    
    print("\n--- Descriptives Summary After Capping ---")
    print(df[['Price', 'Odometer_km']].describe())

    print("\n" + "="*60)
    print("STEP 7: One-Hot Encoding")
    print("="*60)
    # Generate binary structural flags
    df = pd.get_dummies(df, columns=['Location'], prefix='Location', dtype=int)
    dummy_cols = [col for col in df.columns if col.startswith('Location_')]
    print("Generated One-Hot Encoded columns:")
    print(dummy_cols)

    print("\n" + "="*60)
    print("STEP 8: Feature Engineering")
    print("="*60)
    # Current Reference temporal node set to 2026 based on workspace parameters
    current_year = 2026
    
    # Calculate operational lifetime metrics
    df['CarAge'] = current_year - df['Year']
    # Enforce minimum threshold to insulate calculations against operational divisions by zero
    df['CarAge'] = df['CarAge'].apply(lambda x: 1 if x <= 0 else x)
    
    df['Km_per_year'] = df['Odometer_km'] / df['CarAge']
    
    # Spatial consolidation mapping logic
    urban_cols = [col for col in ['Location_City', 'Location_Suburb'] if col in df.columns]
    df['Is_Urban'] = df[urban_cols].sum(axis=1).apply(lambda x: 1 if x >= 1 else 0)
    
    # Target transformation stabilization
    df['LogPrice'] = np.log1p(df['Price'])
    
    print("Engineered Features summary sample:")
    print(df[['Year', 'CarAge', 'Odometer_km', 'Km_per_year', 'Is_Urban', 'Price', 'LogPrice']].head(5))

    print("\n" + "="*60)
    print("STEP 9: Feature Scaling")
    print("="*60)
    # Identify explicit operational targets for continuous normalization scales
    continuous_features = ['Odometer_km', 'Doors', 'Accidents', 'Year', 'CarAge', 'Km_per_year']
    
    scaler = StandardScaler()
    df[continuous_features] = scaler.fit_transform(df[continuous_features])
    
    print("Sample of normalized scale features (StandardScaler):")
    print(df[continuous_features].head(5))

    print("\n" + "="*60)
    print("STEP 10: Final Checks & Persistence")
    print("="*60)
    print("\n--- Final Dataset Profile Info ---")
    df.info()
    
    print("\n--- Post-Pipeline Final Missing Value Matrix Summary ---")
    print(df.isnull().sum())
    
    print("\n--- Descriptive Summary Metrics Summary ---")
    print(df.describe())
    
    # Save processed dataframe array down to csv
    df.to_csv("clean_car_dataset.csv", index=False)
    print("\nSuccess: Cleaned data systematically structured and written to 'clean_car_dataset.csv'")

    print("\n" + "="*60)
    print("SYSTEM CHECKS: Assertions Verification")
    print("="*60)
    
    # Runtime compliance test blocks
    assert pd.api.types.is_float_dtype(df['Price']), "Price must be float type array."
    assert 'LogPrice' in df.columns and pd.api.types.is_numeric_dtype(df['LogPrice']), "LogPrice configuration verification error."
    assert df.isnull().sum().sum() == 0, "Null instances leakage detected within final execution state."
    assert len(dummy_cols) > 0, "One-hot mapping transformation breakdown."
    
    for feat in continuous_features:
        mean_val = df[feat].mean()
        std_val = df[feat].std(ddof=0) # Match population parameters metrics computed by standard scaler
        assert np.isclose(mean_val, 0, atol=1e-2), f"{feat} scaling evaluation failed mean benchmark"
        assert np.isclose(std_val, 1, atol=1e-2), f"{feat} scaling evaluation failed unit variance benchmark"
        
    print("All pipeline assertions pass successfully.")

if __name__ == "__main__":
    run_pipeline()
