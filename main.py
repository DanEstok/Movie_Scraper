from kivy.app import App
from gui import MovieTorrentFinderApp
from updater import Updater
import sys
import os

def get_current_version():
    # Assume version info is stored in a file named VERSION in the same directory as this script
    version_file_path = os.path.join(os.path.dirname(__file__), 'VERSION')
    with open(version_file_path, 'r') as version_file:
        return version_file.read().strip()

def main():
    updater = Updater(repo_url="https://github.com/DanEstok/Movie_Scraper")

    current_version = get_current_version()
    available_updates = updater.check_for_updates(current_version)
    if available_updates:
        # Here, integrate with the GUI to ask the user if they want to update now
        print("Updates are available. Do you want to install them now? [Y/n]")
        user_decision = input().lower()
        if user_decision in ['y', 'yes', '']:
            download_path = "update.zip"
            if updater.download_updates(download_path):
                install_path = "."  # Replace with your installation directory
                if updater.install_updates(download_path, install_path):
                    print("Updates installed successfully. Restarting the application...")
                    os.execv(__file__, ['python'] + sys.argv)  # Restart the application
                else:
                    print("Failed to install updates.")
            else:
                print("Failed to download updates.")
    else:
        print("No updates available.")

    app = MovieTorrentFinderApp()
    app.run()

if __name__ == '__main__':
    main()
