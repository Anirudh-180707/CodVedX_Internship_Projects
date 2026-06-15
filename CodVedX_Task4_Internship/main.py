import pandas as pd
from difflib import get_close_matches

CSV_FILE = "faq_dataset.csv"


def load_faq():
    return pd.read_csv(CSV_FILE)


def ask_question():
    try:
        df = load_faq()

        question = input("\nEnter your question: ")

        questions = df["Question"].tolist()

        match = get_close_matches(
            question,
            questions,
            n=1,
            cutoff=0.4
        )

        if match:
            answer = df.loc[
                df["Question"] == match[0],
                "Answer"
            ].values[0]

            print("\nChatbot:", answer)

        else:
            print(
                "\nChatbot: Sorry, I couldn't find an answer."
            )

    except Exception as e:
        print("Error:", e)


def add_faq():
    try:
        question = input("Enter New Question: ")
        answer = input("Enter Answer: ")

        df = load_faq()

        new_row = pd.DataFrame({
            "Question": [question],
            "Answer": [answer]
        })

        df = pd.concat(
            [df, new_row],
            ignore_index=True
        )

        df.to_csv(
            CSV_FILE,
            index=False
        )

        print("FAQ added successfully!")

    except Exception as e:
        print("Error:", e)


def view_faq():
    try:
        df = load_faq()

        print("\n===== FAQ Dataset =====")
        print(df)

    except Exception as e:
        print("Error:", e)


while True:

    print("\n===== AI Helpdesk Chatbot =====")
    print("1. Ask Question")
    print("2. Add FAQ")
    print("3. View FAQs")
    print("4. Exit")

    try:
        choice = int(
            input("Enter Choice: ")
        )

        if choice == 1:
            ask_question()

        elif choice == 2:
            add_faq()

        elif choice == 3:
            view_faq()

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number.")