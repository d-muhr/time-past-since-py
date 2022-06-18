'''Potential To-Dos



- TODO: some of it might be easier with "dateutil" third-party party library
https://dateutil.readthedocs.io/en/stable/ which is recommended e.g. on
https://realpython.com/lessons/date-time-arithmetic/. Especially the following is aussichtsreich:
"Computing of relative deltas between two given date and/or datetime objects;"

--------------------
- TODO: ideally the input in Option B and the output format are the same. Currently they are not.
 o 1 way to do this might be the following from https://docs.python.org/3/library/string.html#string.ascii_uppercase
 Using type-specific formatting:
>>>

>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'
--------------------



'''

# from datetime import dat (TODO: some of the modules might be mentioned
# twice, so fix this)
from datetime import timedelta
import pyinputplus as pyip
import sys

# Welcome Text
print('''Did you ever wonder for how many days you and your partner are a
couple (or you and your childhood friend know each other) or how many hours
have past since you are born?

''')

# main loop starts
while True:
    # Giving the user 2 options how to proceed
    print('''This program offers you 2 options on what to calculate:
    - A)How many years or weeks or days or minutes or seconds pass, have past or will pass between two different dates (e.g. 1/1/1990 and 5/5/2035)?
    - B)Which date is a certain number of days before or after a certain date (e.g. 1000 days after today)?

    ''')

    chosen_calculation = pyip.inputMenu(
        ['A', 'B'], lettered=False, numbered=False)

    if chosen_calculation == 'A':
        # Let user input 2 dates (the following format works too for the dates:
        # "11/03/21" or "11/3/21)
        chosen_date_1 = pyip.inputDate(
            'Type in the first date in the format "MM/DD/YYYY" (Month-Day-Year) for example "11/03/2021" for November, 3rd 2021) (> ')

        chosen_date_2 = pyip.inputDate(
            'Type in the second date in the format "MM/DD/YYYY" (Month-Day-Year) for example "11/03/2021" for November, 3rd 2022) (> ')

        # Calculate the amout of time between the 2 dates (with datetime
        # module)

        # These Variables are for calculating the seconds, minutes, hours etc.
        delta_1_second = timedelta(seconds=1)
        delta_1_minute = timedelta(minutes=1)
        delta_1_hour = timedelta(hours=1)
        delta_1_day = timedelta(days=1)
        delta_1_week = timedelta(weeks=1)
        delta_1_year = timedelta(days=365)

        # The Date-Difference is calculated
        chosen_date_earlier = min(chosen_date_1, chosen_date_2)
        chosen_date_later = max(chosen_date_1, chosen_date_2)
        date_difference = chosen_date_later - chosen_date_earlier

        # Output
        print(
            "---The amount of time between the 2 dates (",
            chosen_date_earlier,
            "and",
            chosen_date_later,
            ") is:",
            round(
                date_difference /
                delta_1_year,
                2),
            "years or",
            round(
                date_difference /
                delta_1_week,
                2),
            "weeks or",
            round(
                date_difference /
                delta_1_day,
                2),
            "days or",
            round(
                date_difference /
                delta_1_hour,
                2),
            "hours",
            round(
                date_difference /
                delta_1_minute,
                2),
            "minutes or",
            round(
                date_difference /
                delta_1_second,
                2),
            "seconds---")

    if chosen_calculation == 'B':
        # User chooses the first date (the following format works too for the
        # dates: "11/03/21" or "11/3/21)
        chosen_date_1 = pyip.inputDate(
            'Type in the date in the format "MM/DD/YYYY" (Month-Day-Year) for example "11/03/2021" for November, 3rd 2021) (> ')

        # The user chooses if the new date is in the future or the past.
        print("Please type if the new date you want to calculate is in the future or the past.")
        choice_future_past_input = pyip.inputMenu(
            ['future', 'past'], lettered=True, numbered=False)

        # User types in how many days the date is supposed to be in the
        # past/future and the new date is displayed.
        print("Please type the number of days you want to calculate from",
              chosen_date_1, "into the", choice_future_past_input, ".")
        days_difference = pyip.inputInt('Number of Days: >>> ')

        if choice_future_past_input == 'future':
            new_date = chosen_date_1 + timedelta(days=days_difference)

        if choice_future_past_input == 'past':
            new_date = chosen_date_1 - timedelta(days=days_difference)

        print(
            "---The new date which is",
            days_difference,
            "days in the",
            choice_future_past_input,
            "of",
            chosen_date_1,
            "is:",
            new_date,
            "---")

    # User can make another calculation or quit the program
    print("Do you want to make another calculation or quit the program?")

    proceed_how = pyip.inputMenu(
        ['AGAIN', 'QUIT'], lettered=True, numbered=False)

    if proceed_how == 'AGAIN':
        continue

    if proceed_how == 'QUIT':
        print("Thanks for using the program!")
        sys.exit()
