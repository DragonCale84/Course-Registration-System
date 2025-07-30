import csv
from csv import writer
import datetime
from os import system, name
from utilities import return_option, clear

def enroll():
    status = True
    findname = False

    clear()  # Clears the screen
    print("Enroll Students")

    while status is True:  # Takes the name and student ID as inputs and validates them with the data in the file
        while True:
            student_name = input("Insert student's name: ")
            if return_option(student_name):
                return
            if student_name[0].isupper() and all(x.isalpha() or x.isspace() for x in student_name):
                break
            else:
                print("Invalid input! Please try again.\nNote: Name has to be capitalised and no numbers allowed\nType 'Quit' to return to main menu")

        while True:
            student_id = input("Insert student ID: ")
            if return_option(student_id):
                return
            if len(student_id) == 5:
                break
            else:
                print(
                    "Invalid input! Please try again.\nType 'Quit' to return to main menu")

        with open('students.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if student_name == row[2] and student_id == row[1]:
                    status = False
                    break
                line_count += 1

        if status is True:  # If the name and student ID cannot be found, the program will loop again
            print(
                "The name and student ID do not match. Please try again. \nType 'Quit' to return to main menu")
            
    multiple_enrolments = True
    while multiple_enrolments:
        print()
        courselist = []
        print("Available Courses:")
        with open('courses.csv') as csv_file:  # Opens the courses file
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:  # The first line will not be printed because it only contains headers
                    courselist.append(row)  # Writes the first line to the list
                    line_count += 1
                else:
                    courselist.append(row)  # Writes subsequent lines to the list
                    print(str(line_count) + '. ' + row[3])
                    line_count += 1

        with open('enrolments.csv', 'r') as index_obj:
            # Takes the index and loops to the latest one
            csv_reader = csv.reader(index_obj, delimiter=',')
            count = 0
            for row in csv_reader:
                count += 1

        while True:
            # Prompts the user to select a course
            choice = input(
                f'Select a course (Insert a number from 1 to {line_count - 1}): ')
            if return_option(choice):
                return
            choice = int(choice)
            if int(choice) <= line_count:
                # Decreases the number of available seats for a course
                courselist[choice][4] = int(courselist[choice][4]) - 1
                if courselist[choice][4] != -1:
                    break
                else:
                    courselist[choice][4] = int(courselist[choice][4]) + 1
                    print("Seats are all taken! Please choose another course. \nType 'Quit' to return to main menu")
            else:
                print("Invalid input! Please try again.")



        print()
        print("Info:")
        # Prints the student's name, course name, course code and course ID)
        print("Name:", student_name, "\nCourse selected:", courselist[choice][3],
            "\nCourse code: ",courselist[choice][1], "\nCourse ID: ",courselist[choice][2])
        print()
        x = datetime.datetime.now()
        # Inserts the details into the 'mix' variable along with the enrolment date
        mix = [int(count), student_id, courselist[choice][1],
            courselist[choice][2], x.strftime("%x")]

        with open('enrolments.csv', 'a') as f_object:  # Opens the enrolments file
            writer_object = csv.writer(f_object)
            writer_object.writerow(mix)  # Writes the data to the enrolments file

        with open('courses.csv', 'w') as f_object:  # Opens the courses file
            writer = csv.writer(f_object, delimiter=',')
            # Overwrites the entire file with amended data
            writer.writerows(courselist)

        update_student_course(student_id, courselist, choice)
        enrol_again = input("Do you wish to make another enrollment?[Y][N]: ")
        if enrol_again.upper() == 'Y': # Checks for quit input from user
            multiple_enrolments = True
        else:
            multiple_enrolments = False




def update_student_course(student_id, courselist, choice):
    updated_row = []
    student_id_found = False

    with open('students.csv', 'r') as file:
        file_reader = csv.reader(file, delimiter=',')
        for row in file_reader:
            if row[1] == student_id:
                student_id_found = True
                if len(row) < 6:
                    row.append("")
                if row[5]:
                    row[5] = row[5] + ' | ' + \
                        courselist[choice][1] + courselist[choice][2]
                else:
                    row[5] = courselist[choice][1] + courselist[choice][2]
            updated_row.append(row)

    if student_id_found:
        with open('students.csv', 'w', newline='') as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerows(updated_row)
        print("Student's enrolled courses updated successfully.")
    else:
        print("Student ID not found in students.csv.")
