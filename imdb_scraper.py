from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

def scrape_imdb_movies(year_range=None, genre=None, rating=None, movie_title=None):
    # ... (same as the original function)