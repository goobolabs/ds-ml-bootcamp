# Data Science & Machine Learning assignment

### 1: Define Data Science and Machine Learning. What is the relationship between them? Use a real-life example to illustrate how they work together

Data Science prepares and understands the data, while Machine Learning uses that data to build predictive models. They often work together to solve real-world problems such as recommendation systems, fraud detection, medical diagnosis, and demand forecasting.


### 2: Describe the Data Science lifecycle (from problem definition to deployment). At which stage does Machine Learning typically fit in, and why?

The Data Science Lifecycle is a structured process used to turn raw data into useful insights and solutions.

| Stage                                 | Purpose                               |
| ------------------------------------- | ------------------------------------- |
| Problem Definition                    | Define the objective                  |
| Data Collection                       | Gather relevant data                  |
| Data Cleaning                         | Prepare quality data                  |
| EDA                                   | Understand patterns and relationships |
| Feature Engineering                   | Create useful inputs                  |
| **Model Building** | Train predictive models               |
| Model Evaluation                      | Measure performance                   |
| Deployment                            | Put model into production             |
| Monitoring                            | Maintain and improve performance      |

ML is in Model Builing stage becouse this is the point where we actually teach the computer to learn from the prepared data.

---

### 3: compare Supervised Learning and Unsupervised Learning, giving an example of each.

Supervised Learning uses labeled data and learns to predict known outcomes.
Example: Predicting whether an email is spam.

Unsupervised Learning uses unlabeled data and discovers hidden patterns or groups.
Example: Grouping customers into different market segments.

---
### 4: What causes Overfitting? How can it be prevented?

Causes of Overfitting:

* Too little data
* Excessively complex models
* Noisy data
* Too many features
* Training too long

Ways to Prevent It:

* Collect more data
* Use train/test splits
* Apply cross-validation
* Simplify the model
* Select relevant features
* Use regularization
* Apply early stopping
* Pune decision trees

---

### 5: Explain how training data and test data are split, and why this process is necessary.

When building a machine learning model, we usually split the dataset into two parts:

* Training Data – used to teach the model which is commonly 80%.
* Test Data – used to evaluate how well the model performs on new, unseen data and it's the remaining 20%.

The split helps:
* Measure real performance
* Detect overfitting
* Simulate real-world predictions
* Also helps to detect whether the model works on unseen data.

---

## 6: Find one case study (research paper or article) that explains how Data Science or Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings and identify which part of the Data Science lifecycle it covers.


### Case Study: Detecting Diabetic Retinopathy Using Deep Learning in Healthcare

**Research Paper:**
Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs by Varun Gulshan and colleagues. ([Google Research][1])



## 1. Problem Being Solved

**Diabetic retinopathy** is an eye disease caused by diabetes and is a major cause of blindness. Detecting it early can prevent vision loss, but screening requires trained eye specialists, who may not be available in all regions. ([blog.google][2])

The researchers wanted to determine whether a **Machine Learning (Deep Learning)** system could automatically identify the disease from retinal photographs. ([Google Research][1])

---

## 2. What Data Was Used?

The researchers trained a deep neural network using:

* More than **128,000 retinal images**
* Images labeled by **54 ophthalmologists and ophthalmology residents**
* Separate datasets for validation and testing ([Google Research][1])

This provided a large amount of labeled training data for supervised learning.

---

## 3. Findings

The model achieved very high performance in detecting referable diabetic retinopathy:

* Area Under the Curve (AUC) around **0.99**
* Sensitivity above **90%**
* Specificity around **98%** at one operating point on the EyePACS dataset ([Google Research][1])

The results showed that deep learning could detect diabetic retinopathy with accuracy comparable to expert human graders. ([Google Research][1])

---

## 4. Which Parts of the Data Science Lifecycle Does It Cover?

This case study covers several stages of the Data Science lifecycle:

| Lifecycle Stage                   | How the Study Used It                                 |
| --------------------------------- | ----------------------------------------------------- |
| Problem Definition                | Detect diabetic retinopathy automatically             |
| Data Collection                   | Gathered 128,000+ retinal images                      |
| Data Preparation                  | Images were labeled and validated by specialists      |
| Feature Learning / Model Building | Trained a deep convolutional neural network           |
| Model Evaluation                  | Tested performance using separate validation datasets |
| Deployment (Potential)            | Proposed use in real-world screening programs         |

The **main focus** of the paper is on the **Model Building** and **Model Evaluation** stages because the researchers developed and tested a machine learning model. ([Google Research][1])

---

## 5. Why This Is a Good Example of Data Science + Machine Learning

* **Data Science** was used to collect, clean, label, and analyze large amounts of medical image data.
* **Machine Learning** was used to train a model that learned patterns associated with eye disease.
* The resulting system can help doctors screen patients faster and potentially improve access to healthcare in areas with few specialists. ([blog.google][2])

### Short Summary

Researchers trained a deep learning model on over 128,000 retinal images to detect diabetic retinopathy. The model achieved high accuracy and demonstrated that machine learning can assist doctors in identifying eye disease from medical images. The study mainly covers the **Data Collection**, **Data Preparation**, **Model Building**, and **Model Evaluation** stages of the Data Science lifecycle. ([Google Research][1])

[1]: https://research.google/pubs/development-and-validation-of-a-deep-learning-algorithm-for-detection-of-diabetic-retinopathy-in-retinal-fundus-photographs/?utm_source=chatgpt.com "Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs"
[2]: https://blog.google/topics/machine-learning/detecting-diabetic-eye-disease-machine-learning/?utm_source=chatgpt.com "Detecting diabetic eye disease with machine learning"


---