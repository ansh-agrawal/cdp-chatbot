import requests
from bs4 import BeautifulSoup

CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_docs():
    data = []
    for platform, url in CDP_DOCS.items():
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text().strip().replace("\n", " ")
            data.append({"platform": platform, "content": text})
    return data
