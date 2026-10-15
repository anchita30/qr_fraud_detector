import pandas as pd

df = pd.read_csv('phishing_dataset.csv')

keep_cols = [
    'URLLength', 'DomainLength', 'IsDomainIP', 'TLD', 'URLSimilarityIndex',
    'CharContinuationRate', 'TLDLegitimateProb', 'URLCharProb', 'TLDLength',
    'NoOfSubDomain', 'HasObfuscation', 'NoOfObfuscatedChar', 'ObfuscationRatio',
    'NoOfLettersInURL', 'LetterRatioInURL', 'NoOfDegitsInURL', 'DegitRatioInURL',
    'NoOfEqualsInURL', 'NoOfQMarkInURL', 'NoOfAmpersandInURL',
    'NoOfOtherSpecialCharsInURL', 'SpacialCharRatioInURL', 'IsHTTPS',
    'Bank', 'Pay', 'Crypto', 'label'
]

df_trimmed = df[keep_cols]
print(df_trimmed.shape)
print(df_trimmed.dtypes)
print(df_trimmed.isnull().sum())