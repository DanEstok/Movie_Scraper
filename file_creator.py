import xlsxwriter
import docx
import logging
from typing import List, Dict

# Setup logging
logging.basicConfig(filename='/mnt/data/movie_info_log.txt', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def validate_movie_info(movie_info: List[Dict]) -> None:
    """
    Validate the input movie information.

    Parameters:
    - movie_info: List of dictionaries with extended movie details.

    Raises:
    - ValueError: If movie_info is not a list of dictionaries or if any dictionary is missing required keys.
    """
    if not isinstance(movie_info, list) or not all(isinstance(movie, dict) for movie in movie_info):
        raise ValueError("movie_info must be a list of dictionaries.")
    required_keys = {'title_name'}
    for movie in movie_info:
        if not required_keys.issubset(movie.keys()):
            raise ValueError(f"Each movie dictionary must contain at least the following keys: {required_keys}")

def create_excel_spreadsheet(movie_info: List[Dict], file_name: str = 'movie_info.xlsx') -> str:
    """
    Creates an Excel spreadsheet with extended movie information.
    
    Parameters:
    - movie_info: List of dictionaries with extended movie details.
    - file_name: Optional; name of the output Excel file.
    
    Returns:
    - Path to the created Excel file or an error message.
    """
    try:
        validate_movie_info(movie_info)

        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})

        headers = movie_info[0].keys()
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header.capitalize(), bold)

        for row_num, movie in enumerate(movie_info, start=1):
            for col_num, (key, value) in enumerate(movie.items()):
                if isinstance(value, list):
                    value = ', '.join(value)
                worksheet.write(row_num, col_num, value)

        for col_num, header in enumerate(headers):
            column_len = max(len(str(movie.get(header, ''))) for movie in movie_info)
            column_len = max(column_len, len(header))
            worksheet.set_column(col_num, col_num, column_len + 1)

        workbook.close()
        return f"Excel spreadsheet created successfully: {file_name}"
    except Exception as e:
        logging.error(f"Error creating Excel spreadsheet: {e}")
        return f"An error occurred while creating Excel spreadsheet: {e}"

def create_word_document(movie_info: List[Dict], file_name: str = 'movie_info.docx') -> str:
    """
    Creates a Word document with extended movie information.
    
    Parameters:
    - movie_info: List of dictionaries with extended movie details.
    - file_name: Optional; name of the output Word file.
    
    Returns:
    - Path to the created Word file or an error message.
    """
    try:
        validate_movie_info(movie_info)

        doc = docx.Document()
        doc.add_heading('Movie Information', 0)

        for movie in movie_info:
            doc.add_heading(movie.get('title_name', 'N/A'), level=1)
            movie_table = doc.add_table(rows=1, cols=2)
            movie_table.style = 'Table Grid'
            hdr_cells = movie_table.rows[0].cells
            hdr_cells[0].text = 'Category'
            hdr_cells[1].text = 'Details'
            for key, value in movie.items():
                if key != 'title_name':
                    row_cells = movie_table.add_row().cells
                    row_cells[0].text = key.replace('_', ' ').capitalize()
                    row_cells[1].text = ', '.join(value) if isinstance(value, list) else str(value)

        doc.save(file_name)
        return f"Word document created successfully: {file_name}"
    except Exception as e:
        logging.error(f"Error creating Word document: {e}")
        return f"An error occurred while creating Word document: {e}"
