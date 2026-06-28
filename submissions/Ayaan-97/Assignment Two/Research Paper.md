## Research Paper: Furniture Sales and Product Features Dataset:

### 1. Title & Collection Method

**Title:** An Analysis of Furniture Features, Stock, and Popularity for Machine Learning

**Collection Method:**This dataset was created using a**manual logging and observational method.** Data was collected by observing furniture products in local stores and online catalogs. For each product, key information was recorded, including product type, material, dimensions (width and height), price, stock availability, and customer popularity rating.

### 2. Description of Features & Labels

The dataset consists of six input features (X) and one output variable (y).

Features (X)
Feature	Symbol	Description	Type
Product_Type	X1	Type of furniture (Chair, Table, Sofa, Bed, Cabinet)	Categorical
Material	X2	Main material of the product (Wood, Metal, Plastic, Leather, Fabric)	Categorical
Width_cm	X3	Width of the product in centimeters	Numerical
Height_cm	X4	Height of the product in centimeters	Numerical
Price_USD	X5	Price of the product in USD	Numerical
Stock_Available	X6	Number of items available in stock (can include “Out of Stock”)	Numerical / Categorical
Label (y)
Label	Description	Type
Popularity_Rating	Customer popularity rating of the furniture (1–5, or Missing)	Numerical / Categorical

### 3. Dataset Structure

* **Rows:** 100
* **Columns:** 8 (ID + 6 features + 1 label)

**Sample Table (First 10 Rows)**
ID	Product_Type	Material	Width_cm	Height_cm	Price_USD	Stock_Available	Popularity_Rating
1	Chair	Wood	45	90	120	10	4
2	Table	Metal	120	75	250	5	5
3	Sofa	Leather	200	85	600	2	5
4	Bed	Wood	180	50	400	0	4
5	Cabinet	Plastic	80	150	150	Out of Stock	3
6	Chair	Metal	50	85	100	15	3
7	Sofa	Fabric	190	90	550	1	5
8	Bed	Wood	200	55	450	3	4
9	Table	Wood	?	75	200	4	4
10	Chair	Plastic	45	88	90	8	Missing

---

### 4. Quality Issues (The "Messy" Data)

* **Missing Values:** widths of Row 5 "out of stock", and Row 9 is "?" and Row 10 is Missing .
* **Mixed Formats:** Row 6 has "Zero" written as a word instead of "0".
* **Outliers:** Prices vary widely ($50 to $800), reflecting product type differences.

-Widths and heights also vary significantly, which may impact regression models.
* **Duplicates:** Multiple items of the same type/material combination exist, but they may have slightly different dimensions and prices
### 5. Use Case
This dataset is suitable for multiple Machine Learning applications:

**Regression:**

* Predict Price_USD based on product type, material, and dimensions

Help stores estimate pricing for new furniture products

**Classification:**

*  Predict Popularity_Rating (1–5) based on product features

Determine which furniture products are likely to be popular