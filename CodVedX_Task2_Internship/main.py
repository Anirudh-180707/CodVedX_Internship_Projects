import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

CSV_FILE = "student_performance.csv"
MODEL_FILE = "student_model.pkl"


def view_dataset():
    try:
        df = pd.read_csv(CSV_FILE)

        print("\n===== Student Dataset =====")
        print(df)

        print("\n===== Dataset Information =====")
        print(df.info())

        print("\n===== Statistical Summary =====")
        print(df.describe())

    except Exception as e:
        print("Error:", e)


def visualize_data():
    try:
        df = pd.read_csv(CSV_FILE)

        plt.figure(figsize=(6, 4))
        plt.scatter(df["Attendance"], df["FinalPerformance"])
        plt.title("Attendance vs Performance")
        plt.xlabel("Attendance")
        plt.ylabel("Final Performance")
        plt.show()

        plt.figure(figsize=(6, 4))
        plt.scatter(df["Marks"], df["FinalPerformance"])
        plt.title("Marks vs Performance")
        plt.xlabel("Marks")
        plt.ylabel("Final Performance")
        plt.show()

        plt.figure(figsize=(6, 4))
        plt.scatter(df["StudyHours"], df["FinalPerformance"])
        plt.title("Study Hours vs Performance")
        plt.xlabel("Study Hours")
        plt.ylabel("Final Performance")
        plt.show()

    except Exception as e:
        print("Error:", e)


def train_model():
    try:
        os.system("python train_model.py")
    except Exception as e:
        print("Error:", e)


def predict_performance():
    try:
        if not os.path.exists(MODEL_FILE):
            print("Please train the model first!")
            return

        with open(MODEL_FILE, "rb") as file:
            model = pickle.load(file)

        attendance = float(input("Enter Attendance: "))
        marks = float(input("Enter Marks: "))
        study_hours = float(input("Enter Study Hours: "))

        prediction = model.predict(
            [[attendance, marks, study_hours]]
        )

        print(
            f"Predicted Final Performance: "
            f"{prediction[0]:.2f}"
        )

    except Exception as e:
        print("Error:", e)


def evaluate_model():
    try:
        df = pd.read_csv(CSV_FILE)

        with open(MODEL_FILE, "rb") as file:
            model = pickle.load(file)

        X = df[["Attendance", "Marks", "StudyHours"]]
        y = df["FinalPerformance"]

        predictions = model.predict(X)

        accuracy = r2_score(y, predictions)

        print(f"Model Accuracy: {accuracy:.2f}")

    except Exception as e:
        print("Error:", e)


while True:
    print("\n===== Student Performance Prediction System =====")
    print("1. View Dataset")
    print("2. Visualize Data")
    print("3. Train Model")
    print("4. Predict Performance")
    print("5. Evaluate Model")
    print("6. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            view_dataset()

        elif choice == 2:
            visualize_data()

        elif choice == 3:
            train_model()

        elif choice == 4:
            predict_performance()

        elif choice == 5:
            evaluate_model()

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number.")