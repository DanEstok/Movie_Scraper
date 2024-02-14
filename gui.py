import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.filechooser import FileChooserIconView

# Setup logging
logging.basicConfig(filename='/mnt/data/movie_info_log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class MovieTorrentDownloaderApp(App):
    save_directory = '/mnt/data/'  # Default save directory

    def build(self):
        self.root_layout = BoxLayout(orientation='vertical')
        self.setup_header()
        self.setup_content_area()
        self.setup_footer()
        return self.root_layout

    def setup_header(self):
        header_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp')
        logo_image = Image(source='logo.png', size_hint_x=None, width='50dp')
        title_label = Label(text='Movie Torrent Downloader', font_size='20sp', bold=True, size_hint_x=None, width=200)
        header_layout.add_widget(logo_image)
        header_layout.add_widget(title_label)
        self.root_layout.add_widget(header_layout)

    def setup_content_area(self):
        content_layout = BoxLayout(orientation='vertical', padding='10dp')
        self.setup_search_bar(content_layout)
        self.setup_movie_list(content_layout)
        self.root_layout.add_widget(content_layout)

    def setup_search_bar(self, parent_layout):
        search_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp')
        self.search_input = TextInput(hint_text='Search for movies...', multiline=False, size_hint_x=0.8)
        search_button = Button(text='Search')
        search_button.bind(on_release=self.search_movies)
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_button)
        parent_layout.add_widget(search_layout)

    def setup_movie_list(self, parent_layout):
        self.movie_grid = GridLayout(cols=3, spacing='10dp', size_hint_y=None, row_default_height='100dp', padding='10dp')
        movie_scrollview = ScrollView()
        movie_scrollview.add_widget(self.movie_grid)
        parent_layout.add_widget(movie_scrollview)

    def setup_footer(self):
        footer_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', spacing='10dp')
        save_location_button = Button(text='Set Save Location')
        save_location_button.bind(on_release=self.open_file_chooser)
        footer_layout.add_widget(save_location_button)
        self.root_layout.add_widget(footer_layout)

    def open_file_chooser(self, instance):
        filechooser = FileChooserIconView()
        popup = Popup(title="Choose Save Directory", content=filechooser, size_hint=(0.9, 0.9))
        filechooser.bind(on_selection=lambda x: self.set_save_directory(filechooser.selection, popup))
        popup.open()

    def set_save_directory(self, selection, popup):
        if selection:
            self.save_directory = selection[0]
            logging.info(f'Save directory set to: {self.save_directory}')
        popup.dismiss()

    def search_movies(self, instance):
        query = self.search_input.text
        # Placeholder for movie search functionality

    def download_selected_movies(self, instance):
        # Placeholder for downloading selected movies functionality

        def show_error_popup(self, message):
            popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
            popup.open()

    def notify_user_about_update(self, update_callback):
        content = BoxLayout(orientation='vertical')
        message = Label(text='An update is available. Do you want to install it now?')
        content.add_widget(message)

        button_layout = BoxLayout(size_hint_y=None, height='50dp')
        yes_button = Button(text='Yes')
        no_button = Button(text='No')

        def on_yes(instance):
            update_callback()
            popup.dismiss()

        def on_no(instance):
            popup.dismiss()

        yes_button.bind(on_release=on_yes)
        no_button.bind(on_release=on_no)

        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        content.add_widget(button_layout)

        popup = Popup(title='Update Available', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    MovieTorrentDownloaderApp().run()
