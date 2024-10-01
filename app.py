
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('electricity_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        day = float(request.form['day'])
        month = float(request.form['month'])
        forecast_wind = float(request.form['forecast_wind'])
        system_load = float(request.form['system_load'])
        smpea = float(request.form['smpea'])
        ork_temp = float(request.form['ork_temp'])
        ork_wind = float(request.form['ork_wind'])
        co2_intensity = float(request.form['co2_intensity'])
        actual_wind = float(request.form['actual_wind'])
        system_load_ep2 = float(request.form['system_load_ep2'])

        # Prepare the feature array
        features = np.array([[day, month, forecast_wind, system_load, smpea, ork_temp, ork_wind, co2_intensity, actual_wind, system_load_ep2]])

        # Make prediction
        prediction = model.predict(features)
        return render_template('index.html', prediction=prediction[0])

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
