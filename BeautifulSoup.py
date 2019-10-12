from bs4 import BeautifulSoup
import requests

try:
    r = requests.get("https://www.beeradvocate.com/beer/")
except requests.exceptions.MissingSchema as ms: #Missing URL Schema
    print(ms)
except requests.exceptions.ConnectionError as ce: # connection error
    print(ce)
except requests.exceptions.HTTPError as herror: #invalid HTTP response
    print(herror)
except requests.exceptions.Timeout as toerr:
    print(toerr)
else:
    print("Page retrieval ok")
html = r.content
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())
review_titles_list = soup.find_all("h6")
for review_title in review_titles_list:
    print(review_title.get_text())

