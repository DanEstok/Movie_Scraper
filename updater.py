import requests
import os

class Updater:
    def __init__(self, repo_url):
        self.repo_url = repo_url

    def check_for_updates(self, current_version):
        try:
            response = requests.get(f"{self.repo_url}/version.txt")
            latest_version = response.text.strip()
            return latest_version != current_version
        except Exception as e:
            print(f"Error checking for updates: {e}")
            return False

    def download_updates(self, download_path):
        try:
            response = requests.get(f"{self.repo_url}/app.zip")
            with open(download_path, "wb") as file:
                file.write(response.content)
            return True
        except Exception as e:
            print(f"Error downloading updates: {e}")
            return False

    def install_updates(self, download_path, install_path):
        try:
            # Extract downloaded files to install directory
            import zipfile
            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(install_path)
            # Clean up downloaded zip file
            os.remove(download_path)
            return True
        except Exception as e:
            print(f"Error installing updates: {e}")
            return False
