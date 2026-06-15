import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CSV_FILE = "anime.csv"


def load_data():
    return pd.read_csv(CSV_FILE)


def view_dataset():
    try:
        df = load_data()

        print("\n===== Anime Dataset =====\n")
        print(df[["name", "genre", "rating"]].head(20))

    except Exception as e:
        print("Error:", e)


def recommend_anime():
    try:
        df = load_data()

        df = df[["name", "genre", "rating"]]
        df = df.dropna()

        anime_name = input("\nEnter Anime Name: ")

        matches = df[
            df["name"].str.lower() == anime_name.lower()
        ]

        if matches.empty:
            print("Anime not found in dataset.")
            return

        tfidf = TfidfVectorizer(stop_words="english")

        tfidf_matrix = tfidf.fit_transform(
            df["genre"]
        )

        similarity_matrix = cosine_similarity(
            tfidf_matrix
        )

        anime_index = matches.index[0]

        similarity_scores = list(
            enumerate(
                similarity_matrix[anime_index]
            )
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        print("\n===== Recommended Anime =====\n")

        count = 0

        for anime in similarity_scores[1:]:

            index = anime[0]

            print(
                f"{count + 1}. "
                f"{df.iloc[index]['name']} "
                f"(Rating: {df.iloc[index]['rating']})"
            )

            count += 1

            if count == 5:
                break

    except Exception as e:
        print("Error:", e)


while True:

    print("\n===== Smart Recommendation System =====")
    print("1. View Dataset")
    print("2. Get Recommendations")
    print("3. Exit")

    try:
        choice = int(
            input("Enter Choice: ")
        )

        if choice == 1:
            view_dataset()

        elif choice == 2:
            recommend_anime()

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number.")