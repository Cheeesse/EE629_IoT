import requests
from bs4 import BeautifulSoup
import smtplib
import json
import time

URL = "YOUR_URL_HERE"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
PRICE_VALUE = #YOUR_EXPECTED_PRICE_HERE
EMAIL_ADDRESS = "YOUR_EMAIL_HERE"
WEBHOOK = "YOUR_IFTTT_WEBHOOK_HERE"

page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content, 'lxml')
title = soup.find(id='productTitle').get_text().strip()
price = soup.find(id='priceblock_ourprice').get_text().strip()[1:4]

data = {'value1': title,
        'value2': price,
        'value3': URL}

def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still ${diff} higher than your expectation!")
        time.sleep(1800)
        trackPrices()
    else:
        print("Cheaper! Notifying...")
        toPost = requests.post(WEBHOOK, data = json.dumps(data), headers = {'Content-Type': 'application/json'})
        sendEmail()
    pass

def getPrice():
    print(title)
    print(f"The price is {price}")

    return price


def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+'Click the link to buy: '+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'YOUR_GMAIL_PASSWORD_HERE')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    pass

if __name__ == "__main__":
    trackPrices()