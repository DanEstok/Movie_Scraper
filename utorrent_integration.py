# Assuming uTorrent API is used, import necessary libraries for API communication
import requests

def add_to_utorrent(magnet_links):
    try:
        # Assuming the uTorrent API endpoint for adding torrents is '/add'
        # Make a POST request to uTorrent API endpoint with magnet links
        response = requests.post('http://localhost:8080/add', data={'magnet_links': magnet_links})
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Torrents added to uTorrent successfully.")
        else:
            print("Failed to add torrents to uTorrent.")
    except Exception as e:
        print(f"An error occurred while adding torrents to uTorrent: {e}")

def is_utorrent_running():
    try:
        # Implement logic to check if uTorrent is running (for example, check if the API endpoint is accessible)
        response = requests.get('http://localhost:8080')
        return response.status_code == 200
    except Exception as e:
        print(f"An error occurred while checking if uTorrent is running: {e}")
        return False
