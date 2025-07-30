import csv
from utilities import return_option

"""
This function creates an option for the user to edit the data.
"""


def confirm_edit(headers, data, filename):
    # This segment provides user the option to make changes or not
    inputcheck = True
    try:
        while inputcheck:
            changes = input("Do you wish to make changes to the data?[Y][N]: ")
            if changes.upper() == 'Y':  # If yes, it runs the edit list function
                edit_list(headers, data, filename)
                inputcheck = False
            elif changes.upper() == 'N':  # If no, it returns the user to the main menu
                print()
                print("Returning to main menu...")
                inputcheck = False
            else:
                print("Please enter either Y or N")
    except ValueError:
        print("Please input either Y or N")


"""
This function allows the user to select the data they wish to edit by selecting the row
and column. The user is also able to type 'quit' to return to the main menu. It then
asks the user to inout the new data they wish to replace the old one. The program uses
that input and writes it into the selected csv file.
"""


def edit_list(header, data, file_name):
    # This segment receives the users input of the row they wish to edit
    try:
        status = True
        while status:
            try:
                row_input = input(
                    "Please enter the row number of the data you wish to edit (or enter 'Quit' to exit): ")
                # Runs the quit function and returns True if user inputs quit
                if return_option(row_input):
                    return
                row_index = int(row_input)
                # Ensures that the row selected exists
                if row_index <= 0 or row_index > len(data):
                    print(
                        f"Error! Please input a column number between 1 and {len(data)}")
                    print()
                else:
                    # Prints the row index selected
                    print(f"Row number selected: {row_index}")
                    status = False
            except ValueError:  # Catches invalid inputs
                print("Invalid input! Please enter an integer")
        # Outputs the available columns
        print()
        count = 1
        print("Available Columns: ")
        for i in header[1:]:
            print(f"{count}. {i}")
            count += 1
        print()
        # Accepts the users column
        status2 = True
        while status2 == True:
            try:
                column_input = input(
                    "Please enter the column number of the data you wish to edit (or enter 'Quit' to exit): ")
                # Provides user the option to quit
                # Runs the quit function and returns True if user inputs quit
                if return_option(column_input):
                    return
                # Converts the input into int data type for comparison
                column_index = int(column_input)
                # Ensures the column selected exists
                if column_index <= 0 or column_index > len(header):
                    print("Error! Please enter a column that exists")
                else:
                    print(f"Column selected: {header[column_index]}")
                    status2 = False
            except ValueError:
                print("Invalid input! Please enter an integer")

        # Outputs the selected data
        print(f"You have selected: {data[row_index - 1][column_index]}")
        print()
        new_value = input(f"Please enter the new value: ")
        data[row_index - 1][column_index] = new_value

        with open(f'{file_name}', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)  # Writing the new data

            print("\nData updated successfully!")
            print(f"\nUpdated Data: {new_value}")

    except Exception as e:  # A fail safe to catch any unexpected errors and output it
        print(f"An error occurred: {e}")
