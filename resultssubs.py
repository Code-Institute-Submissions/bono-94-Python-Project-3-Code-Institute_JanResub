"""
This is a python-based file that executes code for Life Tracker [v.1]
It reports inputs to google sheets by email through Zapier.
Final code with accompanying files is deployed on the Heroku.
Tracker results get counted and reported back to the user in the code.
Counted results of input results then get updated to the analyzer sheet.
"""
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


def count_sub_results_two():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_two = SHEET.worksheet("tracker")
    sub_column_two = retrieve_sub_data_two.col_values(2)
    push_sub_analyzer_two = SHEET.worksheet("analyzer")

    ss_count = 0
    for item in sub_column_two:
        if item == 'Soul & Spirit':
            ss_count += 1

    print(f"Soul & Spirit - [{ss_count}]")

    push_sub_analyzer_two.update('B5', ss_count)

    return ss_count


def count_sub_results_three():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_three = SHEET.worksheet("tracker")
    sub_column_three = retrieve_sub_data_three.col_values(2)
    push_sub_analyzer_three = SHEET.worksheet("analyzer")

    fitness_count = 0
    for item in sub_column_three:
        if item == 'Fitness':
            fitness_count += 1

    print(f"Fitness - [{fitness_count}]")

    push_sub_analyzer_three.update('B6', fitness_count)

    return fitness_count


def count_sub_results_four():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_four = SHEET.worksheet("tracker")
    sub_column_four = retrieve_sub_data_four.col_values(2)
    push_sub_analyzer_four = SHEET.worksheet("analyzer")

    meditation_count = 0
    for item in sub_column_four:
        if item == 'Meditation':
            meditation_count += 1

    print(f"Meditation - [{meditation_count}] \n")

    push_sub_analyzer_four.update('B7', meditation_count)

    return meditation_count


def count_sub_results_five():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_five = SHEET.worksheet("tracker")
    sub_column_five = retrieve_sub_data_five.col_values(2)
    push_sub_analyzer_five = SHEET.worksheet("analyzer")

    personal_count = 0
    for item in sub_column_five:
        if item == 'Personal Progress':
            personal_count += 1

    print("PROGRESS")
    print(f"Personal Progress - [{personal_count}]")

    push_sub_analyzer_five.update('B10', personal_count)

    return personal_count


def count_sub_results_six():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_six = SHEET.worksheet("tracker")
    sub_column_six = retrieve_sub_data_six.col_values(2)
    push_sub_analyzer_six = SHEET.worksheet("analyzer")

    global_count = 0
    for item in sub_column_six:
        if item == 'Global Progress':
            global_count += 1

    print(f"Global Progress - [{global_count}]")

    push_sub_analyzer_six.update('B11', global_count)

    return global_count


def count_sub_results_seven():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_seven = SHEET.worksheet("tracker")
    sub_column_seven = retrieve_sub_data_seven.col_values(2)
    push_sub_analyzer_seven = SHEET.worksheet("analyzer")

    education_count = 0
    for item in sub_column_seven:
        if item == 'Education Progress':
            education_count += 1

    print(f"Education Progress - [{education_count}]")

    push_sub_analyzer_seven.update('B12', education_count)

    return education_count


def count_sub_results_eight():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_eight = SHEET.worksheet("tracker")
    sub_column_eight = retrieve_sub_data_eight.col_values(2)
    push_sub_analyzer_eight = SHEET.worksheet("analyzer")

    business_count = 0
    for item in sub_column_eight:
        if item == 'Business Progress':
            business_count += 1

    print(f"Business Progress - [{business_count}] \n")

    push_sub_analyzer_eight.update('B13', business_count)

    return business_count


def count_sub_results_nine():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_nine = SHEET.worksheet("tracker")
    sub_column_nine = retrieve_sub_data_nine.col_values(2)
    push_sub_analyzer_nine = SHEET.worksheet("analyzer")

    adventures_count = 0
    for item in sub_column_nine:
        if item == 'Adventures':
            adventures_count += 1

    print("FREEDOM")
    print(f"Adventures - [{adventures_count}]")

    push_sub_analyzer_nine.update('B16', adventures_count)

    return adventures_count


def count_sub_results_ten():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_ten = SHEET.worksheet("tracker")
    sub_column_ten = retrieve_sub_data_ten.col_values(2)
    push_sub_analyzer_ten = SHEET.worksheet("analyzer")

    random_count = 0
    for item in sub_column_ten:
        if item == 'Random Activity':
            random_count += 1

    print(f"Random Activity - [{random_count}]")

    push_sub_analyzer_ten.update('B17', random_count)

    return random_count


def count_sub_results_eleven():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_eleven = SHEET.worksheet("tracker")
    sub_column_eleven = retrieve_sub_data_eleven.col_values(2)
    push_sub_analyzer_eleven = SHEET.worksheet("analyzer")

    rest_count = 0
    for item in sub_column_eleven:
        if item == 'Rest':
            rest_count += 1

    print(f"Rest - [{rest_count}]")

    push_sub_analyzer_eleven.update('B18', rest_count)

    return rest_count


def count_sub_results_twelve():
    """
    Function retrieves list of all subcategories inputs from the column.
    Then it calculates how many times certain subcategory occurs.
    Also reports relevant subcategory consumption results to the user.
    Finally, it pushes users results to the analyzer sheet.
    """
    retrieve_sub_data_twelve = SHEET.worksheet("tracker")
    sub_column_twelve = retrieve_sub_data_twelve.col_values(2)
    push_sub_analyzer_twelve = SHEET.worksheet("analyzer")

    break_count = 0
    for item in sub_column_twelve:
        if item == 'Break':
            break_count += 1

    print(f"Break - [{break_count}]")
    print("------------------------------------------------------------------")

    push_sub_analyzer_twelve.update('B19', break_count)

    return break_count


def report_continue():
    """
    Functions forces user to wait 1 minute before proceeding.
    Function prompts user to press x to access tasks results.
    """
    print("------------------------------------------------------------------")
    print("Please wait 1 minute until the program loads the tasks results. \n")
    print("In the meantime you can view first part of your results below: \n")
    print("[https://bit.ly/life-tracker-sheet] \n")
    print("Loading... \n")

    time.sleep(70)

    print("Loading complete! \n")

    while True:
        task_results_input = input("Please enter letter x to continue: \n")

        if validate_task_results_input(task_results_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return task_results_input


def validate_task_results_input(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


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
