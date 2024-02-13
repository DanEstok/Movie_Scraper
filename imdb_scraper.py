import requests
from bs4 import BeautifulSoup

class IMDbScraper:
    def __init__(self):
        self.cache = {}  # Cache for storing previously scraped data

    def scrape_movie_titles(self, year_range=None, genre=None, rating=None):
        if year_range:
            start_year, end_year = year_range
            cache_key = f"{start_year}-{end_year}-{genre}-{rating}"
        else:
            cache_key = "all"

        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            # Perform IMDb scraping based on provided parameters
            # Example scraping logic goes here
            movie_titles = ['Movie 1', 'Movie 2', 'Movie 3']  # Placeholder data for testing

            # Store scraped data in cache
            self.cache[cache_key] = movie_titles
            return movie_titles
        except Exception as e:
            print(f"An error occurred while scraping IMDb: {e}")
            return []

# Example usage:
# scraper = IMDbScraper()
# movies = scraper.scrape_movie_titles(year_range=(2000, 2020), genre='action', rating='7+')
# print(movies)
