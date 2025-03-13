month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_count(first_month, first_day, first_year, second_month, second_day, second_year):
    # Check for valid input
    assert 1 <= first_month <= 12, "Invalid month for first date."
    assert 1 <= second_month <= 12, "Invalid month for second date."
    assert 1 <= first_day <= month_days[first_month - 1], "Invalid day for first date."
    assert 1 <= second_day <= month_days[second_month - 1], "Invalid day for second date."
    assert first_year >= 1753, "Invalid year for first date."
    assert second_year >= 1753, "Invalid year for second date."

    # Ensure first date is earlier
    if (first_year, first_month, first_day) > (second_year, second_month, second_day):
        first_month, second_month = second_month, first_month
        first_day, second_day = second_day, first_day
        first_year, second_year = second_year, first_year

    # Calculate days left in first year
    days_left_in_month = month_days[first_month - 1] - first_day
    year_days = days_left_in_month
    for i in range(first_month, 12):  # Remaining months of the first year
        year_days += month_days[i]

    # Calculate full years between the two dates
    year_count = second_year - first_year - 1
    day_count = year_count * 365 + year_days

    # Calculate days in last year
    days_passed_in_last_year = sum(month_days[:second_month - 1]) + second_day
    day_count += days_passed_in_last_year

    # Count leap years in range
    leap_years = 0
    for i in range(first_year, second_year):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            leap_years += 1
    day_count += leap_years

    return day_count

# User input
first_month = int(input("Month (1-12): "))
first_day = int(input("Day (1-31): "))
first_year = int(input("Year: "))

second_month = int(input("Month (1-12): "))
second_day = int(input("Day (1-31): ")) 
second_year = int(input("Year: "))

# Output result
print(f"The number of days between {first_month}/{first_day}/{first_year} and {second_month}/{second_day}/{second_year} is {day_count(first_month, first_day, first_year, second_month, second_day, second_year)}.")