from flask import Flask, request, render_template
import numpy as np
import pickle

# Load model
model = pickle.load(open('RandomForest.pkl', 'rb'))

# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosporus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    prediction = model.predict(single_pred)[0]

    crop_dict = {
        'rice': 'rice.jpg',
        'maize': 'maize.jpg',
        'chickpea': 'chickpea.jpg',
        'kidneybeans': 'kidneybeans.jpg',
        'pigeonpeas': 'pigeonpeas.jpg',
        'mothbeans': 'mothbeans.jpg',
        'mungbean': 'mungbean.jpg',
        'blackgram': 'blackgram.jpg',
        'lentil': 'lentil.jpg',
        'pomegranate': 'pomegranate.jpg',
        'banana': 'banana.jpg',
        'mango': 'mango.jpg',
        'grapes': 'grapes.jpg',
        'watermelon': 'watermelon.jpg',
        'muskmelon': 'muskmelon.jpg',
        'apple': 'apple.jpg',
        'orange': 'orange.jpg',
        'papaya': 'papaya.jpg',
        'coconut': 'coconut.jpg',
        'cotton': 'cotton.jpg',
        'jute': 'jute.jpg',
        'coffee': 'coffee.jpg'
    }

    if prediction in crop_dict:
        image_filename = crop_dict[prediction]
        result = prediction.capitalize()
    else:
        image_filename = 'img.jpg'
        result = "Error occurred, please check the input values."

    return render_template('index.html', result=result, image_filename=image_filename)




if __name__ == "__main__":
    app.run(debug=True,port=8001)
