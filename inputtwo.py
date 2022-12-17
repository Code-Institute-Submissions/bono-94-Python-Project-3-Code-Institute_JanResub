"""
This is a python-based file that executes code for Life Tracker [v.1]
It reports inputs to google sheets by email through Zapier.
Final code with accompanying files is deployed on the Heroku.
Users inputs their daily activities per hour in the runned code.
Results then get transferred to the tracker sheet.
"""
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


def input_results_six():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 06:00 and 07:00? \n")
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
        six_sub_input = input("Please enter your sub-category here: \n")

        if validate_six_sub_data(six_sub_input):
            print("Submission accepted! \n")
            break

    return six_sub_input


def validate_six_sub_data(values):
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


def input_task_six(sub_input_six):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        six_task_input = input("Please enter your task here: \n")

        if validate_six_task_data(six_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_six} - {six_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return six_task_input


def validate_six_task_data(values):
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


def data_uploaded_six(sub_input_six, task_input_six):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_six = SHEET.worksheet("tracker")

    update_worksheet_six.update('B8', sub_input_six)

    update_worksheet_six.update('C8', task_input_six.capitalize())

    print("Processing request... \n")
    print("06:00 - 07:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        six_next_input = input("Please enter letter x to continue: \n")

        if validate_six_next_data(six_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return six_next_input


def validate_six_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_seven():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 07:00 and 08:00? \n")
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
        seven_sub_input = input("Please enter your sub-category here: \n")

        if validate_seven_sub_data(seven_sub_input):
            print("Submission accepted! \n")
            break

    return seven_sub_input


def validate_seven_sub_data(values):
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


def input_task_seven(sub_input_seven):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        seven_task_input = input("Please enter your task here: \n")

        if validate_seven_task_data(seven_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_seven} - {seven_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return seven_task_input


def validate_seven_task_data(values):
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


def data_uploaded_seven(sub_input_seven, task_input_seven):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_seven = SHEET.worksheet("tracker")

    update_worksheet_seven.update('B9', sub_input_seven)

    update_worksheet_seven.update('C9', task_input_seven.capitalize())

    print("Processing request... \n")
    print("07:00 - 08:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        seven_next_input = input("Please enter letter x to continue: \n")

        if validate_seven_next_data(seven_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return seven_next_input


def validate_seven_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_eight():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 08:00 and 09:00? \n")
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
        eight_sub_input = input("Please enter your sub-category here: \n")

        if validate_eight_sub_data(eight_sub_input):
            print("Submission accepted! \n")
            break

    return eight_sub_input


def validate_eight_sub_data(values):
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


def input_task_eight(sub_input_eight):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        eight_task_input = input("Please enter your task here: \n")

        if validate_eight_task_data(eight_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_eight} - {eight_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return eight_task_input


def validate_eight_task_data(values):
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


def data_uploaded_eight(sub_input_eight, task_input_eight):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_eight = SHEET.worksheet("tracker")

    update_worksheet_eight.update('B10', sub_input_eight)

    update_worksheet_eight.update('C10', task_input_eight.capitalize())

    print("Processing request... \n")
    print("08:00 - 09:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        eight_next_input = input("Please enter letter x to continue: \n")

        if validate_eight_next_data(eight_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return eight_next_input


def validate_eight_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_nine():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 09:00 and 10:00? \n")
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
        nine_sub_input = input("Please enter your sub-category here: \n")

        if validate_nine_sub_data(nine_sub_input):
            print("Submission accepted! \n")
            break

    return nine_sub_input


def validate_nine_sub_data(values):
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


def input_task_nine(sub_input_nine):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        nine_task_input = input("Please enter your task here: \n")

        if validate_nine_task_data(nine_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_nine} - {nine_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return nine_task_input


def validate_nine_task_data(values):
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


def data_uploaded_nine(sub_input_nine, task_input_nine):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_nine = SHEET.worksheet("tracker")

    update_worksheet_nine.update('B11', sub_input_nine)

    update_worksheet_nine.update('C11', task_input_nine.capitalize())

    print("Processing request... \n")
    print("09:00 - 10:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        nine_next_input = input("Please enter letter x to continue: \n")

        if validate_nine_next_data(nine_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return nine_next_input


def validate_nine_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_ten():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 10:00 and 11:00? \n")
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
        ten_sub_input = input("Please enter your sub-category here: \n")

        if validate_ten_sub_data(ten_sub_input):
            print("Submission accepted! \n")
            break

    return ten_sub_input


def validate_ten_sub_data(values):
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


def input_task_ten(sub_input_ten):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        ten_task_input = input("Please enter your task here: \n")

        if validate_ten_task_data(ten_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_ten} - {ten_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return ten_task_input


def validate_ten_task_data(values):
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


def data_uploaded_ten(sub_input_ten, task_input_ten):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_ten = SHEET.worksheet("tracker")

    update_worksheet_ten.update('B12', sub_input_ten)

    update_worksheet_ten.update('C12', task_input_ten.capitalize())

    print("Processing request... \n")
    print("10:00 - 11:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        ten_next_input = input("Please enter letter x to continue: \n")

        if validate_ten_next_data(ten_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return ten_next_input


def validate_ten_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_eleven():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 11:00 and 12:00? \n")
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
        eleven_sub_input = input("Please enter your sub-category here: \n")

        if validate_eleven_sub_data(eleven_sub_input):
            print("Submission accepted! \n")
            break

    return eleven_sub_input


def validate_eleven_sub_data(values):
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


def input_task_eleven(sub_input_eleven):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        eleven_task_input = input("Please enter your task here: \n")

        if validate_eleven_task_data(eleven_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_eleven} - {eleven_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return eleven_task_input


def validate_eleven_task_data(values):
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


def data_uploaded_eleven(sub_input_eleven, task_input_eleven):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_eleven = SHEET.worksheet("tracker")

    update_worksheet_eleven.update('B13', sub_input_eleven)

    update_worksheet_eleven.update('C13', task_input_eleven.capitalize())

    print("Processing request... \n")
    print("11:00 - 12:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        eleven_next_input = input("Please enter letter x to continue: \n")

        if validate_eleven_next_data(eleven_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return eleven_next_input


def validate_eleven_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


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
