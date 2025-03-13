month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_count(first_month, first_day, first_year, second_month, second_day, second_year):
    if not all(isinstance(i, int) for i in [first_month, first_day, first_year, second_month, second_day, second_year]):
        print("Error: All inputs must be integers.")
        return
    elif not (1 <= first_month <= 12):
        print("Error: Invalid month for first date.")
        return
    elif not (1 <= second_month <= 12):
        print("Error: Invalid month for second date.")
        return
    elif not (1 <= first_day <= month_days[first_month - 1]):
        print("Error: Invalid day for first date.")
        return
    elif not (1 <= second_day <= month_days[second_month - 1]):
        print("Error: Invalid day for second date.")
        return
    elif first_year < 1753:
        print("Error: Invalid year for first date. Must be 1753 or later.")
        return
    elif second_year < 1753:
        print("Error: Invalid year for second date. Must be 1753 or later.")
        return

    if (first_year, first_month, first_day) > (second_year, second_month, second_day):
        first_month, second_month = second_month, first_month
        first_day, second_day = second_day, first_day
        first_year, second_year = second_year, first_year

    days_left_in_month = month_days[first_month - 1] - first_day
    year_days = days_left_in_month
    for i in range(first_month, 12):
        year_days += month_days[i]
    #assert year_days >= 0, "Error: Computed days left in the first year should not be negative."

    year_count = second_year - first_year - 1
    day_count = year_count * 365 + year_days
    #assert day_count >= 0, "Error: Computed day count should not be negative."

    days_passed_in_last_year = sum(month_days[:second_month - 1]) + second_day
    day_count += days_passed_in_last_year
    #assert days_passed_in_last_year >= 0, "Error: Computed days in the last year should not be negative."

    leap_years = 0
    for i in range(first_year, second_year):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            leap_years += 1
    day_count += leap_years

    #assert leap_years >= 0, "Error: Computed leap year count should not be negative."
    #assert day_count >= 0, "Error: Final computed day count should not be negative."

    print(f"The number of days between {first_month}/{first_day}/{first_year} and {second_month}/{second_day}/{second_year} is {day_count}.")

test_case = 1
while test_case <= 12:
    #Before 1752, ERROR
    if test_case == 1:
        first_month = 1
        first_day = 1
        first_year = 2000
        second_month = 1
        second_day = 1
        second_year = 1752
    #Year is not an integer, ERROR
    elif test_case == 2:
        first_month = 1
        first_day = 1
        first_year = "banana"
        second_month = 1
        second_day = 1
        second_year = 2000
    #Month is less than 1: ERROR
    elif test_case == 3:
        first_month = 0
        first_day = 1
        first_year = 2000
        second_month = 1
        second_day = 1
        second_year = 2000
    #Month is greater than 12: ERROR
    elif test_case == 4:
        first_month = 13
        first_day = 1
        first_year = 2000
        second_month = 1
        second_day = 1
        second_year = 2000
    #Day is less than 1: ERROR
    elif test_case == 5:
        first_month = 1
        first_day = 0
        first_year = 2000
        second_month = 1
        second_day = 1
        second_year = 2000
    #Day is greater than the number of days in the month: ERROR
    elif test_case == 6:
        first_month = 1
        first_day = 32
        first_year = 2000
        second_month = 1
        second_day = 1
        second_year = 2000
    #First date is after the second date: Should be an error, but I added correction code
    elif test_case == 7:
        first_month = 1
        first_day = 8
        first_year = 2002
        second_month = 1
        second_day = 7
        second_year = 2000
    #Start and end on the same day
    elif test_case == 8:
        first_month = 1
        first_day = 9
        first_year = 2001
        second_month = 1
        second_day = 9
        second_year = 2001
    #Start and end in the same month & year
    elif test_case == 9:
        first_month = 1
        first_day = 9
        first_year = 2001
        second_month = 1
        second_day = 19
        second_year = 2001
    #Start and end in the same year
    elif test_case == 10:
        first_month = 1
        first_day = 9
        first_year = 2001
        second_month = 4
        second_day = 19
        second_year = 2001
    #Start and end in different years
    elif test_case == 11:
        first_month = 1
        first_day = 9
        first_year = 2001
        second_month = 10
        second_day = 6
        second_year = 2003
    #Take leap years into account
    elif test_case == 12:
        first_month = 1
        first_day = 9
        first_year = 2001
        second_month = 5
        second_day = 27
        second_year = 2028
    day_count(first_month, first_day, first_year, second_month, second_day, second_year)
    test_case +=1