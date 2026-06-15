import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

CSV_FILE = "student_performance.csv"
MODEL_FILE = "student_model.pkl"

try:
    df = pd.read_csv(CSV_FILE)

    # Handle missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    X = df[["Attendance", "Marks", "StudyHours"]]
    y = df["FinalPerformance"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = r2_score(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.2f}")

    with open(MODEL_FILE, "wb") as file:
        pickle.dump(model, file)

    print("Model trained and saved successfully!")

except FileNotFoundError:
    print("Dataset file not found!")

except Exception as e:
    print("Error:", e)