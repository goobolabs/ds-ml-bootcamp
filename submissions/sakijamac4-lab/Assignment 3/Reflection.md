# Reflection: Data Preprocessing Pipeline

## Step 2: Clean Target Formatting (Price)
I removed currency symbols and commas from the Price column
and converted it to float to ensure it is numeric and ready
for analysis.

## Step 4: Imputation Choices

##### Odometer_km → Median
I chose median for Odometer_km because its data contains
outliers with very high and very low values. Unlike mean,
median is not affected by outliers, which is why I chose it.

### Doors, Accidents, Location → Mode
I chose mode for Doors, Accidents, and Location because they
are categorical data, where Mean or Median would not be
meaningful. For example, with Doors I found values like
(2,3,4,4,4,5,3,4,2,5,4,4,4)  the mode gives 4, which is a
real and acceptable value in the dataset. If I chose median
it would give 3.5, which is not a valid door count and makes
no sense in the context of this dataset, making mode the far
better choice.

## Step 6: Outlier Handling (IQR Capping)
I used Interquartile Range (IQR) Capping because my dataset
contained outliers. For example, if the data is
(10k, 20k, 30k, 50k, 900k), the value 900k is an outlier far
from the rest of the data. If this outlier is not handled, it
can negatively affect the model, as the model may treat it as
highly important simply because it is much larger than the
other values  even though it is not truly significant.
Therefore, I used IQR Capping to reduce the effect of
outliers while preserving the data.

## Step 8: Feature Engineering

### CarAge
I created a new feature called CarAge to represent the age
of the vehicle. The age of a car is an important factor that
often affects its price, so this feature provides useful
information for the model.

### Is_Urban
I created a new feature called Is_Urban by combining
Location_City and Location_Suburb into a single binary
feature. This feature indicates whether a vehicle is located
in an urban area (city or suburb) versus a rural area.
I created it because vehicle prices and usage patterns may
differ between urban and non-urban locations.

### Km_per_year
I created a new feature called Km_per_year, which was
calculated by dividing the vehicle's Odometer_km by its age
(CarAge). This feature measures the average number of
kilometers driven per year and provides a better
representation of vehicle usage than the total odometer
reading alone.

## Step 9: Feature Scaling
I used StandardScaler to standardize the numerical features
by transforming them to have a mean of 0 and a standard
deviation of 1. This prevents features with larger values
from dominating those with smaller values and helps many
machine learning algorithms learn more effectively.