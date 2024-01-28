"""
Kyle Krstulich
04/04/2023
CSCI151
stockprices.py

Finally, create interesting Table clients to produce plots of the data.

**Include a comment in your header of the client that indicates how to run the
client on the command line.

Example:
    python3 stockprices.py START_MONTH START_YEAR END_MONTH END_YEAR
    python3 stockprices.py 12 1976 3 2005
"""
import stddraw
import stdstats
import datetime
from table import Table
from sys import argv
from stdio import writeln, readInt

table = Table()


def gather_input():
    if len(argv) < 5:
        writeln('python3 stockprices.py START_MONTH START_YEAR END_MONTH'
                ' END_YEAR')
        exit()
    else:
        return (int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]))


def get_start_end_date():

    start_month, start_year, end_month, end_year = gather_input()

    if start_year > end_year:
        writeln("Start Year must be before end year")
        exit()
    if not (0 < start_month <= 12) or not (0 < end_month <= 12):
        writeln("Month out of range")
        exit()

    month_range = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31,
        12: 30
    }
# Leap year?
    for d in range(1, month_range[start_month] + 1):
        test_day = datetime.date(start_year, start_month, d).timetuple()
        if test_day in table:
            start_day = d
            break

    for d in range(month_range[end_month], 0, -1):
        test_day = datetime.date(end_year, end_month, d).timetuple()
        if test_day in table:
            end_day = d
            break

    start_date = datetime.date(start_year, start_month, start_day).timetuple()
    end_date = datetime.date(end_year, end_month, end_day).timetuple()

    return start_date, end_date


def draw(data: list):
    #  screen config
    stddraw.setCanvasSize(1600, 800)
    stddraw.setXscale(0, len(data))
    stddraw.setYscale(min(data), max(data))
    stdstats.plotLines(data)
    stddraw.show()


def output_csv(start, end):
    stocks = table.get_date_range_title(start, end)
    [writeln(item) for item in stocks]


def menu():
    start_date, end_date = get_start_end_date()
    menu_selection = "Please make a selection\n"\
        "1. Open\n"\
        "2. High\n"\
        "3. Low\n"\
        "4. Close\n"\
        "5. Adj. Close\n"\
        "6. Volume\n"\
        "7. Exit"
    writeln(menu_selection)
    user_input = readInt()

    match user_input:
        case 1:
            total_opens = table.get_opens(start_date, end_date)
            avg_open = table.get_avg_open(start_date, end_date)
            output_csv(start_date, end_date)
            writeln(f"Average Open: ${avg_open:.2f}")
            writeln(f"Minimum Open: $"
                    f"{min(total_opens):.2f}")
            writeln(f"Maximum Open: $"
                    f"{max(total_opens):.2f}")
            draw(total_opens)

        case 2:
            total_highs = table.get_highs(start_date, end_date)
            avg_high = table.get_avg_high(start_date, end_date)
            output_csv(start_date, end_date)
            writeln(f"Average High: ${avg_high:.2f}")
            writeln(f"Minimum High: $"
                    f"{min(total_highs):.2f}")
            writeln(f"Maximum High: $"
                    f"{max(total_highs):.2f}")
            draw(total_highs)

        case 3:
            total_lows = table.get_lows(start_date, end_date)
            avg_low = table.get_avg_low(start_date, end_date)
            output_csv(start_date, end_date)
            writeln(f"Average Low: ${avg_low:.2f}")
            writeln(f"Minimum Low: $"
                    f"{min(total_lows):.2f}")
            writeln(f"Maximum Low: $"
                    f"{max(total_lows):.2f}")
            draw(total_lows)

        case 4:
            total_closes = table.get_closes(start_date, end_date)
            avg_close = table.get_avg_close(start_date, end_date)
            output_csv(start_date, end_date)
            writeln(f"Average Close: ${avg_close:.2f}")
            writeln(f"Minimum Close: $"
                    f"{min(total_closes):.2f}")
            writeln(f"Maximum Close: $"
                    f"{max(total_closes):.2f}")
            draw(total_closes)

        case 5:
            total_adj_closes = table.get_adj_closes(start_date, end_date)
            avg_adj_close = table.get_avg_adj_close(start_date, end_date)
            output_csv(start_date, end_date)
            writeln(f"Average Adj. Close: ${avg_adj_close:.2f}")
            writeln(f"Minimum Adj Close: $"
                    f"{min(total_adj_closes):.2f}")
            writeln(f"Maximum Adj Close: $"
                    f"{max(total_adj_closes):.2f}")
            draw(total_adj_closes)

        case 6:
            total_volumes = table.get_volumes(start_date, end_date)
            avg_volume = table.get_avg_volume(start_date, end_date)
            output_csv(start_date, end_date)
            writeln(f"Average Volume: {avg_volume:.0f} stocks")
            writeln(f"Minimum Volume: "
                    f"{min(total_volumes)} stocks")
            writeln(f"Maximum Volume: "
                    f"{max(total_volumes)} stocks")
            draw(total_volumes)

        case 7:
            writeln("Goodbye!")
            exit()

        case _:
            writeln("Error wrong selection")
            menu()


menu()
