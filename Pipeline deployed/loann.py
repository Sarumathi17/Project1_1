from flask import Flask, render_template, request
import pickle
import numpy as np
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
        # Get input values 
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

        # Create DataFrame
        input_dict = {
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
        }

        input_df = pd.DataFrame(input_dict)

        #Use model to predict
        prob = model.predict_proba(input_df)[0][1]
        prediction = "Loan Approved" if prob >= 0.55 else "Loan Not Approved"
        prediction += f" (Probability: {prob:.2f})"

        return render_template('myloan.html', prediction=prediction)

    except Exception as e:
        return f"Something went wrong: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

    
