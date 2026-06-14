name:Miski Abdikadir Osman

# 1. Data Science and Machine Learning — Definitions and Relationship

Data Science is a field that uses mathematics, statistics, and programming to collect, analyze, and interpret large amounts of data in order to help make better decisions. It involves everything from asking a question to finding the answer using data.

Machine Learning is a part of artificial intelligence where we build systems that can learn from data and improve on their own without being manually programmed for every task. Instead of writing rules, we feed the machine data and it figures out the patterns by itself.

Relationship between them:
Machine Learning is a tool used inside Data Science. Data Science is the bigger process — it includes understanding the problem, collecting data, cleaning it, analyzing it, and communicating results. 

Real-life example:
Think about how Spotify recommends songs. Data Science is the whole process — collecting your listening history, cleaning the data, and figuring out what to do with it. Machine Learning is the part where the algorithm studies your habits and learns that if you like artist A and artist B, you might also like artist C. Data Science sets up the problem; Machine Learning solves it.

---

# 2. The Data Science Lifecycle and Where Machine Learning Fits

The Data Science lifecycle is the step-by-step process of solving a problem using data. The stages are:

Stage 1 — Problem Definition:** You identify what question you are trying to answer. For example, "Which students are likely to fail this semester?"

Stage 2 — Data Collection:** You gather the data you need, such as attendance records, test scores, and assignment submissions.

Stage 3 — Data Preprocessing:** You clean the data — removing errors, filling in missing values, and preparing it in a format the model can understand.

Stage 4 — Modeling:** This is where Machine Learning fits in. You choose an algorithm, train it on the prepared data, and let it learn the patterns.

Stage 5 — Evaluation:** You test how well the model performs using metrics like accuracy. If it is not good enough, you go back and improve it.

Stage 6 — Deployment:** You put the working model into a real application where people can use it.

Why does ML fit at Stage 4?
By the time you reach Stage 4, your data is already clean and structured. The ML algorithm needs good quality data to learn from — it cannot work on raw, messy data. That is why all the earlier stages must happen first. After Stage 4, you still need to evaluate and deploy the model, so ML is in the middle of the process, not the end.

---

# 3. Supervised Learning vs. Unsupervised Learning

Supervised Learning is when we train a model using labeled data, meaning data where the correct answer is already known. The model learns by comparing its predictions to the correct answers and adjusting itself.

Example: Email spam detection. Every email in the training dataset is already tagged as either "Spam" or "Not Spam." The model studies these examples and learns what spam looks like. When a new email arrives, it can classify it correctly on its own.

Unsupervised Learning is when the data has no labels — there are no correct answers given. The model has to find hidden patterns or groups in the data by itself.

Example: Customer segmentation in a supermarket. The store has purchase data for thousands of customers but no categories. A clustering algorithm groups customers automatically — for example, one group that only buys essentials, another that spends on luxury items, and another that shops only during sales. Nobody told the model what the groups should be; it discovered them on its own.

Key difference in simple words: In supervised learning, the model is like a student studying with an answer key. In unsupervised learning, the model is like a student who is given a pile of books and asked to organize them without being told the categories.

---

# 4. What Causes Overfitting and How to Prevent It

What is overfitting?
Overfitting happens when a machine learning model learns the training data too well — including the noise and random mistakes in that data — and then fails to perform well on new data it has never seen before.

A simple way to picture it: imagine a student who memorizes every past exam paper word for word. They will do perfectly on those exact papers but struggle badly if even one question is worded differently. The student memorized instead of actually understanding.

What causes it?
- The model is too complex for the size of the dataset
- There is too little training data
- The model is trained for too long
- The data has a lot of noise or irrelevant features

How to prevent it:
- Train/Test Split — Keep a separate portion of data the model never sees during training, so you can honestly test its performance.
- Cross-Validation— Test the model on different portions of the data multiple times to make sure it generalizes well.
- Regularization — Add a penalty to the model for being too complex, which forces it to stay simple.
- Dropout — Used in neural networks; randomly switches off some neurons during training so the model does not rely too heavily on any single path.
- Early Stopping — Stop training the model once its performance on the validation set starts getting worse instead of better.
- Getting more data — The more real examples the model sees, the better it generalizes.

---

# 5. How Training and Test Data Are Split and Why It Is Necessary

How the split works:
When you have a labeled dataset, you divide it into two parts before training:
- Training set— usually 70% to 80% of the data. This is what the model learns from.
- Test set — usually 20% to 30% of the data. This is set aside and the model never sees it during training.

Sometimes a third portion called the **validation set** is also created (often 10–20%) to help tune the model during training without touching the test set.

The split must be done randomly so that both sets are a fair representation of the full data. In classification problems, we also make sure that the ratio of classes is the same in both sets — this is called **stratified splitting**.

Why is this necessary?
If you tested your model on the same data it was trained on, you would get misleadingly high accuracy because the model has already seen those examples. It would be like giving a student the exact same questions they studied — of course they would score 100%, but that does not mean they understand the subject.

The test set acts like a real exam. It tells you honestly how the model will behave when it is deployed in the real world on data it has never seen before. This makes the split a fundamental and non-negotiable step in building any machine learning model.

---

# 6. Case Study — Machine Learning Applied in Healthcare: Diabetic Retinopathy Detection

Source: Google DeepMind / Gulshan et al. (2016), *Nature* — and related follow-up studies including smartphone-based retinal screening research published on NCBI/PMC.

Background:
Diabetic retinopathy (DR) is an eye disease caused by diabetes and is one of the leading causes of blindness worldwide. Detecting it requires a trained eye specialist to manually examine photographs of the patient's retina — a process that is slow and unavailable in many parts of the world where there are not enough ophthalmologists.

**What the researchers did:**
Google DeepMind trained a deep Convolutional Neural Network (CNN) — a type of supervised machine learning model — on hundreds of thousands of labeled retinal images. Each image had already been examined and graded by ophthalmologists, so the model had correct labels to learn from. After training using TensorFlow and the Inception V3 model architecture, the AI system's diagnostic accuracy was reported to be better than that of ophthalmologists.

Follow-up studies extended this work to smartphone cameras. One study found that the AI software showed 95.8% sensitivity and 80.2% specificity for detecting any diabetic retinopathy, and 99.1% sensitivity when detecting sight-threatening diabetic retinopathy. Most importantly, the algorithm was able to detect diabetic retinopathy signs in 1,258 patients before family doctors had detected them, representing 7.9% of the total DR patients identified by the doctors.

Which stages of the Data Science lifecycle does this cover?

- *Problem Definition: Can AI detect diabetic retinopathy from retinal photos as accurately as a specialist?
- Data Collection:Hundreds of thousands of retinal images were gathered from clinics and hospitals.
- Data Preprocessing:Images were normalized, resized, and cleaned. Low-quality images were removed.
- Modeling (ML): A deep CNN was trained using supervised learning on the labeled retinal images.
- Evaluation:** The model was tested on separate image sets and measured using sensitivity and specificity scores.
- Deployment: The system was integrated into clinical workflows and adapted for use with smartphone cameras for mass screening in areas with limited access to specialists.

This case study is a perfect example of the full Data Science lifecycle in action. It also shows how Machine Learning, when applied correctly, can solve real-world problems in healthcare — helping patients get diagnosed earlier and in places that would otherwise have no access to specialist care.