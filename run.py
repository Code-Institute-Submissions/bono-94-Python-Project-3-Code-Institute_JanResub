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
    This introduction serves to purpose of welcoming user to the program.
    First of, user is presented with current date and time.
    Then a short welcome message followed by next steps explanation.
    Once user has finished reading section how it work, input button that sends user to the rules section is presented.
    """
    print("-------------------------------------------------------------------------------")
    live_timestamp = datetime.now()
    print(live_timestamp)

    print("Welcome to the ultimate Life Tracker! (Daily Tasklist)! [v.1]")

    print("The program serves the purpose synchronizing your daily journal with schedule.")

    print("How it works?")
    print("- Following the introduction, you will proceed to the rules section")
    print("- After covering the rules, users will be asked to provide personal information")
    print("- Next you will be asked to input your daily events per each hour")
    print("- Your results will be exported to an online Google Sheet")
    print("- Once the data is in, program will retrieve next results")
    print("- Those are noted as daily duration of each category and task")
    print("- Once that is reported to you, it will be exported to again")
    print("- This time,to the analysis worksheet")
    print("- Following the link, you will be able to see visual analysis through graphs")
   
    while True:
        rules_input = input("Please input button x and press enter to continue: \n")

        if validate_rules_data(rules_input):
            print("Loading...")
            break

    return rules_input
    print("-------------------------------------------------------------------------------")


def validate_rules_data(values):
    """
    Raises ValueError if string does not match letter "x".
    Raises ValueError if user has inputted more than one letter.
    """
    if values != "x":
        raise ValueError(
            "Invalid letter, please input letter x then and try again."
        )
        return False
    elif len(values) != 1:
        raise ValueError(
            "Too many letters, please input letter x then and try again."
        )
        return False
    else:
        return True      


def rules():
    """
    Rules section allows users to get familiar with important rules.
    At the end, user is asked to input the letter x in order to continue.
    """
    print("-------------------------------------------------------------------------------")
    print("RULES")
    
    print("- In order for program to function correctly, please respect the instructions ")
    print("- When asked to input letter x to proceed, please do not enter any other letter")
    print("- When asked to input letter x, please enter only one character")
    
    print("- When inputting subcategories and tasks, please follow rules precisely")
    print("- Do not enter any numbers")
    print("- Only enter two values separated by comma")
    print("- Only select sub-categories from given list")
    print("- Tasks are custom by your experience with limit of 40 characters")

    while True:
        personal_info_input = input("Please input button x and press enter to continue: \n")

        if validate_personal_data(personal_info_input):
            print("Loading...")
            break

    return personal_info_input
    print("-------------------------------------------------------------------------------")


def validate_personal_data(values):
    """
    Raises ValueError if string does not match letter "x" 
    Raises ValueError if user has inputted more than one letter.
    """
    if values != "x":
        raise ValueError(
            "Invalid letter, please input letter x then and try again."
        )
        return False
    elif len(values) != 1:
        raise ValueError(
            "Too many letters, please input letter x then and try again."
        )
        return False
    else:
        return True


def personal_info():
    print("-------------------------------------------------------------------------------")
    print("Please enter your name and identification number.")

    print("If you did not requested ID yet, you can enter any number above 1000.")

    while True:
        name_input = input("Please enter your first name: \n")

        reference_input = input("Please enter your identification number: \n")

        if validate_name_data(name_input):
            print("Data is valid!")
            break

        if validate_id_data(id_input):
            print("Data is valid!")
            break

    return name_input

    return id_input

    print(f"Thank you {name_input}")

    print("Starting the program...")
    print("-------------------------------------------------------------------------------")

def validate_name_data(values):
    """
    Raises ValueError if name is an integer instead of a string.
    Raises ValueError if name is longer than 50 characters.
    """
    if name_input.isdigit():
        raise ValueError(
            "Invalid name, please do not use any numbers and try again."
        )
        return False
    elif len(values) >= 50:
        raise ValueError(
            "Too many letters, please enter the name under 50 letters and try again."
        )
        return False
    else:
        return True


def validate_id_data(values):
    """
    Raises ValueError if ID number is a string instead of an integer.
    Raises ValueError if the number is less than 1000.
    """
    if id_input.isalpha():
        raise ValueError(
            "Invalid ID number, please only use numbers"
        )
        return False
    elif len(values) <= 1000:
        raise ValueError(
            "Please enter a number above 1000 and then try again."
        )
        return False
    else:
        return True


def input_results_zero():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 00:00 and 01:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_one():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 01:00 and 02:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_two():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 02:00 and 03:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_three():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 03:00 and 04:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_four():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 04:00 and 05:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_five():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 05:00 and 06:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_six():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 06:00 and 07:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_seven():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 07:00 and 08:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_eight():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 08:00 and 09:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_nine():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 09:00 and 10:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_ten():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 10:00 and 11:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_eleven():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 11:00 and 12:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_twelve():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 12:00 and 13:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_thirteen():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 13:00 and 14:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_fourteen():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 14:00 and 15:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_fifteen():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 15:00 and 16:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_sixteen():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 16:00 and 17:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_seventeen():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 17:00 and 18:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_eighteen():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 18:00 and 19:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_nineteen():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 19:00 and 20:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_twenty():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 20:00 and 21:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_twentyone():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 21:00 and 22:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_twentytwo():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 22:00 and 23:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data


def input_results_twentythree():
    """
    Requests direct input from the user.
    User is requested to input one sub-category and one task.
    Both of them will be requested for each hour of a day.
    WHAT IT DOES AND HOW
    RULES
    """
    while True:
        print("What have you done today between 23:00 and 00:00?")
        
        print("GROWTH")
        print("- Body System Care")
        print("- Soul & Spirit")
        print("- Fitness")
        print("- Meditation")

        print("PROGRESS")
        print("- Personal Progress")
        print("- Global ProgresS")
        print("- Education Progress")
        print("- Business Progress")

        print("FREEDOM")
        print("- Adventures")
        print("- Random Activity")
        print("- Rest")
        print("- Break")

        print("Please enter one sub-category from above and a custom task separated by a comma")
        print("Example: [SUB-CATEGORY , TASK] - [Fitness , Stretch]")

        results_input = input("Results:\n")

        results_data = results_input.split(",")

        if validate_input_data(results_data):
            print("Submission accepted!")
            break
        
    return results_data

def validate_input_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def retrieve_categories_results():


def retrieve_tasks_results():


def update_results():


   



sales = SHEET.worksheet('dashboard')

data = sales.get_all_values()

print(data)


def get_main_data():
    """
    Get main data figures input from user
    run a while loop until collected data from terminal is categorized as valid
    """
    while True:
        print("Please enter this DATA")
        print("Data should be six numbers, separated by commas")
        print("Example: 1,2,3,4,5,6\n")

        data_str = input("Enter your data here: ")
        print(f"the data provided is {data_str}")

        sales_data = data_str.split(",")
        print(sales_data)
        validate_data(sales_data)

        if validate_data(sales_data):
            print("Data is valid!")
            break
    
    return sales_data


def validate_data(values):
    """
    Inside the validator:
    Converts all string into integers
    If not possible to convert raises ValueError
    Data is checked for having 6 values only
    """
    print(values)
    [int(value) for value in values]
    try: 
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values requiered, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives list of integers to be inserted into a worksheet
    update specific worksheet with data provided
    """
    print(f"Updating {worksheet} worksheet ... \n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully \n")


def update_sales_worksheet(data):
    """
    Updates sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("dashboard")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated succesfully . \n")


def update_surplus_worksheet(data):
    """
    Updates surplus worksheet, add new row with the list data provided
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("dashboard")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated succesfully . \n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock
    Calculate surplus

    surplus is defined as sales subtracted from stock:
    -positive incidactes waste
    -negative indicates extra made when stock ran out
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("dashboard").get_all_values()
    pprint(stock)
    stock_row = stock[-1]
    print(stock_row)
    print(f"stock row: {stock_row}")
    print(f"sales row: {sales_row}")

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    print(surplus_data)
    return surplus_data


def get_last_5_entries():
    """
    Collects columns of data from sales worksheet
    collecting the last 5 entries per column
    returns data as a list of lists
    """
    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3)
    # print(column)

    columns = []
    for ind in range(1, 7):
        print(ind)
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns


def calculate_stock_data(data):

    """
    Calculae the average stock for each item type
    add 10%
    """    
    print("Calculating stock data ... \n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))
    
    return new_stock_data


def main():
    """
    Run all program functions
    """
    data = get_main_data()
    print(data)
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)

    """
    extra fo refractured code replace upper 2 update codes
        update_worksheet(sales_data, "sales")
        update_worksheet(new_surplus_data, "surplus")
        update_worksheet(stock_data, "stock")
    """


print("Welcome to Life Data Automation")
main()

#raiseSystemExit

# get_last_5_entries()
# stock data = calculate_stock_data(sales_columns)
# print(stock_data)


def get_stock_values(data):
    """
    Print out the calculated stock numbers for each sandwich type.
    """
    headings = SHEET.worksheet("stock").get_all_values()[0]

    # headings = SHEET.worksheet('stock').row_values(1)

    print("Make the following numbers of sandwiches for next market:\n")

    # new_data = {}
    # for heading, stock_num in zip(headings, data):
    #     new_data[heading] = stock_num
    # return new_data
    
    return {heading: data for heading, data in zip(headings, data)}
    
    
stock_values = get_stock_values(stock_data)
print(stock_values)




#errors:
raise SystemExit('You must be older than 18!')
except ZeroDivisionError:
    print("Please enter a valid denominator.")
except ValueError:
    print("Both values have to be integers.")
except Exception:
    print('Another error has occurred')


Please enter only numbers
Please enter only letters

Value must be minimum 1,000,000,000


#calculating analysis
def division(numerator, denominator):
    result = numerator / denominator
    return result
    def multiplication(num1, num2):
    return num1 * num2

result1 = multiplication(2, 3)
print(result1)



# inputs

first_number = input("Input your first number:")
second_number = input("Input your second number:")
print(first_number + second_number)

name = input("What's your name? ")
age = input("What's your age: ")
print(f"Hello {name}, you are {age} years old")

number = int(input("Please enter a number:"))



#Multistrings
result = 40 + float("2.2")
print(result)

result_two = "The answer to the ultimate question is " + str(42)
print(result_two)


print(f"Hello {name}, you are {age} years old")

concat_string = name + " is " + str(age)
print(concat_string)
f_string = f'{name} is {age}'
print(f_string)



#strings processing
capitalize() - first letter
upper() - all uppercase
count() - counts how many time certain value occurs inthe string
my_string = "HELLO WORLD"
my_string_lower_case = my_string.lower()


#if statements
if a == b:
	result_one = 'a has the same value as b' 
    print(result_one)
else:
	result_two = 'a has not got the same value as b'
    print(result_two)


#countdown
countdown_number = 10

print("Initiating Countdown Sequence...")
print("Lift Off Will Commence In...")

while countdown_number >= 0:
    print(f"{countdown_number} seconds...")
    countdown_number -= 1

print("And We Have Lift Off!")



# Press button to continue

while play_game:
    continue_playing = input("Would you like to continue playing the game? y/n ")
    
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("Now closing the game...")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")


#lists in the document
inside the document since it are visual

#adding values
def add (a,b):
    sum = a + b
    return sum

#personal information
Please enter your name - string
Please enter your age - int

username = input("Type in your name and press return: ")
age = int(input("Please enter your age: "))



#running code 
run.py

#maximum letters per task
if len(task_input) < 40
    True
else 
    False
    return or print error


#Returned data caps
returned_data = "all results"
print(returned_data.upper())

#returned data split at comma
returned_data_split = returned_data.split(",")
print(returned_data_split)
