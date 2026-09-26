# 👨‍💼 Employee Attrition Prediction using Machine Learning

## 📌 Project Overview

This project is an end-to-end Machine Learning project that predicts whether an employee is likely to **leave the organization or stay** based on employee-related factors.

The project includes data preprocessing, exploratory data analysis, feature selection, categorical encoding, feature scaling, model training, model comparison, hyperparameter tuning, model evaluation, and model serialization using Joblib.

---

## 💼 Business Problem

Analyze employee data and build a machine learning model to predict whether an employee will leave the company.

---

## 🚀 Features

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Encoding & Scaling
* Feature Selection
* Train-Test Split
* Model Building & Comparison
* Hyperparameter Tuning
* Model Evaluation
* Confusion Matrix & Classification Report
* Model Saving & Attrition Prediction

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

---

## 📂 Dataset

The dataset contains employee-related information such as:

* Age
* Gender
* Years at Company
* Job Role
* Monthly Income
* Work-Life Balance
* Job Satisfaction
* Performance Rating
* Number of Promotions
* Overtime
* Distance from Home
* Education Level
* Marital Status
* Number of Dependents
* Job Level
* Company Size
* Company Tenure
* Remote Work
* Leadership Opportunities
* Innovation Opportunities
* Company Reputation
* Employee Attrition

The target variable is:

```text
Attrition
```

The target indicates whether an employee **left the company or stayed**.

---

## 📊 Project Workflow

```text
Load Dataset
      │
      ▼
Data Exploration
      │
      ▼
Data Cleaning
      │
      ▼
Define Target & Features
      │
      ▼
Train-Test Split
      │
      ▼
Feature Selection
      │
      ▼
Categorical Encoding
      │
      ▼
Feature Scaling
      │
      ▼
Model Building
      │
      ├── Logistic Regression
      ├── Decision Tree
      ├── Random Forest
      └── Other Models
      │
      ▼
Model Evaluation
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Best Model Selection
      │
      ▼
Save Model using Joblib
      │
      ▼
Streamlit Deployment
```

---

## 🤖 Machine Learning Models Used

The following classification models are used to predict employee attrition:

* KNN Classifier
* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

Models can be compared based on their evaluation metrics to understand their performance on the dataset.

---

## 📈 Evaluation Metrics

The models are evaluated using:

* Accuracy Score
* Precision
* Recall
* F1-Score
* Classification Report
* Confusion Matrix
---

## 📁 Project Structure

```text
employee-attrition-prediction/
│
├── employee_attrition.ipynb
├── employee_attrition2.pkl
├── app.py
├── requirements.txt
├── README.md
├── dataset.csv
└── .gitignore
```

---

## 🌐 Streamlit Application

The trained model is used in a Streamlit application to predict employee attrition.

The application takes employee details as input and provides:

```text
Prediction Result

⚠️ High Attrition Risk
```

or

```text
✅ Low Attrition Risk
```

It can also display the model's predicted class probability when the trained model supports probability prediction.

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/YourUsername/employee-attrition-prediction.git
```

### Go to Project Folder

```bash
cd employee-attrition-prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📚 Concepts Covered

* Exploratory Data Analysis
* Data Cleaning
* Data Preprocessing
* Numerical Feature Scaling
* Categorical Encoding
* Feature Selection
* Train-Test Split
* Classification
* Logistic Regression
* Decision Tree
* Random Forest
* Hyperparameter Tuning
* Cross Validation
* Model Evaluation
* Confusion Matrix
* Classification Report
* Machine Learning Pipeline
* Model Serialization
* Streamlit Deployment

---
## **Screenshots**


---



