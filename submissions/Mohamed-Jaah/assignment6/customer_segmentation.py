import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

def iqr_fun(series, k=1.5):
    """Calculate the lower and upper bounds using the Interquartile Range method."""
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

def main():
    # 1. Dynamic Directory Scanning and Data Loading
    dataset_dir = r"D:\Dugsiiye\AI & Mechine Learning Course\DS & ML\assignment-Submissions\ds-ml-bootcamp\dataset"
    target_file = "raw_wholesale_customers.csv" 
    CSV_PATH = os.path.join(dataset_dir, target_file)
    
    print("--- STEP 1: INITIALIZING DATA LOAD ---")
    if not os.path.exists(dataset_dir):
        raise FileNotFoundError(f"The path directory does not exist: {dataset_dir}")
    
    # Check if the specific target file exists
    if not os.path.exists(CSV_PATH):
        print(f"\n[!] ALERT: Could not find '{target_file}' in the dataset directory.")
        print("Checking directory contents to see the exact file names available...")
        available_files = os.listdir(dataset_dir)
        print(f"Available files found: {available_files}\n")
        raise FileNotFoundError(
            f"Could not locate '{target_file}' inside {dataset_dir}.\n"
            f"Please verify its spelling against the available files listed above!"
        )
        
    df = pd.read_csv(CSV_PATH)
    print("Successfully loaded dataset!")
    print("--- RAW DATA PREVIEW ---")
    print(df.head())
    
    # 2. Extract and Outlier-Cap Continuous Spending Features
    FEATURES = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
    X = df[FEATURES].copy()
    
    print("\n--- STEP 2: OUTLIER CAPPING VIA IQR BOUNDS ---")
    for feature in FEATURES:
        lower_bound, upper_bound = iqr_fun(X[feature])
        # Clip values to lie within IQR bounds
        X[feature] = X[feature].clip(lower=lower_bound, upper=upper_bound)
        print(f"{feature:<17} | Bounds: [{lower_bound:9.2f}, {upper_bound:9.2f}] | "
              f"Actual Min/Max after cap: [{X[feature].min():8.2f}, {X[feature].max():8.2f}]")
        
    # Update the primary dataframe with the capped features
    df[FEATURES] = X
    print("\nCapped Feature Preview:")
    print(X.head())
    
    # 3. Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("\n--- STEP 3: FEATURE SCALING ---")
    print(f"Scaled feature matrix shape: {X_scaled.shape}")
    print("First 3 rows of scaled matrix:\n", X_scaled[:3])
    
    # 4. Elbow Method Optimization Log (k=1 to 10)
    print("\n--- STEP 4: ELBOW METHOD OPTIMIZATION LOG ---")
    for k_val in range(1, 11):
        km = KMeans(n_clusters=k_val, n_init="auto", random_state=42)
        km.fit(X_scaled)
        print(f"k={k_val:<2} → Within-Cluster SSE (Inertia) = {km.inertia_:.2f}")
        
    # 5. Fit Final K-Means Clustering Model (Chosen k=3)
    K_OPTIMAL = 3
    print(f"\n--- STEP 5: FITTING FINAL MODEL WITH k={K_OPTIMAL} ---")
    kmeans = KMeans(n_clusters=K_OPTIMAL, n_init="auto", random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    
    # Append integer labels back to our main DataFrame
    df["Cluster"] = labels.astype(int)
    print(df.head())
    
    # 6. Evaluate Model Metrics
    sil = silhouette_score(X_scaled, labels)
    dbi = davies_bouldin_score(X_scaled, labels)
    print("\n=== STEP 6: CLUSTERING MODEL METRICS ===")
    print(f"Silhouette Score : {sil:.3f} (closer to +1 is better)")
    print(f"Davies–Bouldin   : {dbi:.3f} (lower is better)")
    
    # 7. Reverse-Transform Cluster Centers for Spending Profiles
    print("\n--- STEP 7: REVERSED CLUSTER PROFILE CENTERS (ORIGINAL SCALE) ---")
    centers_scaled = kmeans.cluster_centers_
    centers_original = scaler.inverse_transform(centers_scaled)
    
    centers_df = pd.DataFrame(centers_original, columns=FEATURES)
    centers_df.index.name = "Cluster"
    print(centers_df.round(2))
    
    # 8. Run Sanity Checks on Categorical Exclusions
    print("\n--- STEP 8: SANITY CHECK (INSPECTING LABELS VS BEHAVIORAL CATEGORIES) ---")
    sample_idx = [0, 1, 2]
    sanity = df.loc[sample_idx, ["Channel", "Region"] + FEATURES + ["Cluster"]]
    print(sanity)
    
    # 9. Persist Outputs to CSV into your specific Assignment 6 path
    OUT_PATH = r"D:\Dugsiiye\AI & Mechine Learning Course\DS & ML\assignment-Submissions\ds-ml-bootcamp\submissions\Mohamed-Jaah\assignment6\segmented_wholesale_customer.csv"
    
    # Make sure the assignment directory exists before exporting
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    
    df.to_csv(OUT_PATH, index=False)
    print(f"\nExecution Complete! Structured data exported successfully to absolute path:\n'{OUT_PATH}'")

if __name__ == "__main__":
    main()