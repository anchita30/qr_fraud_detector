import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

df = pd.read_csv('phishing_dataset_rebuilt.csv')

feature_cols = [
    'URLLength', 'DomainLength', 'IsDomainIP', 'TLDLegitimateProb', 'TLDLength',
    'NoOfSubDomain', 'HasObfuscation', 'NoOfObfuscatedChar', 'ObfuscationRatio',
    'NoOfLettersInURL', 'LetterRatioInURL', 'NoOfDegitsInURL', 'DegitRatioInURL',
    'NoOfEqualsInURL', 'NoOfQMarkInURL', 'NoOfAmpersandInURL',
    'NoOfOtherSpecialCharsInURL', 'SpacialCharRatioInURL', 'IsHTTPS',
    'Bank', 'Pay', 'Crypto'
]

X = df[feature_cols]
y = df['label']

# 80/20 train-test split, stratified so both sets keep the same class balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=['Phishing', 'Legitimate']))

print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

# Feature importance - which signals matter most
importances = pd.Series(model.feature_importances_, index=feature_cols).sort_values(ascending=False)
print("=== Top 10 Feature Importances ===")
print(importances.head(10))

# Save the trained model to disk for later use in the backend
joblib.dump(model, 'fraud_model.pkl')
print("\nModel saved as fraud_model.pkl")