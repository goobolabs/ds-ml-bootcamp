# Foundational Concepts: Data Science & Machine Learning

## 1. Data Science vs. Machine Learning
* **Data Science :** The big picture. It includes gathering data, cleaning it, and finding useful stories or insights from it.
* **Machine Learning :** A specific tool inside Data Science. It teaches computers to learn from old data so they can make smart choices on new data without human help.
* **The Relationship:** Data Science is the whole journey (collecting and cleaning), while Machine Learning is the specific step where the computer does the smart guesswork.

### Example: Spotify/YouTube
* **Data Science Role:** Gathering your listening history, cleaning up skipped songs, and finding out which genres or artists you listen to the most.
* **Machine Learning Role:** The computer learns your favorite music style and automatically guesses a new song you might love, adding it to your playlist.

---

## 2. The Data Science Lifecycle
A data project flows through these simple steps:
1. **Understand the Goal:** Knowing what problem you want to solve.
2. **Get the Data:** Collecting the raw numbers or information.
3. **Clean the Data:** Fixing mistakes and removing missing or broken information.
4. **Explore the Data:** Looking at charts and simple math to find clues.
5. **Train the Model (ML):** Teaching the computer the patterns in the clean data.
6. **Test the Model:** Checking if the computer's guesses are correct.
7. **Launch & Watch:** Putting the system to work in the real world and monitoring it.

> **Where ML Fits:** Machine Learning happens at **Step 5 (Training)** and **Step 6 (Testing)**. It needs perfectly clean data from the earlier steps to work properly.

---

## 3. Supervised vs. Unsupervised Learning

### Supervised Learning
* **Definition:** The computer learns from data that already has the correct answers (labels) included.
* **Example Hospital Triage Check:** A computer is given thousands of old medical charts. Each chart says "Emergency" or "Normal". The computer learns the signs of a dangerous illness so it can automatically alert a nurse when a new, very sick patient arrives.

### Unsupervised Learning
* **Definition:** The computer is given data without any answers or labels, and it must find hidden groups or patterns completely on its own.
* **Example Smart CCTV Camera:** A security camera watches a quiet building every day. Nobody tells it what a "crime" looks like. However, if a person suddenly climbs through a window at midnight, the computer flags it because that movement looks completely different from normal daily walking patterns.

---

## 4. Overfitting: What is it, and how to fix it?
* **What it is:** Overfitting is when a computer **memorizes** the training data too perfectly instead of understanding the real lesson. It gets a 100% score on old data, but completely fails on new data (like a student who memorizes exam answers but fails when the questions change slightly).

### Main Causes
* The computer model is too complex or overthinking simple data.
* The data is too small, so the computer cannot see the bigger picture.
* The computer practiced on the same data for too long.

### How to Prevent it
* **Keep it Simple:** Use simpler settings so the computer does not overthink.
* **Cross-Validation:** Test the computer on different pieces of data to make sure it is steady.
* **Stop Early:** Stop the training the moment the computer starts memorizing details instead of patterns.

---

## 5. Training and Test Data Splitting
Before teaching the computer, we split our data into two parts:
1. **Training Data (80%):** The study material. The computer uses this to practice and learn patterns.
2. **Test Data (20%):** The final exam. This data is hidden from the computer until the very end.
3. **Why it is Mandatory:** If you test a computer using the exact same data it studied, it can cheat by memorizing the answers. Hiding 20% of the data tells you if the computer is genuinely smart or just lucky.

---

## 6. Case Study: Real-World Healthcare (TECO Model)
* **Overview:** A real study about a smart medical system named **TECO** built to help doctors save lives in Intensive Care Units (ICU).
* **How it works:** Instead of checking a patient just once, TECO checks their heart rate, medications, and lab results every single hour. It successfully learned to warn doctors about dangerous patient dynamic shifts hours before standard hospital alarms went off.
* **Lifecycle Stages Covered:** This project focuses on **Data Preparation to Testing**. The researchers organized messy hospital records and rigorously proved that the system's live warnings were highly accurate.

---

## References
* GeeksforGeeks. (2023). *Data Science Lifecycle*.
* Oracle Cloud. (2024). *Lifecycle of machine learning models*.
* Ramakrishnaiah, Y., et al. (2025). *EHR-ML: Designing machine learning models using electronic health records*.
* Oxford Academy. (2025). *A deep learning model for clinical outcome prediction using electronic health records*.

