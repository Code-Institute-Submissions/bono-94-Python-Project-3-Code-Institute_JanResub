# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
        print(f"iInvalid data: {e}, please try again \n")
        return False

    return True
    
def update_sales_worksheet(data):
    """
    Updates sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet ("dashboard")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated succesfully . \n")

data = get_main_data()
print(data)
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)

