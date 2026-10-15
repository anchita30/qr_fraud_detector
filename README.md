AI-Powered Fake QR Code & Payment Fraud Detector

A Python tool that scans a QR code, decodes its contents, and flags it as safe or suspicious using a machine learning model trained on phishing URLs. Built to help catch malicious QR codes used in payment and phishing scams (a growing problem with UPI-style QR payments).

Status: Work in progress. Core decoding and URL classification work. Visual-tampering detection, UI/API and UPI-specific rules are still to come (see Roadmap).

How it works
QR image  -->  Decode QR  -->  Extract content type (URL / IP-based URL / UPI)
                                        |
                                        v
                            Extract 22 URL features
                                        |
                                        v
                       Random Forest classifier (phishing vs legit)
                                        |
                                        v
                               Verdict: safe / suspicious
Features

Implemented

QR decoding for three payload types: standard URLs, IP-based URLs, and UPI payment links
22-feature URL extractor (lexical and structural features of the URL)
Random Forest classifier (200 trees) for phishing vs legitimate URL detection
Trained model saved as fraud_model.pkl for reuse without retraining

Planned

QR visual-tampering detection using OpenCV heuristics (e.g. a sticker pasted over a genuine QR)
UPI-specific rules (payee/merchant checks, suspicious parameters)
UI or API layer
End-to-end pipeline integration
Dataset
About 235,000 URL records in total
134,850 legitimate
100,945 phishing
Source: <add dataset name / link here>
Tech stack
Python 3.x
scikit-learn (Random Forest)
pandas / NumPy
OpenCV (QR image handling; tampering detection planned)
<add your QR decoding library here, e.g. pyzbar / OpenCV QRCodeDetector>
Installation
bash
git clone <your-repo-url>
cd <your-project-folder>
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
Usage
bash
# Decode and check a QR image
python <your_main_script>.py --image path/to/qr.png

Example output:

Decoded content : http://example-login-secure.xyz/verify
Content type    : URL
Verdict         : SUSPICIOUS

Replace the command and example output above with your actual script name and real output.

Model
Item	Detail
Algorithm	Random Forest
Trees	200
Training records	~235k
Features	22 URL-based features
Saved model	fraud_model.pkl

Evaluation metrics: <add accuracy / precision / recall / F1 and confusion matrix once computed>

Project structure
<replace with your actual layout, for example:>
.
├── qr_decoder.py
├── feature_extractor.py
├── train_model.py
├── fraud_model.pkl
├── requirements.txt
└── README.md
Roadmap
 Target 1: QR decoding (URL, IP-based URL, UPI)
 Target 2: Phishing URL ML classification
 Target 3: QR visual-tampering detection (OpenCV)
 UPI-specific rule checks
 Saved evaluation metrics and plots
 Unit tests (pytest)
 UI or API
 End-to-end integration
Limitations
The classifier judges the URL only; a legitimate-looking URL can still lead to a scam.
Results depend on the quality and recency of the training data.
Not a replacement for caution when paying through a QR code.
