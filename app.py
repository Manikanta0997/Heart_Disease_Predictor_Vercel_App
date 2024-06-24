from flask import *
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pipe = pickle.load(open("Heart_Knn.pkl", "rb"))
        age = int(request.form["input1"])
        gender = request.form["input2"]
        chest_pain_type = request.form["input3"]
        resting_bp = int(request.form["input4"])
        fasting_bs = int(request.form["input5"])
        resting_ecg = request.form["input6"]
        exercise_angina = request.form["input7"]
        old_peak = float(request.form["input8"])
        st_slope = request.form["input9"]
        input_df = pd.DataFrame(
            {
                "Age": [age],
                "Sex": [gender],
                "ChestPainType": [chest_pain_type],
                "RestingBP": [resting_bp],
                "FastingBS": [fasting_bs],
                "RestingECG": [resting_ecg],
                "ExerciseAngina": [exercise_angina],
                "Oldpeak": [old_peak],
                "ST_Slope": [st_slope],
            }
        )
        result = pipe.predict(input_df)
        if int(result[0]) == 0:
            result = "Safe"
        else:
            result = "Danger"
        return render_template("index.html", prediction=result)

    return render_template("index.html", prediction=None)


if __name__ == "__main__":
    app.run(debug=True)
