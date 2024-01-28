"""
Kyle Krstulich
2023-03-29
CSCI151
sportsfilter.py

Problem Statement
Go to the Sports Reference website.  Sports Reference maintains websites
providing top notch statistics and resources for sports fans everywhere.

Pick a sport that you are interested in.  For example, I clicked on Basketball.
Find a set of data you would like to work with.  I selected Seasons and then
2021-22: Summary.

Create a csv file from the data.  Click to learn how to share information from
Sports Reference.

Compose a program that reads in the sports data create an instance of InStream
Produce at least 2 output files (2 instances of OutStream) with filtered data
(you choose how you want to filter the data).  Create some sort of
graph/histogram of your filtered data.

Include a comment in your code that demonstrates how to run the program.
Example:
     >>> python myprog.py data.csv

Be sure to include data with your submission to Moodle.

**You must use the book site modules InStream and OutStream and any others that
may be appropriate.
--------------------------------------------------------------------------------

For this assignment I decided to grab data from the 2022 NFL drafts. I
structured the csv file to get the data needed for the module. I extracted the
Montana alumni and total touchdowns // total games played for each team. I then
had a function translate dictionaries into strings so that I could output it to
either the command-line or an output file.

How to run my program:
    >>> python3 sportsfilter.py draftstats.csv
"""
from sys import argv
from stdio import writeln
from instream import InStream
from outstream import OutStream


# -------------------------------------------------------------------------------
# Private Functions
# -------------------------------------------------------------------------------


def __gather_input():
    """
    Returns command-line input. Else return false.
    """
    if len(argv) > 1:
        return InStream(argv[1])
    else:
        writeln('')


def __structure_data() -> list:
    """
    Reads lines from csv and structures it into an array.
    """
    input_file = __gather_input()
    stat_array = []

    for stat in input_file.readAllLines():
        stat_array.append(stat.split(","))

    for player_index, player in enumerate(stat_array):

        for item_index, item in enumerate(player):
            if not item:  # Fills empty values with '0'

                stat_array[player_index][item_index] = '0'

    return stat_array


def __dictionary_to_string(data: dict, title: list) -> str:
    """
    Reads in a dictionary and outputs a formatted string.
    """

    format_row = title[0] + "{:<20}" * (len(title))
    output_string = format_row.format("", *title[1::]) + "\n"

    for team, players in data.items():
        for player in players:
            format_row = team + "{:<20} " * (len(player) + 1)  # Table data
            output_string += format_row.format("", *player) + "\n"

    return output_string

# -------------------------------------------------------------------------------
# Public Functions
# -------------------------------------------------------------------------------


def get_drafts() -> dict:
    """
    Structures the csv file to get the values necessary for the program to
    function.
    Structure; {TEAM: [ROUND,RANK,NAME,POS,TD,COLLAGE,GAMES_PLAYED], ...}
    """
    data = __structure_data()

    team_drafts = {}

    for line in data[1::]:
        team = line[2]
        passing_td = line[16]
        rushing_td = line[20]
        recieving_td = line[23]
        draft_pick = line[1]
        draft_round = line[0]
        player_name = line[3]
        player_pos = line[4]
        college = line[27]
        games_played = line[12]

        if (passing_td.isdigit() and rushing_td.isdigit() and
                recieving_td.isdigit()):  # checks for digit
            player_td = str(int(passing_td) + int(rushing_td) +
                            int(recieving_td))

        player_data = [draft_round,
                       draft_pick,
                       player_name,
                       player_pos,
                       player_td,
                       college,
                       games_played]

        if team not in team_drafts.keys():
            team_drafts[team] = team_drafts.get(team, [])
        if player_data not in team_drafts.values():
            team_drafts[team].append(player_data)

    return team_drafts  # Round,Rank, Name, Pos, TD's, College, Games played


def get_total_td() -> dict:
    """
    Outputs a dictionary depicting each teams touchdowns for its draft picks.
    Structure; {TEAM: TD}

    """
    data = get_drafts()
    team_td = {}

    for team in data:
        td = 0
        if team not in team_td.keys():
            team_td[team] = team_td.get(team, 0)

        for player in data[team]:
            td += int(player[4])
        team_td[team] = td

    return team_td  # Team, TD


def get_montana_alumi() -> dict:
    """
    Returns a dictionary for all the Montana alumni, includes all schools from
    Montana. Structure: {TEAM: [NAME, POS, COLLEGE]}
    """

    data = get_drafts()
    alumni = {}
    for team in data:
        if team not in alumni.keys():
            alumni[team] = alumni.get(team, [])

        for player in data[team]:
            college = player[5]
            if college == 'Montana St.' or college == "Montana":
                alumni[team].append([player[2], player[3], player[5]])

    return alumni  # name, pos, college


def get_valuable_draft() -> dict:
    """
    Returns a dictionary for all the valuable team drafts. I calculated this by
    taking the amount of touchdowns // number of games played.
    Structure: {TEAM: VALUE}

    """
    data = get_drafts()
    touchdowns = get_total_td()
    valuable_draft = {}
    value = 0

    for team in data:
        if team not in valuable_draft:
            valuable_draft[team]: valuable_draft.get(team, 0)

        for player in data[team]:
            games = int(player[6])
            if games > 0:
                value += int(touchdowns[team])//games

        valuable_draft[team] = str(value)
        value = 0

    return valuable_draft


def valuable_draft_histogram() -> str:
    """
    Outputs a strings for a histogram depicting the team with the most
    valuable draft picks.

    """
    data = get_valuable_draft()
    histogram = 'Team:\tTotal Touchdowns // Total Games Played\n'

    histogram += "---|" + ("-" * 76) + "\n"  # Top line
    for team, value in data.items():
        #  Value as histogram
        histogram += team + "|" + ("*" * int(value)) + "\n"
        histogram += "---|" + ("-" * 76) + "\n"  # Separator

    return histogram


def output_to_file(output_string: str, file_string: str = "output.txt"):
    """
    Takes a string and outputs it to output.txt. New input overrides previous.

    """
    OutStream(file_string).writeln(output_string)

# -------------------------------------------------------------------------------
# Unit Tests
# -------------------------------------------------------------------------------


def testing():
    stat_array = __structure_data()
    total_td = get_total_td()
    alumni = get_montana_alumi()
    valuable_draft = get_valuable_draft()
    drafts = get_drafts()
    draft_str_title = ["Team", "Draft round", "Draft rank", "Name", "Position",
                       "Touchdowns", "College", "Games played"]
    draft_str = __dictionary_to_string(drafts, draft_str_title)

    valuable_draft_title = ["Team", "Draft value"]
    valuable_draft_str = __dictionary_to_string(
        valuable_draft, valuable_draft_title)

    alumni_title = ["Team", "Name", "Position", "College"]
    alumni_str = __dictionary_to_string(alumni, alumni_title)

    valuable_histogram = valuable_draft_histogram()

    writeln(draft_str)
    writeln(valuable_draft_str)
    writeln(alumni_str)
    writeln(valuable_histogram)


def main():
    header = "Kyle Krstulich\n2023-03-30\nCSCI151\noutput.txt\n\n"
    titles = ["\n2022 Drafts\n\n", "\nMontana Alumni\n\n",
              "\nValuable Draft Histogram\n\n"]
    draft_str_title = ["Team", "Draft round", "Draft rank", "Name", "Position",
                       "Touchdowns", "College", "Games played"]
    alumni_title = ["Team", "Name", "Position", "College"]

    alumni = get_montana_alumi()
    drafts = get_drafts()
    valuable_histogram = valuable_draft_histogram()

    draft_str = __dictionary_to_string(drafts, draft_str_title)
    alumni_str = __dictionary_to_string(alumni, alumni_title)
    output_string = header + titles[0] + draft_str
    output_to_file(output_string)

    output_string_2 = titles[1] + alumni_str + titles[2] + valuable_histogram
    output_to_file(output_string_2, "output2.txt")


if __name__ == "__main__":
    main()
