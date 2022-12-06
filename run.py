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
    First of, user is presented with current date and time.
    Then a short welcome message followed by explanation of next steps.
    Once user has finished reading section of how it works, input that sends user to the rules section is presented.
    """
    print("-------------------------------------------------------------------------------")
    live_timestamp = datetime.now()
    print(live_timestamp)

    print("Welcome to the ultimate Life Tracker! (Daily Tasklist)! [v.1]")

    print("The program serves the purpose synchronizing your daily journal with schedule.")

    print("How it works?")
    print("- Following the introduction, you will proceed to the rules section")
    print("- After covering the rules, you will be asked to provide personal information")
    print("- Next you will be asked to input your daily events per each hour")
    print("- Your results will be exported to an online Google Sheet")
    print("- Once the data is in, program will retrieve next results")
    print("- Those are noted as daily duration of each category and task")
    print("- Once that is reported to you, it will be exported again")
    print("- This time, to the analysis worksheet")
    print("- Following the link, you will be able to see visual analysis through graphs")
   
    while True:
        rules_input = input("Please input button x and press enter to continue: \n")

        if validate_rules_data(rules_input):
            print("Loading...")
            break
    print("-------------------------------------------------------------------------------")

    return rules_input
   

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
    
    print("- In order for program to function correctly, please respect the instructions")
    print("- When asked to input letter x to proceed, please do not enter any other letter")
    print("- When asked to input letter x, please enter only one character")
    
    print("- When inputting subcategories and tasks, please follow rules precisely")
    print("- Do not enter any numbers")
    print("- Only enter values when asked for it")
    print("- Only select sub-categories from given list")
    print("- Tasks are custom by your experience with limit of 40 characters")
    print("- Please do not leave any fields empty")
    print("- During reporting sub-categories and tasks, time is in 24-hour format")

    while True:
        personal_info_input = input("Please input button x and press enter to continue: \n")

        if validate_personal_data(personal_info_input):
            print("Loading...")
            break

    print("-------------------------------------------------------------------------------")

    return personal_info_input
   

def validate_personal_data(values):
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


def personal_info():
    """
    This function allows users to enter their name and unique identification number.
    """
    print("-------------------------------------------------------------------------------")
    print("Please enter your name and identification number.")
    print("If you did not request ID yet, you can enter any number above 1000.")

    while True:
        name_input = input("Please enter your first name: \n")

        if validate_name_data(name_input):
            print("Data is valid!")
            break

    while True:
        
        id_input = input("Please enter your identification number: \n")

        if validate_id_data(id_input):
            print("Data is valid!")
            break

    print(f"Thank you {name_input}, #{id_input}.")

    print("Starting the program...")
    print("-------------------------------------------------------------------------------")

    return name_input
    return id_input

def validate_name_data(values):
    """
    Raises ValueError if name is a number instead of letters.
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
    Raises ValueError if ID number contains letters instead of numbers.
    Raises ValueError if the number is less than 1000.
    """
    if id_input.isalpha():
        raise ValueError(
            "Invalid ID number, please only use numbers"
        )
        return False
    elif values <= 1000:
        raise ValueError(
            "Please enter a number above 1000 and then try again."
        )
        return False
    else:
        return True


def input_results_zero():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 00:00 and 01:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        zero_sub_input = input("Please enter your sub-category here: \n")

        if validate_zero_sub_data(zero_sub_input):
            print("Submission accepted!")
            break

    while True:   
        zero_task_input = input("Please enter your task here: \n")

        if validate_zero_task_data(zero_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {zero_sub_input} - {zero_task_input}")
    print("-------------------------------------------------------------------------------")
    
    return zero_sub_input
    return zero_task_input


def validate_zero_sub_data(values):
    """
    Raises ValueError if sub-categories do not match options.
    """
    if zero_sub_input == "Body System Care":
        return True
    elif zero_sub_input == "Soul & Spirit":
        return True
    elif zero_sub_input == "Fitness":
        return True
    elif zero_sub_input == "Meditation":
        return True
    elif zero_sub_input == "Personal Progress":
        return True
    elif zero_sub_input == "Global Progress":
        return True
    elif zero_sub_input == "Education Progress":
        return True
    elif zero_sub_input == "Business Progress":
        return True
    elif zero_sub_input == "Adventures":
        return True
    elif zero_sub_input == "Random Activity":
        return True
    elif zero_sub_input == "Rest":
        return True
    elif zero_sub_input == "Break":
        return True        
    else:
        return False


def validate_zero_task_data(values):
    """
    Raises ValueError if task has more than 40 characters.
    Raises ValueError if task contains any numbers.
    """
    if zero_task_input.isalpha() and len(zero_task_input) <= 40:
        return True
    else: 
        raise ValueError(
            "Please enter letters only task with maximum 40 characters."
        )
        return False


def data_uploaded_zero():
    """
    Function uploads both inputs to the correct row and column of the excel document.
    """
    update_worksheet_zero = SHEET.worksheet(tracker)
    
    update_worksheet_zero.update('B2', zero_sub_input)

    update_worksheet_zero.update('B3', zero_task_input)

    print("Processing request...")

    print("00:00 - 01:00 hour has been successfully uploaded!")

    print("Let's continue with the next hour of your day.")

    while True:
        zero_next_input = input("Please type in letter x and press enter to continue: \n")

        if validate_zero_next_data(zero_next_input):
            print("Loading...")
            break
    
    print("-------------------------------------------------------------------------------")
    
    return zero_next_input


def validate_zero_next_data(values):
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


def input_results_one():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 01:00 and 02:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        one_sub_input = input("Please enter your sub-category here: \n")

        if validate_one_sub_data(one_sub_input):
            print("Submission accepted!")
            break

    while True:   
        one_task_input = input("Please enter your task here: \n")

        if validate_one_task_data(one_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {one_sub_input} - {one_task_input}")
    print("-------------------------------------------------------------------------------")

    return one_sub_input
    return one_task_input


def input_results_two():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 02:00 and 03:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        two_sub_input = input("Please enter your sub-category here: \n")

        if validate_two_sub_data(two_sub_input):
            print("Submission accepted!")
            break

    while True:   
        two_task_input = input("Please enter your task here: \n")

        if validate_two_task_data(two_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {two_sub_input} - {two_task_input}")
    print("-------------------------------------------------------------------------------")

    return two_sub_input
    return two_task_input


def input_results_three():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 03:00 and 04:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        three_sub_input = input("Please enter your sub-category here: \n")

        if validate_three_sub_data(three_sub_input):
            print("Submission accepted!")
            break

    while True:   
        three_task_input = input("Please enter your task here: \n")

        if validate_three_task_data(three_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {three_sub_input} - {three_task_input}")
    print("-------------------------------------------------------------------------------")

    return three_sub_input
    return three_task_input


def input_results_four():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 04:00 and 05:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        four_sub_input = input("Please enter your sub-category here: \n")

        if validate_four_sub_data(four_sub_input):
            print("Submission accepted!")
            break

    while True:   
        four_task_input = input("Please enter your task here: \n")

        if validate_four_task_data(four_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {four_sub_input} - {four_task_input}")
    print("-------------------------------------------------------------------------------")

    return four_sub_input
    return four_task_input


def input_results_five():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 05:00 and 06:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        five_sub_input = input("Please enter your sub-category here: \n")

        if validate_five_sub_data(five_sub_input):
            print("Submission accepted!")
            break

    while True:   
        five_task_input = input("Please enter your task here: \n")

        if validate_five_task_data(five_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {five_sub_input} - {five_task_input}")
    print("-------------------------------------------------------------------------------")

    return five_sub_input
    return five_task_input


def input_results_six():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 06:00 and 07:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        six_sub_input = input("Please enter your sub-category here: \n")

        if validate_six_sub_data(six_sub_input):
            print("Submission accepted!")
            break

    while True:   
        six_task_input = input("Please enter your task here: \n")

        if validate_six_task_data(six_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {six_sub_input} - {six_task_input}")
    print("-------------------------------------------------------------------------------")

    return six_sub_input
    return six_task_input


def input_results_seven():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 07:00 and 08:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        seven_sub_input = input("Please enter your sub-category here: \n")

        if validate_seven_sub_data(seven_sub_input):
            print("Submission accepted!")
            break

    while True:   
        seven_task_input = input("Please enter your task here: \n")

        if validate_seven_task_data(seven_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {seven_sub_input} - {seven_task_input}")
    print("-------------------------------------------------------------------------------")

    return seven_sub_input
    return seven_task_input


def input_results_eight():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 08:00 and 09:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        eight_sub_input = input("Please enter your sub-category here: \n")

        if validate_eight_sub_data(eight_sub_input):
            print("Submission accepted!")
            break

    while True:   
        eight_task_input = input("Please enter your task here: \n")

        if validate_eight_task_data(eight_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {eight_sub_input} - {eight_task_input}")
    print("-------------------------------------------------------------------------------")

    return eight_sub_input
    return eight_task_input


def input_results_nine():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 09:00 and 10:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        nine_sub_input = input("Please enter your sub-category here: \n")

        if validate_nine_sub_data(nine_sub_input):
            print("Submission accepted!")
            break

    while True:   
        nine_task_input = input("Please enter your task here: \n")

        if validate_nine_task_data(nine_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {nine_sub_input} - {nine_task_input}")
    print("-------------------------------------------------------------------------------")

    return nine_sub_input
    return nine_task_input


def input_results_ten():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 10:00 and 11:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        ten_sub_input = input("Please enter your sub-category here: \n")

        if validate_ten_sub_data(ten_sub_input):
            print("Submission accepted!")
            break

    while True:   
        ten_task_input = input("Please enter your task here: \n")

        if validate_ten_task_data(ten_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {ten_sub_input} - {ten_task_input}")
    print("-------------------------------------------------------------------------------")

    return ten_sub_input
    return ten_task_input


def input_results_eleven():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 11:00 and 12:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        eleven_sub_input = input("Please enter your sub-category here: \n")

        if validate_eleven_sub_data(eleven_sub_input):
            print("Submission accepted!")
            break

    while True:   
        eleven_task_input = input("Please enter your task here: \n")

        if validate_eleven_task_data(eleven_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {eleven_sub_input} - {eleven_task_input}")
    print("-------------------------------------------------------------------------------")

    return eleven_sub_input
    return eleven_task_input


def input_results_twelve():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 12:00 and 13:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        twelve_sub_input = input("Please enter your sub-category here: \n")

        if validate_twelve_sub_data(twelve_sub_input):
            print("Submission accepted!")
            break

    while True:   
        twelve_task_input = input("Please enter your task here: \n")

        if validate_twelve_task_data(twelve_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {twelve_sub_input} - {twelve_task_input}")
    print("-------------------------------------------------------------------------------")

    return twelve_sub_input
    return twelve_task_input


def input_results_thirteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 13:00 and 14:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        thirteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_thirteen_sub_data(thirteen_sub_input):
            print("Submission accepted!")
            break

    while True:   
        thirteen_task_input = input("Please enter your task here: \n")

        if validate_thirteen_task_data(thirteen_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {thirteen_sub_input} - {thirteen_task_input}")
    print("-------------------------------------------------------------------------------")

    return thirteen_sub_input
    return thirteen_task_input


def input_results_fourteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 14:00 and 15:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        fourteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_fourteen_sub_data(fourteen_sub_input):
            print("Submission accepted!")
            break

    while True:   
        fourteen_task_input = input("Please enter your task here: \n")

        if validate_fourteen_task_data(fourteen_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {fourteen_sub_input} - {fourteen_task_input}")
    print("-------------------------------------------------------------------------------")

    return fourteen_sub_input
    return fourteen_task_input


def input_results_fifteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 15:00 and 16:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        fifteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_fifteen_sub_data(fifteen_sub_input):
            print("Submission accepted!")
            break

    while True:   
        fifteen_task_input = input("Please enter your task here: \n")

        if validate_fifteen_task_data(fifteen_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {fifteen_sub_input} - {fifteen_task_input}")
    print("-------------------------------------------------------------------------------")

    return fifteen_sub_input
    return fifteen_task_input


def input_results_sixteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 16:00 and 17:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        sixteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_sixteen_sub_data(sixteen_sub_input):
            print("Submission accepted!")
            break

    while True:   
        sixteen_task_input = input("Please enter your task here: \n")

        if validate_sixteen_task_data(sixteen_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {sixteen_sub_input} - {sixteen_task_input}")
    print("-------------------------------------------------------------------------------")

    return sixteen_sub_input
    return sixteen_task_input


def input_results_seventeen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 17:00 and 18:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        seventeen_sub_input = input("Please enter your sub-category here: \n")

        if validate_seventeen_sub_data(seventeen_sub_input):
            print("Submission accepted!")
            break

    while True:   
        seventeen_task_input = input("Please enter your task here: \n")

        if validate_seventeen_task_data(seventeen_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {seventeen_sub_input} - {seventeen_task_input}")
    print("-------------------------------------------------------------------------------")

    return seventeen_sub_input
    return seventeen_task_input


def input_results_eighteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 18:00 and 19:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        eighteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_eighteen_sub_data(eighteen_sub_input):
            print("Submission accepted!")
            break

    while True:   
        eighteen_task_input = input("Please enter your task here: \n")

        if validate_eighteen_task_data(eighteen_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {eighteen_sub_input} - {eighteen_task_input}")
    print("-------------------------------------------------------------------------------")

    return eighteen_sub_input
    return eighteen_task_input


def input_results_nineteen():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 19:00 and 20:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        nineteen_sub_input = input("Please enter your sub-category here: \n")

        if validate_nineteen_sub_data(nineteen_sub_input):
            print("Submission accepted!")
            break

    while True:   
        nineteen_task_input = input("Please enter your task here: \n")

        if validate_nineteen_task_data(nineteen_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {nineteen_sub_input} - {nineteen_task_input}")
    print("-------------------------------------------------------------------------------")

    return nineteen_sub_input
    return nineteen_task_input


def input_results_twenty():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 20:00 and 21:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        twenty_sub_input = input("Please enter your sub-category here: \n")

        if validate_twenty_sub_data(twenty_sub_input):
            print("Submission accepted!")
            break

    while True:   
        twenty_task_input = input("Please enter your task here: \n")

        if validate_twenty_task_data(twenty_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {twenty_sub_input} - {twenty_task_input}")
    print("-------------------------------------------------------------------------------")

    return twenty_sub_input
    return twenty_task_input


def input_results_twentyone():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 21:00 and 22:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        twentyone_sub_input = input("Please enter your sub-category here: \n")

        if validate_twentyone_sub_data(twentyone_sub_input):
            print("Submission accepted!")
            break

    while True:   
        twentyone_task_input = input("Please enter your task here: \n")

        if validate_twentyone_task_data(twentyone_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {twentyone_sub_input} - {twentyone_task_input}")
    print("-------------------------------------------------------------------------------")

    return twentyone_sub_input
    return twentyone_task_input


def input_results_twentytwo():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 22:00 and 23:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        twentytwo_sub_input = input("Please enter your sub-category here: \n")

        if validate_twentytwo_sub_data(twentytwo_sub_input):
            print("Submission accepted!")
            break

    while True:   
        twentytwo_task_input = input("Please enter your task here: \n")

        if validate_twentytwo_task_data(twentytwo_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {twentytwo_sub_input} - {twentytwo_task_input}")
    print("-------------------------------------------------------------------------------")

    return twentytwo_sub_input
    return twentytwo_task_input


def input_results_twentythree():
    """
    Requests direct input from the user about their daily events.
    User is requested to select one sub-category and input one task.
    Both of them will be requested for each hour of a day.
    """  
    print("What have you done today between 23:00 and 00:00?")

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
    print("- Break")

    print("- Please select one sub-category from the list above.")
    print("- Please enter a custom task that best desribes chosen sub-category.")
    print("- Please capitalize first letter of sub-categories and tasks.")

    while True:   
        twentythree_sub_input = input("Please enter your sub-category here: \n")

        if validate_twentythree_sub_data(twentythree_sub_input):
            print("Submission accepted!")
            break

    while True:   
        twentythree_task_input = input("Please enter your task here: \n")

        if validate_twentythree_task_data(twentythree_task_input):
            print("Submission accepted!")
            break

    print(f"Your input was: {twentythree_sub_input} - {twentythree_task_input}")
    print("-------------------------------------------------------------------------------")

    return twentythree_sub_input
    return twentythree_task_input


def all_results_uploaded_successfully():
    """
    This function serves the purpose of updating user on the current upload status.
    It is used as communicative transition with entering a button to the next section.
    """

    print("Loading...")

    print("Upload completed.")

    print("Your daily chedule is now successfully updated!")

    while True:
        results_sub_input = input("Please type in letter x and press enter to acess the results reports: \n")

        if validate_results_sub_data(results_sub_input):
            print("Loading...")
            break
    
    print("-------------------------------------------------------------------------------")
    
    return results_sub_input


def validate_results_sub_data(values):
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


def retrieve_subcategories_results():
    """
    Function retrieves subcategories results and counts items repetitions.
    """
    subcategories_list = worksheet.col_values(2)

    body_system_count = 0
    for item in subcategories_list:
        if item == 'Body System Care':
            body_system_count +=1

    soul_spirit_count = 0
    for item in subcategories_list:
        if item == 'Soul & Spirit':
            soul_spirit_count +=1

    fitness_count = 0
    for item in subcategories_list:
        if item == 'Fitness':
            fitness_count +=1

    meditation_count = 0
    for item in subcategories_list:
        if item == 'Meditation':
           meditation_count +=1

    print(f"Body System Care - [{body_system_count}] hours")
    print(f"Soul & Spirit - [{soul_spirit_count}] hours")
    print(f"Fitness - [{fitness_count}] hours")
    print(f"Meditation - [{meditation_count}] hours")

    return body_system_count
    return soul_spirit_count        
    return fitness_count
    return meditation_count


def retrieve_tasks_results():
    """
    Function retrieves taks results and counts items repetitions.
    """
    tasks_list = worksheet.col_values(3)

    zero_row_count = 0
    for item in tasks_list:
        if item == zero_task_input:
            zero_row_count +=1
    
    print(f"{zero_task_input} - [{zero_row_count}] hours")

    return zero_row_count


def retrieve_categories_results():
    print("a")
    #Returned data caps
    returned_data = "all results"
    print(returned_data.upper())

    #returned data split at comma
    returned_data_split = returned_data.split(",")
    print(returned_data_split)

    print("if first letter or all arent capitalized, show error")

    #adding values
    def add (a,b):
        sum = a + b + c + d
        return sum
    
    #strings processing
    capitalize() - first letter
    upper() - all uppercase
    count() - counts how many time certain value occurs inthe string
    my_string = "HELLO WORLD"
    my_string_lower_case = my_string.lower()



def retrieve_tasks_results():
    print("a")
    #Returned data caps
    returned_data = "all results"
    print(returned_data.upper())

    #returned data split at comma
    returned_data_split = returned_data.split(",")
    print(returned_data_split)

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
    Runs all functions inside the program
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

main()



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


get_last_5_entries()
stock data = calculate_stock_data(sales_columns)
print(stock_data)


def get_stock_values(data):
    """
    Print out the calculated stock numbers for each sandwich type.
    """
    headings = SHEET.worksheet("stock").get_all_values()[0]

    headings = SHEET.worksheet('stock').row_values(1)

    print("Make the following numbers of sandwiches for next market:\n")

    new_data = {}
    for heading, stock_num in zip(headings, data):
        new_data[heading] = stock_num
    return new_data
    
    return {heading: data for heading, data in zip(headings, data)}
    
    
stock_values = get_stock_values(stock_data)
print(stock_values)

def retrieve_tasks_results():
    """
    Function requests list of all tasks inputted in the column.
    Then it converts it in the alphabetically ordered list with hours spent.
    Hours spent are calculated by how many times task strings repeat itself.
    """
    print("These are your daily results in hours spent ")


def export_results_analyzer():
    """
    Results gathered from the tracker and reported to program are being exported after processed.
    Users receive a link to their sheet.
    Users see outro message with input section that leads to exit the program sequence.
    """
    print("Updating results to the analyzer...")

    print("Daily results have been successfully sent to the analyzer.")

    print("Now you can access your daily worksheet with detailed visual analysis.")

    print("Please copy and follow this link: [https://bit.ly/life-tracker-sheet]")

    print("Thank you for participating.")

    print("See you tomorrow at the next tracking and analyzing mission!")

    while True:
        exit_input = input("Please input button x and press enter to exit: \n")

        if validate_exit_data(rules_input):
            print("Loading...")
            break

    return rules_input
    print("-------------------------------------------------------------------------------")


def validate_exit_data(values):
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


def exit_screen():
    """
    Informs the user that exit sequence is initiated.
    Countdown of 10 seconds ends with exit message.
    """
    print("-------------------------------------------------------------------------------")
    print("Initiating Exit Sequence...")

    print("Loading...")

    countdown = 10

    while countdown >= 0:
        print(f"{countdown} seconds...")
        countdown -= 1

    raise SystemExit("Exiting...")
    print("-------------------------------------------------------------------------------")





