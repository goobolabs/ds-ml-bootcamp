# 🚗 Reflection Paper – Car Price Prediction

**👨‍🎓 Student:** Mohamed Abdirahman

---

# 📑 Table of Contents

* 🚀 What Did You Implement?
* ⚖️ Comparison of Models
* 🌲 Understanding Random Forest
* 📊 Metrics Discussion
* 💡 My Findings
* ✅ Conclusion

---

# 🚀 What Did You Implement?

In this assignment, I built **two machine learning regression models** to predict car prices using the cleaned dataset from **Assignment Three**.

## 📂 Data Preparation

Before training the models, I:

* 📥 Loaded the cleaned dataset.
* 🎯 Selected **Price** as the target variable.
* 📋 Used all remaining columns except **Price** and **LogPrice** as input features.

## ⚙️ Model Training

The dataset was divided into:

* 🟢 **80% Training Data**
* 🔵 **20% Testing Data**

using:

```python
random_state = 42
```

to ensure reproducible results.

The following regression models were trained:

* 📉 Linear Regression
* 🌲 Random Forest Regressor

## 📏 Model Evaluation

After training, both models were evaluated using four regression metrics:

* 📈 R² Score
* 📏 Mean Absolute Error (MAE)
* 📐 Mean Squared Error (MSE)
* 📊 Root Mean Squared Error (RMSE)

Finally, I performed a **sanity check** by comparing the actual selling price of one car with the predictions produced by both models.

---

# ⚖️ Comparison of Models

Both models successfully predicted car prices, but their prediction accuracy differed.

During the sanity check, I observed that:

* 🌲 **Random Forest** produced predictions closer to the actual selling price.
* 📉 **Linear Regression** showed slightly larger prediction errors.

## 📉 Linear Regression

Linear Regression assumes a **linear relationship** between the features and the target variable.

### ✅ Advantages

* Easy to understand
* Fast to train
* Simple to interpret

### ❌ Limitations

* Cannot model complex relationships.
* Performance decreases when data is non-linear.

---

## 🌲 Random Forest Regression

Random Forest can model much more complicated relationships because it combines predictions from many decision trees.

### ✅ Advantages

* Higher prediction accuracy
* Handles nonlinear relationships
* More robust with real-world datasets

As a result, Random Forest generally produced better predictions for car prices.

---

# 🌲 Understanding Random Forest

Random Forest is an **ensemble machine learning algorithm**.

Instead of relying on a single decision tree, it creates many trees using different samples of the training data.

Each decision tree makes its own prediction.

The Random Forest model then calculates the **average** of all predictions.

## 🎯 Benefits

* 🌳 Combines multiple decision trees
* 📉 Reduces prediction errors
* 🛡️ Less sensitive to overfitting
* 📊 Produces more stable predictions

Because it combines many trees instead of depending on only one, Random Forest is generally **more accurate** and **more reliable** than a single decision tree.

---

# 📊 Metrics Discussion

The performance of both regression models was evaluated using four standard metrics.

## 📈 R² Score

Measures how well the model explains the variation in car prices.

Higher values indicate better performance.

---

## 📏 Mean Absolute Error (MAE)

Measures the average prediction error.

Lower MAE indicates more accurate predictions.

---

## 📐 Mean Squared Error (MSE)

Measures the average squared prediction error.

Large prediction errors receive greater penalties.

---

## 📊 Root Mean Squared Error (RMSE)

Represents prediction error in the same unit as car prices.

This makes RMSE easier to interpret than MSE.

---

## 📋 Metric Summary

| Metric      | Purpose                 | Better Value |
| ----------- | ----------------------- | ------------ |
| 📈 R² Score | Explains variation      | Higher       |
| 📏 MAE      | Average error           | Lower        |
| 📐 MSE      | Penalizes large errors  | Lower        |
| 📊 RMSE     | Error in original units | Lower        |

The model with the **higher R² Score** and the **lower MAE and RMSE** demonstrated better predictive performance.

These metrics made it easy to compare both regression models and identify the more reliable one.

---

# 💡 My Findings

This assignment helped me understand that different regression algorithms can produce different prediction accuracy even when they use the same dataset.

## 📉 Linear Regression

I learned that Linear Regression is:

* ⚡ Fast
* 📖 Easy to understand
* 🧮 Simple to interpret

It works best when the relationship between variables is approximately linear.

---

## 🌲 Random Forest Regression

I prefer **Random Forest Regression** for predicting car prices because vehicle prices depend on many factors, including:

* 🚗 Mileage
* 📅 Vehicle Age
* 🚨 Accident History
* 📍 Location

These relationships are often nonlinear, making Random Forest a better choice.

The model captured these complex patterns more effectively and produced more accurate and reliable predictions.

---

# ✅ Conclusion

This assignment significantly improved my understanding of:

* 🤖 Machine Learning Regression
* 📊 Model Evaluation
* 📈 Regression Performance Metrics
* 🌲 Random Forest Regression
* ⚖️ Comparing Multiple Machine Learning Models

By comparing Linear Regression and Random Forest, I learned the importance of evaluating multiple models before selecting the best one for a prediction task.

Overall, **Random Forest Regression** proved to be the better model for predicting car prices because it handled complex relationships more effectively and achieved more accurate predictions.

---

# 🙏 Thank You

**🚗 Reflection Paper – Car Price Prediction**

**Prepared by:** Mohamed Abdirahman
