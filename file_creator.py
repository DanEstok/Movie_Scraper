import xlsxwriter
import logging
from docx import Document  # Assuming future use for docx functionalities

# Setup logging
logging.basicConfig(filename='movie_info_log.txt', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def create_excel_spreadsheet(movie_info, file_name='movie_info.xlsx', format_type='xlsx') -> str:
    """
    Creates an Excel spreadsheet with extended movie information.
    
    Parameters:
    - movie_info: List of dictionaries with extended movie details.
    - file_name: Optional; name of the output Excel file.
    - format_type: 'xlsx' or 'xls'; specifies the format of the Excel file.
    
    Returns:
    - Path to the created Excel file or an error message.
    """
    try:
        # Validate input data
        _validate_movie_info(movie_info)

        if format_type == 'xlsx':
            workbook = xlsxwriter.Workbook(file_name)
        else:
            raise ValueError("Unsupported format. Please choose 'xlsx'.")
        
        worksheet = workbook.add_worksheet()

        # Write headers
        _write_headers(workbook, worksheet, movie_info)

        # Write movie data
        _write_movie_data(worksheet, movie_info)

        # Apply conditional formatting
        _apply_conditional_formatting(workbook, worksheet, movie_info)

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

def _write_headers(workbook, worksheet, movie_info):
    # Implementation remains the same

def _write_movie_data(worksheet, movie_info):
    """
    Writes movie data to the specified worksheet.

    Parameters:
    - worksheet: xlsxwriter Worksheet object.
    - movie_info: List of dictionaries with movie details.
    """
    row = 1
    for movie in movie_info:
        for col, value in enumerate(movie.values()):
            worksheet.write(row, col, value)
        row += 1

def _apply_conditional_formatting(workbook, worksheet, movie_info):
    """
    Applies conditional formatting to the 'rating' column to highlight high-rated movies.

    Parameters:
    - workbook: xlsxwriter Workbook object.
    - worksheet: xlsxwriter Worksheet object.
    - movie_info: List of dictionaries with movie details.
    """
    rating_column = None
    for idx, key in enumerate(movie_info[0].keys()):
        if key == 'rating':
            rating_column = idx
            break

    if rating_column is not None:
        # Apply conditional formatting to highlight ratings >= 8.0
        worksheet.conditional_format(1, rating_column, len(movie_info), rating_column, {
            'type': 'cell',
            'criteria': '>=',
            'value': 8.0,
            'format': workbook.add_format({'bg_color': '#FFEB9C', 'font_color': '#9C6500'})
        })

def _auto_adjust_columns_width(worksheet, movie_info):
    """
    Automatically adjusts the columns' width based on the content.

    Parameters:
    - worksheet: xlsxwriter Worksheet object.
    - movie_info: List of dictionaries with movie details.
    """
    for col in range(len(movie_info[0])):
        max_length = 0
        for row in range(len(movie_info)):
            if len(str(movie_info[row][col])) > max_length:
                max_length = len(str(movie_info[row][col]))
        worksheet.set_column(col, col, max_length)

# Note: The rest of the helper functions `_create_worksheet`, `_write_movie_data`, and `_auto_adjust_columns_width`
# should be updated accordingly if their implementations were not fully provided here.
