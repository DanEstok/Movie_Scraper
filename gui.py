import tkinter as tk
from tkinter import messagebox
import subprocess
import time
from datetime import datetime
import tkinter.ttk as ttk
from imdb_scraper import scrape_imdb_movies, scrape_imdb_movie_info
from piratebay_scraper import search_tpb, is_tpb_running
from utorrent_integration import add_to_utorrent, is_utorrent_running
from subtitle_finder import search_subtitles, download_subtitles
from file_creator import create_excel_spreadsheet, create_word_document

# Initialize Tkinter GUI
root = tk.Tk()
root.title('Movie Torrent Finder')

# Initialize variables
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
]

start_year = tk.StringVar()
end_year = tk.StringVar()
start_year.set(str(datetime.now().year - 5))
end_year.set(str(datetime.now().year))

genre_var = tk.StringVar()
genre_var.set('action')

rating_var = tk.StringVar()
rating_var.set('0')

seeder_entry = tk.Entry(root, width=5)
leecher_entry = tk.Entry(root, width=5)
file_size_entry = tk.Entry(root, width=5)

# Create GUI elements
year_label = tk.Label(root, text='Year Range:', font=('Arial', 12, 'bold'))
start_year_label = tk.Label(root, textvariable=start_year, font=('Arial', 10))
end_year_label = tk.Label(root, textvariable=end_year, font=('Arial', 10))
genre_label = tk.Label(root, text='Genre:', font=('Arial', 12, 'bold'))
rating_label = tk.Label(root, text='Rating:', font=('Arial', 12, 'bold'))
seeder_label = tk.Label(root, text='Min Seeders:', font=('Arial', 12, 'bold'))
leech_label = tk.Label(root, text='Max Leechers:', font=('Arial', 12, 'bold'))
file_size_label = tk.Label(root, text='Max File Size (MB):', font=('Arial', 12, 'bold'))

genre_options = ['action', 'comedy', 'drama', 'horror', 'sci-fi']
genre_dropdown = ttk.Combobox(root, textvariable=genre_var, state='readonly', values=genre_options, font=('Arial', 10))

rating_options = [str(i) for i in range(0, 11)]
rating_dropdown = ttk.Combobox(root, textvariable=rating_var, state='readonly', values=rating_options, font=('Arial', 10))

movie_label = tk.Label(root, text='Movie Title:', font=('Arial', 12, 'bold'))
movie_entry = tk.Entry(root, width=50, font=('Arial', 10))

# Create GUI buttons
search_button = ttk.Button(root, text='Search', command=add_torrents, font=('Arial', 10, 'bold'))
download_subtitle_button = ttk.Button(root, text='Download Subtitles', command=download_subtitles, font=('Arial', 10, 'bold'))
excel_button = ttk.Button(root, text='Create Excel Spreadsheet', command=create_excel_spreadsheet, font=('Arial', 10, 'bold'))
word_button = ttk.Button(root, text='Create Word Document', command=create_word_document, font=('Arial', 10, 'bold'))
exit_button = ttk.Button(root, text='Exit', command=root.quit, font=('Arial', 10, 'bold'))

# Create GUI frames
year_range_frame = tk.Frame(root, padding=(5, 5, 5, 0))
genre_frame = tk.Frame(root, padding=(5, 5, 5, 0))
rating_frame = tk.Frame(root, padding=(5, 5, 5, 0))
seeder_frame = tk.Frame(root, padding=(5, 5, 5, 0))
leecher_frame = tk.Frame(root, padding=(5, 5, 5, 0))
file_size_frame = tk.Frame(root, padding=(5, 5, 5, 0))

# Layout GUI elements
year_label.grid(row=0, column=0, sticky='w')
start_year_label.grid(row=0, column=1, sticky='w')
end_year_label.grid(row=0, column=2, sticky='w')
genre_label.grid(row=1, column=0, sticky='w')
rating_label.grid(row=2, column=0, sticky='w')
seeder_label.grid(row=3, column=0, sticky='w')
leech_label.grid(row=4, column=0, sticky='w')
file_size_label.grid(row=5, column=0, sticky='w')

genre_dropdown.grid(row=1, column=1, sticky='w')
rating_dropdown.grid(row=2, column=1, sticky='w')
seeder_entry.grid(row=3, column=1, sticky='w')
leecher_entry.grid(row=4, column=1, sticky='w')
file_size_entry.grid(row=5, column=1, sticky='w')

movie_label.grid(row=6, column=0, sticky='w')
movie_entry.grid(row=6, column=1, sticky='w')

# Place GUI buttons
search_button.grid(row=7, column=0, sticky='w', padx=5, pady=5)
download_subtitle_button.grid(row=7, column=1, sticky='w', padx=5, pady=5)
excel_button.grid(row=7, column=2, sticky='w', padx=5, pady=5)
word_button.grid(row=7, column=3, sticky='w', padx=5, pady=5)
exit_button.grid(row=7, column=4, sticky='w', padx=5, pady=5)

# Place GUI frames
year_range_frame.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
genre_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
rating_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
seeder_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
leecher_frame.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
file_size_frame.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

root.iconbitmap('path/to/icon.ico')

root.mainloop()