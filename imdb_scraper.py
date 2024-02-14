import requests
from bs4 import BeautifulSoup
import time
import logging

class IMDbScraper:
    def __init__(self):
        self.base_url = "https://www.imdb.com/search/title/"
        self.cache = {}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def scrape_movie_titles(self, year_range=None, genre=None, rating=None):
        cache_key = f"{year_range}-{genre}-{rating}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            movie_details = self._scrape_movies(year_range, genre, rating)
            self.cache[cache_key] = movie_details
            return movie_details
        except Exception as e:
            logging.error(f"An error occurred while scraping IMDb: {e}")
            return []

    def _scrape_movies(self, year_range=None, genre=None, rating=None):
        params = self._build_query_params(year_range, genre, rating)
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            return self._parse_movies(response.text)
        else:
            logging.error(f"Failed to retrieve data: {response.status_code}")
            return []

    def _build_query_params(self, year_range, genre, rating):
        # Assuming IMDb URL parameters for filtering by year, genre, and rating
        params = {}
        if year_range:
            params['release_date'] = ','.join(map(str, year_range))
        if genre:
            params['genres'] = genre
        if rating:
            params['user_rating'] = rating
        return params

    def _parse_movies(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        movie_containers = soup.find_all('div', class_='lister-item mode-advanced')
        movies = []
        for movie in movie_containers:
            title = movie.h3.a.text
            year = movie.h3.find('span', class_='lister-item-year').text
            movies.append({'title': title, 'year': year})
            # Add more details extraction logic here as needed
        return movies

    # Throttle requests to respect IMDb's robots.txt and avoid being blocked
    def _throttle_requests(self, seconds=1.0):
        time.sleep(seconds)

# Example Usage
if __name__ == '__main__':
    scraper = IMDbScraper()
    movies = scraper.scrape_movie_titles(year_range=(2020, 2021), genre='action', rating='8,9')
    print(movies)
