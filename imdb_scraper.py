# Import necessary libraries
import requests
from bs4 import BeautifulSoup

def scrape_imdb_movies(year_range=None, genre=None, rating=None):
    try:
        # Initialize an empty list to store movie titles
        movie_titles = []

        # IMDb URL for movies
        imdb_url = 'https://www.imdb.com/search/title/?title_type=feature&sort=year,desc'

        # Add parameters to IMDb URL based on user input
        if year_range:
            start_year, end_year = year_range
            imdb_url += f'&release_date={start_year}-01-01,{end_year}-12-31'
        if genre:
            imdb_url += f'&genres={genre}'
        if rating:
            imdb_url += f'&user_rating={rating}'

        # Send a GET request to IMDb
        response = requests.get(imdb_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all movie titles
            titles = soup.find_all('h3', class_='lister-item-header')

            # Extract movie titles
            for title in titles:
                movie_titles.append(title.a.text)

        # Return the list of movie titles
        return movie_titles
    except Exception as e:
        print(f"An error occurred while scraping IMDb: {e}")
        return []

