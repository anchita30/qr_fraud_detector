import pandas as pd
from feature_extractor import extract_features

df = pd.read_csv('phishing_dataset.csv')

print("Recomputing features for all URLs using our own extractor...")
print("This may take a minute or two for", len(df), "rows.")

feature_rows = []
for url in df['URL']:
    feature_rows.append(extract_features(url))

features_df = pd.DataFrame(feature_rows)
features_df['label'] = df['label'].values

features_df.to_csv('phishing_dataset_rebuilt.csv', index=False)
print("Saved phishing_dataset_rebuilt.csv, shape:", features_df.shape)