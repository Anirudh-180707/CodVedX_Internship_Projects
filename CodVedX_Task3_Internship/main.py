import pickle

MODEL_FILE = "fake_news_model.pkl"
VECTORIZER_FILE = "vectorizer.pkl"


def detect_news():
    try:
        with open(MODEL_FILE, "rb") as model_file:
            model = pickle.load(model_file)

        with open(VECTORIZER_FILE, "rb") as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)

        news_text = input("\nEnter News Text:\n")

        transformed_text = vectorizer.transform(
            [news_text]
        )

        prediction = model.predict(
            transformed_text
        )[0]

        confidence = (
            max(
                model.predict_proba(
                    transformed_text
                )[0]
            ) * 100
        )

        print("\nPrediction:", prediction)
        print(
            f"Confidence Score: "
            f"{confidence:.2f}%"
        )

    except FileNotFoundError:
        print(
            "Model not found. "
            "Run train_model.py first."
        )

    except Exception as e:
        print("Error:", e)


def model_information():
    print("\n===== Model Information =====")
    print("Algorithm : Logistic Regression")
    print("Vectorizer: TF-IDF")
    print("Classes   : FAKE / REAL")


while True:

    print(
        "\n===== AI Based Fake News Detection Tool ====="
    )

    print("1. Detect News")
    print("2. Model Information")
    print("3. Exit")

    try:
        choice = int(
            input("Enter Choice: ")
        )

        if choice == 1:
            detect_news()

        elif choice == 2:
            model_information()

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print(
            "Please enter a valid number."
        )