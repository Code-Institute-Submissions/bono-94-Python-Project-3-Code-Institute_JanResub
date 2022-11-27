# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('life_tracker')


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

#date-time
x=datetime.now()
print(x)


#running code 
run.py