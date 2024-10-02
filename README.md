<h1>Electricity Price Prediction</h1>

This repository contains a machine learning project to predict electricity prices using historical and environmental data. The goal is to forecast the actual electricity price based on various features like wind production, temperature, CO2 intensity, system load, and more.

## Project Overview

The prediction of electricity prices is crucial for businesses relying on computing services or industrial operations where energy consumption fluctuates throughout the day. In this project, we use historical data including weather forecasts, wind production, system load, and other factors to build a model that accurately predicts electricity prices.

### Features of the Dataset:
The dataset includes the following key features:
- `Day`: Day of the month (1–31)
- `Month`: Month of the year (1–12)
- `ForecastWindProduction`: Forecasted wind energy production (MW)
- `SystemLoadEA`: Forecasted national electricity load (MW)
- `SMPEA`: Forecasted price (EUR)
- `ORKTemperature`: Actual temperature (°C)
- `ORKWindspeed`: Actual wind speed (m/s)
- `CO2Intensity`: Actual CO2 intensity (gCO2/kWh)
- `ActualWindProduction`: Actual wind energy production (MW)
- `SystemLoadEP2`: Actual national system load (MW)

The target variable is the **actual electricity price** (`SMPEP2`), which is to be predicted.

## Workflow

1. **Data Preprocessing**:
   - Handling missing values
   - Feature scaling
   - Encoding categorical features (if necessary)
   
2. **Modeling**:
   - We experiment with several regression models, including:
     - Linear Regression
     - Random Forest
     - Gradient Boosting
     - Neural Networks (optional)
   - Model evaluation using cross-validation and error metrics:
     - Mean Absolute Error (MAE)
     - Mean Squared Error (MSE)
     - R² Score

3. **Prediction**:
   - Use the trained model to predict the electricity price based on unseen data.

## How to Run

### Prerequisites

- Python 3.x
- Required Python libraries (can be installed using the command below):

```bash
pip install -r requirements.txt

