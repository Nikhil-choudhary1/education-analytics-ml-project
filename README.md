# Student Performance Prediction System

##  Overview

This project is an end-to-end Machine Learning application that predicts a student's **maths score** based on factors like gender, parental education, lunch type, test preparation, and reading/writing scores.

It covers the complete ML lifecycle including data preprocessing, model training, and deployment using a Flask web application for real-time predictions.


## Features

* End-to-end ML pipeline (training + prediction)
* Data preprocessing & feature engineering
* Multiple model training & evaluation
* Best model selection (**CatBoost Regressor**)
* Modular pipeline-based architecture
* Logging & exception handling
* Flask web app for real-time predictions

##  Tech Stack

* **Programming:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, CatBoost
* **Backend:** Flask
* **Frontend:** HTML, CSS


## Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training & Evaluation
6. Model Selection (CatBoost)
7. Model Serialization
8. Deployment using Flask


## Project Structure


├── artifacts/        # Saved models and processed files
├── notebook/         # EDA and experiments
├── src/              # Source code (pipeline, components)
├── templates/        # HTML templates (UI)
├── app.py            # Flask application
├── requirements.txt  # Dependencies
└── README.md




##  Setup Instructions 

### 1 Clone the repository


git clone https://github.com/Nikhil-choudhary1/education-analytics-ml-project
cd education-analytics-ml-project


### 2 Create virtual environment (Recommended)


conda create -n ml_env python=3.10 -y
conda activate ml_env


### 3 Install dependencies


pip install -r requirements.txt


### 4 Run the application


python app.py

## Output

Open your browser and go to:


http://127.0.0.1:5000/


* Enter student details and get predicted maths score instantly.

## Author

**Nikhil Choudhary**
