"""
This is a python-based file that executes code for Life Tracker [v.1]
It reports inputs to google sheets by email through Zapier.
Final code with accompanying files is deployed on the Heroku.
Tracker results get counted and reported back to the user in the code.
Counted results of input results then get updated to the analyzer sheet.
At the end of program, it automatically exits through raise SystemExit.
"""
from datetime import datetime
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


def count_tasks_results_zero(task_input_zero):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to user, it updates analyzer sheet.
    """
    retrieve_task_data_zero = SHEET.worksheet('tracker')
    task_column_zero = retrieve_task_data_zero.col_values(3)
    push_task_analyzer_zero = SHEET.worksheet("analyzer")

    zero_row_count = 0
    for item in task_column_zero:
        if item == task_input_zero:
            zero_row_count += 1

    print("------------------------------------------------------------------")
    print("These are your daily tasks results in hours spent: \n")
    print(f"{task_input_zero} - [{zero_row_count}]")

    push_task_analyzer_zero.update('A24', task_input_zero)
    push_task_analyzer_zero.update('B24', zero_row_count)

    return zero_row_count


def count_tasks_results_one(task_input_one):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_one = SHEET.worksheet('tracker')
    task_column_one = retrieve_task_data_one.col_values(3)
    push_task_analyzer_one = SHEET.worksheet("analyzer")

    one_row_count = 0
    for item in task_column_one:
        if item == task_input_one:
            one_row_count += 1

    print(f"{task_input_one} - [{one_row_count}]")

    push_task_analyzer_one.update('A25', task_input_one)
    push_task_analyzer_one.update('B25', one_row_count)

    return one_row_count


def count_tasks_results_two(task_input_two):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_two = SHEET.worksheet('tracker')
    task_column_two = retrieve_task_data_two.col_values(3)
    push_task_analyzer_two = SHEET.worksheet("analyzer")

    two_row_count = 0
    for item in task_column_two:
        if item == task_input_two:
            two_row_count += 1

    print(f"{task_input_two} - [{two_row_count}]")

    push_task_analyzer_two.update('A26', task_input_two)
    push_task_analyzer_two.update('B26', two_row_count)

    return two_row_count


def count_tasks_results_three(task_input_three):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_three = SHEET.worksheet('tracker')
    task_column_three = retrieve_task_data_three.col_values(3)
    push_task_analyzer_three = SHEET.worksheet("analyzer")

    three_row_count = 0
    for item in task_column_three:
        if item == task_input_three:
            three_row_count += 1

    print(f"{task_input_three} - [{three_row_count}]")

    push_task_analyzer_three.update('A27', task_input_three)
    push_task_analyzer_three.update('B27', three_row_count)

    return three_row_count


def count_tasks_results_four(task_input_four):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_four = SHEET.worksheet('tracker')
    task_column_four = retrieve_task_data_four.col_values(3)
    push_task_analyzer_four = SHEET.worksheet("analyzer")

    four_row_count = 0
    for item in task_column_four:
        if item == task_input_four:
            four_row_count += 1

    print(f"{task_input_four} - [{four_row_count}]")

    push_task_analyzer_four.update('A28', task_input_four)
    push_task_analyzer_four.update('B28', four_row_count)

    return four_row_count


def count_tasks_results_five(task_input_five):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_five = SHEET.worksheet('tracker')
    task_column_five = retrieve_task_data_five.col_values(3)
    push_task_analyzer_five = SHEET.worksheet("analyzer")

    five_row_count = 0
    for item in task_column_five:
        if item == task_input_five:
            five_row_count += 1

    print(f"{task_input_five} - [{five_row_count}]")

    push_task_analyzer_five.update('A29', task_input_five)
    push_task_analyzer_five.update('B29', five_row_count)

    return five_row_count


def count_tasks_results_six(task_input_six):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_six = SHEET.worksheet('tracker')
    task_column_six = retrieve_task_data_six.col_values(3)
    push_task_analyzer_six = SHEET.worksheet("analyzer")

    six_row_count = 0
    for item in task_column_six:
        if item == task_input_six:
            six_row_count += 1

    print(f"{task_input_six} - [{six_row_count}]")

    push_task_analyzer_six.update('A30', task_input_six)
    push_task_analyzer_six.update('B30', six_row_count)

    return six_row_count


def count_tasks_results_seven(task_input_seven):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_seven = SHEET.worksheet('tracker')
    task_column_seven = retrieve_task_data_seven.col_values(3)
    push_task_analyzer_seven = SHEET.worksheet("analyzer")

    seven_row_count = 0
    for item in task_column_seven:
        if item == task_input_seven:
            seven_row_count += 1

    print(f"{task_input_seven} - [{seven_row_count}]")

    push_task_analyzer_seven.update('A31', task_input_seven)
    push_task_analyzer_seven.update('B31', seven_row_count)

    return seven_row_count


def count_tasks_results_eight(task_input_eight):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_eight = SHEET.worksheet('tracker')
    task_column_eight = retrieve_task_data_eight.col_values(3)
    push_task_analyzer_eight = SHEET.worksheet("analyzer")

    eight_row_count = 0
    for item in task_column_eight:
        if item == task_input_eight:
            eight_row_count += 1

    print(f"{task_input_eight} - [{eight_row_count}]")

    push_task_analyzer_eight.update('A32', task_input_eight)
    push_task_analyzer_eight.update('B32', eight_row_count)

    return eight_row_count


def count_tasks_results_nine(task_input_nine):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_nine = SHEET.worksheet('tracker')
    task_column_nine = retrieve_task_data_nine.col_values(3)
    push_task_analyzer_nine = SHEET.worksheet("analyzer")

    nine_row_count = 0
    for item in task_column_nine:
        if item == task_input_nine:
            nine_row_count += 1

    print(f"{task_input_nine} - [{nine_row_count}]")

    push_task_analyzer_nine.update('A33', task_input_nine)
    push_task_analyzer_nine.update('B33', nine_row_count)

    return nine_row_count


def count_tasks_results_ten(task_input_ten):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_ten = SHEET.worksheet('tracker')
    task_column_ten = retrieve_task_data_ten.col_values(3)
    push_task_analyzer_ten = SHEET.worksheet("analyzer")

    ten_row_count = 0
    for item in task_column_ten:
        if item == task_input_ten:
            ten_row_count += 1

    print(f"{task_input_ten} - [{ten_row_count}]")

    push_task_analyzer_ten.update('A34', task_input_ten)
    push_task_analyzer_ten.update('B34', ten_row_count)

    return ten_row_count


def count_tasks_results_eleven(task_input_eleven):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_eleven = SHEET.worksheet('tracker')
    task_column_eleven = retrieve_task_data_eleven.col_values(3)
    push_task_analyzer_eleven = SHEET.worksheet("analyzer")

    eleven_row_count = 0
    for item in task_column_eleven:
        if item == task_input_eleven:
            eleven_row_count += 1

    print(f"{task_input_eleven} - [{eleven_row_count}]")

    push_task_analyzer_eleven.update('A35', task_input_eleven)
    push_task_analyzer_eleven.update('B35', eleven_row_count)

    return eleven_row_count


def tasks_report_upload():
    """
    Functions forces user to wait 1 minute before proceeding.
    Function prompts user to press x to upload tasks results.
    """
    print("------------------------------------------------------------------")
    print("Please wait 1 minute until program loads more tasks results. \n")
    print("In the meantime you can view first part of your results below: \n")
    print("[https://bit.ly/life-tracker-sheet] \n")
    print("Loading... \n")

    time.sleep(70)

    print("Loading complete! \n")

    while True:
        tasks_upload_input = input("Please enter letter x to continue: \n")

        if validate_tasks_upload_input(tasks_upload_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return tasks_upload_input


def validate_tasks_upload_input(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def count_tasks_results_twelve(task_input_twelve):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_twelve = SHEET.worksheet('tracker')
    task_column_twelve = retrieve_task_data_twelve.col_values(3)
    push_task_analyzer_twelve = SHEET.worksheet("analyzer")

    twelve_row_count = 0
    for item in task_column_twelve:
        if item == task_input_twelve:
            twelve_row_count += 1

    print(f"{task_input_twelve} - [{twelve_row_count}]")

    push_task_analyzer_twelve.update('A36', task_input_twelve)
    push_task_analyzer_twelve.update('B36', twelve_row_count)

    return twelve_row_count


def count_tasks_results_thirteen(task_input_thirteen):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_thirteen = SHEET.worksheet('tracker')
    task_column_thirteen = retrieve_task_data_thirteen.col_values(3)
    push_task_analyzer_thirteen = SHEET.worksheet("analyzer")

    thirteen_row_count = 0
    for item in task_column_thirteen:
        if item == task_input_thirteen:
            thirteen_row_count += 1

    print(f"{task_input_thirteen} - [{thirteen_row_count}]")

    push_task_analyzer_thirteen.update('A37', task_input_thirteen)
    push_task_analyzer_thirteen.update('B37', thirteen_row_count)

    return thirteen_row_count


def count_tasks_results_fourteen(task_input_fourteen):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_fourteen = SHEET.worksheet('tracker')
    task_column_fourteen = retrieve_task_data_fourteen.col_values(3)
    push_task_analyzer_fourteen = SHEET.worksheet("analyzer")

    fourteen_row_count = 0
    for item in task_column_fourteen:
        if item == task_input_fourteen:
            fourteen_row_count += 1

    print(f"{task_input_fourteen} - [{fourteen_row_count}]")

    push_task_analyzer_fourteen.update('A38', task_input_fourteen)
    push_task_analyzer_fourteen.update('B38', fourteen_row_count)

    return fourteen_row_count


def count_tasks_results_fifteen(task_input_fifteen):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_fifteen = SHEET.worksheet('tracker')
    task_column_fifteen = retrieve_task_data_fifteen.col_values(3)
    push_task_analyzer_fifteen = SHEET.worksheet("analyzer")

    fifteen_row_count = 0
    for item in task_column_fifteen:
        if item == task_input_fifteen:
            fifteen_row_count += 1

    print(f"{task_input_fifteen} - [{fifteen_row_count}]")

    push_task_analyzer_fifteen.update('A39', task_input_fifteen)
    push_task_analyzer_fifteen.update('B39', fifteen_row_count)

    return fifteen_row_count


def count_tasks_results_sixteen(task_input_sixteen):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_sixteen = SHEET.worksheet('tracker')
    task_column_sixteen = retrieve_task_data_sixteen.col_values(3)
    push_task_analyzer_sixteen = SHEET.worksheet("analyzer")

    sixteen_row_count = 0
    for item in task_column_sixteen:
        if item == task_input_sixteen:
            sixteen_row_count += 1

    print(f"{task_input_sixteen} - [{sixteen_row_count}]")

    push_task_analyzer_sixteen.update('A40', task_input_sixteen)
    push_task_analyzer_sixteen.update('B40', sixteen_row_count)

    return sixteen_row_count


def count_tasks_results_svnteen(task_input_svnteen):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_svnteen = SHEET.worksheet('tracker')
    task_column_svnteen = retrieve_task_data_svnteen.col_values(3)
    push_task_analyzer_svnteen = SHEET.worksheet("analyzer")

    svnteen_row_count = 0
    for item in task_column_svnteen:
        if item == task_input_svnteen:
            svnteen_row_count += 1

    print(f"{task_input_svnteen} - [{svnteen_row_count}]")

    push_task_analyzer_svnteen.update('A41', task_input_svnteen)
    push_task_analyzer_svnteen.update('B41', svnteen_row_count)

    return svnteen_row_count


def count_tasks_results_eghtteen(task_input_eghtteen):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_eghtteen = SHEET.worksheet('tracker')
    task_column_eghtteen = retrieve_task_data_eghtteen.col_values(3)
    push_task_analyzer_eghtteen = SHEET.worksheet("analyzer")

    eghtteen_row_count = 0
    for item in task_column_eghtteen:
        if item == task_input_eghtteen:
            eghtteen_row_count += 1

    print(f"{task_input_eghtteen} - [{eghtteen_row_count}]")

    push_task_analyzer_eghtteen.update('A42', task_input_eghtteen)
    push_task_analyzer_eghtteen.update('B42', eghtteen_row_count)

    return eghtteen_row_count


def count_tasks_results_nineteen(task_input_nineteen):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_nineteen = SHEET.worksheet('tracker')
    task_column_nineteen = retrieve_task_data_nineteen.col_values(3)
    push_task_analyzer_nineteen = SHEET.worksheet("analyzer")

    nineteen_row_count = 0
    for item in task_column_nineteen:
        if item == task_input_nineteen:
            nineteen_row_count += 1

    print(f"{task_input_nineteen} - [{nineteen_row_count}]")

    push_task_analyzer_nineteen.update('A43', task_input_nineteen)
    push_task_analyzer_nineteen.update('B43', nineteen_row_count)

    return nineteen_row_count


def count_tasks_results_twenty(task_input_twenty):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_twenty = SHEET.worksheet('tracker')
    task_column_twenty = retrieve_task_data_twenty.col_values(3)
    push_task_analyzer_twenty = SHEET.worksheet("analyzer")

    twenty_row_count = 0
    for item in task_column_twenty:
        if item == task_input_twenty:
            twenty_row_count += 1

    print(f"{task_input_twenty} - [{twenty_row_count}]")

    push_task_analyzer_twenty.update('A44', task_input_twenty)
    push_task_analyzer_twenty.update('B44', twenty_row_count)

    return twenty_row_count


def count_tasks_results_twentyone(task_input_twentyone):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_twentyone = SHEET.worksheet('tracker')
    task_column_twentyone = retrieve_task_data_twentyone.col_values(3)
    push_task_analyzer_twentyone = SHEET.worksheet("analyzer")

    twentyone_row_count = 0
    for item in task_column_twentyone:
        if item == task_input_twentyone:
            twentyone_row_count += 1

    print(f"{task_input_twentyone} - [{twentyone_row_count}]")

    push_task_analyzer_twentyone.update('A45', task_input_twentyone)
    push_task_analyzer_twentyone.update('B45', twentyone_row_count)

    return twentyone_row_count


def count_tasks_results_twntytwo(task_input_twntytwo):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_twntytwo = SHEET.worksheet('tracker')
    task_column_twntytwo = retrieve_task_data_twntytwo.col_values(3)
    push_task_analyzer_twntytwo = SHEET.worksheet("analyzer")

    twntytwo_row_count = 0
    for item in task_column_twntytwo:
        if item == task_input_twntytwo:
            twntytwo_row_count += 1

    print(f"{task_input_twntytwo} - [{twntytwo_row_count}]")

    push_task_analyzer_twntytwo.update('A46', task_input_twntytwo)
    push_task_analyzer_twntytwo.update('B46', twntytwo_row_count)

    return twntytwo_row_count


def count_tasks_results_twntythree(task_input_twntythree):
    """
    Function retrieves tasks results and counts items repetitions.
    After reporting to the user, it updates analyzer sheet.
    """
    retrieve_task_data_twntythree = SHEET.worksheet('tracker')
    task_column_twntythree = retrieve_task_data_twntythree.col_values(3)
    push_task_analyzer_twntythree = SHEET.worksheet("analyzer")

    twntythree_row_count = 0
    for item in task_column_twntythree:
        if item == task_input_twntythree:
            twntythree_row_count += 1

    print(f"{task_input_twntythree} - [{twntythree_row_count}]")
    print("------------------------------------------------------------------")

    push_task_analyzer_twntythree.update('A47', task_input_twntythree)
    push_task_analyzer_twntythree.update('B47', twntythree_row_count)

    return twntythree_row_count


def tasks_report_exit():
    """
    Function prompts user to press x to access the final update messages.
    """
    print("------------------------------------------------------------------")

    while True:
        tasks_exit_input = input("Please enter letter x to continue: \n")

        if validate_tasks_exit_input(tasks_exit_input):
            print("Loading...")
            break

    print("------------------------------------------------------------------")

    return tasks_exit_input


def validate_tasks_exit_input(values):
    """
    Input validator function.
    Prints error message if user input does not match letter "x".
    """
    if values != "x":
        print("Invalid data, please input letter x then and try again. \n")
        return False

    return True


def export_results_analyzer():
    """
    User is informed that all reporting and uploading is complete.
    User is infromed on date and time of completion.
    Users receives again a final link to their sheet.
    Users can see outro messages.
    Input of letter x leads user to the sequence of exiting the program.
    """
    print("------------------------------------------------------------------")
    live_timestamp = datetime.now()
    print(f"{live_timestamp} \n")
    print("Daily results have been successfully sent to the analyzer. \n")
    print("Now you can access your sheet with detailed visual analysis. \n")
    print("Please follow this link: [https://bit.ly/life-tracker-sheet] \n")
    print("Thank you for participating. \n")
    print("See you tomorrow at the next tracking and analyzing mission! \n")

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
    Function raises SystemExit to leave the program.
    """
    print("------------------------------------------------------------------")
    print("Initiating Exit Sequence... \n")

    print("Loading... \n")

    time.sleep(3)

    countdown = 10

    while countdown >= 0:
        print(f"{countdown} seconds...")
        countdown -= 1
        time.sleep(1)

    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")

    raise SystemExit("Exiting...")


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
