# Assignment Four – Part C: Reflection Paper

**Name:** Abdurahman Aden (Kacabdev)

---

## 1. What did I implement?

For this assignment I took the cleaned car dataset I built in Assignment Three (`clean_car_dataset.csv`) and used it to predict car `Price`. The features I used were everything in the dataset except `Price` itself and `LogPrice` (I left `LogPrice` out because it's just a log-transformed copy of the price, so keeping it in would basically let the model "cheat").

I split the data 80/20 into training and testing sets (`random_state=42` so it's reproducible), and trained two models on the exact same training data:

- A **Linear Regression** model, as the simple baseline.
- A **Random Forest Regressor** with 100 trees (`n_estimators=100`, `random_state=42`).

Then I wrote a small helper function that prints R², MAE, MSE, and RMSE for whichever model I pass into it, and ran it for both models so I could compare them side by side.

## 2. Comparison of Models

Here's where things got more interesting than I expected. Going into this, I honestly assumed Random Forest would just win across the board — that's the impression I had from the lesson, since it's described as a more powerful, flexible model. But my actual numbers were:

| Metric | Linear Regression | Random Forest |
|---|---|---|
| R² | 0.44 | 0.24 |
| MAE | 1,428.05 | 1,235.20 |
| RMSE | 1,937.86 | 2,248.61 |

Linear Regression actually had the better R² and RMSE, while Random Forest had the better MAE. That's not a typo — it genuinely surprised me the first time I ran it, so I double-checked the code and re-ran it to be sure.

For the sanity check, I picked one row from the test set: a car with an actual price of $4,379.

- Linear Regression predicted **$5,040.46** (off by about $661).
- Random Forest predicted **$4,484.00** (off by about $105).

So for that one specific car, Random Forest was noticeably closer. This actually lines up with the MAE results — Random Forest tends to land closer to "typical" cars on average, but Linear Regression's overall fit (R², RMSE) was better across the whole test set. My read on this is that Random Forest is probably getting a few predictions badly wrong somewhere in the test set (which drags RMSE up a lot, since RMSE punishes big misses harder than MAE does), while doing reasonably well on the rest.

## 3. Understanding Random Forest

In my own words: Random Forest is not one single model, it's actually a **team of decision trees** working together. Each individual decision tree looks at the data and makes its own split-by-split decision to arrive at a predicted price. On its own, one decision tree can be pretty unstable and prone to overfitting — a small change in the data can change the whole tree.

Random Forest fixes this by training a whole bunch of trees (in my case, 100), where each tree only sees a random subset of the training data and, often, a random subset of the features at each split. Once all the trees are trained, Random Forest doesn't just trust one of them — for regression, it takes the **average** of all 100 trees' predictions. The idea is that even if individual trees are a bit noisy or wrong in different directions, averaging them out cancels a lot of that noise and gives a more stable, reliable prediction than any single tree could give alone.

## 4. Metrics Discussion

Looking strictly at the numbers: Linear Regression had the better R² (0.44 vs. 0.24) and the better RMSE (1,937.86 vs. 2,248.61). Random Forest had the better MAE (1,235.20 vs. 1,428.05).

What this tells me is that neither model is "clearly" the winner here — it depends which metric you care about most. Random Forest is doing a decent job on most "normal" cars (hence the lower average absolute error), but it seems to be making a few larger mistakes somewhere that hurt its RMSE and R² more than they hurt Linear Regression's. Since RMSE and R² are both more sensitive to large errors, this suggests Random Forest's error distribution has more of these bigger misses, even if its typical error is smaller.

I think a big part of the explanation is dataset size. My dataset only has 140 rows total, so after the 80/20 split, Random Forest was trained on just 112 examples. Random Forest models generally need more data than a simple Linear Regression to really show their advantage, because with only 112 rows split across 100 trees (each seeing a bootstrap sample), there's a real risk some trees are trained on very little useful variety, which can hurt the ensemble's overall fit. Linear Regression, being a much simpler model with far fewer parameters to estimate, doesn't need nearly as much data to find a reasonably stable line/plane through the data.

## 5. My Findings

If I had to pick one model for this specific car price prediction task, right now, with this specific dataset, I would lean towards **Linear Regression** — mainly because of its higher R² and lower RMSE, which suggests it's capturing the overall pattern in the data a bit more consistently, and it's also simpler and easier to explain to someone (e.g., "price goes up as the car gets newer and mileage goes down, roughly like this"). That interpretability matters to me as someone still learning — I can actually look at the coefficients and reason about whether they make sense.

That said, I don't think this means Random Forest is a "worse" model in general — I think it's more that 140 rows is a pretty small dataset for a model that thrives on volume and variety. If I collected a lot more car listings (say, a few thousand instead of 140), I would genuinely expect Random Forest to pull ahead, especially if the real relationship between mileage, age, accidents, and price isn't purely linear (which, realistically, it probably isn't — depreciation curves are rarely straight lines, just like the Polynomial Regression example from Lesson 4). So my honest conclusion is: for now, with this dataset, Linear Regression; but I wouldn't rule out Random Forest doing better once there's more data to work with.

Fiiro gaar ah: dataset-kaygu wuxuu leeyahay 141 saf oo keliya, taasoo keentay natiijo aan la filayn — Linear Regression ayaa ka fiican Random Forest R² ahaan, taasoo taariikh-ahaan macquul ah (RF wuxuu u baahan yahay data badan si uu u muujiyo awoodiisa). Waan ku daray sabab dhab ah oo ku saabsan tan, aadan tahay kaliya "RF ayaa had iyo jeer wanaagsan."

---

