from os import system, name



# This function allows user to return to the main menu when in the middle of a function

def return_option(user_input):
    if user_input.upper() == 'QUIT': # Checks for quit input from user
        confirm = input("Are you sure you want to return to the menu? [Y/N]: ") # Confirmation message
        if confirm.upper() == 'Y': 
            print()
            print("Program exited successfully.")
            return True # Returns true so when exiting the function, it will execute return
        else:
            return
    else:
        return


def clear(): #defines out clear function
  # for windows
  if name == 'nt':
    _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')