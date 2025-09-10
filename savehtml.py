import requests
from bs4 import BeautifulSoup
url = "https://www.healthline.com/directory/topics"
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers)

with open('healthline.html','w',encoding='utf-8') as f:
    soup = BeautifulSoup(r.text,'html.parser')
    f.write(soup.prettify())