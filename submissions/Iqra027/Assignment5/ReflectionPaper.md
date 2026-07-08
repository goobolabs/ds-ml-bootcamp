## 1.What did you implement?
In this Assignment i restructred raw_loan_dataset which has missing values,currency formatting sympols($,) which we converted later into float, there is also mixed category strings which we made into two categories(Yes and No) and also we implement IQR capping to clip  the extreme features values to not effect on the data.
we used feature engineering and add two new columns(DebtToIncome ,IncomePerYearEmployed)while deliberately ignoring the label array to guarantee zero data leakage.
**Leakage-Free Preprocessing:** Partitioned the dataframe into Stratified Training (80%) and Testing (20%) splits before applying transformations. 
I selected a RobustScaler (which scales data using the median and IQR to remain highly resilient to remaining extreme bounds) and strictly ran fit_transform() exclusively on the training subset, followed by a pure transform() on the test dataset.
Ultimately, I trained and evaluated three distinct classification systems: the core lesson models (Logistic Regression and Random Forest) alongside an independently researched third architecture (Support Vector Classifier).
## 2.Comparison of Models
**Prediction Differences:** In the single-row check, models gave different results for borderline applicants. Logistic Regression used strict lines, while Random Forest and SVC were more flexible.
**Most Realistic Model:** Random Forest and SVC gave more realistic results. Loan data has complex, non-linear relationships (like credit score vs. income) that Logistic Regression cannot capture well on its own.
## 3.Understanding Random Forest
Random Forest is a team of many individual Decision Trees working together to make one final prediction:
During training, it builds hundreds of different decision trees using random parts of the data.
When a new loan application arrives, every single tree gives its own prediction.
The model counts all the predictions and chooses the winner by a majority vote.
This team-based approach stops the model from memorizing the data (overfitting) and makes it highly accurate.
## 4.Other Algorithms (Your Third Classifier)
*Chosen Model:* Support Vector Classifier (SVC)
*How it works:* SVC finds the best geometric boundary line (called a hyperplane) that separates approved and rejected applicants with the widest safety gap. It uses a "Kernel" trick to handle non-linear data.
*Advantage:* Very powerful at finding complex patterns in datasets with many features.
*Metrics:* SVC performed better than Logistic Regression but was slightly behind Random Forest.
## 5.Metrics Discussion
*Best Model:* Random Forest won across all metrics (Accuracy, Precision, Recall, and F1-Score).
**Strengths & Weaknesses:**
Random Forest is balanced. High Precision means it rarely approves bad loans, and high Recall means it rarely rejects good customers.
Logistic Regression is fast and simple, but too weak to see non-linear patterns.
SVC is highly accurate with good scaling, but it needs a lot of manual tuning to work perfectly.
## 6.Your Findings & Recommendation
I highly recommend using the **Random Forest Classifier** for this loan approval system. In banking, approving a high-risk person who defaults (False Positive) hurts the bank much more than accidentally rejecting a safe client. Random Forest reduces this financial risk because it requires a majority vote from hundreds of trees before approving an applicant.

Additionally, Random Forest is very reliable in production. It works smoothly with both numbers and categories, and it does not get confused by outliers or scaling issues. This makes it the safest and most profitable choice for the bank.