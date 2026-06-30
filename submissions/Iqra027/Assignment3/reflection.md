**The Reflection Of Data Preprocessed**
*We have a car dataset that has many misisng values,typos,and so much more so we will expalin here how we have clean our dataset to become ready for prediction*

1.Loading the Dataset into our enviroment while we are using (built_in function called)read_csv and print the head and the shape of the dataset to look for what to work and is_null.sum to see if there is missing values which gives us some describtion.

*2.Cleaning  the label data(output=Price) which had $ and , and we converted float number
afetr that it comes that this (Price) is extremely right-skewned with skewness of 7.87 and for that many ML model (like Linear Regression) assume normally distributed targets, But applying log transformation (np.log1p), we compressed the large variances and reduced the skewness to 1.94,making easier for the model to generalize and make accurate predictions.*

3.We also fixed some typo errors before imputing in the Location column.

4.There are 3 columns which needs to impute(Location,Odometer_km,Doors) 
first to impue the location(categorical data) &Doors(Discrete Numeric) column we used mode in the location because our whole dataset contain 3 categories(City,Suburb,Rural) but we used mode in the Door column also as we know its number but as a logical way we can't say car has 2.4 or something like that,But we use median for the Odometer_km because its continuous numerical data that contain outliers.Median is robust against compared to mean,ensuring the missing milage values are imputed with a realistic middle-ground representation.

5.Stage we dropped the duplicates in the Dataset.

6.we remove outliers by using IQr for Price_log colum instead of Price because if we use price values the IQR capping would be considered outliers for the expensive cars and it will clipped important data.

7.after that Location colum has a tetx data and it will be a difficult the model to understand so  we used One-Hot Encoding to transform the categorical data into three bianry columns and we  ensured the output as integers dtype="init" instead of boolean values.

8.At this stage we use our knowledge and creativity to give the model pure data so we used feature transformation to add 5 new columns in the dataset.

9.Finally, we have scaled feature data or the x to easy the model for predictions.
We will use feature Scaling(standarization via StandardScaler), there is numerical features like Odometer_km that have very large ranges comapred to features like Doors or carAge, this imbalance can cause ML model to favor hihg-magnitude features incorrectly.So we used 'StandardScaler' from scikit-Learn to scale continuous numerical columns('Odometer_km','Doors','Accidents',etc.) so that they have a mean of 0 and a standard deviation of 1.