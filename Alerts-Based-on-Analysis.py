import smtplib
from email.mime.text import MIMEText

# Alerting function
def send_alert(symbol, price):
    msg = MIMEText(f"Alert: {symbol} crossed the price threshold with a value of {price}!")
    msg['Subject'] = 'Stock Price Alert'
    msg['From'] = 'alert@financialapp.com'
    msg['To'] = 'your-email@example.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your-email@example.com', 'your-password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# Modify analyze_stock_data to include alerting
def analyze_stock_data(data):
    if data['price'] > 1000:
        print(f"Alert: {data['symbol']} crossed $1000 with price {data['price']}!")
        send_alert(data['symbol'], data['price'])
