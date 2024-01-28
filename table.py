"""
Kyle Krstulich
04/03/2023
CSCI151
table.py

Then, compose a data type Table that reads the file to build an array of Entry
objects and supports methods for computing averages over various periods of
time. Finally, create interesting Table clients to produce plots of the data.

TODO
--------------------------------------------------------------------------------

Output the csv file to the command-line
"""
from stdio import writeln
from instream import InStream
from entry import Entry
import datetime


# -------------------------------------------------------------------------------
# Public classes
# -------------------------------------------------------------------------------


class Table:

    # ------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------

    def __init__(self, path_to_csv: str = "djia.csv"):
        self._csv_array = [Entry(item.split(",")) for item in
                           InStream(path_to_csv).readAllLines()]
        self._dates = [item.get_date() for item in self.get_items()]
        self._iter = 0
        self._end_iter = len(self._csv_array)

    # ------------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------------

    def __str__(self):
        output = ""
        for item in self._csv_array:
            output += str(item)+"\n"
        return output

    def __contains__(self, timetuple):
        if timetuple in self._dates:
            return True
        else:
            return False

    # ------------------------------------------------------------
    # Private Methods
    # ------------------------------------------------------------

    def __avg(self, values: list) -> float:
        return sum(values)/len(values)

    def __get_date_list(self, start_date, end_date) -> list:
        """
        input; (year, month, day)
        """
        def __date_conv(date: tuple) -> object:
            year, month, day = date
            if year.isdigit():  # Format the date value to my liking
                if int(year) <= 6:
                    year = "20"+year
                else:
                    year = "19"+year

            return datetime.date(int(year), int(month), int(day)).timetuple()

        if type(start_date) == tuple:
            start_date = __date_conv(start_date)
            end_date = __date_conv(end_date)
        date_list = []

        if start_date not in self:
            writeln("enter a correct start date")
            return
        if end_date not in self:
            writeln("enter a correct end date")
            return

        for item in self.get_items():

            if start_date <= item <= end_date:
                date_list.append(item)

        return date_list

    # ------------------------------------------------------------
    # Public Methods
    # ------------------------------------------------------------

    def get_avg_open(self, start, end) -> float:
        return self.__avg([item.get_open()
                           for item in self.__get_date_list(start, end)])

    def get_avg_high(self, start, end) -> float:
        return self.__avg([item.get_high()
                           for item in self.__get_date_list(start, end)])

    def get_avg_low(self, start, end) -> float:
        return self.__avg([item.get_low()
                           for item in self.__get_date_list(start, end)])

    def get_avg_close(self, start, end) -> float:
        return self.__avg([item.get_close()
                           for item in self.__get_date_list(start, end)])

    def get_avg_adj_close(self, start, end) -> float:
        return self.__avg([item.get_adj_close()
                           for item in self.__get_date_list(start, end)])

    def get_avg_volume(self, start, end) -> float:
        return self.__avg([item.get_volume()
                           for item in self.__get_date_list(start, end)])

    def get_all(self) -> str:
        return reversed(self._csv_array)

    def get_title(self) -> str:
        return self._csv_array[0]

    def get_items(self) -> list:
        items = reversed(self._csv_array[1::])
        return list(items)

    def get_date_range_title(self, start, end) -> list:
        output = [self.get_title()]
        [output.append(item) for item in self.__get_date_list(start, end)]
        return output

    def get_date_range(self, start, end) -> list:
        return self.__get_date_list(start, end)

    def get_opens(self, start: object, end: object) -> list:
        dates = self.__get_date_list(start, end)
        return [item.get_open() for item in dates]

    def get_highs(self, start: object, end: object) -> list:
        dates = self.__get_date_list(start, end)
        return [item.get_high() for item in dates]

    def get_lows(self, start: object, end: object) -> list:
        dates = self.__get_date_list(start, end)
        return [item.get_low() for item in dates]

    def get_closes(self, start: object, end: object) -> list:
        dates = self.__get_date_list(start, end)
        return [item.get_close() for item in dates]

    def get_adj_closes(self, start: object, end: object) -> list:
        dates = self.__get_date_list(start, end)
        return [item.get_adj_close() for item in dates]

    def get_volumes(self, start: object, end: object) -> list:
        dates = self.__get_date_list(start, end)
        return [item.get_volume() for item in dates]


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------

def iter_test():
    table = Table()
    start = datetime.date(1999, 8, 19)
    end = datetime.date(2003, 7, 24)
    [writeln(item) for item in table.range(start, end)]


def main():
    table_obj = Table()

    start_date = ('00', '8', '24')  # 2000, Aug, 24
    end_date = ('06', '3', '9')  # 2006, March, 9

    date_list = table_obj._Table__get_date_list(start_date, end_date)
    avg_open = table_obj.get_avg_open(start_date, end_date)
    avg_high = table_obj.get_avg_high(start_date, end_date)
    avg_low = table_obj.get_avg_low(start_date, end_date)
    avg_close = table_obj.get_avg_close(start_date, end_date)
    avg_adj_close = table_obj.get_avg_adj_close(start_date, end_date)
    avg_volume = table_obj.get_avg_volume(start_date, end_date)
    writeln(table_obj)


if __name__ == "__main__":
    main()
