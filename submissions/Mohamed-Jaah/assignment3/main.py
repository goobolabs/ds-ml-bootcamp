import pandas as pd
import numpy as np

CSV_PATH = 'climate_dataset.csv'
df = pd.read_csv(CSV_PATH)
# print(df.head(10))
# print(df.shape)
# print(df["Humidity_percent"].value_counts(dropna=False))
# print(df.isnull().sum())

df["RainfallAmount_mm"] = df["RainfallAmount_mm"].replace(r"[\$%,@]","", regex = True).astype(float)
# print(df["RainfallAmount_mm"].head(5))

df["SoilMoistureLevel"] = df["SoilMoistureLevel"].replace({
    "Med": "Medium", 
    "MEDIUM": "Medium",
    "medium" :"Medium", 
    "low": "Low",
    "LOW": "Low", 
    "HIGH": "High",
    "high": "High"
})

df["ClimateCondition"] = df["ClimateCondition"].replace({
    "drought":"Drought",
    "RAINY":"Rainy",
    "rainy":"Rainy"
})

df["SoilMoistureLevel"] = df["SoilMoistureLevel"].replace("Drought",np.nan)
# print(df["RainfallAmount_mm"].skew())

# to change from sting datatype to int
# df["RainfallAmount_mm"] = df["RainfallAmount_mm"].replace(r"[$%@]","",regex=True).astype(float)
# print(df.info())

# df["RecordID"] = df["RecordID"].replace({"P010":"R010", "PO41":"R010", 
# "??":pd.NA, "-":pd.NA})
# print(df["RecordID"].head(10).value_counts(dropna=False))

df["RainfallAmount_mm"] = df["RainfallAmount_mm"].fillna(df["RainfallAmount_mm"].median())
df["Humidity_percent"] = df["Humidity_percent"].fillna(df["Humidity_percent"].median())
df["RainyDaysCount"] = df["RainyDaysCount"].fillna(df["RainyDaysCount"].median())
df["SoilMoistureLevel"] = df["SoilMoistureLevel"].fillna(df["SoilMoistureLevel"].mode()[0])
# print(df["SoilMoistureLevel"])
df["ClimateCondition"] = df["ClimateCondition"].fillna(df["ClimateCondition"].mode()[0])

# print(df.isnull().sum())


#Removing Duplications
# before = df.shape

df = df.drop_duplicates()

after = df.shape

# print("Before",before, "Afer : ",after)

#Removing outlier
# 1. Define the function with a return statement
def iqrFunction(column, k=1.5):
    q1, q3 = column.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    heigher = q3 + k * iqr

    #You must return these values so they can be captured outside
    return lower,heigher

# 2. Execute the function outside the block using your DataFrame
# print("Rainfall amount part :-")
low_rain,high_rain = iqrFunction(df["RainfallAmount_mm"]);
# print("Lowest rainfall must be :",low_rain, "Highest rainfall must be :",high_rain)

# print("Temperature part :-")
low_temp,high_temp = iqrFunction(df["AvgTemperature_C"]);
# print("Lowest temp must be :",low_temp, "Highest temp must be :",high_temp)

# print("Humidity Part :-")
lowHumid, highHumid = iqrFunction(df["Humidity_percent"])
# print("Highest Humidity must be : ",highHumid ,"Lowest Humidity must be : ",lowHumid )

# print("Raining Days Part :-")
leastRain , mostRain  = iqrFunction(df["RainyDaysCount"])
# print("Most Rain days is : ",mostRain," Days Raining","Least Rain days is : ",leastRain," Days Raining")

df["RainfallAmount_mm"]=df["RainfallAmount_mm"].clip(lower =low_rain , upper =high_rain )
df["AvgTemperature_C"]=df["AvgTemperature_C"].clip(lower =low_temp , upper =high_temp )
df["Humidity_percent"]=df["Humidity_percent"].clip(lower =lowHumid , upper =high_temp )
df["RainyDaysCount"]=df["RainyDaysCount"].clip(lower =leastRain , upper =mostRain )

# print("Clipping Part : ")
# print(df["RainfallAmount_mm"].describe())
# print(df["AvgTemperature_C"].describe())
# print(df["Humidity_percent"].describe())
# print(df["RainyDaysCount"].describe())

#in SoilMoistureLevel and ClimateCondition are text , so the meachine don't understand , to configure , use this :
df = pd.get_dummies(df, columns = ["SoilMoistureLevel"],drop_first=False)
# print([c for c in df.columns if c.startswith("SoilMoistureLevel")])

df = pd.get_dummies(df, columns = ["ClimateCondition"],drop_first=False)
# print([c for c in df.columns if c.startswith("ClimateCondition")])

df["isItDrought"] = df["ClimateCondition_Drought"].astype(int) 
df["isItRainy"] = df["ClimateCondition_Rainy"].astype(int) 

# print(df.head)


print(df["RainfallAmount_mm"].describe())

