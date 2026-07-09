def get_recommendation(result):

    if result == "High Risk":

        return {
            "risk": "High Diabetes Risk",

            "message": "The patient has a high probability of diabetes. Immediate medical consultation is recommended.",

            "recommendations": [

                "Consult a diabetologist or physician immediately.",

                "Monitor blood glucose regularly.",

                "Follow a low-sugar, high-fiber diet.",

                "Exercise for at least 30 minutes daily.",

                "Reduce body weight if overweight.",

                "Avoid sugary drinks and processed foods.",

                "Schedule regular HbA1c tests."
            ]
        }

    else:

        return {
            "risk": "Low Diabetes Risk",

            "message": "The patient currently has a low probability of diabetes. Continue maintaining a healthy lifestyle.",

            "recommendations": [

                "Maintain a balanced diet.",

                "Exercise regularly.",

                "Drink enough water daily.",

                "Maintain a healthy body weight.",

                "Avoid excessive sugar intake.",

                "Get regular health check-ups.",

                "Continue healthy lifestyle habits."
            ]
        }