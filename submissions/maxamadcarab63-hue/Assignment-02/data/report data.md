Personal Daily Income in Ethiopia Dataset: Design and Machine Learning Applications

Abstract
This study presents a synthetic dataset designed to model personal daily income in Ethiopia using machine learning techniques. The dataset contains demographic, educational, occupational, and socioeconomic variables that influence income levels. It includes 50 observations and 8 variables, where Daily_Income_ETB is the target variable. The dataset is intended for educational use in data science and predictive modeling.

1. Introduction

Income prediction is an important problem in economics and social development. Understanding income determinants helps in designing policies to reduce poverty and improve living standards.

This dataset was synthetically generated to represent individuals from different regions of Ethiopia with varying education levels, occupations, and experience. It avoids privacy concerns associated with real-world income data.

2. Dataset Collection Method

The dataset was manually generated based on realistic assumptions about Ethiopia’s labor market:

Higher education leads to higher income
Occupation strongly affects earnings
Urban regions (e.g., Addis Ababa) have higher income opportunities
Work experience increases income
Household size may influence economic conditions indirectly

The dataset is fully synthetic and used for educational purposes only.

3. Features and Label

Input Features (X):

Age (Numerical)
Gender (Categorical)
Education_Level (Categorical)
Occupation (Categorical)
Region (Categorical)
Years_Experience (Numerical)
Household_Size (Numerical)

Target Variable (y):

Daily_Income_ETB (Numerical)
4. Dataset Structure
Rows: 50
Columns: 8
Features: 7
Target: 1
5. Data Quality Considerations

5.1 Limited Sample Size
Only 50 records are included, which may not fully represent Ethiopia’s diverse population.

5.2 Synthetic Nature
The dataset is artificially generated, so it may not perfectly reflect real-world distributions.

5.3 Potential Bias
Income values depend on assumed rules, which may introduce bias in modeling.

6. Machine Learning Applications

This dataset can be used for:

Linear Regression
Random Forest Regression
Decision Tree Models
Feature importance analysis
Educational ML projects