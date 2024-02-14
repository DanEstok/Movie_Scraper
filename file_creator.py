import xlsxwriter
import docx
import logging
import xlwt

# Setup logging
logging.basicConfig(filename='movie_info_log.txt', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def create_excel_spreadsheet(movie_info, file_name='movie_info.xlsx') -> str:
    """
    Creates an Excel spreadsheet with extended movie information.
    
    Parameters:
    - movie_info: List of dictionaries with extended movie details.
    - file_name: Optional; name of the output Excel file.
    
    Returns:
    - Path to the created Excel file or an error message.
    """
    try:
        # Validate input data
        _validate_movie_info(movie_info)

        # Create workbook and worksheet
        workbook = _create_workbook(file_name)
        worksheet = _create_worksheet(workbook)

        # Write headers
        _write_headers(workbook, worksheet, movie_info)

        # Write movie data
        _write_movie_data(worksheet, movie_info)

        # Auto-adjust columns' width
        _auto_adjust_columns_width(worksheet, movie_info)

        workbook.close()
        return f"Excel spreadsheet created successfully: {file_name}"
    except Exception as e:
        logging.error(f"Error creating Excel spreadsheet: {e}")
        return f"An error occurred while creating Excel spreadsheet: {e}"

def _validate_movie_info(movie_info):
    """
    Validates the input movie information.
    
    Parameters:
    - movie_info: List of dictionaries with extended movie details.
    
    Raises:
    - ValueError: If movie_info is not a list of dictionaries.
    """
    if not isinstance(movie_info, list) or not all(isinstance(movie, dict) for movie in movie_info):
        raise ValueError("movie_info must be a list of dictionaries.")

def _create_workbook(file_name):
    """
    Creates a new Excel workbook.
    
    Parameters:
    - file_name: Name of the output Excel file.
    
    Returns:
    - Workbook object.
    """
    return xlsxwriter.Workbook(file_name)

def _create_worksheet(workbook):
    """
    Adds a new worksheet to the Excel workbook.
    
    Parameters:
    - workbook: Workbook object.
    
    Returns:
    - Worksheet object.
    """
    return workbook.add_worksheet()

def _write_headers(workbook, worksheet, movie_info):
    """
    Writes headers to the Excel worksheet.

    Parameters:
    - workbook: Workbook object.
    - worksheet: Worksheet object.
    - movie_info: List of dictionaries with extended movie details.
    """

    # Define cell formatting
    bold = workbook.add_format({'bold': True})

    # Write headers
    headers = movie_info[0].keys()
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header.capitalize(), bold)



def _write_movie_data(worksheet, movie_info):
    """
    Writes the movie data to the worksheet.
    
    Parameters
    - worksheet: Worksheet object.
    - movie_info: List of dictionaries with extended movie details.
    """
    for row_num, movie in enumerate(movie_info, start=1):
        for col_num, (key, value) in enumerate(movie.items()):
            if isinstance(value, list):
                value = ', '.join(value)
            worksheet.write(row_num, col_num, value)


def _auto_adjust_columns_width(worksheet, movie_info):
    """
    Auto-adjusts columns' width based on the longest item in each column.
    
    Parameters
    - worksheet: Worksheet object.
    - movie_info: List of dictionaries with extended movie details.
    """
    headers = movie_info[0].keys()
    for col_num, header in enumerate(headers):
        column_len = max(len((movie.get(header, ''))) for movie in movie_info)
        worksheet.set_column(col_num, col_num, column_len)

if __name__ == "__main__":
    # Define the movie_info variable
    movie_info = [
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "director": "Frank Darabont",
            "cast": ["Tim Robbins", "Morgan Freeman"],
            "genre": ["Crime", "Drama"],
            "rating": 9.3,
            "duration": "142 min"
        },
        {
            "title": "The Godfather",
            "year": 1972,
            "director": "Francis Ford Coppola",
            "cast": ["Marlon Brando", "Al Pacino"],
            "genre": ["Crime", "Drama"],
            "rating": 9.2,
            "duration": "175 min"
        }
    ]

    # Create a new workbook and select the active sheet
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Movie Info')

    # Add a title to the worksheet
    title = "Movie Information"
    title_style = xlwt.XFStyle()
    title_font = xlwt.Font()
    title_font.bold = True
    title_style.font = title_font
    worksheet.write(0, 0, title, title_style)

    # Write the movie data to the worksheet
    _write_movie_data(worksheet, movie_info)

    # Auto-adjust columns' width based on the longest item in each column
    _auto_adjust_columns_width(worksheet, movie_info)

    # Save the workbook
    workbook.save('movie_info.xls')