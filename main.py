from kivy.app import App
from gui import MovieTorrentFinderApp
from gui import Updater

if __name__ == '__main__':
    updater = Updater()
    updater.check_for_updates()
    updater.download_updates()
    updater.install_updates()
    app = MovieTorrentFinderApp()
    app.run()
