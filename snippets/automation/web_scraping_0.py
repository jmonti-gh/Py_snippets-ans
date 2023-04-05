### web_scraping.py

import requests
from bs4 import BeautifulSoup  

response = requests.get('https://www.bbc.com/news')
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser') 
#print(soup)
print(soup.find_all('h2'))