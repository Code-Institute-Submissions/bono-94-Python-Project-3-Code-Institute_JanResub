"""
This is a python-based file that executes code for Life Tracker [v.1]
Final code with accompanying files is deployed on the Heroku.
"""
from datetime import datetime
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('life_tracker')


def introduction():
    """
    This introduction welcomes users to the program.
    First, user is presented with current date and time.
    Then a short welcome message followed by explanation of next steps.
    Once user has finished reading section of how program works,
    input of letter x sends user to rules section.
    """
    print("----------------------------------------------------------------")
    live_timestamp = datetime.now()
    print(live_timestamp)
    print("Welcome to the ultimate Life Tracker! (Daily Tasklist)! [v.1] \n")
    print("The program synchronizes your daily journal with schedule. \n")
    print("HOW IT WORKS? \n")
    print("- Following the introduction, you will proceed to rules section")
    print("- After that, you will be asked to enter personal identification")
    print("- When starting a program, previous cell values will be cleared")
    print("- Your inputs and results can be found on Google Sheet below:")
    print("- [LINK]")
    print("- You will be asked to input your daily events per each hour")
    print("- Your data will be exported to the worksheet: tracker")
    print("- You can see visual analysis on the worksheet: analysis \n")

    while True:
        rules_input = input("Type in letter x and press enter to continue: \n")

        if validate_rules_data(rules_input):
            print("")
            print("Loading...")
            break
    print("------------------------------------------------------------------")

    return rules_input


def validate_rules_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid letter, please type letter x then and try again. \n")
        return False

    return True


def rules():
    """
    Rules section allows users to get familiar with important rules.
    At the end, user is asked to input the letter x to start identification.
    """
    print("------------------------------------------------------------------")
    print("RULES: \n")
    print("- Each hour of a day is in 24-hour format \n")
    print("For program to function correctly, respect the instructions \n")
    print("- When asked to input letter x, do not enter any other letters")
    print("- When asked to input letter x, enter only one character \n")
    print("- When inputting subcategories, please follow rules precisely")
    print("- Only enter values when asked for it")
    print("- Select subcategories number from provided list of options \n")
    print("- When inputting tasks, please follow rules precisely")
    print("- Only enter values when asked for it")
    print("- Do not enter numbers or symbols, only letters for top experience")
    print("- Tasks are custom by your experience with limit of 40 characters")
    print("- Please do not leave any fields empty \n")

    while True:
        personal_info_input = input("Please enter letter x to continue: \n")

        if validate_personal_data(personal_info_input):
            print("")
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return personal_info_input


def validate_personal_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def personal_info_name():
    """
    This function requests user to enter their username.
    """
    print("------------------------------------------------------------------")
    print("PERSONAL IDENTIFICATION: username and ID number.")
    print("- Please try to keep username letters-only")
    print("- Please try to keep ID number to digits-only.")
    print("- If you did not request ID yet, you can enter any number.")
    print("- Please do not enter any blank spaces. \n")

    while True:
        name_input = input("Please enter your username: \n")

        if validate_name_data(name_input):
            print(f"Thank you {name_input.capitalize()}! \n")
            break

    return name_input


def validate_name_data(values):
    """
    Input validator function.
    Prints error message if name is a number instead of letters.
    Prints error message if name is longer than 50 characters.
    Prints error message if name has no input of min 1 characters.
    """
    if len(values) >= 50:
        print("Too many letters, enter name under 50 letters. \n")
        return False

    if len(values) <= 0:
        print("No input, enter name with above 1 letter and try again. \n")
        return False

    if values.isdigit():
        print("Please use letters, not numbers. \n")
        return False

    return True


def personal_info_id():
    """
    This function requests user to enter their unique identification number.
    Also, it prints the verified input back so user can know it was successful.
    """
    while True:

        id_input = input("Please enter unique identification number: \n")

        if validate_id_data(id_input):
            print(f"Thank you, your ID number {id_input} is valid! \n")
            break

    print("Starting the program...")
    print("------------------------------------------------------------------")

    return id_input


def validate_id_data(values):
    """
    Input validator function.
    Prints error message if ID number is letters-only instead of numbers.
    Prints error message if ID number input doesn't have at least 1 character.
    """
    if values.isalpha():
        print("Invalid ID number, please only use numbers \n")
        return False

    if len(values) <= 0:
        print("No input, enter number with at least 1 digit and try again. \n")
        return False

    return True


def clear_previous_inputs():
    """
    Function clears all tasks and subcategories inputs on the tracker sheet.
    """
    clear_tracker = SHEET.worksheet("tracker")
    clear_tracker.batch_clear(["B2:B25", "C2:C25"])


def all_inputs():
    """
    Function that loops all subcategories and tasks inputs for all hours.
    After both inputs, subcategories get renamed.
    Both inputs get pushed to tracker worksheet before looping again.
    """
    for hour in range(0, 24):
        sub = input_subcategory(hour)
        task = task_input()
        sub_name = subcategory_rename(sub)
        data_uploader(sub_name, task, hour)


def input_subcategory(hour):
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    hour_end = hour + 1

    print(f"What have you done today between {hour}:00 and {hour_end}:00? \n")
    print("- Please select one sub-category from the list below: \n")
    print("GROWTH")
    print("1) Body System Care")
    print("2) Soul & Spirit")
    print("3) Fitness")
    print("4) Meditation")
    print("PROGRESS")
    print("5) Personal Progress")
    print("6) Global Progress")
    print("7) Education Progress")
    print("8) Business Progress")
    print("FREEDOM")
    print("9) Adventures")
    print("10) Random Activity")
    print("11) Rest")
    print("12) Break \n")

    while True:
        sub_input = input("Please enter the number of sub-category here: \n")

        if validate_sub_data(sub_input):
            print("")
            print("Submission accepted!")
            break

    print("------------------------------------------------------------------")

    return sub_input


def validate_sub_data(values):
    """
    Input validator function.
    Prints error message if sub-category input doesn't match given numbers.
    """
    subcategories = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
    ]

    if values in subcategories:
        return True
    else:
        print("Please enter sub-categories number from list of options. \n")
        return False


def task_input():
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    """
    while True:
        task_input = input("Please enter your task here: \n")

        if validate_task_input(task_input):
            print("")
            print("Submission accepted!")
            break

    print("------------------------------------------------------------------")

    return task_input


def validate_task_input(values):
    """
    Input validator function.
    Prints error message if task has more than 40 characters.
    Prints error message if task input is a number.
    Prints error message if task has less than 3 letters.
    """
    if len(values) >= 40:
        print("Please enter tasks with maximum 40 characters. \n")
        return False

    if values.isdigit():
        print("Please do not include numbers in the tasks. \n")
        return False

    if len(values) <= 2:
        print("Failed input, enter at least 3 letters and try again. \n")
        return False

    return True


def subcategory_rename(sub):
    """
    Subcategories input renaming function.
    Converts number input to specific linked option from list of options.
    """
    if sub == '1':
        return 'Body System Care'
    if sub == '2':
        return 'Soul & Spirit'
    if sub == '3':
        return 'Fitness'
    if sub == '4':
        return 'Meditation'
    if sub == '5':
        return 'Personal Progress'
    if sub == '6':
        return 'Global Progress'
    if sub == '7':
        return 'Education Progress'
    if sub == '8':
        return 'Business Progress'
    if sub == '9':
        return 'Adventures'
    if sub == '10':
        return 'Random Activity'
    if sub == '11':
        return 'Rest'
    if sub == '12':
        return 'Break'


def data_uploader(sub_name, task, hour):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    hour_end = hour + 1

    update_worksheet = SHEET.worksheet("tracker")
    update_worksheet.update(f"B{hour+2}", sub_name)
    update_worksheet.update(f"C{hour+2}", task.capitalize())

    print("Processing request... \n")
    print(f"{hour}:00 - {hour_end}:00 hour has been successfully uploaded! \n")
    print(f"Your input was: {sub_name} - {task.capitalize()} \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        next_input = input("Please enter letter x to continue: \n")

        if validate_next_input(next_input):
            print("")
            print("Loading...")
            break

    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")

    return next_input


def validate_next_input(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def all_results_uploaded():
    """
    This function informs user when all results are updated to the sheet.
    It is a communicative transition to results report.
    """
    print("Updating sheet... \n")
    print("Upload completed. \n")
    print("Your daily schedule is now successfully updated! \n")

    while True:
        all_results_input = input("Please enter letter x to get results: \n")

        if validate_all_results(all_results_input):
            print("")
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return all_results_input


def validate_all_results(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def export_results_analyzer():
    """
    User is informed that all reporting and uploading is complete.
    User is infromed on date and time of completion.
    Users receives again a final link to their sheet.
    Users can see outro messages.
    Input of letter x leads user to the sequence of exiting the program.
    """
    print("------------------------------------------------------------------")
    live_timestamp = datetime.now()
    print(f"{live_timestamp} \n")
    print("Daily results have been successfully sent to analyzer sheet. \n")
    print("Now you can access your detailed visual analysis. \n")
    print("Please follow this link: [https://bit.ly/life-tracker-sheet] \n")
    print("Thank you for participating. \n")
    print("See you tomorrow at the next tracking and analyzing mission! \n")
    print("After exiting program, you can press 'RUN PROGRAM' to restart \n")

    while True:
        exit_input = input("Please enter letter x to exit: \n")

        if validate_exit_input(exit_input):
            print("")
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return exit_input


def validate_exit_input(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def exit_screen():
    """
    Informs the user that exit sequence is initiated.
    Countdown of 10 seconds ends with exit message.
    Function raises SystemExit to leave the program.
    """
    print("------------------------------------------------------------------")
    print("Initiating Exit Sequence... \n")

    print("Loading... \n")

    countdown = 10

    while countdown >= 0:
        print(f"{countdown} seconds...")
        countdown -= 1
        time.sleep(1)

    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")

    raise SystemExit("Exiting...")


def run_program():
    """
    Runs all functions inside the program in correct order.
    """
    introduction()
    rules()
    personal_info_name()
    personal_info_id()
    clear_previous_inputs()
    all_inputs()
    all_results_uploaded()
    export_results_analyzer()
    exit_screen()


run_program()
