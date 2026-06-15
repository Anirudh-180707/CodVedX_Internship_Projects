import pandas as pd
import pickle
import os

CSV_FILE = "usage_data.csv"
MODEL_FILE = "utility_model.pkl"


def add_data():
    try:
        month = int(input("Enter Month: "))
        units = float(input("Enter Units Consumed: "))
        bill = float(input("Enter Bill Amount: "))

        df = pd.read_csv(CSV_FILE)

        new_data = pd.DataFrame({
            "Month": [month],
            "Units": [units],
            "Bill": [bill]
        })

        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

        print("Data added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print("Error:", e)


def view_data():
    try:
        df = pd.read_csv(CSV_FILE)

        if df.empty:
            print("No records found.")
        else:
            print("\n===== Usage Data =====")
            print(df)

    except FileNotFoundError:
        print("CSV file not found!")
    except Exception as e:
        print("Error:", e)


def update_data():
    try:
        month = int(input("Enter Month to Update: "))
        df = pd.read_csv(CSV_FILE)

        if month in df["Month"].values:
            units = float(input("Enter New Units: "))
            bill = float(input("Enter New Bill Amount: "))

            df.loc[df["Month"] == month, "Units"] = units
            df.loc[df["Month"] == month, "Bill"] = bill

            df.to_csv(CSV_FILE, index=False)

            print("Record updated successfully!")
        else:
            print("Month not found!")

    except ValueError:
        print("Invalid input!")
    except Exception as e:
        print("Error:", e)


def train_model():
    try:
        os.system("python train_model.py")
    except Exception as e:
        print("Error:", e)


def predict_usage():
    try:
        if not os.path.exists(MODEL_FILE):
            print("Model not found! Train the model first.")
            return

        with open(MODEL_FILE, "rb") as file:
            model = pickle.load(file)

        future_month = int(input("Enter Future Month: "))

        prediction = model.predict([[future_month]])

        print(
            f"Predicted Utility Usage for Month "
            f"{future_month}: {prediction[0]:.2f} Units"
        )

    except ValueError:
        print("Invalid month value!")
    except Exception as e:
        print("Error:", e)


while True:
    print("\n===== Utility Usage Prediction Tool =====")
    print("1. Add Usage Data")
    print("2. View Usage Data")
    print("3. Update Usage Data")
    print("4. Train Model")
    print("5. Predict Future Usage")
    print("6. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_data()

        elif choice == 2:
            view_data()

        elif choice == 3:
            update_data()

        elif choice == 4:
            train_model()

        elif choice == 5:
            predict_usage()

        elif choice == 6:
            print("Exiting Program...")
            break

        else:
            print("Invalid choice! Please select 1-6.")

    except ValueError:
        print("Please enter a valid number.")