import joblib

# Load your model
model = joblib.load("model/model.pkl")

def classify(data):
    prediction = model.predict(data)
    res = ''
    if prediction == 0:
        res = 'risk_high'
    elif prediction == 1:
        res = 'risk_low'
    elif prediction == 2:
        res = 'risk_medium'

    return res




'''
"risk_category_High" → 0

"risk_category_Low" → 1

"risk_category_Medium" → 2'''