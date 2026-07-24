# Used Car Price Prediction 🚗

A Machine Learning project that predicts the price of used cars based on vehicle information such as brand, model year, mileage, engine specifications, and vehicle condition.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, machine learning model training, and deployment using FastAPI with a web interface.

## Dataset

The dataset contains used car information with details about vehicle specifications and prices.

Original dataset shape:

- Rows: 3918
- Columns: 13

The main features include:

| Feature         | Description                                |
| --------------- | ------------------------------------------ |
| brand           | Car manufacturer (Toyota, BMW, Ford, etc.) |
| model_year      | Year the car was manufactured              |
| milage          | Total distance driven by the car           |
| fuel_type       | Type of fuel used                          |
| transmission    | Gear type                                  |
| accident        | Accident history                           |
| clean_title     | Vehicle title condition                    |
| horsepower      | Engine power                               |
| engine_capacity | Engine size in liters                      |
| layout          | Engine cylinder configuration              |
| model           | Car model name                             |
| engine          | Engine specification                       |

Target variable:

- `price` - The selling price of the used car

## Data Preprocessing

The data was cleaned and prepared before training the machine learning model.

Steps performed:

- Converted `price` from string format to numeric format
- Converted `milage` values to numeric format
- Removed missing values
- Checked and removed duplicate records
- Handled categorical variables using encoding
- Applied feature scaling where required

## Feature Engineering

New features were created to improve model performance:

### Car_Age

Calculates the age of the vehicle:

### Mileage_per_Year

Calculates the average mileage driven per year:

These features help the model understand vehicle usage patterns better.

## Machine Learning Model

The project uses machine learning regression models to predict used car prices.

Models tested:

- Linear Regression
- Random Forest Regressor

The final model was saved as:

The pipeline contains:

- Data preprocessing
- Feature transformation
- Trained Random Forest model

## Model Evaluation

The model was evaluated using regression metrics:

| Metric   | Description                         |
| -------- | ----------------------------------- |
| MAE      | Average prediction error            |
| RMSE     | Measures prediction error magnitude |
| R² Score | Explains model performance          |

Final model performance:

- MAE: 16,324.95
- RMSE: 121,982.55
- R² Score: 0.16

The trained model can predict the estimated price of a used car based on its features.

## FastAPI Deployment

The trained machine learning pipeline was deployed using FastAPI.

The API provides an endpoint that receives car information and returns a predicted price.

API endpoint:

Example response:

```json
{
  "predicted_price": 31398.47
}

git clone https://github.com/bille2026/used-car-price-prediction.git

cd used-car-price-prediction

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn api.app:app --reload

http://127.0.0.1:8000

## Project Structure

used-car-price-prediction/
│
├── api/
│ ├── app.py
│ ├── static/
│ │ └── style.css
│ └── templates/
│ └── index.html
│
├── dataset/
│ └── cleaned_used_car.csv
│
├── models/
│ └── car_price_pipeline.pkl
│
├── src/
│ ├── preprocessing.py
│ ├── train_pipeline.py
│ ├── evaluate_model.py
│ └── pipeline_test.py
│
├── requirements.txt
├── README.md
└── project_paper.md




## Author

**Bille Abdul Ali**

Computer Science Student

Machine Learning Project - Used Car Price Prediction
```
