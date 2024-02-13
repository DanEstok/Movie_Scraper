# Import necessary libraries
import requests
from bs4 import BeautifulSoup

def search_tpb(movie_title):
    try:
        # Initialize an empty list to store search results
        results = []

        # The Pirate Bay URL for movie search
        tpb_url = f'https://thepiratebay.org/search/{movie_title}/0/99/200'

        # Send a GET request to The Pirate Bay
        response = requests.get(tpb_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all search results
            torrents = soup.find_all('tr')

            # Extract relevant information for each torrent
            for torrent in torrents:
                title = torrent.find('div', class_='detName').text
                seeds = int(torrent.find('td', class_='vertTh').text)
                leechers = int(torrent.find_all('td', class_='vertTh')[1].text)
                magnet_link = torrent.find('a', title='Download this torrent using magnet')['href']
                results.append({'title': title, 'seeds': seeds, 'leechers': leechers, 'magnet_link': magnet_link})

        # Return the list of search results
        return results
    except Exception as e:
        print(f"An error occurred while searching The Pirate Bay: {e}")
        return []
