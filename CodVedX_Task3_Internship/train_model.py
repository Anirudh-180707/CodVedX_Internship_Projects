import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

try:
    fake_df = pd.read_csv("Fake.csv")
    true_df = pd.read_csv("True.csv")

    fake_df["label"] = "FAKE"
    true_df["label"] = "REAL"

    df = pd.concat([fake_df, true_df], ignore_index=True)

    df = df[["text", "label"]]

    X = df["text"]
    y = df["label"]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_df=0.7
    )

    X_vectorized = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression(
        max_iter=1000
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    with open(
        "fake_news_model.pkl",
        "wb"
    ) as file:
        pickle.dump(model, file)

    with open(
        "vectorizer.pkl",
        "wb"
    ) as file:
        pickle.dump(vectorizer, file)

    print("Model and Vectorizer saved successfully!")

except Exception as e:
    print("Error:", e)