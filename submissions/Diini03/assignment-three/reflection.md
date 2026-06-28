# Reflection: Data Preprocessing Pipeline

## Price Cleaning

The Price column was a mix of strings like `$1,500` and plain floats like `1500.0`. I stripped the `$` and `,` characters then converted to numeric. This had to happen before anything else because Price is the target — if it stays as a string, nothing downstream works.

## Fixing Location Before Imputation

I fixed the typos first (`Subrb → Suburb`) and converted `??` to null before imputing. If I did it the other way around, the mode would have been calculated on dirty data and I might have filled missing rows with a wrong value.

## Imputation Choices

- **Odometer_km → median:** Mileage is usually skewed — a few very high-mileage cars pull the mean up. Median is more stable.
- **Doors → mode:** Doors is basically a category (2, 3, 4, 5). Most cars have 4 doors, so mode makes sense.
- **Accidents → mode:** Same logic. Most cars have 0 accidents. Using mean would give a decimal like 0.3 which doesn't make sense.
- **Location → mode:** City is the most common location. Filling with the most frequent category is a safe assumption when there's no other context.

## Removing Duplicates

I dropped duplicates after cleaning Price and fixing Location so duplicates are compared on clean values, not messy ones.

## IQR Capping

I used IQR capping instead of removing outliers completely because removing rows loses data. Capping clips extreme values to the fence (Q1 - 1.5×IQR, Q3 + 1.5×IQR) so they stay in the dataset but don't distort the model.

## Feature Engineering

- **CarAge:** More interpretable than raw Year. A model understands "this car is 10 years old" better than "this car is from 2015."
- **Km_per_year:** Combines Odometer and CarAge into one signal — how hard was the car used per year. A car with 200k km but 20 years old is different from one with 200k km but 5 years old.
- **Is_Urban:** Simple binary derived from Location_City. Useful if the model benefits from a direct city/non-city signal without needing to look at all three location dummies.
- **LogPrice:** Added as an alternative target because Price is skewed. A log-transformed target often helps regression models perform better on skewed distributions.

## Scaling

I only scaled continuous numeric features: Odometer_km, Doors, Accidents, CarAge, Km_per_year. I left Price, LogPrice, and the Location dummy columns unscaled. Scaling binary (0/1) columns is unnecessary and can make them harder to interpret.
