from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

from imdb_scraper import scrape_imdb_movies
from piratebay_scraper import search_tpb
from utorrent_integration import add_to_utorrent
from subtitle_finder import download_subtitles
from file_creator import create_excel_spreadsheet, create_word_document
from ml_recommendation import MovieRecommendationSystem

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.recommendation_system = MovieRecommendationSystem()

        # Year range input
        self.start_year = TextInput(multiline=False, hint_text='Start Year')
        self.end_year = TextInput(multiline=False, hint_text='End Year')
        year_layout = BoxLayout(orientation='horizontal', spacing=10)
        year_layout.add_widget(self.start_year)
        year_layout.add_widget(self.end_year)
        self.add_widget(year_layout)

        # Genre selection
        self.genre_spinner = Spinner(text='Genre', values=['action', 'comedy', 'drama', 'horror', 'sci-fi'])
        self.add_widget(self.genre_spinner)

        # Rating input
        self.rating = TextInput(multiline=False, hint_text='Minimum Rating')
        self.add_widget(self.rating)

        # Dark mode toggle button
        self.dark_mode_button = ToggleButton(text='Dark Mode: OFF', group='mode')
        self.add_widget(self.dark_mode_button)

        # Buttons
        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.search_button = Button(text='Search')
        self.search_button.bind(on_press=self.add_torrents)
        button_layout.add_widget(self.search_button)
        self.download_subtitle_button = Button(text='Download Subtitles')
        self.download_subtitle_button.bind(on_press=self.download_subtitles)
        button_layout.add_widget(self.download_subtitle_button)
        self.excel_button = Button(text='Create Excel Spreadsheet')
        self.excel_button.bind(on_press=self.create_excel_spreadsheet)
        button_layout.add_widget(self.excel_button)
        self.word_button = Button(text='Create Word Document')
        self.word_button.bind(on_press=self.create_word_document)
        button_layout.add_widget(self.word_button)
        self.exit_button = Button(text='Exit')
        self.exit_button.bind(on_press=self.exit_app)
        button_layout.add_widget(self.exit_button)
        self.add_widget(button_layout)

        # Progress indicator
        self.progress_indicator = ProgressBar(max=100, size_hint_y=None, height=20)
        self.progress_indicator.opacity = 0
        self.add_widget(self.progress_indicator)

    def add_torrents(self, instance):
        start_year = self.start_year.text
        end_year = self.end_year.text
        genre = self.genre_spinner.text
        rating = self.rating.text

        # Show progress indicator
        self.show_progress_indicator()

        # Perform torrent search task
        try:
            movie_titles = self.recommendation_system.recommend_movies({'start_year': start_year, 'end_year': end_year, 'genre': genre, 'rating': rating})
            self.display_recommendations(movie_titles)
        except Exception as e:
            print(f"An error occurred during torrent search: {e}")
            # Hide progress indicator on error
            self.hide_progress_indicator()

    def download_subtitles(self, instance):
        # Show progress indicator
        self.show_progress_indicator()

        movie_title = 'Example Movie'
        subtitle_url = download_subtitles(movie_title)
        if subtitle_url:
            print(f"Subtitles downloaded successfully from: {subtitle_url}")
        else:
            print("No subtitles found for the movie.")

        # Hide progress indicator after task completion
        Clock.schedule_once(self.hide_progress_indicator, 2)

    def create_excel_spreadsheet(self, instance):
        # Show progress indicator
        self.show_progress_indicator()

        movie_info = [{'title': 'Movie 1', 'rating': 8.0, 'genre': 'Action'},
                      {'title': 'Movie 2', 'rating': 7.5, 'genre': 'Comedy'},
                      {'title': 'Movie 3', 'rating': 7.2, 'genre': 'Drama'}]  # Example data
        create_excel_spreadsheet(movie_info)
        print("Excel spreadsheet created successfully.")

        # Hide progress indicator after task completion
        Clock.schedule_once(self.hide_progress_indicator, 2)

    def create_word_document(self, instance):
        # Show progress indicator
        self.show_progress_indicator()

        movie_info = [{'title': 'Movie 1', 'rating': 8.0, 'genre': 'Action'},
                      {'title': 'Movie 2', 'rating': 7.5, 'genre': 'Comedy'},
                      {'title': 'Movie 3', 'rating': 7.2, 'genre': 'Drama'}]  # Example data
        create_word_document(movie_info)
        print("Word document created successfully.")

        # Hide progress indicator after task completion
        Clock.schedule_once(self.hide_progress_indicator, 2)

    def exit_app(self, instance):
        App.get_running_app().stop()

    def display_recommendations(self, movie_titles):
        # Display recommended movies to the user
        for movie_title in movie_titles:
            print(movie_title)

    def show_progress_indicator(self):
        self.progress_indicator.opacity = 1

    def hide_progress_indicator(self, dt):
        self.progress_indicator.opacity = 0

class MovieTorrentFinderApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    app = MovieTorrentFinderApp()
    app.run()
