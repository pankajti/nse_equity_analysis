import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.screener.in/company/YESBANK/')
soup = BeautifulSoup(response.text)
print(soup)