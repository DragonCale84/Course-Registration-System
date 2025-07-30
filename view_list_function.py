import csv
from edit_list_function import confirm_edit
from utilities import clear
"""
 This function outputs the file selected into a table
"""


def table_view(filename):
    clear()
    columns, headers, data = view_List(filename)

    formated_headers = []
# This segment calculates the max width of each column
    max_width_of_column = []
    for column in columns:  # Iterates between columns
        max_value = 0
        for i in column:  # Iterates between data within the columns
            if len(i) > max_value:  # Tests if the data is larger than max value
                max_value = len(i)  # Updates the max width of data
        # Adds the max data width of each column into a list
        max_width_of_column.append(max_value)

# This segment produces the formatted header of the table
    # Combines the header with its respective max width
    header_with_width = zip(headers, max_width_of_column)
    for header, width in header_with_width:  # Iterates between headers
        # Produces the format and adds it into the list
        formated_headers.append(header.ljust(width))
    header_row = " | ".join(formated_headers)  # Combines columns
    print(header_row)
    print("-" * len(header_row))

# This segment produces the formatted data of the table
    for row in data:  # Iterates between each row of data
        formated_row = []  # Reset the formatted_row list for each row
        # Combines the row with its respective max width
        for item, width in zip(row, max_width_of_column):
            # Iterates between the two elements into item[] and width[]
            formated_row.append(item.ljust(width))
        # Produces the format and adds it into the list
        data_row = " | ".join(formated_row)
        print(data_row)
    print("-" * len(data_row))

    confirm_edit(headers, data, filename)

# This segment reads the file and segregates it into headers,data and columns


def view_List(filename):
    clear()
    try:
        with open(f'{filename}', 'r') as file:
            fileReader = csv.reader(file)
            # Reads the first row of values into headers
            headers = next(fileReader)
            data_in_file = list(fileReader)  # Read the remaining row
            # Combine each element into a column instead of a row
            columns = list(zip(headers, *data_in_file))
            return columns, headers, data_in_file
    except FileNotFoundError:  # Handles if File Not Found Error
        print("Error! File not found")
