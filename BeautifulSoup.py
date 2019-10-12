from bs4 import BeautifulSoup
import requests
r = requests.get("https://en.wikipedia.org/wiki/HTML")

html = r.content
soup = BeautifulSoup(html,'html.parser')
print(soup.h1)
