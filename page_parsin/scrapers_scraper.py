import requests
from bs4 import BeautifulSoup

class Wikiscraper():
    
    def __init__(self, url):
        self.url = url
        self.soup = self.fetch_and_parse()
        
    def fetch_and_parse(self):
        
        response = requests.get(self.url)
        
        return BeautifulSoup(response.content, 'html.parser')
        
    def get_title(self):
        
        title = self.soup.find('h1', {'id': 'firstHeading'}).text
        
        return title.replace('/', '-').replace('\\', '-')
    
    def get_citations_needed_report(self):
        
        citation_needed = self.soup.find_all('span', string='citation needed')
        
        num_citation = self.get_citations_needed_count(citation_needed)
        
        passage = []
        for citation in citation_needed:
            parent = citation.find_parent('p')
            if parent:
                passage.append(parent.text.strip())
                
        return num_citation, passage
    
    def get_citations_needed_count(self, content):
        return len(content)
    
    def parse_citation_save(self, title, citation, passages):
    
        with open(f'{title}.txt', 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n")
            file.write(f"Number of citations needed: {citation}\n")
            for passage in passages:
                file.write(f"Citation needed for: \"{passage}\"\n")
    
    def ignition(self):
        
        title = self.get_title()
        num_citations, citation_passages = self.get_citations_needed_report()
        
        print(f"Number citations needed: {num_citations}\n")
        for passage in citation_passages:
            print(f"Citation needed for: \"{passage}\"\n")
            
        self.parse_citation_save(title, num_citations, citation_passages)