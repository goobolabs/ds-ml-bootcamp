# Part C — Reflection Paper
## What did you implement?
I reproduced the Lesson 5 preprocessing pipeline by building a clean workflow that handles missing data, isolates column types, and utilizes RobustScaler on the numerical columns to safely manage financial outliers. I split the dataset using a stratified 80/20 train/test split to preserve our target class ratios, resulting in 80 training samples and 20 test samples. Using this processed xog (data), I successfully trained and evaluated three classification models: Logistic Regression, Random Forest, and a Decision Tree.

## omparison of Models
- Sanity Check Differences: 
When I performed a single-row sanity check on index 7 (where the actual ground truth was a rejection), all three of my models incorrectly predicted "Approved (1)". This showed me that individual test cases can still fool the models.

- Which Model Gave More Realistic Results? 
Even though the technical test scores varied, Random Forest provides more structurally realistic predictions for real-world data. Because our current test set is very small (20 rows), the single Decision Tree overfitted aggressively, making its high scores less realistic for future datasets. Random Forest averages many trees, making it much more stable.

## Understanding Random Forest
Random Forest is an ensemble algorithm that builds a collection of independent Decision Trees during training. When making a prediction for a loan applicant, every single tree in the forest casts a "vote" for either approval or rejection. The algorithm counts these votes and outputs the category that receives the majority vote, which significantly cuts down on errors and overfitting.

## Other Algorithms (My Third Classifier)
1. Which Additional Algorithm I Chose and Why: I chose a single Decision Tree. I wanted to see exactly how a individual tree performs on its own compared to the Random Forest ensemble that combines them.

2. Research Summary: A Decision Tree works by repeatedly splitting the dataset using simple if-else rules based on feature thresholds.

- Advantage: It is incredibly easy to visualize and interpret exactly why a loan was approved or denied.

- Limitation: It suffers heavily from overfitting, meaning it easily memorizes the training data but fails to generalize well to new test data.

3. Metric Comparison: On my specific split, the single Decision Tree surprisingly achieved the highest F1-Score (0.800) and the highest Recall (0.923), outperforming the Random Forest due to the small size of the test partition.

## Metrics Discussion
Based on my exact script outputs, here is how the models stacked up:

- Logistic Regression: Accuracy: 0.700 | Precision: 0.733 | Recall: 0.846 | F1-Score: 0.786

- Random Forest: Accuracy: 0.650 | Precision: 0.714 | Recall: 0.769 | F1-Score: 0.741

- Decision Tree: Accuracy: 0.700 | Precision: 0.706 | Recall: 0.923 | F1-Score: 0.800

- Best Performers: The Decision Tree held the highest F1-Score (0.800) and Recall (0.923), while Logistic Regression achieved the highest overall Precision (0.733) and tied for the best Accuracy (0.700).

- Strengths and Weaknesses: This tells me that Logistic Regression is highly reliable when it makes a positive guess (fewer False Positives). The Decision Tree has a high capacity to catch approved borrowers, but its weakness is that it approves risky candidates too easily (5 False Positives). Random Forest underperformed here because a 100-row dataset is too small for an ensemble to show its true strength.

## Findings
If I had to select one model to deploy for loan approval prediction right now, I would choose Logistic Regression. In banking, approving an applicant who will default (a False Positive) is incredibly expensive and risky. Because my Logistic Regression model achieved the highest Precision score (0.733), it is the safest choice for minimizing those costly default errors.

While the Decision Tree technically shows a slightly higher F1-score, its confusion matrix shows that it is far too aggressive—wrongly approving 5 out of 7 rejected candidates. Therefore, Logistic Regression provides a much more balanced, conservative, and financially sound risk profile for automated underwriting given my current dataset size.