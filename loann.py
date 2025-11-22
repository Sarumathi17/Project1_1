from flask import Flask, render_template, request
import pickle
import pandas as pd

# Load trained pipeline
with open('loan_approval_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('myloan.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicant_income = float(request.form['applicant_income'])
        coapplicant_income = float(request.form['coapplicant_income'])
        loan_amount = float(request.form['loan_amount'])
        credit_history = float(request.form['credit_history'])
        property_area = request.form['property_area']

        input_data = pd.DataFrame({
            'Gender': [gender],
            'Married': [married],
            'Dependents': [dependents],
            'Education': [education],
            'Self_Employed': [self_employed],
            'ApplicantIncome': [applicant_income],
            'CoapplicantIncome': [coapplicant_income],
            'LoanAmount': [loan_amount],
            'Credit_History': [credit_history],
            'Property_Area': [property_area]
        })

        # Predict class: 'Y' or 'N'
        prediction_label = model.predict(input_data)[0]

        # Get probability for 'Y' (Approved)
        probs = model.predict_proba(input_data)[0]
        classes = list(model.classes_)          # e.g. ['N', 'Y']
        idx_approved = classes.index('Y')       # index of 'Y'
        prob_approved = probs[idx_approved]

        # Map to text
        prediction = "Loan Approved" if prediction_label == 'Y' else "Loan Not Approved"
        prediction += f" (Probability: {prob_approved:.2f})"

        return render_template('myloan.html', prediction=prediction)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
