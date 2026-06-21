Social Media Usage in Somalia

A Self-Collected Dataset for Machine Learning Foundations



Name: Alisalad



1\. Title \& Collection Method



This dataset examines social media usage habits among people in Somalia, including which platforms they use, how much time they spend on them, what they use them for, and whether that usage is tied to income or business activity.

Data was collected through a self-designed Google Form survey, distributed directly via WhatsApp to personal and business contacts, including customers and contacts connected to ongoing mobile retail work. The survey was open for two days and gathered 14 responses, recorded automatically into a linked Google Sheet.



2\. Description of Features \& Labels



The dataset includes the following input variables (features, X):

•	Age (categorical range: 15-24, 25-35, 35-55)

•	Gender (categorical: Male, Female)

•	Platform — most-used social media platform (categorical: WhatsApp, TikTok, YouTube, etc.)

•	Hours per day spent on social media (ordinal categories)

•	Primary purpose of use (categorical: News, Entertainment, Studying, Business/selling, Communication)

The output variable (label, y) is:

•	Income — whether the respondent uses social media to support a business or earn income (binary: Yes / No)

This label was chosen because it has a clear, well-defined yes/no answer that other features could plausibly help predict — for example, someone whose main purpose is "Business/selling" is more likely to answer Yes.



3\. Dataset Structure



The full dataset currently contains 14 rows (responses) and 6 usable columns (5 features + 1 label), plus a timestamp column generated automatically by the form. A sample of 8 rows is shown below:

Age	Gender	Platform	Hours/day	Purpose	Income (y)

15-24	Male	WhatsApp	1-2 hours	News \& information	Yes

15-24	Male	TikTok	5+ hours	News \& information	No

15-24	Female	TikTok	1-2 hours	News \& information	Yes

25-35	Male	YouTube	3-4 hours	News \& information	(missing)

25-35	Male	WhatsApp	3-4 hours	News \& information	No

15-24	Male	TikTok	5+ hours	Studying	Yes

25-35	Male	WhatsApp	5+ hours	Business/selling	Yes

25-35	Female	WhatsApp	Less than 1 hour	News \& information	No





4\. Quality Issues



•	Missing value: one respondent (row 4 in the raw data) left the Income field blank — a genuine missing value that would need to be handled in preprocessing (e.g., dropped or imputed).

•	Small sample size: 14 responses is below the 50-row target, limiting how reliable any patterns are.

•	Age imbalance: the majority of respondents fall in the 15-24 and 25-35 ranges, with only one respondent in the 35-55 range — older age groups are underrepresented.

•	Gender imbalance: more male respondents than female in this sample.

•	Sampling bias: respondents were drawn from personal and business contacts rather than a random sample of the population, so results likely skew toward younger, more digitally active people already connected to mobile retail/tech circles.

•	Inconsistent text encoding: hour-range values exported with corrupted dash characters (e.g., “1â€“2 hour” instead of “1-2 hours”), requiring cleanup before analysis.



5\. Learning Type



This is a supervised learning problem. There is a clear label, y (Income: Yes/No), and the goal would be to predict that label using the other features (age, gender, platform, hours, purpose). Because the label is binary and categorical, this is specifically a binary classification problem rather than regression.

If the Income column were removed and the goal instead became finding natural groupings among respondents (e.g., clustering similar usage patterns without a target label), the same data could also support an unsupervised learning task — but as collected, with a defined target column, it fits supervised learning.



6\. Use Case



This dataset could support a classification model predicting whether a person is likely to use social media for income/business purposes based on their age, platform choice, usage hours, and stated purpose. A business such as a mobile phone retailer could use this to identify which customer segments are more likely to be business-driven social media users, and tailor marketing or product offerings accordingly (e.g., promoting devices better suited for content creation or business use).

In the Data Science lifecycle, this dataset currently sits at the data collection and preparation stage. The next step (Lesson 4) would be preprocessing — handling the missing value, fixing encoding issues, encoding categorical variables numerically, and addressing class imbalance — before moving into modeling, evaluation, and eventual deployment.



