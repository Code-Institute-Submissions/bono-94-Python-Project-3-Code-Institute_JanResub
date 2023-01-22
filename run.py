"""
This is a python-based file that executes code for Life Tracker [v.1]
Final code with accompanying files is deployed on the Heroku.
This segment introduces user to the program.
It also discloses rules and requests personal information.
"""
from datetime import datetime
import time
import gspread
from google.oauth2.service_account import Credentials
import inputone
import inputtwo
import inputthree
import inputfour
import resultssubs
import resultstasks

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
    print("- With starting a program, previous cell values will be cleared")
    print("- Your results sheet access: [https://bit.ly/life-tracker-sheet]")
    print("- Next you will be asked to input your daily events per each hour")
    print("- Your data will be exported to an external Google Sheet: tracker")
    print("- Once the data is in, program will retrieve your results")
    print("- Those are noted as daily duration of each category and task")
    print("- Once that is reported to you, it will be exported again")
    print("- This time, to the second Google worksheet: analysis")
    print("- You will be able to see visual analysis of your results. \n")

    time.sleep(10)

    while True:
        rules_input = input("Type in letter x and press enter to continue: \n")

        if validate_rules_data(rules_input):
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
    At the end, user is asked to input the letter x to start the program.
    """
    print("------------------------------------------------------------------")
    print("RULES: \n")
    print("For program to function correctly, respect the instructions \n")
    print("- When asked to input letter x, do not enter any other letters")
    print("- When asked to input letter x, enter only one character \n")
    print("- When inputting subcategories, please follow rules precisely")
    print("- When inputting tasks, please follow rules precisely")
    print("- Do not enter any numbers or symbols, only letters ")
    print("- Only enter values when asked for it")
    print("- Only select sub-categories from provided list of options")
    print("- Tasks are custom by your experience with limit of 40 characters")
    print("- Please do not leave any fields empty")
    print("- Each hour of a day is in 24-hour format \n")

    time.sleep(10)

    while True:
        personal_info_input = input("Please enter letter x to continue: \n")

        if validate_personal_data(personal_info_input):
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
    print("Personal identification: username and ID number.")
    print("- Please try to keep username letters-only")
    print("- Please try to keep ID digits-only.")
    print("- If you did not request ID yet, you can enter any number.")
    print("- Please do not enter any blank spaces. \n")

    time.sleep(5)

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

    time.sleep(5)

    print("------------------------------------------------------------------")

    return id_input


def validate_id_data(values):
    """
    Input validator function.
    Prints error message if ID number contains letters instead of numbers.
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
    Function clears all tasks and subcategories inputs on the analyzer sheet.
    """
    clear_tracker = SHEET.worksheet("tracker")
    clear_analyzer = SHEET.worksheet("analyzer")

    clear_tracker.batch_clear(["B2:B25", "C2:C25"])
    clear_analyzer.batch_clear(["B4:B7", "B10:B13"])
    clear_analyzer.batch_clear(["B16:B19", "B24:B47"])
    clear_analyzer.batch_clear(["A24:A47"])

def input_results_zero():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 00:00 and 01:00? \n")
    print("GROWTH")
    print("- Body System Care")
    print("- Soul & Spirit")
    print("- Fitness")
    print("- Meditation")
    print("PROGRESS")
    print("- Personal Progress")
    print("- Global Progress")
    print("- Education Progress")
    print("- Business Progress")
    print("FREEDOM")
    print("- Adventures")
    print("- Random Activity")
    print("- Rest")
    print("- Break \n")
    print("- Please select one sub-category from the list above")
    print("- Please enter a custom task that best desribes your activity \n")

    while True:
        zero_sub_input = input("Please enter your sub-category here: \n")

        if validate_zero_sub_data(zero_sub_input):
            print("Submission accepted! \n")
            break

    return zero_sub_input


def validate_zero_sub_data(values):
    """
    Input validator function.
    Prints error message if sub-category input doesn't match options.
    """
    subcategories = [
        'Body System Care',
        'Soul & Spirit',
        'Fitness',
        'Meditation',
        'Personal Progress',
        'Global Progress',
        'Education Progress',
        'Business Progress',
        'Adventures',
        'Random Activity',
        'Rest',
        'Break',
    ]

    if values in subcategories:
        return True

    print("Please only enter sub-categories from the list of options. \n")
    return False


def input_task_zero(sub_input_zero):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        zero_task_input = input("Please enter your task here: \n")

        if validate_zero_task_data(zero_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_zero} - {zero_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return zero_task_input


def validate_zero_task_data(values):
    """
    Input validator function.
    Prints error message if task has more than 40 characters.
    Prints error message if task input is a number.
    Prints error message if task contains any numbers.
    """
    if len(values) >= 40:
        print("Please enter tasks with maximum 40 characters. \n")
        return False

    if values.isdigit():
        print("Please do not include any digits in the tasks. \n")
        return False

    if len(values) <= 2:
        print("No input, enter at least 3 letters and try again. \n")
        return False

    return True


def data_uploaded_zero(sub_input_zero, task_input_zero):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_zero = SHEET.worksheet("tracker")

    update_worksheet_zero.update('B2', sub_input_zero)

    update_worksheet_zero.update('C2', task_input_zero.capitalize())

    print("Processing request... \n")
    print("00:00 - 01:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        zero_next_input = input("Please enter letter x to continue: \n")

        if validate_zero_next_data(zero_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return zero_next_input


def validate_zero_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def all_results_uploaded_successfully():
    """
    This function informs user when all results are updated to the sheet.
    It is a communicative transition to results report.
    """
    print("------------------------------------------------------------------")
    print("Updating sheet... \n")

    time.sleep(5)

    print("Upload completed. \n")
    print("Your daily chedule is now successfully updated! \n")

    while True:
        results_sub_input = input("Please enter letter x to acess results: \n")

        if validate_results_sub_data(results_sub_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return results_sub_input


def validate_results_sub_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def count_sub_results_one():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_one = SHEET.worksheet("tracker")
    sub_column_one = retrieve_sub_data_one.col_values(2)
    push_sub_analyzer_one = SHEET.worksheet("analyzer")

    body_system_count = 0
    for item in sub_column_one:
        if item == 'Body System Care':
            body_system_count += 1

    print("------------------------------------------------------------------")
    print("These are your daily subcategories results in hours spent: \n")
    print("GROWTH")
    print(f"Body System Care - [{body_system_count}]")

    push_sub_analyzer_one.update('B4', body_system_count)

    return body_system_count





def run_introduction():
    """
    Runs all introductory functions inside the program.
    """
    introduction()
    rules()
    personal_info_name()
    personal_info_id()
    clear_previous_inputs()


run_introduction()
inputone.run_data_inputs_first()
inputtwo.run_data_inputs_second()
inputthree.run_data_inputs_third()
inputfour.run_data_inputs_fourth()
resultssubs.run_sub_report()
resultstasks.run_task_report_first()
resultstasks.run_task_report_second()
resultstasks.run_task_report_third()
resultstasks.run_task_report_fourth()
resultstasks.run_program_exit()
