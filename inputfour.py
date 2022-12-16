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


def input_results_eighteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 18:00 and 19:00? \n")
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
        eighteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_eighteen_sub_data(eighteen_sub_input):
            print("Submission accepted! \n")
            break

    return eighteen_sub_input


def validate_eighteen_sub_data(values):
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


def input_task_eighteen(sub_input_eighteen):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        eighteen_task_input = input("Please enter your task here: \n")

        if validate_eighteen_task_data(eighteen_task_input):
            print("Submission accepted! \n")
            break

    print(f"Input: {sub_input_eighteen} - {eighteen_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return eighteen_task_input


def validate_eighteen_task_data(values):
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


def data_uploaded_eighteen(sub_input_eighteen, task_input_eighteen):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_eighteen = SHEET.worksheet("tracker")

    update_worksheet_eighteen.update('B20', sub_input_eighteen)

    update_worksheet_eighteen.update('C20', task_input_eighteen.capitalize())

    print("Processing request... \n")
    print("18:00 - 19:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        eighteen_next_input = input("Please enter letter x to continue: \n")

        if validate_eighteen_next_data(eighteen_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return eighteen_next_input


def validate_eighteen_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_nineteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 19:00 and 20:00? \n")
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
        nineteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_nineteen_sub_data(nineteen_sub_input):
            print("Submission accepted! \n")
            break

    return nineteen_sub_input


def validate_nineteen_sub_data(values):
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


def input_task_nineteen(sub_input_nineteen):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        nineteen_task_input = input("Please enter your task here: \n")

        if validate_nineteen_task_data(nineteen_task_input):
            print("Submission accepted! \n")
            break

    print(f"Input: {sub_input_nineteen} - {nineteen_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return nineteen_task_input


def validate_nineteen_task_data(values):
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


def data_uploaded_nineteen(sub_input_nineteen, task_input_nineteen):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_nineteen = SHEET.worksheet("tracker")

    update_worksheet_nineteen.update('B21', sub_input_nineteen)

    update_worksheet_nineteen.update('C21', task_input_nineteen.capitalize())

    print("Processing request... \n")
    print("19:00 - 20:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        nineteen_next_input = input("Please enter letter x to continue: \n")

        if validate_nineteen_next_data(nineteen_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return nineteen_next_input


def validate_nineteen_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_twenty():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 20:00 and 21:00? \n")
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
        twenty_sub_input = input("Please enter your sub-category here: \n")

        if validate_twenty_sub_data(twenty_sub_input):
            print("Submission accepted! \n")
            break

    return twenty_sub_input


def validate_twenty_sub_data(values):
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


def input_task_twenty(sub_input_twenty):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        twenty_task_input = input("Please enter your task here: \n")

        if validate_twenty_task_data(twenty_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_twenty} - {twenty_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return twenty_task_input


def validate_twenty_task_data(values):
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


def data_uploaded_twenty(sub_input_twenty, task_input_twenty):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_twenty = SHEET.worksheet("tracker")

    update_worksheet_twenty.update('B22', sub_input_twenty)

    update_worksheet_twenty.update('C22', task_input_twenty.capitalize())

    print("Processing request... \n")
    print("20:00 - 21:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        twenty_next_input = input("Please enter letter x to continue: \n")

        if validate_twenty_next_data(twenty_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return twenty_next_input


def validate_twenty_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_twentyone():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 21:00 and 22:00? \n")
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
        twentyone_sub_input = input("Please enter your sub-category here: \n")

        if validate_twentyone_sub_data(twentyone_sub_input):
            print("Submission accepted! \n")
            break

    return twentyone_sub_input


def validate_twentyone_sub_data(values):
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


def input_task_twentyone(sub_input_twentyone):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        twentyone_task_input = input("Please enter your task here: \n")

        if validate_twentyone_task_data(twentyone_task_input):
            print("Submission accepted! \n")
            break

    print(f"Data: {sub_input_twentyone} - {twentyone_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return twentyone_task_input


def validate_twentyone_task_data(values):
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


def data_uploaded_twentyone(sub_input_twentyone, task_input_twentyone):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_twentyone = SHEET.worksheet("tracker")

    update_worksheet_twentyone.update('B23', sub_input_twentyone)

    update_worksheet_twentyone.update('C23', task_input_twentyone.capitalize())

    print("Processing request... \n")
    print("21:00 - 22:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        twentyone_next_input = input("Please enter letter x to continue: \n")

        if validate_twentyone_next_data(twentyone_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return twentyone_next_input


def validate_twentyone_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_twentytwo():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 22:00 and 23:00? \n")
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
        twentytwo_sub_input = input("Please enter your sub-category here: \n")

        if validate_twentytwo_sub_data(twentytwo_sub_input):
            print("Submission accepted! \n")
            break

    return twentytwo_sub_input


def validate_twentytwo_sub_data(values):
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


def input_task_twentytwo(sub_input_twentytwo):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        twentytwo_task_input = input("Please enter your task here: \n")

        if validate_twentytwo_task_data(twentytwo_task_input):
            print("Submission accepted! \n")
            break

    print(f"Data: {sub_input_twentytwo} - {twentytwo_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return twentytwo_task_input


def validate_twentytwo_task_data(values):
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


def data_uploaded_twentytwo(sub_input_twentytwo, task_input_twentytwo):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_twentytwo = SHEET.worksheet("tracker")

    update_worksheet_twentytwo.update('B24', sub_input_twentytwo)

    update_worksheet_twentytwo.update('C24', task_input_twentytwo.capitalize())

    print("Processing request... \n")
    print("22:00 - 23:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        twentytwo_next_input = input("Please enter letter x to continue: \n")

        if validate_twentytwo_next_data(twentytwo_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return twentytwo_next_input


def validate_twentytwo_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_twentythree():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 23:00 and 00:00? \n")
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
        twentythree_sub_input = input("Enter your sub-category here: \n")

        if validate_twentythree_sub_data(twentythree_sub_input):
            print("Submission accepted! \n")
            break

    return twentythree_sub_input


def validate_twentythree_sub_data(values):
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


def input_task_twentythree(sub_input_twentythree):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        twentythree_task_input = input("Please enter your task here: \n")

        if validate_twentythree_task_data(twentythree_task_input):
            print("Submission accepted! \n")
            break

    print(f"{sub_input_twentythree} - {twentythree_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return twentythree_task_input


def validate_twentythree_task_data(values):
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


def data_uploaded_twentythree(sub_input_twentythree, task_input_twthree):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the document upload screen.
    """
    update_worksheet_twentythree = SHEET.worksheet("tracker")

    update_worksheet_twentythree.update('B25', sub_input_twentythree)

    update_worksheet_twentythree.update('C25', task_input_twthree.capitalize())

    print("Processing request... \n")
    print("23:00 - 00:00 hour has been successfully uploaded! \n")
    print("Let's continue to your daily results. \n")

    while True:
        twentythree_next_input = input("Please enter letter x to continue: \n")

        if validate_twentythree_next_data(twentythree_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return twentythree_next_input


def validate_twentythree_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


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
