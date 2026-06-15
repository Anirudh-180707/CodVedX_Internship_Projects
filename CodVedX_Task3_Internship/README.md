# AI Based Fake News Detection Tool

## Overview

The AI Based Fake News Detection Tool is a Natural Language Processing (NLP) and Machine Learning project developed as part of the CodVedX AI/ML Internship Program.

The application analyzes news articles entered by the user and classifies them as **FAKE** or **REAL** using Machine Learning techniques. The project demonstrates text preprocessing, TF-IDF vectorization, text classification, model training, confidence score generation, and trained model storage.

## Features

* News text input
* Fake / Real news classification
* Confidence score output
* TF-IDF vectorization
* NLP-based text processing
* Logistic Regression classifier
* Trained model storage using Pickle
* Console-based user interface
* Exception handling

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Logistic Regression
* Pickle

## Project Structure

```text
AI_Based_Fake_News_Detection/
│
├── main.py
├── train_model.py
├── fake_news_model.pkl
├── vectorizer.pkl
└── README.md
```

## Dataset

The dataset used for this project is not included in this repository due to its large size.

Dataset Source:

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Required Files:

```text
Fake.csv
True.csv
```

After downloading, place both files in the project directory before training the model.

## Machine Learning Workflow

### Data Collection

* Fake news articles from Fake.csv
* Real news articles from True.csv

### Text Processing

* Text extraction
* TF-IDF Vectorization

### Model Training

* Logistic Regression Classifier

### Model Storage

* fake_news_model.pkl
* vectorizer.pkl

### Prediction

* Fake / Real classification
* Confidence score generation

## How to Run

### Install Required Libraries

```bash
pip install pandas scikit-learn
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
python main.py
```

## Sample Usage

Input:

```text
The White House announced new measures to improve economic growth and employment opportunities across the country.
```

Output:

```text
Prediction: REAL
Confidence Score: 54.68%
```

Input:

```text
Aliens have established a city under the Pacific Ocean and are trading technology with humans.
```

Output:

```text
Prediction: FAKE
Confidence Score: 69.76%
```

## Learning Outcomes

* Natural Language Processing Fundamentals
* Text Classification
* TF-IDF Vectorization
* Machine Learning Model Training
* Logistic Regression
* Model Evaluation
* Model Persistence using Pickle
* Python Programming
* Git and GitHub Workflow

## Author

Anirudh L

Developed as part of the CodVedX Artificial Intelligence & Machine Learning Internship Program.
