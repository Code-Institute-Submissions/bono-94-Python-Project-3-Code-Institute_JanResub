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
    """
    print("Please enter this DATA")
    print("Data should be six numbers, separated by commas")
    print("Example: 1,2,3,4,5,6\n")

    data_str = input("Enter your data here")
    print(f"the data provided is {data_str}")

get_main_data()