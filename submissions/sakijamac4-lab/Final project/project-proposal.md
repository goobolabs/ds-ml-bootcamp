# Final Project Proposal

## 1. Certificate Name
SAKARIYE JAMAC MOHAMED OSMAN

## 2. Project Title and Description
**Title: Mobile Price Range Classification**

Choosing a mobile phone at a fair price is difficult for consumers because prices depend on a mix of technical specifications rather than a single obvious factor, such as **RAM, battery power, internal memory, and camera quality**. This project predicts the **price range** of a mobile phone (Low, Medium, High, or Very High cost) based on these specifications. The problem is not limited to consumers alone  it benefits three groups: **customers**, who can estimate a fair price range for a phone before buying; **retailers**, who can price and position phones competitively within the current market; and **manufacturers**, who can see where a new phone model falls relative to existing price tiers and design or price it accordingly.

## 3. Problem Type
This project is a **Classification** problem: predicting the `price_range` category (Low cost, Medium cost, High cost, Very High cost) of a phone from its specifications.

## 4. Dataset
- **Source**: [Mobile Price Classification Dataset](https://www.kaggle.com/datasets/navjotkaushal/mobile-price-classification-dataset) (Kaggle). The dataset contains 2,000 mobile phone records downloaded from Kaggle.
- **Size**: 2,000 rows (meets the 1,000-row minimum)
- **Target column**: `price_range`  a categorical label representing the price tier of the phone (Low cost, Medium cost, High cost, Very High cost)
- **Main features (8 total)**:

| Feature | Meaning |
|---|---|
| `Battery_power_mAh` | Total battery capacity (mAh) |
| `Front_camera` | Front camera resolution (megapixels) |
| `4G` | Whether the phone supports 4G (Yes/No) |
| `Internal_memeory_gb` | Internal storage capacity (GB) |
| `Primary_camera` | Rear (primary) camera resolution (megapixels) |
| `px_height` | Pixel resolution height of the screen |
| `Pixel_width` | Pixel resolution width of the screen |
| `Ram_mb` | RAM capacity (MB) |

Only the most relevant features were selected to keep the model simple, interpretable, and focused on the smartphone characteristics that most strongly influence price. As part of future feature engineering, a combined `total_pixels` feature (`px_height` × `Pixel_width`) may be derived to capture overall screen resolution as a single measure.

## 5. Algorithms You Plan to Train
1. **Logistic Regression** (bootcamp) : a strong, interpretable baseline for multi-class classification problems like predicting 4 price categories.
2. **Decision Tree** (bootcamp) : captures non-linear relationships between specs (e.g., RAM and battery combined) and price range, and is easy to interpret.
3. **Random Forest** (bootcamp) : an ensemble of decision trees that typically improves accuracy and reduces overfitting compared to a single tree.
4. **XGBoost** (self-researched) : often outperforms simpler models on structured/tabular data like this dataset and will be compared against the bootcamp algorithms.

## 6. Evaluation Plan
- **Metrics**: Accuracy, Precision, Recall, F1-score
- **Best model selection**: **F1-score** (macro-averaged across the 4 price classes), since it balances precision and recall and is more reliable than plain accuracy when classes could be imbalanced.

## 7. Deployment Sketch
- **Framework**: FastAPI
- **Input JSON example**:
```json
{
  "Battery_power_mAh": 1500,
  "Front_camera": 5,
  "4G": "Yes",
  "Internal_memeory_gb": 32,
  "Primary_camera": 12,
  "px_height": 800,
  "Pixel_width": 1200,
  "Ram_mb": 3000
}
```
- **Output JSON example**:
```json
{
  "predicted_price_range": "High cost",
  "class_probabilities": {
    "Low cost": 0.05,
    "Medium cost": 0.15,
    "High cost": 0.65,
    "Very High cost": 0.15
  }
}
```

## 8. Repository Plan

```text
sakijamac4-lab-project/
├── dataset/
│   └── Mobile.csv
├── src/
│   ├── preprocess.py
│   └── train_classifiers.py
├── api/
│   └── app.py
├── models/
│   └── best_model.pkl
├── README.md
└── project_paper.md
```

