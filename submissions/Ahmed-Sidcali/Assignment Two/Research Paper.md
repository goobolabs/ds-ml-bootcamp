# This is the research paper for assigment Two 

---
## Title and collection method 
- **Title** screentime spend hours for students and how it affects their study. **Collection method**I make a survey and asked 52 students through a form I have created. Each students tells us his name, age, favorite app, spend hours daily on screen, if he believe whether it makes negetive affect on his study or not, and if he would like to reduce it or not.

---
## Description
### Feature(X)
- Gender(String)
- Age(Numeric between 18-30)
- Fav app(string)
- Spend Hrs(Numeric range e.g. 2-3)
- Neg affect(Yes/No/Maybe)
- Want to reduce spend Hrs(Yes/No/Maybe)
### Label (Y)
- Screentime reduce: Yes/No
Whether the students want to reduce screentime or not to make siminars about making schudule.

---
## Dataset Structure

* **Rows:** 52 students (samples)
* **Columns:** 6 (5 features + 1 label)

### Sample Table (10 rows)


| Gender	| Age |	Fav app |	Spend Hrs |	Neg affect	| Want to reduce spend Hrs|
|---------|-----|---------|-----------|-------------|-------------------------|
|Female	  |20	|TikTok	|2-3 hours	|Yes	|Yes
|Male	    |20	|TikTok |4-5 hours	|Maybe	|Yes
|Female	  |21	|YouTube |6-7 hours	|Yes	|Yes
|Male	    |24	|YouTube	|4-5 hours	|Maybe	|Yes
|Female	  |20	|TikTok	|6-7 hours	|Maybe	|Yes
|Male	    |23	|Facebook	|4-5 hours	|Yes	|Yes
|Male	    |20	|WhatsApp	|6-7 hours	|No	|Yes

---
## Quality isues 
- Missing values like students did enter the age.
- Wrong data type like putting number in yes, no or maybe column

---
## Use case  
It can be used to train a model that creates customized schedule for students who wants to reduce the screentime and focus on studying.




