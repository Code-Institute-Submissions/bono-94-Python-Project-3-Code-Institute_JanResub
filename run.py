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


def run_introduction():
    """
    Runs all introductory functions inside the program.
    """
    introduction()
    rules()
    personal_info_name()
    personal_info_id()
    clear_previous_inputs()


def run_data_inputs_first():
    """
    Runs first quarter of input functions inside the program.
    """
    sub_input_zero = input_results_zero()
    task_input_zero = input_task_zero(sub_input_zero)
    data_uploaded_zero(sub_input_zero, task_input_zero)
    sub_input_one = input_results_one()
    task_input_one = input_task_one(sub_input_one)
    data_uploaded_one(sub_input_one, task_input_one)
    sub_input_two = input_results_two()
    task_input_two = input_task_two(sub_input_two)
    data_uploaded_two(sub_input_two, task_input_two)
    sub_input_three = input_results_three()
    task_input_three = input_task_three(sub_input_three)
    data_uploaded_three(sub_input_three, task_input_three)
    sub_input_four = input_results_four()
    task_input_four = input_task_four(sub_input_four)
    data_uploaded_four(sub_input_four, task_input_four)
    sub_input_five = input_results_five()
    task_input_five = input_task_five(sub_input_five)
    data_uploaded_five(sub_input_five, task_input_five)


def run_data_inputs_second():
    """
    Runs second quarter of input functions inside the program.
    """
    sub_input_six = input_results_six()
    task_input_six = input_task_six(sub_input_six)
    data_uploaded_six(sub_input_six, task_input_six)
    sub_input_seven = input_results_seven()
    task_input_seven = input_task_seven(sub_input_seven)
    data_uploaded_seven(sub_input_seven, task_input_seven)
    sub_input_eight = input_results_eight()
    task_input_eight = input_task_eight(sub_input_eight)
    data_uploaded_eight(sub_input_eight, task_input_eight)
    sub_input_nine = input_results_nine()
    task_input_nine = input_task_nine(sub_input_nine)
    data_uploaded_nine(sub_input_nine, task_input_nine)
    sub_input_ten = input_results_ten()
    task_input_ten = input_task_ten(sub_input_ten)
    data_uploaded_ten(sub_input_ten, task_input_ten)
    sub_input_eleven = input_results_eleven()
    task_input_eleven = input_task_eleven(sub_input_eleven)
    data_uploaded_eleven(sub_input_eleven, task_input_eleven)


def run_data_inputs_third():
    """
    Runs third quarter of input functions inside the program.
    """
    sub_input_twelve = input_results_twelve()
    task_input_twelve = input_task_twelve(sub_input_twelve)
    data_uploaded_twelve(sub_input_twelve, task_input_twelve)
    sub_input_thirteen = input_results_thirteen()
    task_input_thirteen = input_task_thirteen(sub_input_thirteen)
    data_uploaded_thirteen(sub_input_thirteen, task_input_thirteen)
    sub_input_fourteen = input_results_fourteen()
    task_input_fourteen = input_task_fourteen(sub_input_fourteen)
    data_uploaded_fourteen(sub_input_fourteen, task_input_fourteen)
    sub_input_fifteen = input_results_fifteen()
    task_input_fifteen = input_task_fifteen(sub_input_fifteen)
    data_uploaded_fifteen(sub_input_fifteen, task_input_fifteen)
    sub_input_sixteen = input_results_sixteen()
    task_input_sixteen = input_task_sixteen(sub_input_sixteen)
    data_uploaded_sixteen(sub_input_sixteen, task_input_sixteen)
    sub_input_seventeen = input_results_seventeen()
    task_input_seventeen = input_task_seventeen(sub_input_seventeen)
    data_uploaded_seventeen(sub_input_seventeen, task_input_seventeen)


def run_data_inputs_fourth():
    """
    Runs fourth quarter of input functions inside the program.
    """
    sub_input_eighteen = input_results_eighteen()
    task_input_eighteen = input_task_eighteen(sub_input_eighteen)
    data_uploaded_eighteen(sub_input_eighteen, task_input_eighteen)
    sub_input_nineteen = input_results_nineteen()
    task_input_nineteen = input_task_nineteen(sub_input_nineteen)
    data_uploaded_nineteen(sub_input_nineteen, task_input_nineteen)
    sub_input_twenty = input_results_twenty()
    task_input_twenty = input_task_twenty(sub_input_twenty)
    data_uploaded_twenty(sub_input_twenty, task_input_twenty)
    sub_input_twentyone = input_results_twentyone()
    task_input_twentyone = input_task_twentyone(sub_input_twentyone)
    data_uploaded_twentyone(sub_input_twentyone, task_input_twentyone)
    sub_input_twentytwo = input_results_twentytwo()
    task_input_twentytwo = input_task_twentytwo(sub_input_twentytwo)
    data_uploaded_twentytwo(sub_input_twentytwo, task_input_twentytwo)
    sub_input_twentythree = input_results_twentythree()
    task_input_twthree = input_task_twentythree(sub_input_twentythree)
    data_uploaded_twentythree(sub_input_twentythree, task_input_twthree)


def run_sub_report():
    """
    Runs all the subcategories functions that count and report results.
    """
    all_results_uploaded_successfully()
    count_sub_results_one()
    count_sub_results_two()
    count_sub_results_three()
    count_sub_results_four()
    count_sub_results_five()
    count_sub_results_six()
    count_sub_results_seven()
    count_sub_results_eight()
    count_sub_results_nine()
    count_sub_results_ten()
    count_sub_results_eleven()
    count_sub_results_twelve()
    report_continue()


def run_task_report_first():
    """
    Runs first quarter of tasks functions that count and report results.
    """
    get_task_data_first = SHEET.worksheet('tracker')
    task_input_zero = get_task_data_first.acell('C2').value
    count_tasks_results_zero(task_input_zero)
    task_input_one = get_task_data_first.acell('C3').value
    count_tasks_results_one(task_input_one)
    task_input_two = get_task_data_first.acell('C4').value
    count_tasks_results_two(task_input_two)
    task_input_three = get_task_data_first.acell('C5').value
    count_tasks_results_three(task_input_three)
    task_input_four = get_task_data_first.acell('C6').value
    count_tasks_results_four(task_input_four)
    task_input_five = get_task_data_first.acell('C7').value
    count_tasks_results_five(task_input_five)


def run_task_report_second():
    """
    Runs second quarter of tasks functions that count and report results.
    """
    get_task_data_second = SHEET.worksheet('tracker')
    task_input_six = get_task_data_second.acell('C8').value
    count_tasks_results_six(task_input_six)
    task_input_seven = get_task_data_second.acell('C9').value
    count_tasks_results_seven(task_input_seven)
    task_input_eight = get_task_data_second.acell('C10').value
    count_tasks_results_eight(task_input_eight)
    task_input_nine = get_task_data_second.acell('C11').value
    count_tasks_results_nine(task_input_nine)
    task_input_ten = get_task_data_second.acell('C12').value
    count_tasks_results_ten(task_input_ten)
    task_input_eleven = get_task_data_second.acell('C13').value
    count_tasks_results_eleven(task_input_eleven)
    tasks_report_upload()


def run_task_report_third():
    """
    Runs third quarter of tasks functions that count and report results.
    """
    get_task_data_third = SHEET.worksheet('tracker')
    task_input_twelve = get_task_data_third.acell('C14').value
    count_tasks_results_twelve(task_input_twelve)
    task_input_thirteen = get_task_data_third.acell('C15').value
    count_tasks_results_thirteen(task_input_thirteen)
    task_input_fourteen = get_task_data_third.acell('C16').value
    count_tasks_results_fourteen(task_input_fourteen)
    task_input_fifteen = get_task_data_third.acell('C17').value
    count_tasks_results_fifteen(task_input_fifteen)
    task_input_sixteen = get_task_data_third.acell('C18').value
    count_tasks_results_sixteen(task_input_sixteen)
    task_input_svnteen = get_task_data_third.acell('C19').value
    count_tasks_results_svnteen(task_input_svnteen)


def run_task_report_fourth():
    """
    Runs final quarter of tasks functions that count and report results.
    """
    get_task_data_fourth = SHEET.worksheet('tracker')
    task_input_eghtteen = get_task_data_fourth.acell('C20').value
    count_tasks_results_eghtteen(task_input_eghtteen)
    task_input_nineteen = get_task_data_fourth.acell('C21').value
    count_tasks_results_nineteen(task_input_nineteen)
    task_input_twenty = get_task_data_fourth.acell('C22').value
    count_tasks_results_twenty(task_input_twenty)
    task_input_twentyone = get_task_data_fourth.acell('C23').value
    count_tasks_results_twentyone(task_input_twentyone)
    task_input_twntytwo = get_task_data_fourth.acell('C24').value
    count_tasks_results_twntytwo(task_input_twntytwo)
    task_input_twntythree = get_task_data_fourth.acell('C25').value
    count_tasks_results_twntythree(task_input_twntythree)


def run_program_exit():
    """
    Function that runs all final exiting functions of the program.
    """
    tasks_report_exit()
    export_results_analyzer()
    exit_screen()


run_introduction()
run_data_inputs_first()
run_data_inputs_second()
run_data_inputs_third()
run_data_inputs_fourth()
run_sub_report()
run_task_report_first()
run_task_report_second()
run_task_report_third()
run_task_report_fourth()
run_program_exit()
