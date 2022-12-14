import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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
    print("How it works?")
    print("- Following the introduction, you will proceed to rules section")
    print("- After that, you will be asked to enter personal identification")
    print("- Next you will be asked to input your daily events per each hour")
    print("- Your data will be exported to an external online Google Sheet")
    print("- Once the data is in, program will retrieve your results")
    print("- Those are noted as daily duration of each category and task")
    print("- Once that is reported to you, it will be exported again")
    print("- This time, to the second worksheet: analysis")
    print("- You will be able to see visual analysis of your results. \n")

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
    print("- Do not enter any numbers or symbols, only letters are allowed")
    print("- Only enter values when asked for it")
    print("- Only select sub-categories from provided list of options")
    print("- Tasks are custom by your experience with limit of 40 characters")
    print("- Please do not leave any fields empty")
    print("- Each hour of a day is in 24-hour format \n")

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
    print("Personal identification: name and ID number.")
    print("- If you did not request ID yet, you can enter any number. \n")

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
            print(f"Thank you, your ID number {id_input} is valid!")
            break

    print("Starting the program...")
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

    update_worksheet_zero.update('C2', task_input_zero)

    print("Processing request...")

    print("00:00 - 01:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_one.update('C3', task_input_one)

    print("Processing request...")

    print("01:00 - 02:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_two.update('C4', task_input_two)

    print("Processing request...")

    print("02:00 - 03:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_three.update('C5', task_input_three)

    print("Processing request...")

    print("03:00 - 04:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_four.update('C6', task_input_four)

    print("Processing request...")

    print("04:00 - 05:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_five.update('C7', task_input_five)

    print("Processing request...")

    print("05:00 - 06:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

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

    update_worksheet_six.update('C8', task_input_six)

    print("Processing request...")

    print("06:00 - 07:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

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

    update_worksheet_seven.update('C9', task_input_seven)

    print("Processing request...")

    print("07:00 - 08:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

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

    update_worksheet_eight.update('C10', task_input_eight)

    print("Processing request...")

    print("08:00 - 09:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

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

    update_worksheet_nine.update('C11', task_input_nine)

    print("Processing request...")

    print("09:00 - 10:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

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

    update_worksheet_ten.update('C12', task_input_ten)

    print("Processing request...")

    print("10:00 - 11:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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
    print("- Please enter a custom task that best desribes your activity")
    print("- Please enter letters only, no numbers or symbols")
    print("- Please capitalize first letter of each word inputted \n")

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


def data_uploaded_eleven(sub_input_zero, task_input_zero):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the next hour of a day.
    """
    update_worksheet_eleven = SHEET.worksheet("tracker")

    update_worksheet_eleven.update('B13', sub_input_zero)

    update_worksheet_eleven.update('C13', task_input_zero)

    print("Processing request...")

    print("11:00 - 12:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_twelve.update('C14', task_input_twelve)

    print("Processing request...")

    print("12:00 - 13:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_thirteen.update('C15', task_input_thirteen)

    print("Processing request...")

    print("13:00 - 14:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_fourteen.update('C16', task_input_fourteen)

    print("Processing request...")

    print("14:00 - 15:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_fifteen.update('C17', task_input_fifteen)

    print("Processing request...")

    print("15:00 - 16:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_sixteen.update('C18', task_input_sixteen)

    print("Processing request...")

    print("16:00 - 17:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_seventeen.update('C19', task_input_seventeen)

    print("Processing request...")

    print("17:00 - 18:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_eighteen.update('C20', task_input_eighteen)

    print("Processing request...")

    print("18:00 - 19:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_nineteen.update('C21', task_input_nineteen)

    print("Processing request...")

    print("19:00 - 20:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_twenty.update('C22', task_input_twenty)

    print("Processing request...")

    print("20:00 - 21:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_twentyone.update('C23', task_input_twentyone)

    print("Processing request...")

    print("21:00 - 22:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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

    update_worksheet_twentytwo.update('C24', task_input_twentytwo)

    print("Processing request...")

    print("22:00 - 23:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

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


def data_uploaded_twentythree(sub_input_twentythree, task_input_twentythree):
    """
    Function uploads both inputs to the correct cell of the excel document.
    Upload status is discosed to user.
    User is asked to enter letter x to continue to the document upload screen.
    """
    update_worksheet_twentythree = SHEET.worksheet("tracker")

    update_worksheet_twentythree.update('B25', sub_input_twentythree)

    update_worksheet_twentythree.update('C25', task_input_twentythree)

    print("Processing request...")

    print("23:00 - 00:00 hour has been successfully uploaded!")

    print("Let's continue to your daily results.")

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


def all_results_uploaded_successfully():
    """
    This function informs user when all results are updated to the sheet.
    It is a communicative transition to results report.
    """
    print("------------------------------------------------------------------")
    print("Updating sheet...")
    print("Upload completed.")
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
    """
    retrieve_sub_data_first = SHEET.worksheet("tracker")
    sub_column_one = retrieve_sub_data_first.col_values(2)

    body_system_count = 0
    for item in sub_column_one:
        if item == 'Body System Care':
            body_system_count += 1
    return body_system_count

    soul_spirit_count = 0
    for item in subcategories_list:
        if item == 'Soul & Spirit':
            soul_spirit_count += 1
    return soul_spirit_count

    fitness_count = 0
    for item in subcategories_list:
        if item == 'Fitness':
            fitness_count += 1
    return fitness_count

    meditation_count = 0
    for item in subcategories_list:
        if item == 'Meditation':
            meditation_count += 1
    return meditation_count


def report_sub_results():
    """
    Function retrieves subcategories results and counts items repetitions.
    """
    print("------------------------------------------------------------------")
    print("These are your daily task results in hours spent: \n")
    print("GROWTH")
    print(f"Body System Care - [{count_body_system}]")
    print(f"Soul & Spirit - [{count_soul_spirit}]")
    print(f"Fitness - [{count_fitness}]")
    print(f"Meditation - [{count_meditation}] \n")
    print("PROGRESS")
    print(f"Personal Progress - [{count_personal}]")
    print(f"Global Progress - [{count_global}]")
    print(f"Education Progress - [{count_education}]")
    print(f"Business Progress - [{count_business}] \n")
    print("FREEDOM")
    print(f"Adventures - [{count_body_system}]")
    print(f"Random Activity - [{count_soul_spirit}]")
    print(f"Rest - [{count_fitness}]")
    print(f"Break - [{count_meditation}] \n")

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


def retrieve_tasks_results():
    """
    Function retrieves taks results and counts items repetitions.
    """
    calculate_task_data_first = SHEET.worksheet('tracker').col_values(3)

    zero_row_count = 0
    for item in tasks_list:
        if item == zero_task_input:
            zero_row_count += 1

    print(f"{zero_task_input.capitalize()} - [{zero_row_count}] hours")

    return zero_row_count


def export_results_analyzer():
    """
    Results are gathered from the tracker.
    They are reported to program are being exported after processed.
    Users receive a link to their sheet.
    Users see outro message with input section.
    Message leads to exit the program sequence.
    """
    print("Updating results to the analyzer...")
    print("Daily results have been successfully sent to the analyzer.")
    live_timestamp = datetime.now()
    print(live_timestamp)
    print("Now you can access your worksheet with detailed visual analysis.")
    print("Please follow this link: [https://bit.ly/life-tracker-sheet]")
    print("Thank you for participating.")
    print("See you tomorrow at the next tracking and analyzing mission!")

    while True:
        exit_input = input("Please enter letter x to exit: \n")

        if validate_exit_data(exit_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")
    return exit_input


def validate_exit_data(values):
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
    """
    print("------------------------------------------------------------------")
    print("Initiating Exit Sequence...")

    print("Loading...")

    countdown = 10

    while countdown >= 0:
        print(f"{countdown} seconds...")
        countdown -= 1

    print("------------------------------------------------------------------")

    raise SystemExit("Exiting...")


def main():
    """
    Runs all functions inside the program.
    """
    data = get_main_data()
    print(data)
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)


def run_introduction():
    """
    Runs all introductory functions inside the program.
    """
    introduction()
    rules()
    personal_info_name()
    personal_info_id()


def run_data_inputs():
    """
    Runs all data input functions inside the program.
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
    task_input_twentythree = input_task_twentythree(sub_input_twentythree)
    data_uploaded_twentythree(sub_input_twentythree, task_input_twentythree)


run_introduction()
run_data_inputs()
