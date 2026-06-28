Reflection:
in this project, i cleaned and prepared the dataset for machine learning.
First i convered Price column from text to numeric format  by removing symbol such as $ and commas.

Missing values: i checked for missing values and hanled them appropriately to ensure the dataset was complete.
i used median to fill missing Odometer_km because it is less effect by outlier.
i used mode to fill missing catagorical value like Doors , Accidents, Location because it repersents the most common catagory.

Duplicate removes: I removed duplicate rows to avoid repeat effect dataset final. I corrected catagory values in Location like subrb to suburb and ?? as missing.
Outlier: I identified outliers and handled them using the   IQR method on Price and Odometer_km to reducethier impact on the dataset.
I use one hot encoding for Location columns so catogorical values to numerical feature .
I create new feature like CarAge , Km_per_year , is_urban , LogPrice so these feature could be useful information by machine learning.
Feature scaling: I scaled numerical features to ensure they had similar ranges and improve model performance. I did`nt scale target values like Price and LogPrice.

After preprocessing, the dataset become clean , consistent and ready for machine learning.
