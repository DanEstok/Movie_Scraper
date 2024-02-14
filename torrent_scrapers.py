from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class TorrentScraper(ABC):
    @abstractmethod
    def search(self, query):
        pass

class PirateBayScraper(TorrentScraper):
    # Implement PirateBay specific search logic
    def search(self, query):
        pass

class RealDebridScraper(TorrentScraper):
    # Implement Real-Debrid specific search logic
    def search(self, query):
        pass

# Additional scrapers can be defined here following the same pattern.

class ScraperAggregator:
    def __init__(self):
        self.scrapers = [PirateBayScraper(), RealDebridScraper()]  # Add instances of all scrapers here

    def search_all(self, query):
        results = []
        for scraper in self.scrapers:
            try:
                results.extend(scraper.search(query))
            except Exception as e:
                print(f"Error with {scraper.__class__.__name__}: {e}")
        return results
