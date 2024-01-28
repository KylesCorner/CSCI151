"""
Kyle Krstulich
dateMDY
CSCI151
library.py

Description
"""
from stdio import writeln
from instream import InStream

# -------------------------------------------------------------------------------
# Classes
# -------------------------------------------------------------------------------


class Book:

    def __init__(self, title: str, author: str,
                 publisher: str, copyright: str):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._copyright = copyright

    def __str__(self) -> str:
        return f"{self._title} by {self._author}\n"\
            f"Published by {self._publisher} on {self._copyright}\n"


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input():
    """
    Returns command-line input. Else return false.
    """
    file_list = InStream("book.txt").readAllLines()
    output_list = [[] for x in range((len(file_list)//4))]
    output_index = -1

    for index, item in enumerate(file_list):
        if index % 4 == 0:
            output_index += 1
        output_list[output_index].append(item)

    return output_list


# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def list_to_book(book_data) -> Book:
    """
    """
    title, author, publisher, copyright = book_data
    return Book(title, author, publisher, copyright)


# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def main():
    books = __gather_input()
    for book in books:
        writeln(list_to_book(book))


if __name__ == "__main__":
    main()
