from csv import writer
from os import system, name
import re
import csv
from utilities import return_option, clear


def add_student():  # Function to add a student into the system
    clear()  # Clears the screen
    status = True
    print("\nAdding a new student")  # Title
    while True:
        try:
            while status:
                name = input("Name: ")  # Takes the name as the input
                if return_option(name):
                    return
                # If 1st character is capital and others are alphabets, it will not loop
                if name[0].isupper() and all(x.isalpha() or x.isspace() for x in name):
                    status = False  # Exits the while loop
                else:
                    # If not, the program will prompt the user to input the name again
                    print(
                        "Invalid name! Please try again. \nType 'Quit' to return to main menu")
            while True:
                age = input("Age: ")  # Takes the age as the input
                if return_option(age):
                    return
                age = int(age)
                if age < 0 or age > 100:
                    print(
                        "Invalid age! Please input an age between 0 and 100.\nType 'Quit' to return to main menu")
                else:
                    break
            while status is False:
                # Takes the email address as the input
                email = input("Email: ")
                if return_option(email):
                    return
                valid = re.match(
                    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
                if valid:
                    # If the email address is valid, the program will not loop.
                    status = True
                else:
                    # If the email address is invalid, the program will prompt the user to type it again
                    print(
                        "Invalid email address! Please try again.\nType 'Quit' to return to main menu")
        except ValueError:
            # If the age is not an integer, the user has to type it in again
            print("Invalid input! Please try again. \nType 'Quit' to return to main menu")
        else:
            with open('students.csv') as index_obj:
                csv_reader = csv.reader(index_obj, delimiter=',')
                count = 0
                for row in csv_reader:
                    if count == 1:
                        if row[1] == "":
                            student_id = 20000
                    count += 1
                    student_id = row[1]
            course = ''
            # Creates a variable that puts the name, age and email address into a list
            mix = [count, int(student_id) + 1, name, age, email, course]
            # Opens a file named students.csv in append mode
            with open('students.csv', 'a') as f_object:
                # Defines the file that would be written to
                writer_object = writer(f_object)
                # Writes the student's information to the file
                writer_object.writerow(mix)
            # Message that indicates that the information is added successfully
            print("Added successfully!\n")
            break  # Exits the loop
