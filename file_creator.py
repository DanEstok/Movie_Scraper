import xlsxwriter
import docx

def create_excel_spreadsheet(movie_info):
    try:
        # Create an Excel spreadsheet using the provided movie info data
        # Example:
        workbook = xlsxwriter.Workbook('movie_info.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0
        for movie in movie_info:
            worksheet.write(row, col, movie['title'])
            worksheet.write(row, col + 1, movie['rating'])
            worksheet.write(row, col + 2, movie['genre'])
            row += 1
        workbook.close()
        print("Excel spreadsheet created successfully.")
    except Exception as e:
        print(f"An error occurred while creating Excel spreadsheet: {e}")

def create_word_document(movie_info):
    try:
        # Create a Word document using the provided movie info data
        # Example:
        doc = docx.Document()
        for movie in movie_info:
            doc.add_paragraph(f"Title: {movie['title']}, Rating: {movie['rating']}, Genre: {movie['genre']}")
        doc.save('movie_info.docx')
        print("Word document created successfully.")
    except Exception as e:
        print(f"An error occurred while creating Word document: {e}")
