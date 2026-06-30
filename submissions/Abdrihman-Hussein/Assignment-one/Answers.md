# Assignment One: Data Science and Machine Learning

## 1. Define Data Science and Machine Learning. What is the relationship between them? Use a real-life example to illustrate how they work together.

### Data Science

Data Science is the process of collecting, cleaning, analyzing, and interpreting data to gain useful insights and support decision-making. It combines statistics, programming, and domain knowledge to solve real-world problems.

### Machine Learning

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions without being explicitly programmed for every task.

### Relationship Between Data Science and Machine Learning

Machine Learning is a tool used within Data Science. Data Science focuses on the entire process of working with data, while Machine Learning is often used to build predictive models from that data.

### Real-Life Example

In a hospital, Data Scientists collect and clean patient data such as age, symptoms, and medical history. A Machine Learning model is then trained using this data to predict whether a patient is at risk of developing a serious disease. Doctors can use these predictions to provide earlier treatment and improve patient care.

---

## 2. Describe the Data Science Lifecycle (from problem definition to deployment). At which stage does Machine Learning typically fit in, and why?

The Data Science lifecycle consists of several stages:

1. **Problem Definition** – Identify the problem and define the objectives.
2. **Data Collection** – Gather relevant data from different sources.
3. **Data Cleaning and Preparation** – Remove errors, missing values, and inconsistencies.
4. **Exploratory Data Analysis (EDA)** – Analyze the data to understand patterns and relationships.
5. **Model Building** – Create statistical or Machine Learning models.
6. **Model Evaluation** – Test the model's performance using appropriate metrics.
7. **Deployment** – Implement the model in a real-world environment.
8. **Monitoring and Maintenance** – Continuously monitor and update the model when necessary.

### Where Does Machine Learning Fit?

Machine Learning typically fits into the Model Building stage. At this stage, algorithms learn patterns from prepared data and create models that can make predictions or classifications. This stage is important because it transforms data into actionable insights.

---

## 3. Compare Supervised Learning and Unsupervised Learning, Giving an Example of Each

### Supervised Learning

Supervised Learning uses labeled data, meaning the correct answers are already known. The model learns from this data and predicts outcomes for new data.

**Example:** Predicting house prices based on features such as location, size, and number of rooms.

### Unsupervised Learning

Unsupervised Learning uses unlabeled data, where no correct answers are provided. The model identifies hidden patterns or groups within the data.

**Example:** Grouping customers into different categories based on their purchasing behavior.

### Difference

The main difference is that Supervised Learning predicts known outcomes, while Unsupervised Learning discovers hidden patterns.

---

## 4. What Causes Overfitting? How Can It Be Prevented?

Overfitting occurs when a Machine Learning model learns the training data too closely, including noise and unnecessary details. As a result, the model performs very well on training data but poorly on new, unseen data.

### Causes of Overfitting

- Using a very complex model.
- Having a small dataset.
- Training the model for too long.
- Including noisy or irrelevant data.

### Prevention Methods

- Collecting more training data.
- Using cross-validation techniques.
- Simplifying the model.
- Applying regularization methods.
- Using early stopping during training.

These techniques help the model generalize better to new data.

---

## 5. Explain How Training Data and Test Data Are Split, and Why This Process Is Necessary

In Machine Learning, datasets are usually divided into two parts:

- **Training Data:** Used to train the model.
- **Test Data:** Used to evaluate the model's performance.

A common split is 80% training data and 20% test data.

### Example

If a dataset contains 1,000 records:

- 800 records are used for training.
- 200 records are used for testing.

### Why Is This Necessary?

This process helps determine whether the model can perform well on new data. Without a test dataset, it would be difficult to know if the model has truly learned useful patterns or simply memorized the training data.

---

## 6. Case Study: Machine Learning in Healthcare

A recent healthcare study used Machine Learning to predict COVID-19 patient outcomes using electronic health records. Researchers analyzed patient information such as medical history, symptoms, and clinical measurements.

### Objectives

The study aimed to predict:

- Positive COVID-19 cases.
- Need for ventilator support.
- Length of hospital stay.
- Risk of death.

### Findings

The Machine Learning models achieved high prediction accuracy and helped identify important risk factors affecting patient health. The study demonstrated that Machine Learning can support doctors in making faster and more informed decisions.

### Data Science Lifecycle Stages Used

- Problem Definition
- Data Collection
- Data Preparation
- Model Building
- Evaluation
- Deployment

---

## References

1. GeeksforGeeks. Machine Learning Lifecycle.
2. Springer Nature. Machine Learning Approach for Diagnostic and Prognostic Predictions in Healthcare (2024).
3. MDPI. Healthcare Predictive Analytics Using Machine Learning.
