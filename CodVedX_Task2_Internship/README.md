# Student Performance Prediction System

## Overview

The Student Performance Prediction System is a Machine Learning project developed as part of the CodVedX AI/ML Internship. The system predicts a student's final academic performance based on key factors such as attendance, marks, and study hours.

The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, performance prediction, data visualization, and model evaluation.

## Features

* Student performance prediction using Machine Learning
* Data preprocessing and cleaning
* Handling missing values
* Exploratory Data Analysis (EDA)
* Data visualization using charts
* Linear Regression model training
* Model accuracy evaluation
* Console-based user interface
* Exception handling

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Pickle

## Project Structure

```text
Student_Performance_Prediction/
│
├── main.py
├── train_model.py
├── student_performance.csv
├── student_model.pkl
└── README.md
```

## Dataset Features

| Feature          | Description                   |
| ---------------- | ----------------------------- |
| Attendance       | Student attendance percentage |
| Marks            | Internal assessment marks     |
| StudyHours       | Average study hours           |
| FinalPerformance | Final performance score       |

## Sample Dataset

```csv
Attendance,Marks,StudyHours,FinalPerformance
75,65,2,68
80,70,3,72
85,78,4,80
90,85,5,88
95,92,6,94
```

## Machine Learning Model

This project uses the Linear Regression algorithm to predict student performance based on attendance, marks, and study hours.

## Functionalities

### View Dataset

Displays all student records along with dataset information and statistical summary.

### Visualize Data

Generates charts to analyze relationships between:

* Attendance and Performance
* Marks and Performance
* Study Hours and Performance

### Train Model

Trains a Linear Regression model using the dataset and saves it as a `.pkl` file.

### Predict Performance

Allows users to enter attendance, marks, and study hours to predict final student performance.

### Evaluate Model

Calculates and displays the model accuracy using the R² Score metric.

## How to Run

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
python main.py
```

## Learning Outcomes

* Data Cleaning and Preprocessing
* Handling Missing Values
* Exploratory Data Analysis (EDA)
* Feature Selection
* Data Visualization
* Machine Learning Workflow
* Model Evaluation
* Python Programming

## Author

Anirudh L

Developed as part of the CodVedX Artificial Intelligence & Machine Learning Internship Program.
