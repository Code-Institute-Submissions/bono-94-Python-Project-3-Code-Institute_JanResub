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
    print("- Please enter letters only, no numbers or symbols")
    print("- Please select one sub-category from the list above")
    print("- Please copy sub-categories exactly as they are written")
    print("- Please enter a custom task that best desribes your activity")
    print("- Please capitalize first letter of first task word inputted \n")

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


def input_results_one():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 01:00 and 02:00? \n")
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
        one_sub_input = input("Please enter your sub-category here: \n")

        if validate_one_sub_data(one_sub_input):
            print("Submission accepted! \n")
            break

    return one_sub_input


def validate_one_sub_data(values):
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


def input_task_one(sub_input_one):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        one_task_input = input("Please enter your task here: \n")

        if validate_one_task_data(one_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_one} - {one_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return one_task_input


def validate_one_task_data(values):
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


def data_uploaded_one(sub_input_one, task_input_one):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_one = SHEET.worksheet("tracker")

    update_worksheet_one.update('B3', sub_input_one)

    update_worksheet_one.update('C3', task_input_one.capitalize())

    print("Processing request... \n")
    print("01:00 - 02:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        one_next_input = input("Please enter letter x to continue: \n")

        if validate_one_next_data(one_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return one_next_input


def validate_one_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_two():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 02:00 and 03:00? \n")
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
        two_sub_input = input("Please enter your sub-category here: \n")

        if validate_two_sub_data(two_sub_input):
            print("Submission accepted! \n")
            break

    return two_sub_input


def validate_two_sub_data(values):
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


def input_task_two(sub_input_two):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        two_task_input = input("Please enter your task here: \n")

        if validate_two_task_data(two_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_two} - {two_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return two_task_input


def validate_two_task_data(values):
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


def data_uploaded_two(sub_input_two, task_input_two):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_two = SHEET.worksheet("tracker")

    update_worksheet_two.update('B4', sub_input_two)

    update_worksheet_two.update('C4', task_input_two.capitalize())

    print("Processing request... \n")
    print("02:00 - 03:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        two_next_input = input("Please enter letter x to continue: \n")

        if validate_two_next_data(two_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return two_next_input


def validate_two_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_three():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 03:00 and 04:00? \n")
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
        three_sub_input = input("Please enter your sub-category here: \n")

        if validate_three_sub_data(three_sub_input):
            print("Submission accepted! \n")
            break

    return three_sub_input


def validate_three_sub_data(values):
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


def input_task_three(sub_input_three):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        three_task_input = input("Please enter your task here: \n")

        if validate_three_task_data(three_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_three} - {three_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return three_task_input


def validate_three_task_data(values):
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


def data_uploaded_three(sub_input_three, task_input_three):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_three = SHEET.worksheet("tracker")

    update_worksheet_three.update('B5', sub_input_three)

    update_worksheet_three.update('C5', task_input_three.capitalize())

    print("Processing request... \n")
    print("03:00 - 04:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        three_next_input = input("Please enter letter x to continue: \n")

        if validate_three_next_data(three_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return three_next_input


def validate_three_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_four():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 04:00 and 05:00? \n")
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
        four_sub_input = input("Please enter your sub-category here: \n")

        if validate_four_sub_data(four_sub_input):
            print("Submission accepted! \n")
            break

    return four_sub_input


def validate_four_sub_data(values):
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


def input_task_four(sub_input_four):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        four_task_input = input("Please enter your task here: \n")

        if validate_four_task_data(four_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_four} - {four_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return four_task_input


def validate_four_task_data(values):
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


def data_uploaded_four(sub_input_four, task_input_four):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_four = SHEET.worksheet("tracker")

    update_worksheet_four.update('B6', sub_input_four)

    update_worksheet_four.update('C6', task_input_four.capitalize())

    print("Processing request... \n")
    print("04:00 - 05:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        four_next_input = input("Please enter letter x to continue: \n")

        if validate_four_next_data(four_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return four_next_input


def validate_four_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def input_results_five():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category from the list of options.
    """
    print("What have you done today between 05:00 and 06:00? \n")
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
        five_sub_input = input("Please enter your sub-category here: \n")

        if validate_five_sub_data(five_sub_input):
            print("Submission accepted! \n")
            break

    return five_sub_input


def validate_five_sub_data(values):
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


def input_task_five(sub_input_five):
    """
    Requests direct input from the user about their daily events.
    User is requested to enter one custom task for specific hour.
    At the end, user can see both subcategories and task inputs.
    """
    while True:
        five_task_input = input("Please enter your task here: \n")

        if validate_five_task_data(five_task_input):
            print("Submission accepted! \n")
            break

    print(f"Your input: {sub_input_five} - {five_task_input.capitalize()}")
    print("------------------------------------------------------------------")

    return five_task_input


def validate_five_task_data(values):
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


def data_uploaded_five(sub_input_five, task_input_five):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_five = SHEET.worksheet("tracker")

    update_worksheet_five.update('B7', sub_input_five)

    update_worksheet_five.update('C7', task_input_five.capitalize())

    print("Processing request... \n")
    print("05:00 - 06:00 hour has been successfully uploaded! \n")
    print("Let's continue with the next hour of your day. \n")

    while True:
        zero_next_input = input("Please enter letter x to continue: \n")

        if validate_zero_next_data(zero_next_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return zero_next_input


def validate_five_next_data(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


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
