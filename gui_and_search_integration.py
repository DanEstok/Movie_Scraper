from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from torrent_scrapers import ScraperAggregator

class TorrentSearchApp(App):
    def build(self):
        self.aggregator = ScraperAggregator()
        layout = BoxLayout(orientation='vertical')
        self.query_input = TextInput(size_hint_y=None, height='30dp', hint_text='Enter search query')
        search_button = Button(text='Search', size_hint_y=None, height='50dp')
        search_button.bind(on_press=self.perform_search)
        layout.add_widget(self.query_input)
        layout.add_widget(search_button)
        return layout

    def perform_search(self, instance):
        query = self.query_input.text
        results = self.aggregator.search_all(query)
        # Display results in a new popup or another preferred UI element
        results_label = Label(text=str(results))
        popup = Popup(title='Search Results', content=results_label)
        popup.open()

if __name__ == '__main__':
    TorrentSearchApp().run()
