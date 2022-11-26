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

def update_worksheet (data, worksheet):
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

    extra fo refractured code replace upper 2 update codes
        update_worksheet(sales_data, "sales")
        update_worksheet(new_surplus_data, "surplus")


print("Welcome to Life Data Automation")
main()

