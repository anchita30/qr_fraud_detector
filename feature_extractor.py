import pandas as pd
from urllib.parse import urlparse

# Load the TLD legitimacy lookup table we built from training data
_tld_table = pd.read_csv('tld_legitimacy.csv', index_col='TLD')['mean'].to_dict()
_overall_legitimacy_rate = 0.5718950783519583  # fallback for unseen/rare TLDs


def get_tld(domain: str) -> str:
    """Extract the TLD (last part after the final dot) from a domain."""
    parts = domain.split('.')
    return parts[-1] if len(parts) > 1 else ''


def extract_features(url: str) -> dict:
    parsed = urlparse(url)
    domain = parsed.netloc
    tld = get_tld(domain)

    url_len = len(url) if len(url) > 0 else 1  # avoid divide-by-zero

    return {
        'URLLength': len(url),
        'DomainLength': len(domain),
        'IsDomainIP': 1 if domain.replace('.', '').isdigit() else 0,
        'TLDLegitimateProb': _tld_table.get(tld, _overall_legitimacy_rate),
        'TLDLength': len(tld),
        'NoOfSubDomain': domain.count('.'),
        'HasObfuscation': 1 if '%' in url else 0,
        'NoOfObfuscatedChar': url.count('%'),
        'ObfuscationRatio': url.count('%') / url_len,
        'NoOfLettersInURL': sum(c.isalpha() for c in url),
        'LetterRatioInURL': sum(c.isalpha() for c in url) / url_len,
        'NoOfDegitsInURL': sum(c.isdigit() for c in url),
        'DegitRatioInURL': sum(c.isdigit() for c in url) / url_len,
        'NoOfEqualsInURL': url.count('='),
        'NoOfQMarkInURL': url.count('?'),
        'NoOfAmpersandInURL': url.count('&'),
        'NoOfOtherSpecialCharsInURL': sum(not c.isalnum() for c in url),
        'SpacialCharRatioInURL': sum(not c.isalnum() for c in url) / url_len,
        'IsHTTPS': 1 if url.startswith('https') else 0,
        'Bank': 1 if 'bank' in url.lower() else 0,
        'Pay': 1 if 'pay' in url.lower() else 0,
        'Crypto': 1 if 'crypto' in url.lower() else 0,
    }