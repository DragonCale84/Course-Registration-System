import os
import add_student
import enrol_student
import add_course
import drop_course
from view_list_function import table_view
from utilities import clear

should_exit = False
'''
def drop_course_m1():
  delete_row_from_db(seats=50) #just added this to assign a seat variable (can remove this comment later)
'''
# def pause():
#  os.system("pause")

def pause():
    i = input()

while not should_exit:
    clear()
    print("\n    French Fries Software Solutions co. unlimited presents:")
    print("""
   _____                            _____            _     _             _   _             
  / ____|                          |  __ \\          (_)   | |           | | (_)            
 | |     ___  _   _ _ __ ___  ___  | |__) |___  __ _ _ ___| |_ _ __ __ _| |_ _  ___  _ __  
 | |    / _ \\| | | | '__/ __|/ _ \\ |  _  // _ \\/ _` | / __| __| '__/ _` | __| |/ _ \\| '_ \\ 
 | |___| (_) | |_| | |  \\__ \\  __/ | | \\ \\  __/ (_| | \\__ \\ |_| | | (_| | |_| | (_) | | | |
  \\_____\\___/ \\__,_|_|  |___/\\___| |_|  \\_\\___|\\__, |_|___/\\__|_|  \\__,_|\\__|_|\\___/|_| |_|
  / ____|         | |                           __/ |                                      
 | (___  _   _ ___| |_ ___ _ __ ___            |___/                                       
  \\___ \\| | | / __| __/ _ \\ '_ ` _ \\                                                       
  ____) | |_| \\__ \\ ||  __/ | | | | |                                                      
 |_____/ \\__, |___/\\__\\___|_| |_| |_|                                                      
          __/ |                                                                            
         |___/  
""")

    print("""\n  +----------- Main Menu -----------------+
  |                                       |
  | Select one of these options:          |
  |  1 - Add a New Student                |
  |  2 - Add a New Course                 |
  |  3 - Enrol a Student In a Course      |
  |  4 - Drop a Course                    |
  |  5 - View or Edit Available Courses   |
  |  6 - View or Edit Student Information |
  |  7 - View or Edit Enrollment History. |
  |  8 - Exit                             |
  +---------------------------------------+
  """)
    try:
        c = int(input(">  "))
    except ValueError:
        print("The input wasn't a whole number!\n")
    else:
        match c:
            case 1:
                add_student.add_student()
                print("Press Enter to return to Main Menu")
                pause()
            case 2:
                add_course.add_course()
                print("Press Enter to return to Main Menu")
                pause()
            case 3:
                enrol_student.enroll()
                print("Press Enter to return to Main Menu")
                pause()
            case 4:
                drop_course.drop_course()
                print("Press Enter to return to Main Menu")
                pause()
            case 5:
                table_view('courses.csv')
                print("Press Enter to return to Main Menu")
                pause()
            case 6:
                table_view('students.csv')
                print("Press Enter to return to Main Menu")
                pause()
            case 7:
                table_view('enrolments.csv')
                print("Press Enter to return to Main Menu")
                pause()
            case 8:
                print("Exiting program...")
                should_exit = True
            case 9:
                pass
            case _:
                print(
                    "The number given doesn't match any of the actions listed, please type a number between 1 - 8"
                )
