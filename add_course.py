from csv import writer
from os import system, name
import csv
from utilities import return_option, clear

status = True


def add_course():  # Function for adding a course
    clear()  # Clears the screen
    print("Adding a new course")
    while True:
        try:
            while status:
                # Takes the course code as an input
                course_code = input("Insert the course code (Example: MAT): ")
                if return_option(course_code):
                    return
                if course_code.isupper() and len(course_code) == 3:
                    break  # Exits the loop
                else:
                    # Loops until the input is valid
                    print(
                        "Invalid input! Please try again.\nType 'Quit' to return to main menu")

            while status:
                # Takes the course number as the input
                course_num = input("Insert the course number: ")
                if return_option(course_num):
                    return
                if course_num.isdigit() and len(course_num) == 4:
                    break  # Exits the loop
                else:
                    # Loops until the input is valid
                    print(
                        "Invalid input! Please try again.\nType 'Quit' to return to main menu")

            while status:
                # Takes the course name as the input from the user
                course_name = input("Insert the full course name: ")
                if return_option(course_name):
                    return
                # Checks to see if it only contains alphabets and first letter is in uppercase
                if course_name[0].isupper() and all(x.isalpha() or x.isdigit() or x.isspace() for x in course_name):
                    break  # Exits the loop
                else:
                    # Loops again until the input is valid
                    print(
                        "Invalid input! Please try again.\nType 'Quit' to return to main menu")

            while status:
                # Takes the course name as the input from the user
                seats = input("Insert the available seats: ")
                if return_option(seats):
                    return
                if seats.isdigit():
                    break
                else:
                    # Loops again until the input is valid
                    print(
                        "Invalid input! Please try again.\nType 'Quit' to return to main menu")

        except ValueError:
            # Loops until the input is valid
            print("Invalid input! Please try again.")
        else:
            with open('courses.csv', 'r+') as index_obj:
                csv_reader = csv.reader(index_obj, delimiter=',')
                count = 0
                for row in csv_reader:
                    count += 1
                # Variable that combines the course name, course number and seats available into a list
                mix = [int(count), course_code, course_num,
                       course_name, int(seats), int(seats)]
             # with open('courses.csv', 'a') as object: #Opens the courses.csv file in append mode
                # Defines the file that will be written to
                writer_object = writer(index_obj)
                writer_object.writerow(mix)  # Writes mix into the file
            print("Added!")  # Statement that shows the user the course is added
            break  # Exits the loop
