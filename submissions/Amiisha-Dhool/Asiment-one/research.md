# Data Science and Machine Learning Assignment

## 1. Define Data Science and Machine Learning. What is the relationship between them?

**Data Science** is the field of collecting, processing, analyzing, and interpreting data to extract useful insights and support decision-making. It combines statistics, programming, and domain knowledge to solve real-world problems.

**Machine Learning (ML)** is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions without being explicitly programmed.

### Relationship Between Data Science and Machine Learning

Machine Learning is a subset of Data Science. Data Science involves the entire process of working with data, while Machine Learning focuses specifically on building models that can learn from data and make predictions.

### Real-Life Example

Netflix uses Data Science to collect and analyze user viewing behavior. Machine Learning algorithms then use this data to recommend movies and TV shows based on the user's interests.

---

## 2. Describe the Data Science Lifecycle

The Data Science Lifecycle consists of the following stages:

### 1. Problem Definition

Identify the business or research problem that needs to be solved.

### 2. Data Collection

Gather data from databases, websites, sensors, surveys, or APIs.

### 3. Data Cleaning and Preparation

Remove errors, duplicates, and missing values to improve data quality.

### 4. Exploratory Data Analysis (EDA)

Analyze and visualize data to understand patterns and relationships.

### 5. Feature Engineering

Create and select useful variables that improve model performance.

### 6. Model Building

Develop Machine Learning models using prepared data.

### 7. Evaluation

Measure model performance using metrics such as accuracy, precision, and recall.

### 8. Deployment

Implement the model in a real-world environment.

### 9. Monitoring

Continuously monitor and update the model to maintain performance.

### Where Does Machine Learning Fit?

Machine Learning is mainly used during the **Model Building** stage because this is where algorithms are trained on data to make predictions or classifications.

---

## 3. Compare Supervised Learning and Unsupervised Learning

| Supervised Learning     | Unsupervised Learning          |
| ----------------------- | ------------------------------ |
| Uses labeled data       | Uses unlabeled data            |
| Predicts outcomes       | Finds hidden patterns          |
| Requires known outputs  | No known outputs required      |
| Example: Spam Detection | Example: Customer Segmentation |

### Example of Supervised Learning

Email spam detection, where emails are labeled as "spam" or "not spam."

### Example of Unsupervised Learning

Customer segmentation, where customers are grouped according to purchasing behavior without predefined labels.

---

## 4. What Causes Overfitting? How Can It Be Prevented?

### Overfitting

Overfitting occurs when a Machine Learning model learns the training data too closely, including noise and irrelevant details, resulting in poor performance on new data.

### Causes

* Small training dataset
* Complex models
* Too many features
* Excessive training

### Prevention Methods

* Use more training data
* Apply cross-validation
* Use regularization techniques
* Perform feature selection
* Use simpler models
* Apply early stopping during training



## 5. Explain How Training Data and Test Data Are Split

Datasets are typically divided into:

* **Training Set:** 70–80%
* **Test Set:** 20–30%

The training set is used to train the model, while the test set is used to evaluate its performance on unseen data.

### Why Is This Necessary?

* Prevents overfitting
* Measures model generalization
* Provides reliable performance evaluation

For example, if a model achieves 98% accuracy on training data but only 65% on test data, it indicates overfitting.



## 6. Case Study: Machine Learning in Healthcare

### Research Paper

**Rajpurkar, P., et al. (2017). CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning. Stanford University.**

### Objective

The study aimed to develop a deep learning model capable of detecting pneumonia from chest X-ray images.

### Methodology

* Collected over 100,000 chest X-ray images.
* Cleaned and labeled the dataset.
* Trained a deep Convolutional Neural Network (CNN).
* Evaluated performance against radiologists.

### Findings

* The model achieved performance comparable to experienced radiologists.
* Improved speed and efficiency in diagnosing pneumonia.
* Demonstrated the potential of AI-assisted healthcare systems.

# Data Science Lifecycle Stages Covered

* Problem Definition
* Data Collection
* Data Preparation
* Model Building
* Evaluation
* Deployment Potential

 Conclusion

This case study shows how Data Science and Machine Learning can improve healthcare by providing faster and more accurate disease diagnosis.


# References

1. Rajpurkar, P., Irvin, J., Zhu, K., et al. (2017). *CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning*. Stanford University.

2. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd Edition). O'Reilly Media.

3. Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media.

4. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd Edition). Springer.

5. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.

6. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd Edition). Morgan Kaufmann.
