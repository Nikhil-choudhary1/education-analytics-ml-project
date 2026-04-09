# Student Performance Prediction System

## Overview
This project is an end-to-end Machine Learning application that predicts a student's maths score based on various factors such as gender, parental education, test preparation, and reading/writing scores.

The system includes data preprocessing, model training, and a web-based interface for real-time predictions.

---

## Features
- End-to-end ML pipeline (training + prediction)
- Data preprocessing and feature engineering
- Model training using CatBoost and other regression models
- Real-time prediction using Flask web app
- Modular project structure (pipeline-based)
- Logging and exception handling

---

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- CatBoost
- Flask
- HTML/CSS (Frontend)

---

## Machine Learning Workflow
1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training & Evaluation
6. Model Selection (CatBoost)
7. Model Serialization
8. Deployment using Flask

---

##  Project Structure
├── artifacts/ # Saved models and files
├── notebook/ # EDA and experiments
├── src/ # Source code (pipeline, components)
├── templates/ # HTML templates (UI)
├── app.py # Flask application
├── requirements.txt # Dependencies
└── README.md

## ⚙️ How to Run Locally

```bash
# Clone repository
git clone <your-repo-link>

# Move into folder
cd education-analytics-ml-project

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
