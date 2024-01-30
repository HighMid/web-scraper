from bs4 import BeautifulSoup
import requests

def parse(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('h1', {'id': 'firstHeading'}).text
    
    clean_title = title.replace('/', '-').replace('\\', '-')
    
    citations = soup.find_all('span', string='citation needed')
    
    passages = []
    
    for citation in citations:
        parent = citation.find_parent('p')
        if parent:
            passages.append(parent.text.strip())
            
    return clean_title, len(citations), passages

    
