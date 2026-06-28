**Research Paper: Digital Wellbeing: Tracking the Impact of Screen Time on Mood**

**A. Title & Collection Method**
**Project Title:** Screen Time, Doom-Scrolling, and Their Impact on Daily Psychological Mood.
**Collection Method:** This dataset was compiled using manual logging,self-reported mood surveys. 
A cohort of participants tracked their daily smartphone utilization alongside subjective mental state logs completed every evening before sleeping.

**B. Use cases of the Machine Learning**
Features(x) are User_ID,Screen_Time_Hours,Scroll_Session_Count,Dominant_App_Category,Physical_Activity_Min and Sleep_Quality while Label(y) is Evening_Mood_Score.
This is Supervised Learning because it has input and target output data specifically A primary use case is ***Regression type*** because the target label is continuous numerical rating scale(1-10).
 A secondary task could be ***Classification*** if the scores are later binned into categories like "Good Mood" vs "Bad Mood."

**C. Description of Features & Labels:**
The dataset consists of 5 input features (X) and 1 target label (y):
***Input Features (X)***
*Screen_Time_Hours (Numerical / Continuous):* Total daily active smartphone usage time.
*Scroll_Session_Count (Numerical / Discrete):* The number of times the user opened social media apps to scroll.
*Dominant_App_Category (Categorical / Nominal):* The category where most time was spent (Social, Productivity, Gaming, News).
*Physical_Activity_Min (Numerical / Discrete):* Total minutes of movement, walking, or exercise during the day.
*Sleep_Quality (Categorical / Ordinal):* Self-reported quality of sleep from the prior night (Good, Average, Poor).
***Target Label (y)***
*Evening_Mood_Score (Numerical / Continuous):* Nighttime mental well-being self-assessment score from 1.0 (Anxious/Depressed) to 10.0 (Calm/Happy).

**D. Data Science Lifecycle Fit:** This project fulfills the Data Collection and Understanding phase. It establishes whether an empirical baseline correlation exists between phone habits and psychological health before moving on to model building.

**E. Dataset Structure & Sample Table**
Total Rows (Samples): 54
Total Columns (Variables): 7 (ID + 5 Features + 1 Label)

**F. Quality issues:**
***Missing Values (NaNs):***
User 6 is missing the target variable Evening_Mood_Score.
user 10 is missing the Sleep_Quality ratings.

***Inconsistent Casing & Typos:***
User 5 has a lowercase social, while User 9 made spelling mistake the word Social.
We also have some people(User 5,16,41,53) who make an excuse to not share their Physical_Activity_Min because OF their privacy and we respect that.

**Outliers & Scales:**
Numerical features are scaling differently. Physical_Activity_Min reaches up to 60, while Screen_Time_Hours stays single-digit. You will need to apply scale transformation techniques like normalization or standardization.

*Screen_Time_Hours:* Usually small numbers like 2, 5, or 8.
*Physical_Activity_Min:* Bigger numbers like 15, 45, or 60.Because 60 is mathematically much larger than 8, a machine learning model will accidentally think that physical activity is way more important than screen time. It will give the bigger numbers extra power, ruining your predictions.

I have the Sample in a different file called Sample.xlsx