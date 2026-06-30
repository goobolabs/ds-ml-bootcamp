# Reflection Paper — Car Price Prediction

---

## 1. What I Implemented

I used the cleaned car dataset from Assignment Three to build two regression models that predict car prices. The dataset went through a full preprocessing pipeline — cleaning, encoding, feature engineering, and scaling — before being used here.

I trained a Linear Regression model as a baseline and a Random Forest Regressor as the stronger model. Both were trained on 80% of the data and evaluated on the remaining 20%.

---

## 2. Comparison of Models

In the sanity check, I picked one row from the test set and compared both predictions against the actual price. The Random Forest prediction was noticeably closer to the actual value. Linear Regression gave a reasonable estimate but was further off.

This makes sense — car prices depend on multiple factors that interact in non-linear ways. Age, mileage, accidents, and location don't just add up in a straight line. Random Forest handles those interactions better by nature.

---

## 3. Understanding Random Forest

Random Forest is an ensemble model — it builds many decision trees during training, each one trained on a random subset of the data and features. When making a prediction, every tree gives its own answer and the final result is the average of all of them.

The strength of this approach is that individual trees can overfit, but when you average hundreds of them together the errors cancel out and the overall prediction becomes more stable and accurate.

---

## 4. Metrics Discussion

Random Forest had a higher R² and lower MAE and RMSE compared to Linear Regression. A higher R² means it explains more of the variance in car prices. Lower MAE and RMSE means its predictions are closer to the actual values on average.

Linear Regression's weakness here is that it assumes a straight-line relationship between features and price. That assumption doesn't hold well for car pricing — a car that's 1 year old vs 10 years old doesn't lose value in a straight line, and the effect of accidents on price depends on the car type and mileage.

---

## 5. My Findings

Random Forest is the better model for this problem. The metrics are stronger and the sanity check showed it predicting closer to the real price. More importantly it captures the kind of non-linear patterns that actually drive car prices — mileage interacting with age, location affecting price differently depending on car type, and so on.

That said, Linear Regression still has value as a baseline. If the Random Forest result didn't beat it by much, I'd question whether the extra complexity is worth it. In this case it clearly was.
