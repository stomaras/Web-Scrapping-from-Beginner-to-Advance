import requests

r = requests.get("https://en.wikipedia.org/wiki/HTML")
print(r.content)
