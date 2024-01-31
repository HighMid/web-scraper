from scrapers_scraper import Wikiscraper

def scraper():
    
    scrap = Wikiscraper("https://en.wikipedia.org/wiki/Terraria")
    scrap.ignition()       
        
scraper()