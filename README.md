# Crop Recommendation System 🌾

## Motivation 💪💪

Precision agriculture is in trend nowadays. Precision agriculture is a modern farming technique that uses the data of soil characteristics, soil types, crop yield data, weather conditions, and suggests the farmers with the most optimal crop to grow in their farms for maximum yield and profit. This technique can reduce crop failures and will help the farmers to take informed decisions about their farming strategy.

In order to mitigate the agrarian crisis in the current status quo, there is a need for better recommendation systems to alleviate the crisis by helping the farmers to make an informed decision before starting the cultivation of crops.

## Goal 🎯

**To recommend optimum crops to be cultivated by farmers based on several parameters and help them make an informed decision before cultivation.**

## About the Data 📊

The data used in this project is made by augmenting and combining various publicly available datasets of India like weather, soil, etc. You can access the dataset [here](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset). This data is relatively simple with very few but useful features unlike the complicated features affecting the yield of the crop.

The data have Nitrogen, Phosphorous, Potassium, and pH values of the soil. Also, it contains the humidity, temperature, and rainfall required for a particular crop.


## Technologies Used 💻

- **Python**: Programming language used for backend development and machine learning.
- **Flask**: Micro web framework used for building the web application.
- **HTML/CSS**: Frontend markup and styling languages.
- **Bootstrap**: Frontend framework for responsive and mobile-first design.
- **Pandas, NumPy, Scikit-learn**: Python libraries used for data manipulation, analysis, and machine learning modeling.
- **GitHub**: Platform for hosting the project repository and collaboration.
- **Jupyter Notebook**: Used for data exploration and model development (if applicable).

## Project Structure 📁

- `app.py`: Flask application to serve the crop recommendation model.
- `model.pkl`: Pre-trained machine learning model for crop recommendation.
- `templates/`: Folder containing HTML templates.
  - `index.html`: Main page of the web application.
- `static/`: Folder containing static files like CSS, images, etc.
  - `logo.png`: Logo used in the application.
  - `background.jpg`: Background image for the application.
  - `<crop_name>.jpg`: Images of the crops for displaying recommendations.
- `README.md`: This file.

## How to Run the Project 🏃‍♂️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/crop-recommendation-system.git
   cd crop-recommendation-system

2. **Install Dependencies**:
    ```bash
   pip install -r requirements.txt

3. **Run the Application**:
    ```bash
    python app.py

4. **Open Your Browser**:
  - Navigate to http://127.0.0.1:5000/ to see the application in action.


## Usage 🖥️

1. **Enter the values for Nitrogen, Phosphorous, Potassium, Temperature, Humidity, pH, and Rainfall in the form.**
   
2. **Click on "Get Recommendation".**
   
3. **The recommended crop will be displayed along with an image of the crop.**


## Screenshots 📸

![Homepage screenshot](screenshots/1.png)
![Recommendation screenshot](screenshots/2.png)

## Video 📹

https://github.com/user-attachments/assets/724f023f-dc3d-4939-90e5-c270078f9bfc

## Contributing 🤝

Contributions are welcome! Feel free to submit issues and enhancement requests. If you'd like to contribute code, please fork the repository and submit a pull request.

## Final Note 🎉

Thank you for exploring our Crop Recommendation System! We hope it proves useful for farmers and enthusiasts alike. Your feedback and contributions are valuable to us.

Happy farming! 🌱

























































