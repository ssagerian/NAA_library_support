import openpyxl
import json

def save_to_file(book_data):
    with open("books_seen.json", "w") as file:
        json.dump(book_data, file, indent=2)
    print("Data saved to 'books_seen.json'.")

def read_excel_to_list(file_path, sheet_name, max_rows=None):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the specified sheet by name
    sheet = workbook[sheet_name]

    # Get the header row
    headers = [cell.value for cell in sheet[1]]

    # Initialize the list to store dictionaries
    data_list = []

    # Iterate over rows starting from the second row (index 2)
    for row_number, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
        # Create a dictionary using the headers and current row values
        data_dict = dict(zip(headers, row))
        data_list.append(data_dict)

        # Check if a maximum number of rows is specified and break if reached
        if max_rows is not None and len(data_list) >= max_rows:
            break

        # Check for an empty row (assuming that an empty first cell indicates an empty row)
        if row[0] is None:
            break

    return data_list

if __name__ == "__main__":
    # Replace 'path/to/your/excel/file.xlsx' and 'YOUR_SHEET_NAME' with your actual values
    excel_file_path = 'compiled.xlsx'
    sheet_name = 'Catalog'

    # Specify the maximum number of rows to process (set to None to process all rows)
    max_rows_to_process = 1000

    # Get data from Excel sheet
    excel_data = read_excel_to_list(excel_file_path, sheet_name, max_rows=max_rows_to_process)

    save_to_file(excel_data)

    # Print the resulting list of dictionaries
    print(excel_data)
