import requests
from bs4 import BeautifulSoup

class PirateBayScraper:
    def __init__(self):
        pass

    def search_tpb(self, movie_title):
        try:
            results = self._scrape_pirate_bay(movie_title)
            return results
        except Exception as e:
            print(f"An error occurred while searching The Pirate Bay: {e}")
            return []

    def _scrape_pirate_bay(self, movie_title):
        # Perform search on The Pirate Bay
        url = f"https://thepiratebay.org/search/{movie_title}/0/99/0"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch The Pirate Bay search results. Status code: {response.status_code}")

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract search results from parsed content
        results = []
        for row in soup.find_all('tr', {'class': 'odd'}):
            title = row.find('div', {'class': 'detName'}).find('a').text
            seeds = int(row.find('td', {'align': 'right'}).text)
            leechers = int(row.find_all('td', {'align': 'right'})[1].text)
            magnet_link = row.find('a', {'title': 'Download this torrent using magnet'}).get('href')
            results.append({'title': title, 'seeds': seeds, 'leechers': leechers, 'magnet_link': magnet_link})

        return results

# Example usage:
# scraper = PirateBayScraper()
# results = scraper.search_tpb(movie_title='Inception')
# print(results)
