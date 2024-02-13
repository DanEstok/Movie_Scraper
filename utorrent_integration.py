import requests

def add_to_utorrent(magnet_links):
    try:
        # Make a POST request to uTorrent API endpoint '/add' with magnet links
        response = requests.post('http://localhost:8080/add', data={'magnet_links': magnet_links})
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Torrents added to uTorrent successfully.")
        else:
            print(f"Failed to add torrents to uTorrent. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while adding torrents to uTorrent: {e}")

def is_utorrent_running():
    try:
        # Check if uTorrent is running by sending a GET request to the API endpoint
        response = requests.get('http://localhost:8080')
        
        # Return True if uTorrent is running (status code 200), False otherwise
        return response.status_code == 200
    except Exception as e:
        print(f"An error occurred while checking if uTorrent is running: {e}")
        return False
