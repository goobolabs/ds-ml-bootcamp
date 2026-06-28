# 📊 Research Assignment: Introduction to Data Science and Machine Learning

| Field      | Information                       |
| ---------- | --------------------------------- |
| **Name**   | Abdullahi Abdiweli Adam           |
| **Course** | Data Science and Machine Learning |
| **Date**   | June 15, 2026                     |

---

# 1️⃣ Relationship Between Data Science and Machine Learning

Today, organizations collect huge amounts of information from websites, mobile applications, hospitals, banks, and social media platforms. However, having data alone is not enough. The data must be organized and analyzed before it becomes useful.

Data Science focuses on understanding data and turning it into information that can help people make better decisions. It involves collecting data, preparing it, studying patterns, and presenting findings.

Machine Learning is one of the techniques that can be used during this process. Instead of manually creating rules, Machine Learning learns patterns from previous data and uses those patterns to make predictions.

For example, an online shopping company may want to know which products customers are likely to buy next. Data Science is used to collect customer information, clean the data, and analyze purchasing behavior. Machine Learning is then used to predict future purchases based on previous customer activity.

This shows that Data Science and Machine Learning work together. Data Science provides the foundation, while Machine Learning helps generate predictions from the prepared data.

---

# 2️⃣ Data Science Lifecycle and the Role of Machine Learning

A Data Science project usually follows several connected stages.

The first stage is understanding the problem. Before collecting any data, an organization must know what question it wants to answer. Without a clear objective, the results may not be useful.

The second stage involves collecting relevant data from databases, surveys, websites, or other sources. After collection, the data is usually cleaned because real-world data often contains missing values, duplicate records, or incorrect information.

Once the data has been prepared, analysts explore it to identify patterns, trends, and unusual observations. This helps them understand the data before making decisions.

After exploration, Machine Learning may be introduced if predictions are needed. At this stage, algorithms learn from historical data and build models that can estimate future outcomes.

The model is then tested to determine whether it performs well on new data. Finally, the results or models are deployed so that organizations can use them in real situations.

Machine Learning normally appears after the data has been prepared and explored because learning algorithms require clean and meaningful data. If poor-quality data is used, the model's predictions will also be poor.

### 📋 Data Science Lifecycle

| Stage                 | Purpose                      |
| --------------------- | ---------------------------- |
| Problem Understanding | Identify the objective       |
| Data Collection       | Gather information           |
| Data Preparation      | Clean and organize data      |
| Data Exploration      | Discover patterns and trends |
| Machine Learning      | Build prediction models      |
| Evaluation            | Measure performance          |
| Deployment            | Use results in practice      |

---

# 3️⃣ Supervised Learning and Unsupervised Learning

Machine Learning methods can be grouped into different categories depending on the type of data available.

Supervised Learning is used when the correct answers already exist in the dataset. The algorithm studies examples and learns how inputs are connected to outputs. After learning, it can make predictions for new cases.

A common example is predicting student performance. If previous records contain study hours and exam results, the model can learn the relationship and estimate future scores.

Unsupervised Learning works differently because no correct answers are provided. Instead of predicting known outcomes, the algorithm searches for hidden structures and similarities within the data.

For example, a supermarket may have information about customer purchases but no predefined customer categories. An unsupervised learning algorithm can automatically group customers with similar buying behaviors.

### 📊 Comparison of Learning Types

| Feature | Supervised Learning    | Unsupervised Learning |
| ------- | ---------------------- | --------------------- |
| Data    | Has known answers      | Has no known answers  |
| Goal    | Make predictions       | Discover patterns     |
| Example | Predicting exam scores | Grouping customers    |
| Output  | Labels or values       | Clusters or groups    |

---

# 4️⃣ Causes of Overfitting and Prevention Methods

One challenge in Machine Learning is ensuring that a model performs well not only on the data used for training but also on new data.

Overfitting happens when a model becomes too focused on the training dataset. Instead of learning general patterns, it memorizes details that may not appear again in future data.

Several factors can contribute to overfitting. One common cause is using a model that is more complex than necessary. Another cause is training with a small amount of data, which prevents the model from learning broader patterns.

Overfitting can be reduced in several ways. Using more training data often improves generalization. Simpler models may also perform better because they focus on important patterns instead of memorizing details. Techniques such as cross-validation and regularization can further help control model complexity.

The main objective is to build a model that learns useful patterns rather than memorizing specific examples.

---

# 5️⃣ Training Data and Test Data

When developing a Machine Learning model, it is important to evaluate its ability to handle new information.

To achieve this, the available dataset is divided into two parts. The first part is the training set, which is used to teach the model. The second part is the test set, which is used only after training is complete.

A common practice is to use approximately 80% of the data for training and 20% for testing. The exact percentages may vary depending on the project.

This separation is important because evaluating a model on the same data used during training does not provide a realistic measure of performance. The model may appear accurate simply because it has already seen the data before.

Testing on unseen data provides a better indication of how the model will perform in real-world situations and helps identify problems such as overfitting.

---

# 6️⃣ Case Study: Machine Learning in Healthcare

A widely known application of Machine Learning in healthcare involves the detection of skin cancer from medical images.

Researchers trained a deep learning model using thousands of images of skin lesions. Before training, the images were collected, organized, and prepared for analysis. The model then learned patterns associated with cancerous and non-cancerous conditions.

The results showed that the system could identify certain skin cancers with a level of accuracy similar to experienced medical professionals. This demonstrated how Machine Learning can support doctors by providing faster and more consistent analysis.

This case study includes several stages of the Data Science lifecycle. The researchers first identified a healthcare problem, collected medical image data, prepared the dataset, trained a Machine Learning model, and evaluated its performance before considering practical use.

The study highlights how Data Science and Machine Learning can work together to solve important real-world challenges and improve healthcare services.

---

# 📚 References

1. IBM. *"What is Data Science?"* Available at:
   https://www.ibm.com/topics/data-science

2. Oracle. *"What is Data Science?"* Available at:
   https://www.oracle.com/data-science/what-is-data-science/
