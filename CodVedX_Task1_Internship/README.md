# Utility Usage Prediction Tool

## Overview

The Utility Usage Prediction Tool is a Python-based Machine Learning application developed as part of the CodVedX AI/ML Internship. The project uses historical utility consumption data to predict future usage through a simple Linear Regression model.

The application provides a menu-driven console interface that allows users to manage utility records, train a machine learning model, and generate future usage predictions.

## Features

* Menu-driven console application
* Add new utility usage records
* View existing records
* Update existing records
* CSV file handling for data storage
* Machine Learning model training using Linear Regression
* Future utility usage prediction
* Exception handling for invalid inputs and file errors

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Pickle

## Project Structure

```text
Utility_Usage_Prediction_Tool/
│
├── main.py
├── train_model.py
├── usage_data.csv
├── utility_model.pkl
└── README.md
```

## Dataset

The dataset contains the following fields:

| Column | Description            |
| ------ | ---------------------- |
| Month  | Month Number           |
| Units  | Utility Units Consumed |
| Bill   | Utility Bill Amount    |

Sample Data:

```csv
Month,Units,Bill
1,250,1800
2,280,2000
3,310,2200
4,340,2400
5,370,2600
```

## How to Run

### Install Required Libraries

```bash
pip install pandas numpy scikit-learn
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
python main.py
```

## Menu Options

1. Add Usage Data
2. View Usage Data
3. Update Usage Data
4. Train Model
5. Predict Future Usage
6. Exit

## Machine Learning Model

This project uses the Linear Regression algorithm to learn patterns from historical utility consumption data and predict future utility usage based on the month entered by the user.

## Learning Outcomes

* Python Programming Fundamentals
* Data Handling using Pandas
* CSV File Operations
* Exception Handling
* Machine Learning Workflow
* Model Training and Prediction
* Git and GitHub Project Management

## Author

Anirudh L

Developed as part of the CodVedX Artificial Intelligence & Machine Learning Internship Program.
