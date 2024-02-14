import requests
from bs4 import BeautifulSoup

class PirateBayScraper:
    def __init__(self):
        self.base_url = 'https://thepiratebay.org/search/'

    def search_tpb(self, query):
        search_url = f"{self.base_url}{query}/0/99/0"
        try:
            response = requests.get(search_url)
            response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
            soup = BeautifulSoup(response.text, 'html.parser')
            torrents = []
            for row in soup.find_all("a", class_="detLink"):
                title = row.text
                link = 'https://thepiratebay.org' + row['href']
                # Further processing to extract torrent details like size, seeds, etc. can be added here
                torrents.append({'title': title, 'link': link})
            return torrents
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch torrents: {e}")
            return []

# Example usage:
scraper = PirateBayScraper()
print(scraper.search_tpb("Inception"))
