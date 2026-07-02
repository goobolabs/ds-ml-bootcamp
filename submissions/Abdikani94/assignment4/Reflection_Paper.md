
1. What I Did

I used my cleaned dataset from Assignment Three (140 rows, no missing values). I split it 80/20 into train and test sets with random_state=42. Then I trained two models on the same training data: Linear Regression and a Random Forest with 100 trees. After that I checked R², MAE, MSE, and RMSE for both, and did a sanity check by comparing both models' predictions to one real test row.

2. Comparing the Models

For the test row I checked, the actual price was $7,009. Linear Regression predicted $5,580 (off by about $1,429). Random Forest predicted $6,935 (off by only about $74). On this one example, Random Forest was much closer.

3. What Random Forest Is

Random Forest is a bunch of decision trees put together. Each tree trains on a random slice of the data, so every tree turns out a bit different. To make a prediction, all the trees guess and the forest averages those guesses. Averaging cancels out the mistakes any single tree makes, which is why it's usually more stable than one tree alone.

4. Looking at the Metrics

Linear Regression:
  R²   : 0.453
  MAE  : 1,392
  MSE  : 3,643,877
  RMSE : 1,909

Random Forest:
  R²   : 0.292
  MAE  : 1,172
  MSE  : 4,710,242
  RMSE : 2,170

This was mixed. Random Forest had the lower MAE, so on average its errors were smaller. But Linear Regression had the higher R² and lower RMSE, meaning it explained more of the price variation and didn't make as many big mistakes.

My guess: Random Forest does well on most rows but messes up badly on a few, which drags down its R² and RMSE since those two punish big errors more than MAE does. With only 112 training rows, the forest probably doesn't have enough data to build solid splits yet.

5. My Take

Going off the numbers alone, I'd pick Linear Regression here, mainly because of the better R² and RMSE — it's more consistent across the whole test set. But the sanity check is a reminder that one row isn't the whole story; Random Forest nailed that car's price almost exactly while Linear Regression missed it by over a thousand dollars.

If I had more data, I think Random Forest would pull ahead, since tree models usually need more rows to perform well. For now, with this small dataset, Linear Regression feels like the safer choice.