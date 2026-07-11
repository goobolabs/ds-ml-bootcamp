### Data Science

Data Science is the process of collecting, organizing, analyzing, and interpreting data to discover useful information and support decision-making.

### Machine Learning

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions automatically.

### Relationship Between Data Science and Machine Learning

Machine Learning is one of the tools used in Data Science. Data Science focuses on the entire data process, while Machine Learning focuses on creating predictive models.

### Real-Life Example

A government agency collects rainfall, river levels, and weather information.

- Data Science organizes and analyzes the collected data.
- Machine Learning predicts areas that are likely to experience flooding.
- Authorities use these predictions to issue early warnings and protect communities.

---

## 2. Data Science Lifecycle

The Data Science Lifecycle consists of several stages:

1. Problem Definition
2. Data Collection
3. Data Cleaning
4. Data Exploration
5. Feature Engineering
6. Model Building
7. Model Evaluation
8. Deployment

### Where Does Machine Learning Fit?

Machine Learning mainly fits into the Model Building and Model Evaluation stages.

During these stages, algorithms learn patterns from data and generate predictions that can be tested for accuracy.

---

## 3. Supervised Learning vs Unsupervised Learning

| Supervised Learning | Unsupervised Learning |
|--------------------|----------------------|
| Uses labeled data. | Uses unlabeled data. |
| Learns from known outcomes. | Finds hidden patterns in data. |
| Used for prediction. | Used for grouping and discovery. |
| Example: Predicting whether a solar panel needs maintenance based on temperature and energy output. | Example: Grouping wildlife animals based on GPS movement patterns. |
| Requires correct answers during training. | Does not require correct answers during training. |

### Conclusion

Supervised Learning learns from labeled data and is mainly used for prediction tasks. Unsupervised Learning works with unlabeled data and is used to discover hidden structures and patterns.

---

## 4. What Causes Overfitting?

Overfitting occurs when a model memorizes the training data instead of learning general patterns.

### Causes

- Small datasets
- Too many features
- Complex models
- Excessive training

### Prevention Methods

- Collect more data
- Use cross-validation
- Apply regularization
- Use simpler models
- Stop training at the appropriate time

### Example

A crop prediction model is trained using data from only one farm. The model performs very well on that farm's data but fails when used on farms in different regions because it memorized the training data instead of learning general farming patterns.

---

## 5. Training Data vs Test Data

Datasets are commonly divided into:

- Training Data (80%)
- Test Data (20%)

### Example

A school has records for 5,000 students.

- Training Data = 4,000 students
- Test Data = 1,000 students

The model learns from the training data and is then tested on the remaining data.

### Why Is This Necessary?

The test dataset helps measure how well the model performs on new data and ensures that it can generalize beyond the data used during training.

---

## 6. Case Study: Machine Learning for Wildfire Prediction

### Objective

To predict areas that are at high risk of wildfire before fires occur.

### Method

Researchers collected data from:

- Satellite images
- Temperature records
- Humidity levels
- Wind speed measurements

The data was cleaned, analyzed, and used to train Machine Learning models.

### Findings

- Earlier detection of wildfire-prone areas
- Faster emergency response planning
- Reduced environmental damage
- Improved public safety

### Data Science Lifecycle Stages Covered

- Problem Definition
- Data Collection
- Data Cleaning
- Data Exploration
- Feature Engineering
- Model Building
- Model Evaluation
- Deployment

### Conclusion

Machine Learning can help governments and environmental organizations predict wildfire risks and take preventive action before disasters occur.

---

# References

1. Han, J., Kamber, M., & Pei, J. *Data Mining: Concepts and Techniques*.

2. James, G., Witten, D., Hastie, T., & Tibshirani, R. *An Introduction to Statistical Learning*.

3. Géron, A. *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*.

4. Mitchell, T. *Machine Learning*.

5. Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*.