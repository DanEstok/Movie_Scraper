from kivy.app import App
from gui import MovieTorrentFinderApp
from updater import Updater

def main():
    # Initialize the updater
    updater = Updater()
    
    # Check for updates
    updater.check_for_updates()
    
    # Download updates
    updater.download_updates()
    
    # Install updates if any
    updater.install_updates()
    
    # Run the MovieTorrentFinderApp
    app = MovieTorrentFinderApp()
    app.run()

if __name__ == '__main__':
    main()
