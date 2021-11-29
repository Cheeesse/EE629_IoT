# EE629_IoT Project: Amatracker
Amatracker is an Amazon price tracking tool written in Python.

## Functionality
Users are able to set an expected price for a specific Amazon product, the program will keep tracking the product price. Once the price lower than user's expected price, program will alert user by cloud service.

## Requirement
[Requests](https://docs.python-requests.org/en/latest/) will be used to send HTTP/1.1 requests to Amazon server. <br>
You can install it by:
```sh
$ python -m pip install requests
```

[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) will be used to grabbing data from Amazon website. <br>
You can install it by:
```sh
$ sudo pip install beautifulsoup4
```
[smtplib](https://docs.python.org/3/library/smtplib.html) is a SMTP protocol client for Python. It will be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. <br>
You can install it by:
```sh
$ python -m pip install secure-smtplib
```
## Set Your Data
URL is the link of your Amazon product page.<br>
You can put your expected price in PRICE_VALUE.