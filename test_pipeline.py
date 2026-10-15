import joblib
import pandas as pd
from feature_extractor import extract_features

model = joblib.load('fraud_model.pkl')

test_urls = [
    'https://www.google.com',
    'http://192.168.1.1/verify-account-now',
    'https://accounts-secure-verify-bank-login.tk/reset?token=abc123',
]

for url in test_urls:
    features = extract_features(url)
    X = pd.DataFrame([features])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0]
    label = 'Legitimate' if pred == 1 else 'Phishing'
    print(f"{url}\n  -> {label} (confidence: {max(prob):.2%})\n")