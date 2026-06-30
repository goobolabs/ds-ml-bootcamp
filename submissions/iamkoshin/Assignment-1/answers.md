1. **Data Science** is the process of collecting, cleaning, studying, and understanding data to solve problems and make better decisions. It combines knowledge from statistics, programming, and business or other fields.

**Machine Learning** is a part of Data Science. It allows computers to learn from data and make predictions or decisions without being programmed for every task.

Data Science and Machine Learning work together. Data Science covers the whole process of working with data, while Machine Learning focuses on building models that can learn patterns and make predictions.

**Real-Life Example: Online Shopping (Amazon)**

When you shop on an online store like Amazon, Data Science collects and studies information such as the products you search for, the items you buy, and the products you view.

---

2. The Data Science lifecycle starts with defining the problem. This means understanding what needs to be solved, such as predicting customer sales or detecting diseases.

The next step is collecting data from different sources such as databases, surveys, websites, or sensors.

After collecting data, it is cleaned and prepared. Missing values are fixed, errors are removed, and the data is organized so it can be used correctly.

Then, data analysts explore the data to understand patterns, trends, and relationships. This helps them learn more about the problem and decide what methods to use.

Machine Learning usually fits into the model-building stage. At this stage, algorithms are trained using prepared data so they can learn patterns and make predictions. The models are then tested to see how well they perform.

Once a model works well, it is deployed so people or organizations can use it in real situations. Finally, the model is monitored and updated when necessary to keep it working accurately.

Machine Learning belongs in the model-building stage because its main purpose is to learn from data and make predictions.

---

3. **Supervised Learning** uses labeled data. This means the correct answers are already known before the model is trained. The model learns from these examples and then predicts the correct answer for new data.

**Example:** A bank uses supervised learning to decide whether to approve or reject a loan application. The model is trained using past applications that are already labeled as **"approved"** or **"rejected."** It learns from these examples and predicts whether a new application should be approved.

**Unsupervised Learning** uses unlabeled data. This means there are no correct answers given. The model looks for hidden patterns or groups in the data by itself.

**Example:** A supermarket uses unsupervised learning to group customers based on their shopping habits. The model may discover groups such as customers who buy groceries every week, customers who mainly buy electronics, or customers who only shop during sales. This helps the supermarket create better marketing campaigns.

---

4. Overfitting happens when a machine learning model learns the training data too well, including small details and noise. As a result, the model performs very well on training data but poorly on new data.

Overfitting can happen when there is too little training data, when the model is too complex, or when the data contains many errors.

It can be prevented by collecting more data, removing unnecessary features, using simpler models, and testing the model on different datasets. Another method is early stopping, which stops training before the model starts memorizing the data.

---

5. A dataset is usually divided into two parts: training data and test data.

**The training data** is used to teach the machine learning model. **The test data** is used to check how well the model performs on data it has never seen before.

A common split is 80% for training and 20% for testing.

This process is necessary because it helps us know whether the model can work well on new data. If we only test the model using the same data it learned from, we cannot tell if it will make good predictions in real-life situations.

---

6. One example comes from healthcare, where researchers used machine learning to predict diabetes. They collected patient information such as age, blood sugar levels, blood pressure, and body weight. The data was cleaned and prepared before training machine learning models.

The study found that machine learning models could identify patients who were at high risk of developing diabetes. This helps doctors provide treatment earlier and improve patient care.

This case study covers several stages of the Data Science lifecycle, including problem definition, data collection, data preparation, model building, and model evaluation.

**References**

Géron, A. (2022). Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow: Concepts, tools, and techniques to build intelligent systems (3rd ed.). O'Reilly Media.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An introduction to statistical learning: With applications in R (2nd ed.). Springer. https://doi.org/10.1007/978-1-0716-1418-1

Studer, S., Bui, T. B., Drescher, C., Hanuschkin, A., Winkler, L., Peters, S., & Müller, K.-R. (2020). Towards CRISP-ML(Q): A machine learning process model with quality assurance methodology. arXiv. https://arxiv.org/abs/2003.05155
