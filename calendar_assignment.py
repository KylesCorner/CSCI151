"""
Kyle Krstulich
Chance Salois
Mason Hazel
3/9/23
CSCI151

2.1.35 Calendar. Compose a program cal.py that takes two command-line arguments
m and y and writes the monthly calendar for the mth month of year y.
"""
import stdio
import stdarray
from sys import argv


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __get_start_date(month: str, year: str) -> int:
    """
   Calculate the day of the week that a month starts on, given the month and
   year.

    Args:
        month (str): The month of the year as a string, from '1' to '12'.
        year (str): The year as a string in the format 'YYYY'.

    Returns:
        int: The day of the week that the month starts on, as an integer from
        0 (Sunday) to 6 (Saturday).

    Raises:
        ValueError: If the month or year arguments are not in the correct
        format.

    Example:
        >>> __get_start_date('3', '2022')
        1
    """
    if int(year) < 100:
        century = 0
        decade = int(year)
    else:
        decade = int(year[2::])
        century = int(year[0: len(year)-2])

    month = int(month)
    month_code = int("144025036146"[month-1])
    year_code = (decade + (decade // 4))
    leap_year_code = __is_leap_year(year)

    if century >= 24 or century < 17:  # Converts to the Julian calendar.
        century_code = (18 - century) % 7
    else:
        century_code = int("4206420"[century-17])

    if month in [1, 2] and leap_year_code:
        week_day = (year_code + month_code + century_code - 1) % 7
    else:
        week_day = (year_code + month_code + century_code) % 7

    return week_day


def __is_leap_year(year: str) -> bool:
    """
    Determine whether a year is a leap year.

    Args:
        year (str): The year as a string in the format 'YYYY'.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        ValueError: If the year argument is not in the correct format.

    Example:
        >>> __is_leap_year('2022')
        False
        >>> __is_leap_year('2024')
        True
    """
    leap_year_code = (int(year) % 4 == 0)
    leap_year_code = leap_year_code and ((int(year) % 100) != 0)
    leap_year_code = leap_year_code or ((int(year) % 400) == 0)

    return leap_year_code


def __days_in_month(month: str, year: str) -> int:
    """
    Given a month and year as strings, returns the number of days in that
    month.

    Parameters:
        month (str): A string representing the month of the year (1-12).
        year (str): A string representing the year (e.g. '2022').

    Returns:
        int: The number of days in the specified month and year.

    Raises:
        ValueError: If the month or year parameter is not a valid string
                    representation of a number.

    """
    month = int(month)
    if month == 2:
        if __is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def __alternate_input_method() -> tuple:
    """
    Prompts the user to enter a month and year until the input is valid
    based on the validate_inputs() function. Returns a tuple with the
    validated month and year.

    Returns:
        tuple[str, str]: A tuple containing the validated month and year
    """
    while True:
        stdio.writeln()
        month = input(
            "Please enter a number between 1 and 12 for the month: ").strip()
        year = input("Please enter a year: ").strip()
        if __validate_inputs(month, year):
            return month, year


def __validate_inputs(month: str, year: str) -> bool:
    """
    Validate inputs for the calendar function.

    Parameters:
        month (str): A string representing the month of the calendar
        (e.g. '1' for January)
        year (str): A string representing the year of the calendar
        (e.g. '2022')

    Returns:
        bool: True if inputs are valid, False otherwise.

    """

    if not (month.isdigit() and year.isdigit()):
        stdio.writeln("\nWait, that's illegal")
        return False

    if (1 <= int(month) <= 12) and (int(year) >= 1):
        return True
    else:
        stdio.writeln("\nWait, that's illegal")
        return False

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def get_date() -> tuple:
    """
    Retrieves the month and year input from command-line arguments and
    returns them as a tuple.

    If the arguments are missing or invalid, the function returns the result
    of calling the alternate_input_method function.

    Returns:
        str: A tuple containing the month (as a string) and year (as a string).

    """
    if len(argv) > 1:
        month, year = argv[1].strip(), argv[2].strip()

    else:
        month, year = __alternate_input_method()

    if not __validate_inputs(month, year):
        month, year = __alternate_input_method()

    return month, year


def calendar(month: str, year: str) -> None:
    """
    Given a month and year, print a calendar for that month and year.

    Parameters:
        month (str): A string representing the month of the calendar
        (e.g. '1' for January)
        year (str): A string representing the year of the calendar
        (e.g. '2022')

    Returns:
        None

    """
    start_date = __get_start_date(month, year)
    calendar = stdarray.create1D(45, 0)
    month_length = __days_in_month(month, year)
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]

    for index in range(month_length + 1):
        calendar[index + start_date-1] = index

    stdio.writeln()
    for day in weekdays:
        stdio.writef("%4.3s", day)
    stdio.writeln()

    for index, number in enumerate(calendar):
        if number != 0:

            stdio.writef("%4.0f", number)
            if (index+1) % 7 == 0:
                stdio.writeln()

        else:
            stdio.writef("%4.0s", "")

    stdio.writeln()

# -------------------------------------------------------------------------------
# Unit Test
# -------------------------------------------------------------------------------


def main():
    month, year = get_date()
    calendar(month, year)


def loop_tests():

    for year in range(1, 3000):
        for month in range(1, 13):

            stdio.writeln(f"Month: {month}, Year: {year}")
            calendar(str(month), str(year))


if __name__ == "__main__":
    main()
