import calendar

def count_days(year: int, month: int, whichday: int) -> int:
    """Given a set of year, month and weekday, return how many of that weekdays there are in that month.
    Parameters:
        year (int): Four-digit year
        month (int): Two-digit month
        whichday (int): Number of the weekday (0 is Monday, 6 is Sunday)
    Example:
        Input: 2025, 12, 0 (December 2025, Monday)
        Output: 5 (There are five Mondays in December 2025)
    """
    # Your code goes here.
    day_count = 0
    weeks = calendar.monthcalendar(year, month)
    for week in weeks:
        if week[whichday] != 0:
            day_count += 1
    return day_count

testyear = 2025
testmonth = 5
testday = 5
print(count_days(testyear, testmonth, testday))

