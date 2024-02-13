from kivy.app import App
from gui import MovieTorrentFinderApp
from updater import Updater

def main():
    updater = Updater()  # Initialize the updater
    
    try:
        updater.check_for_updates()  # Check for updates
        updater.download_updates()  # Download updates
        updater.install_updates()  # Install updates if any
    except Exception as e:
        print(f"An error occurred during the update process: {e}")
        # Notify the user about the error
        # For example: show an error message in the GUI
        
    app = MovieTorrentFinderApp()
    app.run()

if __name__ == '__main__':
    main()
