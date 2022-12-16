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


def input_results_twelve():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 12:00 and 13:00? \n")
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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

    while True:
        twelve_sub_input = input("Please enter your sub-category here: \n")

        if validate_twelve_sub_data(twelve_sub_input):
            print("Submission accepted! \n")
            break

    return twelve_sub_input


def validate_twelve_sub_data(values):
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


def input_task_twelve(sub_input_twelve):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        twelve_task_input = input("Please enter your task here: \n")

        if validate_twelve_task_data(twelve_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_twelve} - {twelve_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return twelve_task_input


def validate_twelve_task_data(values):
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


def data_uploaded_twelve(sub_input_twelve, task_input_twelve):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_twelve = SHEET.worksheet("tracker")

    update_worksheet_twelve.update('B14', sub_input_twelve)

    update_worksheet_twelve.update('C14', task_input_twelve.capitalize())

    print("Processing request... \n")
    print("12:00 - 13:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        twelve_next_input = input("Please enter letter x to continue: \n")

        if validate_twelve_next_data(twelve_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return twelve_next_input


def validate_twelve_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_thirteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 13:00 and 14:00? \n")
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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

    while True:
        thirteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_thirteen_sub_data(thirteen_sub_input):
            print("Submission accepted! \n")
            break

    return thirteen_sub_input


def validate_thirteen_sub_data(values):
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


def input_task_thirteen(sub_input_thirteen):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        thirteen_task_input = input("Please enter your task here: \n")

        if validate_thirteen_task_data(thirteen_task_input):
            print("Submission accepted! \n")
            break

    print(f"Input: {sub_input_thirteen} - {thirteen_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return thirteen_task_input


def validate_thirteen_task_data(values):
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


def data_uploaded_thirteen(sub_input_thirteen, task_input_thirteen):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_thirteen = SHEET.worksheet("tracker")

    update_worksheet_thirteen.update('B15', sub_input_thirteen)

    update_worksheet_thirteen.update('C15', task_input_thirteen.capitalize())

    print("Processing request... \n")
    print("13:00 - 14:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        thirteen_next_input = input("Please enter letter x to continue: \n")

        if validate_thirteen_next_data(thirteen_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return thirteen_next_input


def validate_thirteen_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_fourteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 14:00 and 15:00? \n")
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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

    while True:
        fourteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_fourteen_sub_data(fourteen_sub_input):
            print("Submission accepted! \n")
            break

    return fourteen_sub_input


def validate_fourteen_sub_data(values):
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


def input_task_fourteen(sub_input_fourteen):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        fourteen_task_input = input("Please enter your task here: \n")

        if validate_fourteen_task_data(fourteen_task_input):
            print("Submission accepted! \n")
            break

    print(f"Input: {sub_input_fourteen} - {fourteen_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return fourteen_task_input


def validate_fourteen_task_data(values):
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


def data_uploaded_fourteen(sub_input_fourteen, task_input_fourteen):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_fourteen = SHEET.worksheet("tracker")

    update_worksheet_fourteen.update('B16', sub_input_fourteen)

    update_worksheet_fourteen.update('C16', task_input_fourteen.capitalize())

    print("Processing request... \n")
    print("14:00 - 15:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        fourteen_next_input = input("Please enter letter x to continue: \n")

        if validate_fourteen_next_data(fourteen_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return fourteen_next_input


def validate_fourteen_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_fifteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 15:00 and 16:00? \n")
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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

    while True:
        fifteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_fifteen_sub_data(fifteen_sub_input):
            print("Submission accepted! \n")
            break

    return fifteen_sub_input


def validate_fifteen_sub_data(values):
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


def input_task_fifteen(sub_input_fifteen):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        fifteen_task_input = input("Please enter your task here: \n")

        if validate_fifteen_task_data(fifteen_task_input):
            print("Submission accepted! \n")
            break

    print(f"Input: {sub_input_fifteen} - {fifteen_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return fifteen_task_input


def validate_fifteen_task_data(values):
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


def data_uploaded_fifteen(sub_input_fifteen, task_input_fifteen):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_fifteen = SHEET.worksheet("tracker")

    update_worksheet_fifteen.update('B17', sub_input_fifteen)

    update_worksheet_fifteen.update('C17', task_input_fifteen.capitalize())

    print("Processing request... \n")
    print("15:00 - 16:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        fifteen_next_input = input("Please enter letter x to continue: \n")

        if validate_fifteen_next_data(fifteen_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return fifteen_next_input


def validate_fifteen_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_sixteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 16:00 and 17:00? \n")
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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

    while True:
        sixteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_sixteen_sub_data(sixteen_sub_input):
            print("Submission accepted! \n")
            break

    return sixteen_sub_input


def validate_sixteen_sub_data(values):
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


def input_task_sixteen(sub_input_sixteen):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        sixteen_task_input = input("Please enter your task here: \n")

        if validate_sixteen_task_data(sixteen_task_input):
            print("Submission accepted! \n")
            break

    print(f"Input: {sub_input_sixteen} - {sixteen_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return sixteen_task_input


def validate_sixteen_task_data(values):
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


def data_uploaded_sixteen(sub_input_sixteen, task_input_sixteen):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_sixteen = SHEET.worksheet("tracker")

    update_worksheet_sixteen.update('B18', sub_input_sixteen)

    update_worksheet_sixteen.update('C18', task_input_sixteen.capitalize())

    print("Processing request... \n")
    print("16:00 - 17:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        sixteen_next_input = input("Please enter letter x to continue: \n")

        if validate_sixteen_next_data(sixteen_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return sixteen_next_input


def validate_sixteen_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_seventeen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 17:00 and 18:00? \n")
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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

    while True:
        seventeen_sub_input = input("Please enter your sub-category here: \n")

        if validate_seventeen_sub_data(seventeen_sub_input):
            print("Submission accepted! \n")
            break

    return seventeen_sub_input


def validate_seventeen_sub_data(values):
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


def input_task_seventeen(sub_input_seventeen):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        seventeen_task_input = input("Please enter your task here: \n")

        if validate_seventeen_task_data(seventeen_task_input):
            print("Submission accepted! \n")
            break

    print(f"Data: {sub_input_seventeen} - {seventeen_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return seventeen_task_input


def validate_seventeen_task_data(values):
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


def data_uploaded_seventeen(sub_input_seventeen, task_input_seventeen):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_seventeen = SHEET.worksheet("tracker")

    update_worksheet_seventeen.update('B19', sub_input_seventeen)

    update_worksheet_seventeen.update('C19', task_input_seventeen.capitalize())

    print("Processing request... \n")
    print("17:00 - 18:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        seventeen_next_input = input("Please enter letter x to continue: \n")

        if validate_seventeen_next_data(seventeen_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return seventeen_next_input


def validate_seventeen_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True
