import requests
from bs4 import BeautifulSoup
 
lapa = requests.get("https://vvsprogramm.github.io/A/")
# print(lapa)
# #print(lapa.content)
 
soup = BeautifulSoup(lapa.content, 'html.parser')
# print(soup.prettify())
 
print(list(soup.children))
# print([type(item) for item in list(soup.children)])
 
html = list(soup.children)[2]
print(list(html.children))
 
body = list(html.children)[3]
print(list(body.children))

div = list(body.children)[1]
print(list(div.children))

p = list(div.children)[1]
print(p.get_text())


pp = list(div.children)[3]
print(pp.get_text())

p_arejais = list(body.children)[3]
print(list(p_arejais.children))
 
b = list(p_arejais.children)[1]
print(b.get_text())

p_arejais_divi = list(body.children)[5]
print(list(p_arejais_divi.children))
 
bb = list(p_arejais_divi.children)[1]
print(bb.get_text())

