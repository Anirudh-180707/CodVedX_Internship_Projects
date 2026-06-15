# Smart Recommendation System

## Overview

The Smart Recommendation System is an AI/ML project developed as part of the CodVedX AI/ML Internship Program. The system provides personalized anime recommendations based on user preferences using Content-Based Filtering and Machine Learning similarity scoring techniques.

The application analyzes anime genres and recommends similar anime titles using TF-IDF Vectorization and Cosine Similarity.

## Features

* User preference input
* Personalized recommendations
* Content-based filtering
* ML similarity scoring
* Anime recommendation engine
* Console-based interface
* Dataset exploration

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* TF-IDF Vectorization
* Cosine Similarity

## Project Structure

```text
Smart_Recommendation_System/
│
├── main.py
├── anime.csv
└── README.md
```

## Dataset

The project uses an anime dataset containing information about anime titles, genres, ratings, episode counts, and popularity metrics.

Dataset Source (Kaggle):

https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

Dataset File Used:

```text
anime.csv
```

Dataset Columns:

```text
anime_id
name
genre
type
episodes
rating
members
```

Due to the dataset size, the original dataset is not included in this repository. It can be downloaded from the Kaggle link above and placed in the project directory before running the application.

## Machine Learning Workflow

### Data Processing

* Load anime dataset
* Handle missing values
* Extract anime genres

### Feature Extraction

* TF-IDF Vectorization

### Similarity Calculation

* Cosine Similarity Scoring

### Recommendation Generation

* Identify anime with similar genres
* Display top recommendations

## Functionalities

### View Dataset

Displays anime information including names, genres, and ratings.

### Get Recommendations

Allows users to enter an anime title and receive similar anime recommendations.

### Exit

Closes the application.

## How to Run

### Install Required Libraries

```bash
pip install pandas scikit-learn
```

### Run the Application

```bash
python main.py
```

## Sample Usage

Input:

```text
Naruto
```

Output:

```text
Recommended Anime:

1. Naruto: Shippuden
2. Bleach
3. One Piece
4. Fairy Tail
5. Hunter x Hunter
```

## Learning Outcomes

* Recommendation Systems
* Content-Based Filtering
* Similarity Algorithms
* Machine Learning Workflow
* TF-IDF Vectorization
* Cosine Similarity
* Data Processing with Pandas
* Python Programming

## Author

Anirudh L

Developed as part of the CodVedX Artificial Intelligence & Machine Learning Internship Program.
