from flask import Flask
import joblib

app = Flask(__name__)

model = joblib.load('fraud_model.pkl')

@app.route('/')
def home():
    return "Fraud Detection Model Running Successfully"

if __name__ == '__main__':
    app.run(debug=True)