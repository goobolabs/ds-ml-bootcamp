1. Overview of implementation

In this project I built an end-to-end machine learning pipeline to predict loan approval using a cleaned loan dataset . The workflow was a close follow-up of the Lesson 5 preprocessing pipeline and was extended with an additional classification algorithm.

The first step in the process was to load the clean_loan_dataset.csv file and separate the input features (X) from the target variable (Approved). Then the dataset was split into train (80%) and test (20%) sets with stratify=y to preserve the class distribution and random_state=42 for reproducibility.

After preprocessing I trained 3 different classification models. The first two models, Logistic Regression and Random Forest, were used as discussed in class. I also used Gradient Boosting as a classifier because it has been shown to be a strong classifier on structured datasets and it.

Following preprocessing, I trained three different classification models. The first two models, Logistic Regression and Random Forest, are implemented as discussed in class. The other classifier I chose was Gradient Boosting . It learns from the mistakes it makes in prediction and thus helps to boost the accuracy of the model . It also works well on structured data . Finally, I checked the performance of all the three models using Accuracy, Precision, Recall and F1-Score.

2. Comparison of Models

I performed a sanity check to validate the models, comparing the class predicted by the model for a test sample against its actual label. All three models did a reasonable job of prediction, but they did not do as well as each other.

The Gradient Boosting classifier produced the most consistent and trustworthy predictions on the test set. It could correct mistakes made in earlier stages of learning, and therefore was able to pick up more complex patterns in the loan approval data. Logistic Regression and Random Forest also performed well however overall, Gradient Boosting produced the most realistic predictions.

3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm that uses predictions from many decision trees to make a final classification. Instead of using one tree, the algorithm trains many trees using different subsets of the training data and features .

In prediction, each decision tree casts a vote for a class and the class that receives the majority of votes is the final prediction. This ensemble approach decreases overfitting and improves model stability, and generally yields better generalization than a single decision tree. So, Random Forest is considered as a reliable algorithm for classification problems such as prediction of loan approval.

4. Other Algorithm (Gradient Boosting)

For my third classifier, I selected Gradient Boosting because it is widely recognized for its excellent performance on tabular datasets and its ability to produce highly accurate predictions.

Unlike Random Forest, which builds many independent decision trees in parallel, Gradient Boosting constructs trees sequentially. Each new tree is trained to correct the errors made by the previous trees, gradually improving the overall model. This iterative learning process enables the algorithm to capture complex relationships between features and generate more accurate predictions.

One of the main advantages of Gradient Boosting is its high predictive accuracy, especially when working with structured data. However, because each tree depends on the previous one, the algorithm requires more computational time and can overfit the training data if its hyperparameters are not carefully tuned.

Based on my evaluation, Gradient Boosting achieved the strongest overall performance among the three classifiers, outperforming both Logistic Regression and Random Forest across the evaluation metrics.

5. Metrics Discussion

The evaluation results showed that Gradient Boosting achieved the highest Accuracy, Precision, Recall, and F1-Score among the three models. These results indicate that it provided the best overall balance between correctly identifying approved loans and minimizing incorrect predictions.

Logistic Regression served as a simple and interpretable baseline model, while Random Forest improved predictive performance by combining multiple decision trees. However, both models produced slightly lower evaluation scores than Gradient Boosting. In particular, the higher Recall achieved by Gradient Boosting suggests that it was more effective at correctly identifying eligible loan applicants while reducing false negatives.


6. My Findings:

Based on the overall evaluation, I would choose Gradient Boosting as the preferred model for loan approval prediction. Its sequential learning approach allows it to continuously improve by correcting previous prediction errors, resulting in stronger predictive performance than the other models.

Since loan approval is a high-impact financial decision, selecting a model with high Accuracy, Precision, Recall, and F1-Score is essential. The superior performance of Gradient Boosting demonstrates its ability to make more reliable predictions while effectively capturing the complex relationships between applicant characteristics and loan approval decisions. For these reasons, it is the most suitable model for this loan prediction task.
