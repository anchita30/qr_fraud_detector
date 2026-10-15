import qrcode

qrcode.make('https://www.google.com').save('test_legit_url.png')
qrcode.make('upi://pay?pa=merchant@upi&pn=TestMerchant&am=500&cu=INR').save('test_upi.png')
qrcode.make('http://192.168.1.1/verify-account-now').save('test_suspicious.png')

print("Test QR images created")