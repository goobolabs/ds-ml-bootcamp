### Name:miski mohamed nur
## Research paper:
## Impact of Social Media Usage on Sleep Quality Dataset
# Impact of Social Media Usage on Sleep Quality Dataset


## Title & Data Collection Method

**Title:** Impact of Social Media Usage on Sleep Quality Dataset

**Data Collection Method:**
An online survey questionnaire was designed and distributed to students within a limited time frame. The survey focused on students’ social media usage habits and their sleep quality. A total of **[50] students** participated in the survey and provided information about their most-used social media platform, daily usage hours, purpose of usage, night-time usage behavior, notification settings, and overall sleep quality.



## Description of Features & Label

### **Features (X):**

1. **Most Used Social Media Platform (Categorical):**
   The social media platform used most frequently by the student (e.g., Facebook, TikTok, WhatsApp, Instagram).

2. **Hours per Day (Numeric):**
   Average number of hours spent on social media per day.

3. **Purpose of Usage (Categorical: Education / Entertainment):**
   Main reason for using social media.

4. **Night Usage (Categorical: Yes / No):**
   Whether the student uses social media late at night before sleeping.

5. **Notifications Status (Categorical: On / Off):**
   Indicates whether social media notifications are enabled or disabled.

### **Label (Y):**

* **Sleep Quality (Categorical: Good / Poor)**

This formulation defines the problem as a **classification task**, where the goal is to predict a student’s sleep quality based on their social media usage behavior.

---

## Dataset Structure

* **Rows:** [N] students (samples)
* **Columns:** 6 (5 features + 1 label)

### **Sample Dataset (10 Rows)**

  |Age | Platform | Hours/Day | Purpose       | Night Usage | Notifications | Sleep Quality |
       
    22 year old	TikTok	5 Hours	Both	No	Off		Good
    17	TikTok	3 Hours	Education	No	On		Good
    23	TikTok	3 Hours	Education	Yes	On		Good
    20	WhatsApp	4 Hours	Education	Yes	Off		Good
    20	WhatsApp	3Hour       Both    Yea off       poor

---

## Data Quality Issues

* **Missing Values:** There is no missin value bacause of hot topic 
* **Categorical Variables:** Platform, purpose, night usage, and notification status must be encoded before model training.
* **Self-Reported Data:** Usage hours may not be perfectly accurate due to personal estimation.
* **Class Imbalance:** There may be more students reporting good sleep quality than poor sleep quality.



## Use Case

This dataset can be used to train a **machine learning classification model** that predicts sleep quality based on social media usage habits.

### **Possible Algorithms:**

* Logistic Regression
* Decision Tree
* Random Forest

The results of this study can help students, educators, and health professionals understand how excessive social media usage—especially at night—affects sleep quality and overall well-being. It can also support awareness campaigns promoting healthier digital habits.
