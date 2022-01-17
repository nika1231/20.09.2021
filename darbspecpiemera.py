import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://vvsprogramm.github.io/A/")

soup = BeautifulSoup(lapa.content, 'html.parser')

print(soup.find_all('p'))

print(soup.find_all('p')[0].get_text())

pp = list(div.children)[1]
print(pp.get_text())

