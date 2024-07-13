from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the model
RF = pickle.load(open('RandomForest.pkl', 'rb'))

# Creating Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get the form data and convert to floats
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])
        
        def recommendation(N,P,k,temperature,humidity,ph,rainfall):
            features = np.array([[N,P,k,temperature,humidity,ph,rainfall]])
            prediction = RF.predict(features)
    
            return prediction[0]

        # Get the prediction
        result = recommendation(N, P, K, temp, humidity, ph, rainfall)
        result = result.capitalize()

        return render_template('index.html', result=result)
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return render_template('index.html', result="Value error occurred, please check the input values.")
    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', result="An unexpected error occurred.")

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
