import requests
from bs4 import BeautifulSoup

def download_subtitles(movie_title):
    try:
        subtitle_url = _search_subtitles(movie_title)
        return subtitle_url
    except Exception as e:
        print(f"An error occurred while downloading subtitles: {e}")
        return None  # Return None if an error occurs

def _search_subtitles(movie_title):
    # Perform subtitle search using the provided movie_title
    search_url = f"https://subscene.com/subtitles/release?q={movie_title.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch subtitles from Subscene. Status code: {response.status_code}")

    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract subtitle download URL from parsed content
    subtitle_link = soup.find('a', {'class': 'a1'}).get('href')
    return subtitle_link

# Example usage:
# subtitle_url = download_subtitles(movie_title='Inception')
# if subtitle_url:
#     print(f"Subtitles for 'Inception' are available at: {subtitle_url}")
# else:
#     print("Failed to download subtitles.")
