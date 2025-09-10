from bs4 import BeautifulSoup
import pandas as pd
import requests

file_path = 'healthline.html'
names = []
urls = []

with open(file_path,'r',encoding='utf-8') as fp:
    soup = BeautifulSoup(fp,'html.parser')
    titles = soup.find_all('a', class_='css-vpljeo')
    for item in titles:
        if item:
            disease_name = item.text.strip()
            disease_url = item['href']
            names.append(disease_name)
            urls.append(disease_url)

all_diseases = []

for disease_name, url in zip(names, urls):
    print(f"\n Scraping {disease_name} \n")
    fetch_url = requests.get(url)
    soup = BeautifulSoup(fetch_url.text, "html.parser")
    sections = soup.find_all("div", {"data-testid": "tabbed-article-section"})

    for sec in sections:
        heading = sec.find("h2")
        heading_text = heading.get_text(strip=True) if heading else "Overview"
        
        content_parts = []
        for p in sec.find_all(["p", "li"]):
            text = p.get_text(strip=True)
            if text:
                content_parts.append(text)

        all_diseases.append({
            "disease": disease_name,
            "section": heading_text,
            "content": " ".join(content_parts)   
        })

df = pd.DataFrame(all_diseases)
df.to_csv('disease_data.csv')
print(df)