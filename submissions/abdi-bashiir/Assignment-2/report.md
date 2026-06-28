# Project Report: Analysis of Coding Course Pricing

## 1. Introduction
In this assignment, I decided to analyze how online coding courses are priced. Often, we see prices range from free to expensive, and I wanted to investigate if there is a logical pattern behind these costs. By collecting data on 50 different courses, I aimed to see which factors—like duration, course difficulty, and project count—actually drive the price up.

## 2. Data Collection Process
For this project, I manually gathered data from various online learning platforms. I selected 50 courses with different profiles to ensure a balanced dataset. I focused on five main features:
* **Duration_Hours:** The number of hours of video content.
* **Difficulty_Level:** (1: Beginner, 2: Intermediate, 3: Advanced).
* **Enrolled_Students:** The number of students who signed up.
* **Includes_Certificate:** Whether the course offers a completion certificate.
* **Projects_Included:** The number of practical projects provided.

## 3. Dataset Overview
The table below represents a sample of the data I collected during the research process:

| Duration (Hrs) | Difficulty | Students | Certificate | Projects | Price ($) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 12 | 1 | 5000 | 0 | 1 | 0 |
| 45 | 2 | 2400 | 1 | 5 | 49 |
| 80 | 3 | 1100 | 1 | 10 | 89 |
| 15 | 1 | 4500 | 0 | 2 | 19 |
| 55 | 2 | 3200 | 1 | 6 | 59 |
| 100 | 3 | 800 | 1 | 15 | 99 |
| 20 | 1 | 3800 | 1 | 3 | 29 |
| 35 | 2 | 2100 | 1 | 4 | 39 |
| 70 | 3 | 1500 | 1 | 12 | 79 |
| 10 | 1 | 6000 | 0 | 1 | 0 |

## 4. Observations and Findings
During the data collection, I noticed a clear trend: Beginner courses are often priced lower or offered for free to attract students. However, as the difficulty level increases, the price rises significantly. Also, courses that include hands-on projects are usually more expensive, which makes sense because these projects provide more value to the learner.

## 5. Modeling with KNN
To predict the prices, I chose the K-Nearest Neighbors (KNN) Regressor algorithm. In my understanding, this model works by comparing a new course to the most similar courses in my dataset. By finding the "neighbors," it calculates an average price. I found this to be a straightforward approach for a regression problem like this.

## 6. Conclusion
This assignment was a great learning experience for me. It helped me understand how raw data can be turned into a useful prediction model. Although my dataset is limited to 50 courses, the results show that course attributes are strong indicators of price. In the future, I would like to expand this by adding more variables, such as instructor ratings, to improve the accuracy of my predictions.