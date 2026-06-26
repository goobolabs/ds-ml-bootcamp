# Data Foundations for Machine Learning
## A Self-Collected Dataset on Football Highlight Video Engagement

**Prepared by:** SeadAbdirizak
**Assignment:** Data Foundations for Machine Learning (Lessons 1–3)
**Date:** June 2026

---

## 1. Title and Collection Method

**Dataset title:** *Engagement Performance of Football Highlight Clips on Social Media*

I work as a content editor producing short football highlight reels (Messi, Ronaldo, Neymar, Argentina, Barcelona, and a few local clubs), which I publish on TikTok, Instagram, and Facebook, some under my own page and a few under the Sead Creativity brand for clients. For this assignment I treated my own publishing history as a live data source instead of pulling something from Kaggle.

Between May 20 and June 14, 2026, I logged every highlight clip I edited and posted, recording how it was made and how it performed. The method was observation: each time I published a video, I noted production details (length, color grading, caption language, posting time) in a spreadsheet, then came back 7 days later to record the views, likes, comments, and shares shown on the platform. That gave me 55 rows, one per published video.

Before any cleaning, modeling, or analysis can happen, somebody has to decide what's worth measuring and go get it. That's the stage this dataset belongs to — data collection. Lesson 4 will move it into preprocessing.

## 2. Description of Features and Label

The dataset splits into two kinds of columns: things I knew *before* publishing a video (the features, X), and things I could only know *after* publishing it (the raw outcome numbers, which I used to build the label, y).

**Features (X), known at publish time:**

| Feature | Type | Description |
|---|---|---|
| Platform | Categorical | TikTok, Instagram, or Facebook |
| Video Length (seconds) | Numeric | Clip duration |
| Player/Team Featured | Categorical | Messi, Ronaldo, Neymar, Argentina, Barcelona, Local Team, Other |
| Caption Language | Categorical | Somali, English, Arabic, or Mixed |
| Posting Time | Categorical | Morning, Afternoon, Evening, Night |
| Day of Week | Categorical | Monday through Sunday |
| Color Graded | Binary | Whether I applied color correction before export |
| Burned-in Captions | Binary | Whether subtitles were embedded in the video itself |

**Raw outcome data, recorded 7 days after posting:**

Views, Likes, Comments, Shares.

**Label (y):** From the raw outcomes I calculated an **Engagement Rate**, defined as (Likes + Comments + Shares) ÷ Views × 100. That single number is what the dataset is ultimately trying to explain or predict — the column that turns this from a pile of numbers into a supervised learning problem.

## 3. Dataset Structure

The full dataset has **55 rows and 13 columns** (8 features, 4 raw outcome metrics, and 1 derived label). Below is a sample of 8 rows, showing the columns most relevant to the prediction problem.

| ID | Platform | Length (s) | Player/Team | Caption Lang | Posting Time | Color Graded | Views | Likes | Comments | Shares | Engagement Rate (%) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TikTok | 38 | Messi | Somali | Evening | Yes | 14,200 | 1,850 | 96 | 210 | 15.18 |
| 2 | Instagram | 52 | Ronaldo | English | Night | Yes | 9,800 | 740 | 41 | 88 | 8.88 |
| 3 | Facebook | 27 | Neymar | Mixed | Afternoon | No | 5,200 | 310 | 15 | 22 | 6.67 |
| 4 | TikTok | 45 | Argentina | Somali | Morning | Yes | 22,100 | 3,100 | 188 | 402 | 16.69 |
| 5 | Instagram | 33 | Barcelona | English | Evening | No | 4,100 | 205 | 9 | 14 | 5.56 |
| 6 | TikTok | 60 | Local Team | Somali | Afternoon | Yes | 1,800 | 95 | — | 7 | (missing) |
| 7 | Facebook | "0:41"* | Messi | English | Night | No | 6,300 | 410 | 19 | 31 | 7.33 |
| 8 | TikTok | 29 | Ronaldoo* | English | Night | Yes | 8,700 | 690 | 33 | 71 | 9.13 |

\* Row 7 was logged in mm:ss format instead of seconds. Row 8 has a typo in the team name ("Ronaldoo"). Both are kept in the table on purpose, to show what the raw data actually looked like before cleaning.

### Full Dataset (All 55 Rows)

This is the complete dataset, numbered 1 to 55 in the order each video was logged, with all 13 columns. Blank cells and unconverted formats (mm:ss length, "Ronaldoo", "Barca") are left exactly as I originally recorded them — none of that gets fixed until Lesson 4.

| ID | Platform | Length(s) | Player/Team | Caption Lang | Posting Time | Day of Week | Color Graded | Burned-in Captions | Views | Likes | Comments | Shares | Engagement Rate(%) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Instagram | 61 | Neymar | Mixed | Evening | Thursday | No | Yes | 10,522 | 620 | 86 | 146 | 8.1 |
| 2 | Instagram | 64 | Ronaldo | Mixed | Evening | Friday | Yes | Yes | 22,621 | 2,347 | 102 | 400 | 12.59 |
| 3 | Facebook | 54 | Messi | Arabic | Evening | Saturday | Yes | No | 16,775 | 2,581 | 178 | 295 | 18.21 |
| 4 | TikTok | 1:04 | Ronaldo | Arabic | Night | Wednesday | No | No | 16,405 | 1,031 | 79 | 326 | 8.75 |
| 5 | TikTok | 65 | Barca | English | Night | Thursday | No | Yes | 8,192 | 1,147 | 131 | 74 | 16.5 |
| 6 | Instagram | 40 | Neymar | Mixed | Afternoon | Tuesday | Yes | Yes | 6,767 | 776 | 51 | 20 | 12.52 |
| 7 | Instagram | 52 | Messi | Arabic | Evening | Tuesday | Yes | Yes | 20,119 | 2,409 | 98 | 90 | 12.91 |
| 8 | TikTok | 46 | Neymar | English | Morning | Wednesday | Yes | Yes | 5,002 | 587 | 24 | 37 | 12.95 |
| 9 | Instagram | 27 | Local Team | Arabic | Evening | Friday | Yes | Yes | 2,616 | 269 | 21 | 16 | 11.7 |
| 10 | Facebook | 39 | Ronaldoo | Arabic | Night | Sunday | Yes | No | 2,263 | 284 | 38 | 44 | 16.17 |
| 11 | Instagram | 59 | Barcelona | Somali | Evening | Friday | Yes | Yes | 9,325 | 804 | 66 | 194 | 11.41 |
| 12 | TikTok | 33 | Messi | Mixed | Afternoon | Tuesday | No | Yes | 8,172 | 582 | (missing) | 86 | (missing) |
| 13 | Instagram | 64 | Ronaldo | Mixed | Evening | Friday | Yes | Yes | 22,621 | 2,347 | 102 | 400 | 12.59 |
| 14 | Facebook | 40 | Ronaldo | Somali | Morning | Thursday | Yes | Yes | 3,969 | 611 | 55 | 52 | 18.09 |
| 15 | Facebook | 23 | Barcelona | English | Afternoon | Tuesday | Yes | Yes | 6,733 | 948 | (missing) | 117 | (missing) |
| 16 | Instagram | 27 | Neymar | English | Morning | Monday | Yes | No | 9,136 | 668 | 68 | 86 | 9.0 |
| 17 | TikTok | 55 | Ronaldo | Arabic | Evening | Friday | No | Yes | 9,956 | 1,136 | 165 | 121 | 14.28 |
| 18 | TikTok | 26 | Argentina | English | Morning | Sunday | No | Yes | 43,760 | 6,126 | 525 | 875 | 17.2 |
| 19 | Instagram | 61 | Other | Mixed | Morning | Friday | Yes | Yes | 6,675 | 746 | 97 | 154 | 14.94 |
| 20 | Instagram | 38 | Argentina | English | Evening | Thursday | No | No | 8,410 | 660 | 99 | 199 | 11.39 |
| 21 | Instagram | 26 | Ronaldo | Mixed | Morning | Thursday | No | Yes | 5,160 | 429 | 29 | 103 | 10.87 |
| 22 | Facebook | 59 | Argentina | Arabic | Afternoon | Wednesday | Yes | Yes | 5,705 | 387 | 76 | 45 | 8.9 |
| 23 | Facebook | 45 | Argentina | Mixed | Evening | Thursday | Yes | Yes | 4,948 | 497 | 68 | 56 | 12.55 |
| 24 | Facebook | 57 | Barca | Arabic | Morning | Monday | Yes | Yes | 3,007 | 239 | 17 | 36 | 9.71 |
| 25 | Facebook | 34 | Messi | Mixed | Afternoon | Friday | No | No | 10,772 | 1,042 | 54 | 254 | 12.53 |
| 26 | Facebook | 23 | Local Team | Arabic | Morning | Friday | Yes | Yes | 2,580 | 285 | 43 | 22 | 13.57 |
| 27 | TikTok | 20 | Neymar | English | Morning | Tuesday | Yes | Yes | 11,736 | 1,567 | (missing) | 164 | (missing) |
| 28 | TikTok | 35 | Messi | Arabic | Morning | Wednesday | Yes | Yes | 6,572 | 671 | 112 | 35 | 12.45 |
| 29 | Facebook | 45 | Ronaldo | Mixed | Night | Friday | Yes | No | 8,704 | 1,111 | 112 | 103 | 15.23 |
| 30 | Instagram | 21 | Neymar | English | Morning | Monday | Yes | Yes | 9,120 | 963 | 160 | 147 | 13.93 |
| 31 | Facebook | 36 | Other | Somali | Night | Tuesday | Yes | Yes | 6,429 | 1,017 | 54 | 24 | 17.03 |
| 32 | Instagram | 31 | Ronaldo | Arabic | Afternoon | Monday | Yes | Yes | 5,756 | 607 | (missing) | 50 | (missing) |
| 33 | TikTok | 27 | Messi | Mixed | Morning | Thursday | Yes | Yes | 22,363 | 3,217 | 138 | 506 | 17.27 |
| 34 | Facebook | 42 | Argentina | Arabic | Night | Tuesday | Yes | No | 12,621 | 1,869 | 161 | 241 | 17.99 |
| 35 | Facebook | 26 | Local Team | Somali | Afternoon | Monday | Yes | Yes | 1,686 | 168 | 7 | 5 | 10.68 |
| 36 | Facebook | 61 | Argentina | English | Night | Wednesday | Yes | Yes | 2,316 | 283 | 11 | 44 | 14.59 |
| 37 | Instagram | 22 | Ronaldo | Arabic | Afternoon | Saturday | Yes | Yes | 16,894 | 2,115 | 248 | 279 | 15.64 |
| 38 | Facebook | 30 | Barcelona | Somali | Afternoon | Wednesday | Yes | No | 5,434 | 562 | 95 | 28 | 12.61 |
| 39 | TikTok | 61 | Neymar | Mixed | Evening | Saturday | Yes | Yes | 28,635 | 2,059 | 506 | 675 | 11.31 |
| 40 | TikTok | 36 | Neymar | Mixed | Morning | Sunday | No | Yes | 20,714 | 2,360 | 123 | 300 | 13.44 |
| 41 | Instagram | 26 | Messi | Arabic | Morning | Saturday | Yes | Yes | 19,164 | 965 | 208 | 247 | 7.41 |
| 42 | Instagram | 64 | Messi | English | Night | Wednesday | No | Yes | 5,017 | 713 | 28 | 117 | 17.1 |
| 43 | Facebook | 18 | Ronaldo | Arabic | Evening | Wednesday | Yes | Yes | 9,501 | 922 | 74 | 38 | 10.88 |
| 44 | TikTok | 0:21 | Neymar | Arabic | Afternoon | Tuesday | Yes | Yes | 28,092 | 2,726 | 123 | 554 | 12.11 |
| 45 | Instagram | 53 | Barcelona | English | Morning | Monday | No | Yes | 15,638 | 866 | 265 | 90 | 7.81 |
| 46 | Instagram | 44 | Local Team | Arabic | Evening | Wednesday | Yes | No | 3,689 | 455 | 20 | 63 | 14.58 |
| 47 | TikTok | 31 | Ronaldo | Mixed | Afternoon | Thursday | Yes | Yes | 21,323 | 1,868 | 112 | 176 | 10.11 |
| 48 | Instagram | 0:54 | Messi | English | Morning | Saturday | No | Yes | 13,872 | 1,841 | 152 | 216 | 15.92 |
| 49 | Facebook | 40 | Ronaldo | Somali | Morning | Thursday | Yes | Yes | 3,969 | 611 | 55 | 52 | 18.09 |
| 50 | Instagram | 63 | Messi | Mixed | Night | Monday | Yes | Yes | 25,663 | 1,590 | 158 | 371 | 8.26 |
| 51 | Facebook | 24 | Messi | Mixed | Morning | Friday | Yes | Yes | 5,418 | 451 | 31 | 46 | 9.75 |
| 52 | Facebook | 45 | Argentina | Somali | Morning | Monday | Yes | No | 11,639 | 583 | 134 | 290 | 8.65 |
| 53 | Instagram | 38 | Neymar | English | Night | Friday | Yes | No | 10,546 | 591 | 70 | 236 | 8.51 |
| 54 | Facebook | 44 | Messi | Somali | Evening | Tuesday | No | Yes | 8,367 | 751 | 79 | 26 | 10.23 |
| 55 | Instagram | 65 | Ronaldo | Somali | Afternoon | Thursday | Yes | Yes | 7,894 | 650 | 136 | 109 | 11.34 |

---

## 4. Quality Issues

The dataset is about as messy as you'd expect from a spreadsheet logged by hand over three weeks.

The biggest gap is missing comment counts — 4 of the 55 rows don't have one, mostly from early in the collection period before I got into the habit of checking that field every time. Engagement rate can't be calculated for those rows until I decide how to handle it. Close behind that is a formatting problem: 3 entries have video length written as mm:ss ("0:41") instead of plain seconds, because I copied the duration straight off the CapCut timeline and never converted it.

There are also a few typos in the player/team names — "Ronaldoo" instead of "Ronaldo," and "Barca" instead of "Barcelona" in two rows. Left uncleaned, a model would read these as separate categories from the correctly spelled ones, which makes no sense. And two videos show up twice in the log; I'd recorded their numbers once at the 24-hour mark and again at 7 days, before I settled on one consistent measurement window, and never went back to delete the earlier entries.

Then there's class imbalance: Messi, Ronaldo, and Neymar content together make up 36 of the 55 videos, while local Somali club content is only 4. A model trained on this would end up knowing a lot about global stars and almost nothing about local teams. And one outlier sits well outside the rest of the data — an Argentina World Cup compilation that pulled in over 40,000 views, roughly four times the dataset average, which would throw off any model that isn't built to handle it.

## 5. Learning Type: Supervised

This is a **supervised learning** problem. Every row pairs known inputs (platform, length, team, caption language, timing, editing choices) with a measurable output (engagement rate) recorded after the fact. That input-output pairing is what defines supervised learning in Lesson 2: the model learns a mapping from X to y using examples where y is already known.

There's a secondary, unsupervised angle worth mentioning too. If I dropped the engagement rate column entirely and just clustered the videos by their feature values — length, team, caption language, timing — I could look for natural groupings in *how* I produce content, separate from how well it performed. That would be a legitimate unsupervised exploration, just not the main framing here, since I built this dataset specifically around a label I can calculate and actually care about.

## 6. Use Case and Lifecycle Placement

I want this data for two things. First, predicting the actual engagement rate a video will get before I even publish it — that's regression. Second, just sorting upcoming clips into High, Medium, or Low engagement buckets so I know which ones are worth extra promotion — that's classification.

Regression would run off the planned length, team, caption language, and posting time. A decent model could tell me, before I even export a clip, whether it's worth posting at 9pm versus waiting for the evening slot, or whether a Somali caption beats an English one for a given matchup. Classification is the easier, more forgiving version of the same idea — I don't need an exact number, just a quick flag for which clips deserve extra push.

In terms of the data science lifecycle from Lesson 1, this assignment covers data collection. Lesson 4 takes it into data preparation: filling or dropping the missing comment counts, standardizing the length column to seconds, fixing the name typos, removing the duplicate rows, and encoding categorical columns like platform and caption language into numbers a model can actually use. After that comes modeling and evaluation — training a regression or classification model and checking its error rate — and eventually deployment, which for me would realistically just mean a small checklist or script I run before publishing a new clip.

## Next Steps

The dataset itself (the full 55-row spreadsheet) can be exported as a CSV file for submission alongside this report, if needed.
