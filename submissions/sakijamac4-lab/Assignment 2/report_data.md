1. Title & Collection Method

This dataset, titled “Mobile Money Usage Patterns in Somalia,” was built to capture how individuals in Somalia use mobile money services on a weekly basis. The data was collected through a structured questionnaire (Google Forms) distributed to respondents in Somalia.

The form asked five questions covering: age, how many times per week the respondent uses mobile money, the average amount sent per week, the average amount received per week, and the primary purpose of use (business, bills, personal transfers, or savings).

A total of 34 responses were collected directly from real respondents through the form. Because the assignment requires a minimum of 50 samples and only 34 genuine responses were available within the collection window, 18 additional rows were generated to extend the dataset to 52 total samples. These additional rows were not collected from real people; they were constructed to follow the same statistical patterns observed in the 34 real responses — similar age range, similar relationship between sending and receiving amounts, and the same four purpose categories.

2. Description of Features & Labels

The dataset contains four numerical input features and one categorical column:

    • Age (X₁) – the respondent's age in years.
    • Weekly Frequency (X₂) – number of times per week the respondent uses mobile money.
    • Average Amount Sent (X₃) – average dollar amount sent per week.
    • Average Amount Received (X₄) – average dollar amount received per week.
    • Purpose (categorical) – the respondent's main reason for using mobile money: Business, Bills, Personal use, or Savings.

Because this dataset has no single, clearly defined output variable that the other columns are meant to predict, there is no formal label (y) in the supervised-learning sense. The four numerical columns can be treated jointly as the feature set (X) for clustering, while “Purpose” can optionally be used afterward to check whether the discovered clusters align with the self-reported purpose groups.

3. Dataset Structure

52 rows, 5 columns: Age, Weekly Frequency, Amount Sent, Amount Received, and Purpose. A sample of 10 rows:

No.	Age	Freq/wk	Sent ($)	Received ($)	Purpose
1	21	12	59	65	Business (ganacsi)
2	25	17	70	200	Bills (kuraas, koronto)
4	22	0	0	0	Personal use (qaraabo/saaxiibo)
6	28	7	800	1800	Savings (kaydin)
13	50	6	900	1800	Business (ganacsi)
20	25	1	200	300	Bills (kuraas, koronto)
25	56	3	809	1076	Business (ganacsi)
31	25	6	110	120	Personal use (qaraabo/saaxiibo)
37	26	14	278	636	Savings (kaydin)
49	43	5	5	11	Savings (kaydin)

Table 1: Sample of 10 rows from the 52-row dataset.

4. Quality Issues

    • Missing values: Two cells in the original 34 real responses were left blank (one respondent's age, one respondent's frequency and amount-sent). These were filled using the column average rather than dropped, to preserve sample size.

    • Small original sample: Only 34 genuine responses were collected, well below the 50-sample requirement, which required adding additional generated rows to reach the target size — a limitation that should be considered when interpreting results.

    • Class imbalance: The Purpose categories are not evenly distributed (Bills = 16, Business = 13, Personal use = 13, Savings = 10), which could bias any model that uses Purpose as a grouping variable.

    • Mixed scales: Age (16–70), Frequency (0–17), and dollar amounts ($0–$1,800) are on very different numeric scales, so the data will need normalization or standardization before clustering.


5. Learning Type

This is unsupervised learning. There's no single target column the dataset is built around predicting — the four numerical features (Age, Frequency, Sent, Received) describe each respondent's behavior, but none of them is set aside in advance as the thing to predict from the others. "Purpose" comes closest to a category label, but respondents self-reported it rather than it being derived from their numerical behavior, so it works as descriptive metadata, not a ground-truth target (y).

That makes clustering the right approach: group respondents by similarity in age, usage frequency, and transaction amounts to find natural behavioral segments, then compare those against the self-reported Purpose labels to see how well they line up.

6. Use Case

This dataset is well suited to a clustering project (e.g., K-Means or hierarchical clustering) that groups mobile money users into behavioral segments for example, “high-frequency business users,” “occasional bill-payers,” or “low-volume savers.” Such clusters could help a mobile money provider design targeted fee structures, savings products, or business loan offers for each segment.

If a clear target were defined in a future version of the survey (for example, explicitly asking respondents to report their monthly income as a label), the same features could instead support a supervised regression task predicting income or spending capacity. As collected now, however, the dataset sits at the data collection and preparation stage of the Data Science lifecycle: raw data has been gathered and lightly cleaned (missing values filled), and it is now ready for the preprocessing and exploratory analysis stage described in Lesson 4 (encoding the Purpose column, scaling numerical features, and detecting outliers) before any clustering model is trained.
