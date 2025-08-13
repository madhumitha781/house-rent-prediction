Houserent predictions 

This project is a Flask-based web application that allows users to compare different machine learning regression models for a given dataset. The app loads a dataset, trains several models, and provides a simple web interface where you can input features and see predictions from a chosen model.

Features

Multiple Regression Models: Compares the performance of Linear, Ridge, Lasso, Decision Tree, Random Forest, and Support Vector Regressor (SVR) models.

User-Friendly Interface: A web form lets you input data and select a model for prediction.

Local Data Integration: Reads a data.csv file to train the models, making it easy to swap datasets.

Scalable: The code is structured to easily add more regression models and features.

Project Structure

app.py: The main Flask application. It's responsible for loading the data, training all the models, handling web routes, and serving the prediction results.

data.csv: The sample dataset used for training the models. It contains features and a target variable for a regression task.

requirements.txt: Lists all the necessary Python libraries required to run the project.

templates/: (Implied by app.py) This directory would contain your HTML files:

index.html: The main page with the input form and model selection dropdown.

result.html: Displays the prediction result.

Technologies Used
Flask: A micro-framework for building the web application.

Scikit-learn: A robust machine learning library for model training and data preprocessing.

Pandas: For efficient data loading and manipulation from the CSV file.

NumPy: A fundamental library for numerical computing.

<img width="756" height="448" alt="Screenshot (68)" src="https://github.com/user-attachments/assets/d01f8aa2-91cd-4eb0-830b-93ed53a6c8cc" />

<img width="745" height="442" alt="Screenshot (69)" src="https://github.com/user-attachments/assets/378bf7b7-3648-4bec-b443-c5aaaac6b501" />

<img width="746" height="439" alt="Screenshot (70)" src="https://github.com/user-attachments/assets/597f8e85-1cb1-4d22-b997-5a0516aaa0cd" />
