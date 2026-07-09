from flask import Flask, render_template, request
import sqlite3
from predict import predict_diabetes
from recommendations import get_recommendation

app = Flask(__name__)


# ---------------- Home Page ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- Prediction ---------------- #

@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]
    pregnancies = int(request.form["pregnancies"])
    glucose = float(request.form["glucose"])
    blood_pressure = float(request.form["blood_pressure"])
    skin_thickness = float(request.form["skin_thickness"])
    insulin = float(request.form["insulin"])
    bmi = float(request.form["bmi"])
    diabetes_pedigree = float(request.form["diabetes_pedigree"])
    age = int(request.form["age"])

    patient_data = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]

    # Predict diabetes risk
    result, probability = predict_diabetes(patient_data)

    # Get AI recommendations
    report = get_recommendation(result)

    # Save into database
    conn = sqlite3.connect("diabetes.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients (
            name,
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age,
            prediction,
            probability
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age,
        result,
        probability
    ))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        name=name,
        result=result,
        probability=probability,
        report=report
    )


# ---------------- Patient History ---------------- #

@app.route("/history")
def history():

    conn = sqlite3.connect("diabetes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients ORDER BY date DESC")

    patients = cursor.fetchall()

    conn.close()

    return render_template("history.html", patients=patients)


# ---------------- Run Flask ---------------- #

if __name__ == "__main__":
    app.run(debug=True)