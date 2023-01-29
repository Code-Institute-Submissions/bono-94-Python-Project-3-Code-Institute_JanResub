# [Life Tracker](https://life-tracker.herokuapp.com/) 

Life tracker is a Phyton-based terminal program that runs in the Code Institute mock terminal deployed on Heroku.

Users can run this daily tracker and analyzer in order to capture and process their daily activities. 

Users input their events per each hour of the day inside the terminal that automatically updates the external Google Sheet and analyzes data.

- [Run program](https://life-tracker.herokuapp.com/)
- [Access results sheet](https://bit.ly/life-tracker-sheet)

![Multi-devices Views](./assets/media/images/extra/responsiveness.jpg)

----

## How it works?

- Life tracker is created to be the starting point in the ultimate processing of all aspects of life
- In this version user is presented first with an introduction, instructions, and rules
- User is requested to enter their personal information (username + ID number)
- Each time that program starts, it clears previous values in Google Sheet
- The program requests user to enter their daily events in the format of subcategories and custom tasks
- All inputs are exported to the tracking sheet
- Total time consumption per subcategories and tasks are presented in the analyzer worksheet
- It is where the user can see a visual representation of time consumption
- Users can save or share their results and start the program again

----

## Flowchart

![Flowchart](./assets/media/images/extra/flow.jpg)

----

## Features

### Existing Features

![Options](./assets/media/images/features/options.jpg)
- First sheet that visually shows user examples that they can use for their custom tasks

---


![Tracker](./assets/media/images/features/tracker.jpg)
- Second sheet where users' input get uploaded as per example in the row [2]

---


![Analyzer](./assets/media/images/features/analyzer.jpg)
- Third sheet where all calculated users' subcategories results of time consumption get uploaded

---

![Analyzer Tasks](./assets/media/images/features/analyzer-task.jpg)
- Third sheet where all calculated users' tasks results of time consumption get uploaded

---

![Intro](./assets/media/images/features/intro.jpg)
- Introduction to the program with the current date and time
- General steps of how the program works are disclosed to users
- Includes a link to external Google Sheet where user can track results

---

![rules](./assets/media/images/features/rules.jpg)
- General rules that should be respected in the program are disclosed to users

---

![ID](./assets/media/images/features/id.jpg)
- Users are informed on what is needed for personal identification and what are the rules for inputting them
- When message "Starting the program..." is printed, all previously inputted date in Google Sheet gets deleted

---

![Subcategory](./assets/media/images/features/sub.jpg)
- Main inputting function segment where the user is given the relevant time frame of a past event
- It repeats 24 times as for 24 hours in user's day
- Function displays numerical options for the user's convenience not having to constantly look at the options sheet or constantly retype options

---

![Subcategory Input](./assets/media/images/features/input.jpg)
- When sub-category input satisfies criteria being identical to the options, the code returns confirmation of success

---

![Tasks](./assets/media/images/features/tasks.jpg)
- Additional input function that captures custom task from user and expands general subcategory input to unique daily event 
- It repeats 24 times as for 24 hours in user's day
- User can input anything meaningful or detailed as they wish

---

![Input Track](./assets/media/images/features/input-track.jpg)
- User is presented with results for their previous 2 inputs for specific hour of a day
- Each number chosen by relevant subcategory gets converted to actual belonging Subcategory label
- As each function per hour of the day is processed, this is when it uploads the values to the Google Sheet tracker
- Once the last sub-category and tasks are inputted, the program does not continue running the same input functions again but sends the user to the next outro section of program
---

![Inputs Completed](./assets/media/images/features/inputs-completed.jpg)
- Informative break from longer periods of input
- When all values are inside of the tracker sheet, a user is informed that the whole process of updating tracker has occurred without an issue
---

![Outro](./assets/media/images/features/outro.jpg)
- After completing all the inputs and receiving reports, the user is presented with an outro message
- First, there is a time and date for each program completion
- Also user is reminded of the Google Sheets link in case they have not opened them yet to check the results
- After farewell with the user, the program informs the user how to start it again upon finishing the exiting sequence
- Inputting letter 'x' starts exiting sequence

---

![Exit](./assets/media/images/features/exit.jpg)
- The countdown from 10 seconds to 0 seconds starts

---

![Exit Two](./assets/media/images/features/exit-two.jpg)
- Countdown variable has inside 1 second waiting time so it creates the effect of and actual countdown
- Once the countdown reaches 0, the user receives a message that the program is exiting and raises system exit task

---
![Tracker Results](./assets/media/images/features/analyzer-results-one.jpg)
![Analyzer Results](./assets/media/images/features/analyzer-results.jpg)
- Once user has all inputs sent to the tracking worksheet, analyzer worksheet additionally reports consumption with graphic support

---

![Zapier](./assets/media/images/extra/zapier.jpg)
- After every upload of inputs or results to any sheet updates, Zapier sends and email alert of new input on the Google Sheets

---

### Upcoming Features

- Allow users to choose a 12-hour or 24-hour format
- Use regex patterns so the user cannot enter the username that contains any digits next to letters
- Use regex patterns so the user cannot enter an ID number that contains any letters next to digits
- Prevent user from entering any blank spaces for username and ID number
- Remove double values from the tasks analyzer and replace empty fields with sub-tasks
- Create a Microsoft Word document where user can carry out their to-do list that automatically
- Expand the list of categories, sub-categories, tasks, and sub-tasks
- Create a rewarding system
- Create a unique sheet for every user so the public cannot access private information
- Add voice-controlled inputs

----

## Data Structure Model

### Version 1
- Due to the code total length of approximately 5000 lines, it needed to be fractioned and spread across 7 Python files.
- Those files are all imported to the main file run.py
- Once they were imported all functions including "running functions" were synchronized so the code can run.
- Templates for all sub-category and tasks inputs segments have been expanded across other repetitive functions per hours
- All variables have been placed inside the functions with docstrings describing the purpose
- Each function has only a few main variables and some have a lot of small amount of print statements
- All functions were organized to flow in logical order and priority of usage
- Since all functions above line 1000 were placed in their belonging new Python files, all of the functions that assist in calling up function were also moved with them
- Only at the main run.py all of their "calling" pr "running functions" were introduced to and organized at the bottom of the code ensuring that the code actually runs
- Each function has been made under 80 characters horizontally and 24 rows vertically

### Version 2
- Major adjustments in the data structure model for Version 2 have been implemented
- Instead of extremely long project counting 5000+ lines of code, DRY method has been implemented to the fullest
- Creating advanced looping function allowed the total code to be reduced to under 600 lines
- Instead of repetitive functions for each of 24 hours per day, one architecural adjustment has converted those repetitive functions to a template that gets run for each 24 hours of a day
- Not only this reduces the gspread requests limit per minute but makes code much easier to read and evaluate
- When there is a change or addition it is easier to adjust one template function instead of doing it 24 times for each hour of a day
- This also reduces pressure on hardware and increases overall productivity and smooth user interaction

----

## Testing

This project was manually tested with following procedures:

- Code was passed through a PEP8 linter inside gitpod without any errors returned
- Program was tested with correct and incorrect inputs in the both gitpod and Heroku terminals

- If the user inputs ANYTHING besides the letter "x" and presses enter, it will show an error 

![Test X](./assets/media/images/testing/x.jpg)
- Inputting letter x, and all of it's repetitive functions under different name functions does not allow any other letters or multiple characters across all the files
---

![Test Info](./assets/media/images/testing/info.jpg)
- Inputting username, the program does not allow numbers as value, and successfully returns lowercase names to first letter capitalized
- Inputting ID number, the program does not allow letters only as the value as intended
- Starting the program line clears all values from the sheet as intended
---

![Test Info Two](./assets/media/images/testing/info-two.jpg)
- Username is successfully programmed to not alow user to leave it empty or enter more than 50 characters
---

![Test Sub](./assets/media/images/testing/sub.jpg)
- Sub-categories input successfully does not allow empty fields, lowercase, spaces, not identical values util input is identical to one from list of options
--- 

![Test Task](./assets/media/images/testing/task.jpg)
- Tasks input successfully does not allow empty fields, or inputs over 50 characters and under 3 letters
--- 

### Bugs

__Solved Bugs__


![Long Line](./assets/media/images/problems/line-long.jpg)
- All lines longer than 79 characters have been reduced by adjusting vocabulary and making content as concise as possible
--- 

![Max Read](./assets/media/images/problems/max-read.jpg)
- Terminal cannot read more than 60 read variables per minute, causing code to crash half-way through reporting tasks time consumption
--- 

![Max Read](./assets/media/images/problems/max-read-solved-two.jpg)
- Function was created half-way through tasks reporting to give 60 seconds break in order to execute the all funtions without causing problems with maximum readability per month
--- 

![Max Read](./assets/media/images/problems/max-read-solved.jpg)
- Finished runned code of introducting break of 1 minute at the half of tasks reports provided to the user 
--- 

__Unsolved Bugs__

- All bugs were solved
---

__Validator Testing__

PEP8
- No errors found when validating all 5000 lines of code from:
- [Code Institute CI Python Linter](https://pep8ci.herokuapp.com)

![Validator](./assets/media/images/extra/validator.jpg)

--- 

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku website.

### Deployment steps:
- Update requierements.txt
- Create or login to Heroku account
- Activate Student GitHub Pack
- Update billing information
- Create new app/website
    - add name and region
- Access settings
- Create Config Var
    - input “CREDS” into the “KEY” field
    - copy creds.json file contents and paste into “VALUE” field
    - add “PORT” to “KEY” and “8000” to “VALUE”
- Add Buildpack
    - add python to the top of the list
    - add nodejs to the bottom of the list
- Go to deployment section
    - select github and connect to the relevant account
    - search for relevant repository and connect
    - choose manual deployment option
    - everything gets installed
    - link is provided when finished
- Subscribe to ecodynos plan under the billing options
- Create README file
- Push changes
- Quick Redeployment

### [Run program](https://life-tracker.herokuapp.com/)
### [Access results sheet](https://bit.ly/life-tracker-sheet)
----

## Credits

### Content, Knowledge and Code
  
- All content and code are 100% unique and custom-made per request for a client in order to prevent any legal issues in the future and to provide full control over an optimized experience

- All content, concepts, and visuals have been exclusively written for this site and to solve specific problem for any user without any external inspiration

- Code structure is also 100% original and completely created by a developer. A developer has followed HTML, CSS, JavaScript and Python courses at [Code Institute](https://codeinstitute.net/global/) where theory on building blocks has been taught. After reading through knowledge materials to see what are possibilities of creating this site are, general blocks have been put together separately to create original work. Given completed examples have not been plagiarized but served as a general guide from a client for a developer from project examles such as: love-sandwiches and battleships. Finally, the README structure has been used by Code Institute's template and example in this project in order to be created under industry standards and expectations. A general python template for repository created for students before commencing their project for convenience has been imported before the first coding lines. Project requirements have been used as secondary rough guidelines for the content structure. Consultations with Student Care, Tutors, and Personal Mentor Rowan were provided by them as well which was crucial in this project creation by providing support, motivation, and mistakes indications

- All debugging and problem-solving has been done strictly by the developer trying different combinations with known and unknown elements and attributes. No external sources and no professional help just tutors for complex problems and developer's imagination and creativity

- [Code Institute Python Template](https://github.com/Code-Institute-Org/python-essentials-template)

__Code References:__

- [Free Code Camp](https://www.freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time/)

        from datetime import datetime

        current_dateTime = datetime.now()

        print(current_dateTime)
        # 2022-09-20 10:27:21.240752


- [Real Python](https://realpython.com/python-modules-packages/)

        import mod


- [Real Python](https://realpython.com/python-sleep/)

        >>> import time
        >>> time.sleep(3) # Sleep for 3 seconds


- [gspread](https://docs.gspread.org/en/v5.7.0/user-guide.html#clear-a-worksheet)

        worksheet.batch_clear(["A1:B1", "C2:E2", "my_named_range"])


- [gspread](https://docs.gspread.org/en/v5.7.0/user-guide.html#getting-a-cell-value)

        val = worksheet.acell('B1').value

- [gspread](https://www.freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time/)

        worksheet.update('B1', 'Bingo!')
---

### Media
  
- [Am I Responsive?](https://ui.dev/amiresponsive) - The photo from the website was used in this README file to demonstrate responsiveness

---

### Tools

- [Grammarly](https://app.grammarly.com/) - software has been used to verify grammar on the site and this README file

- [Zapier](https://zapier.com/) - online automation website that is used to send emails every time new user enters a new imput

- [Bitly](https://app.bitly.com/Bmbr0grLTGI/bitlinks/3gHaGFi/details) - online website that shorted the link to access the Google Sheet

---
Thank you for READING ME!

