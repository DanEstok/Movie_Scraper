from kivy.app import App
from kiv.uix.boxlayout import BoxLayout
from kivuix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.combobox import ComboBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget

from imdb_scraper import scrape_imdb_movies, scrape_imdb_movie_info
from piratebay_scraper import search_tpb, is_tpb_running
from utorrent_integration import add_to_utorrent, is_utorrent_running
from subtitle_finder import search_subtitles, download_subtitles
from file_creator import create_excel_spreadsheet, create_word_document

class MovieTorrentFinderApp(App):
    def build(self):
        self.root_widget = RootWidget()
        return self.root_widget

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        # Add your GUI elements and layout here

if __name__ == '__main__':
    app = MovieTorrentFinderApp()
    app.run()