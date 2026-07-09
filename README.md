# 🩺 Diabetes Risk Assessment AI Agent

## Overview

This project is an AI-powered healthcare monitoring system that predicts diabetes risk using Machine Learning.

The system allows users to enter patient health information, predicts diabetes risk, provides health recommendations, and stores prediction history in a SQLite database.

---

## Features

- Diabetes Risk Prediction
- AI Health Recommendations
- Patient History
- SQLite Database
- Flask Web Application
- Machine Learning Model
- Responsive User Interface

---

## Technologies Used

- Python
- Flask
- Scikit-Learn
- SQLite
- HTML
- CSS
- Joblib
- NumPy

---

## Machine Learning Models Compared

- Logistic Regression
- Random Forest
- XGBoost
- SVM
- KNN
- MLP

Random Forest was selected as the final model.

---

## Project Structure

```
Diabetes_Risk_Assessment_Agent/
│
├── app.py
├── database.py
├── predict.py
├── recommendations.py
├── diabetes_model.pkl
├── scaler.pkl
├── diabetes.db
├── requirements.txt
├── templates/
├── static/
└── README.md
```

---

## How to Run

Activate Virtual Environment

```
.\venv\Scripts\activate
```

Run Flask

```
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Author

Meghana Tottempudi
