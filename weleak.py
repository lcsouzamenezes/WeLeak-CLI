import requests
import json
import cloudscraper
import re
import sys
from bs4 import BeautifulSoup

mode = input('''Select mode:
 - Email: email
 - Username: username
 - Email by password: epwd
 - Username by password: elogin
 - Phone (BETA): phone
 - Domain (BETA): domain
 - Email by hash: hash

''').lower()

try:
    query = str(input('Select your query: ')).rstrip()
    print()
except:
    print('Please enter a valid query.')
    sys.exit()

url = 'https://weleakinfo.to/system/ajax/search.php?type=search'

headers = {
    "Host": "weleakinfo.to",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-type": "application/x-www-form-urlencoded",
    "Content-Length": "71",
    "Origin": "https://weleakinfo.to",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://weleakinfo.to/",
    "Cookie": "__cfduid=d2578cdc2c2a1033b81a83678fc50d64d1596046136; __ddg1=6nCPL8o6dfDcGXKhNCOT; PHPSESSID=48a46430e524883800d701888dbdacbd",
    "TE": "Trailers"
}

scraper = cloudscraper.create_scraper()
response = scraper.get("https://weleakinfo.to").text
soup = BeautifulSoup(response)
csrf = soup.find("input", {"name":"csrf"})['value']

data = {
    'query': query,
    'type': mode,
    'csrf': '88bff874b8bdd92a5ad36c0eeadc2211b29e300f'
}

response = requests.post(url, data=data, headers=headers)
phrase = ''
for i in response.text:
    phrase = phrase+i.rstrip()

soup = BeautifulSoup(phrase)
if 'Noentriesfound' in soup:
    print('No entries found or bad query.\n')
    sys.exit()
else:
    tables = soup.findChildren('tbody')
    my_table = tables[0]
    rows = my_table.findChildren(['th', 'tr'])
    for row in rows:
        cells = row.findChildren('th')
        for cell in cells:
            value = cell.string
            print(value)
sys.exit()
