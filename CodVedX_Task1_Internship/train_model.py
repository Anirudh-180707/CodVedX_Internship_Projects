import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

CSV_FILE = "usage_data.csv"
MODEL_FILE = "utility_model.pkl"

try:
    # Load data
    df = pd.read_csv(CSV_FILE)

    # Check if enough data exists
    if len(df) < 2:
        print("Need at least 2 records to train the model.")
        exit()

    # Features and target
    X = df[["Month"]]
    y = df["Units"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save model
    with open(MODEL_FILE, "wb") as file:
        pickle.dump(model, file)

    print("Model trained successfully!")
    print(f"Model saved as '{MODEL_FILE}'")

except FileNotFoundError:
    print("Error: usage_data.csv not found!")

except Exception as e:
    print("Error:", e)