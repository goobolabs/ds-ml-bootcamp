Assignment three 

Why were median and mode used?
What it entails is lining up all of your numbers from smallest to largest and selecting the precise number that falls in the center.
Motives behind using: Use it if there are many outliers or distorted data. The median completely ignores how insane the extreme ends are; it only takes into account what is happening in the middle.
What it is: The most frequently occurring category or number.
Motives for its use: Use it when dealing with categorical data (words or labels instead of numbers) or when you need to identify the single most popular choice.

The Reasons for IQR Caping
IQR Capping is mostly used in data cleaning since it offers a solid middle ground by reducing the detrimental effects of outliers without eliminating your crucial data.
For instance
If you exclude each row with an outlier, your dataset will become smaller. If a row has a ridiculous outlier in the Price column but wonderful, significant data in other columns, such as "house_age, location, and size," removing the entire row would be a waste of that valuable information.

which features you designed and the rationale behind securely calculating km_per_year I developed a new feature by dividing the Odometer_km by the Car_Age.
IQR Capping on ODOMETER_KM & PRICE
Q1 - 1.5 X IQR and Q3 + 1.5 X IQR were used to calculate the boundaries, and values outside of these bounds were capped using np.clip().
Encoding One-Hot (pd.dummies())
created distinct binary columns (0s and 1s) from categorical text features (such as Location).