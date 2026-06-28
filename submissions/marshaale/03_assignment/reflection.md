# Explanation Doc

### PART ZERO SETUP

Directory structure constants root dir,dataset dir,csv file,output csv file. paths created using `pathlib module`

### PART ONE LOAD DATASET AND EDA

Dataset Loading and Exploratory Data Analysis (EDA) to know our dataset columns,shape,information,sum of missing value,categorical data value counts.

### PART TWO CLEAN TARGET & FORMAT

Clean and format target value `Price` remove non numeric eg $40 or 1,200 using regex `df['Price'].replace(r'[^0-9.]','',regex=True)` takes numbers and replace str '' example 1,200.0 -> 1200.0.
covert dtype to float

### PART FOUR IMPUTE MISSING VALUES

Filling missing values

- `Location` fill using mode most frequently location eg `city,rural,city,city,rural` it fills the missing value to `city`
- `Doors,Accidents` fill using mode same as location
- `Odometer_km` fill using median the middle number it's the best guess for filling missing values and it's most commonly used or when there is outlier.

### PART SIX IQR CAPPING

Handle outliers using the IQR (Interquartile Range) method.

First is calculating the lowest and highest acceptable values for the column `lower` and `upper`.

Second is capping, The values below the lower bound are replaced with lower, and values above the upper bound are replaced with upper.

### PART EIGHT FEATURE ENGINEERING

Is adding new features using your domain knowledge and creatively.

add these new features

- car age
- Km_per_year
- Is_Urban
- LogPrice

### PART NINE FEATURE SCALING

Scaling is a way of telling the model that no feature is more important than another because of its numerical range.

Using `StandardScaler` from `sklearn.preprocessing`, features are standardized to have the same scale, preventing larger-valued features from having a greater influence on the model.
