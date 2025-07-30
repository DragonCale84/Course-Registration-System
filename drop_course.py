import csv
from csv import writer
from os import system, name
from utilities import return_option, clear


def drop_course():
    status = True

    clear()
    print('Drop Course\nEnter "quit" to return to main menu')

    while status is True:
        student_courses = []
        student_found = False
        while True:
            student_id = input("Insert student ID: ")
            if return_option(student_id):
                return
            if len(student_id) == 5:
                with open('students.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        if row[1] == student_id:
                            if len(row) > 5:
                                student_courses = row[5].split(' | ')
                break
            if not student_courses:
                print(
                    "Invalid input! Please try again.\nType 'Quit' to return to main menu")

        print("\nEnrolled Courses:")
        for i, course in enumerate(student_courses):
            print(f"{i + 1}. {course}")

        while True:
            try:
                choice = input(
                    f'Select a course to drop (Enter the number from 1 to {len(student_courses)}): ')
                choice = int(choice)
                if 1 <= choice <= len(student_courses):
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            if return_option(choice):
                return

        dropped_course = student_courses[choice - 1]
        del student_courses[choice - 1]

        updated_courses_string = ' | '.join(student_courses)

        updated_rows = []
        with open('students.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[1] == student_id:
                    if len(row) > 5:
                        row[5] = updated_courses_string
                    else:
                        row.append(updated_courses_string)
                updated_rows.append(row)

        with open('students.csv', 'w', newline='') as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerows(updated_rows)

        remove_enrollment(student_id, dropped_course)
        increase_course_seats(dropped_course)

        print(f"Course '{dropped_course}' dropped successfully.")
        break


def remove_enrollment(student_id, dropped_course):
    count = 0
    updated_enrollments = []
    with open('enrolments.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] != student_id or (row[2] + row[3]) != dropped_course:
                updated_enrollments.append([count, row[1], row[2], row[3], row[4]])
                count += 1

    with open('enrolments.csv', 'w', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerows(updated_enrollments)


def increase_course_seats(dropped_course):
    courselist = []
    with open('courses.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] + row[2] == dropped_course:
                row[4] = str(int(row[4]) + 1)
            courselist.append(row)

    with open('courses.csv', 'w', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerows(courselist)
