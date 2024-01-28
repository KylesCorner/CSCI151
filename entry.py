"""
Kyle Krstulich
04/03/2023
CSCI151
entry.py

Compose a data type Entry that can hold one entry in the table, with values for
date, opening price, daily high, daily low, closing price, and so forth.
"""
import datetime
from stdio import writeln


# -------------------------------------------------------------------------------
# Public Classes
# -------------------------------------------------------------------------------

class Entry:

    def __init__(self, table_entry: list):

        date_conv = {
            'Jan': '1',
            'Feb': '2',
            'Mar': '3',
            'Apr': '4',
            'May': '5',
            'Jun': '6',
            'Jul': '7',
            'Aug': '8',
            'Sep': '9',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12'
        }

        self._table_entry = table_entry
        date = self._table_entry[0].split('-')
        if date[0].isdigit():  # Format the date value to my liking
            if int(date[2]) <= 6:
                year = "20"+date[2]
            else:
                year = "19"+date[2]
            date = (date[0], date_conv[date[1]],
                    year)  # day, month, year
            day, month, year = date
            self._date = datetime.date(int(year), int(month), int(day))

        self._opening_price = self._table_entry[1]
        self._daily_high = self._table_entry[2]
        self._daily_low = self._table_entry[3]
        self._closing_price = self._table_entry[4]
        self._volume = self._table_entry[5]
        self._adj_closing_price = self._table_entry[6]

    # ------------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------------

    def __str__(self):
        format_str = "{:<15}" * (len(self._table_entry)+1)
        return format_str.format("", *self._table_entry)

    def __lt__(self, timetuple):
        if self.get_date() < timetuple:
            return True
        else:
            return False

    def __le__(self, timetuple):
        if self.get_date() == timetuple or \
                self.get_date() < timetuple:
            return True
        else:
            return False

    def __ge__(self, timetuple):
        if self.get_date() == timetuple or \
                self.get_date() > timetuple:
            return True
        else:
            return False

    def __gt__(self, timetuple):
        if self.get_date() > timetuple:
            return True
        else:
            return False

    def __eq__(self, timetuple):
        if self.get_date() == timetuple:
            return True
        else:
            return False

    def __ne__(self, timetuple):
        if self.get_date() != timetuple:
            return True
        else:
            return False

    # ------------------------------------------------------------
    # Public Methods
    # ------------------------------------------------------------

    def get_date(self) -> tuple:
        return self._date.timetuple()

    def get_day(self) -> int:
        return int(self._date.day)

    def get_month(self) -> int:
        return int(self._date.month)

    def get_year(self) -> int:
        return int(self._date.year)

    def get_open(self) -> float:
        return float(self._opening_price)

    def get_high(self) -> float:
        return float(self._daily_high)

    def get_low(self) -> float:
        return float(self._daily_low)

    def get_close(self) -> float:
        return float(self._closing_price)

    def get_volume(self) -> int:
        return int(self._volume)

    def get_adj_close(self) -> float:
        return float(self._adj_closing_price)


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------

def main():
    test_array = "1-Oct-28,239.43,242.46,238.24,240.01,3500000,240.01".split(
        ",")
    test_array_2 = \
        "28-Feb-06,11096.75,11115.24,10947.07,10993.41,2370860032,10993.41".\
        split(',')
    entry_obj = Entry(test_array)
    entry_obj_2 = Entry(test_array_2)

    writeln(entry_obj.get_date())
    writeln(entry_obj_2.get_date())
    writeln(entry_obj < entry_obj_2)
    writeln(entry_obj > entry_obj_2)
    writeln(entry_obj_2 == entry_obj)
    writeln(entry_obj != entry_obj_2)
    writeln(entry_obj <= entry_obj_2)
    writeln(entry_obj >= entry_obj_2)
    writeln(entry_obj.get_day())
    writeln(entry_obj.get_month())
    writeln(entry_obj.get_year())
    writeln(entry_obj)


if __name__ == "__main__":
    main()
