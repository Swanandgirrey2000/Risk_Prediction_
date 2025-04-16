from flask import Flask, request, render_template_string, url_for

app = Flask(__name__)

# HTML form template with CSS link added
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Loan Risk Prediction</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h2>Loan Risk Prediction Form</h2>
    <div class="form-container">
        <form method="POST">
            <label>Age:</label>
            <input type="number" name="age" required><br>

            <label>Income:</label>
            <input type="text" name="income" required><br>

            <label>Loan Amount:</label>
            <input type="text" name="loan_amount" required><br>

            <label>Loan Duration (in years):</label>
            <input type="number" name="loan_duration" required><br>

            <label>Credit History:</label>
            <select name="credit_history">
                <option value="good">Good</option>
                <option value="bad">Bad</option>
            </select><br>

            <label>Employment Status:</label>
            <select name="employment_status">
                <option value="employed">Employed</option>
                <option value="unemployed">Unemployed</option>
            </select><br>

            <label>Housing Status:</label>
            <select name="housing_status">
                <option value="own">Own</option>
                <option value="rent">Rent</option>
            </select><br>

            <label>Job Type:</label>
            <input type="text" name="job_type"><br>

            <label>Savings Balance:</label>
            <input type="text" name="savings_balance" required><br>

            <input type="submit" value="Predict Risk">
        </form>

        {% if result is not none %}
            <div class="result">
                <h3>Prediction:</h3>
                <p>{{ result }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def predict_risk():
    result = None
    if request.method == "POST":
        try:
            # Convert only numeric fields
            age = int(request.form['age'])
            income = float(request.form['income'].replace(',', ''))
            loan_amount = float(request.form['loan_amount'].replace(',', ''))
            loan_duration = int(request.form['loan_duration'])
            savings_balance = float(request.form['savings_balance'].replace(',', ''))

            # String fields - no conversion
            credit_history = request.form['credit_history']
            employment_status = request.form['employment_status']
            housing_status = request.form['housing_status']
            job_type = request.form['job_type']

            # Simple risk rule
            if income > 50000 and credit_history == 'good':
                result = "Low Risk"
            else:
                result = "High Risk"

        except ValueError as e:
            result = f"Input Error: {e}"

    return render_template_string(form_template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
