import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_citations_needed_count(url):
    soup = fetch_and_parse(url)
    return len(soup.find_all('span', string='citation needed'))

def get_citations_needed_report(url):
    soup = fetch_and_parse(url)
    citation_needed = soup.find_all('span', string='citation needed')

    report = ""
    for citation in citation_needed:
        parent = citation.find_parent('p')
        if parent:
            report += parent.text.strip() + "\n\n"
    
    return report.strip()


url = "https://en.wikipedia.org/wiki/Terraria"
count = (get_citations_needed_count(url))
print(f"This was gathered from, {url}\n")
print(f'Citations needed: {count}\n')
print(get_citations_needed_report(url))
