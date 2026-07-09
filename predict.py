import joblib
import numpy as np

# Load the trained model
model = joblib.load("diabetes_model.pkl")

# Load the scaler
scaler = joblib.load("scaler.pkl")


def predict_diabetes(data):
    """
    data should be in this order:
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
    """

    # Convert input into NumPy array
    data = np.array(data).reshape(1, -1)

    # Scale the input
    data = scaler.transform(data)

    # Make prediction
    prediction = model.predict(data)[0]

    # Get prediction probability
    probability = model.predict_proba(data)[0][prediction]

    if prediction == 1:
        result = "High Risk"
    else:
        result = "Low Risk"

    return result, round(probability * 100, 2)
if __name__ == "__main__":

    test_data = [0, 85, 70, 20, 80, 22.5, 0.2, 25]

    result, probability = predict_diabetes(test_data)

    print("Prediction:", result)
    print("Probability:", probability)
    