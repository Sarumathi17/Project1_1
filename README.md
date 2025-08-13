# Loan Approval Prediction - Deployment

This project is a **Machine Learning web app** for predicting loan approvals using Flask.  
It uses a trained Logistic Regression model stored as a `.pkl` file and serves predictions via a web interface.

---

## 📂 Project Structure

Pipeline deployed/

│

├── templates/ # HTML templates for Flask

├── Logistic Regression.ipynb # Model training notebook

├── loan_approval_pipeline.pkl # Trained ML model

├── loan_approved.csv # Dataset

└──  loann.py # Flask app

Additional:
LOAN PREDICTION.ipynb # Notebook trained with multiple models

---

## 🚀 How to Run Locally

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Sarumathi17/Project1_1.git
cd Project1_1/Pipeline\ deployed
```

### 2️⃣ Install dependencies

Make sure you have Python installed (>=3.8), then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python loann.py
```

### 4️⃣ Access the app

#### 🖥 Run Locally
Open your browser and go to:
```bash
http://127.0.0.1:8000/
```
#### ☁️ Run on AWS EC2
1. Find your EC2 instance's **public IPv4 address** in the AWS console.  
2. Replace `127.0.0.1` with that public IP in the URL:
3. Make sure port **8000** is allowed in your EC2 **Security Group inbound rules**.
```bash
Example:
http://<your-public-ip>:8000/
```

---


## 📸 Screenshot

<p align="center"> <img src="images/"C:\Users\msaru\OneDrive\Pictures\Screenshots\Screenshot 2025-08-13 215848.png"" width="800"> </p>


---


## 📄 License

This project is for learning purposes.

