from kivy.app import App
from gui import MovieTorrentFinderApp
from updater import Updater

def main():
    # Initialize the updater
    updater = Updater(repo_url="https://github.com/DanEstok/Movie_Scraper")

    # Check for updates
    current_version = "1.0"  # Replace with your current version
    if updater.check_for_updates(current_version):
        # Download updates
        download_path = "update.zip"
        if updater.download_updates(download_path):
            # Install updates
            install_path = "."  # Replace with your installation directory
            if updater.install_updates(download_path, install_path):
                print("Updates installed successfully.")
            else:
                print("Failed to install updates.")
        else:
            print("Failed to download updates.")
    else:
        print("No updates available.")

    # Run the application
    app = MovieTorrentFinderApp()
    app.run()

if __name__ == '__main__':
    main()
