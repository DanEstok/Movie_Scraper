import requests
import logging

# Set up logging
logging.basicConfig(filename='utorrent_integration.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_to_utorrent(magnet_links):
    try:
        # Assuming the uTorrent API endpoint for adding torrents is '/add'
        # Make a POST request to uTorrent API endpoint with magnet links
        response = requests.post('http://localhost:8080/add', data={'magnet_links': magnet_links}, timeout=10)
        
        # Log API request and response
        logging.info(f"Request to uTorrent API: {response.request.method} {response.request.url}")
        logging.info(f"Request data: {response.request.body}")
        logging.info(f"Response from uTorrent API: {response.status_code} {response.text}")
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Torrents added to uTorrent successfully.")
        else:
            print("Failed to add torrents to uTorrent.")
    except requests.RequestException as e:
        logging.error(f"Error adding torrents to uTorrent: {e}")
        print(f"An error occurred while adding torrents to uTorrent: {e}")

def is_utorrent_running():
    try:
        # Implement logic to check if uTorrent is running (for example, check if the API endpoint is accessible)
        response = requests.get('http://localhost:8080', timeout=5)
        return response.status_code == 200
    except requests.RequestException as e:
        logging.error(f"Error checking if uTorrent is running: {e}")
        print(f"An error occurred while checking if uTorrent is running: {e}")
        return False
