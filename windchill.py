"""
Kyle Krstulich
1/19/23
windchill.py

Given the temperature and the wind speed calculates wind chill.
"""
import stdio
from sys import argv

current_temp, wind_speed = float(argv[1]), float(argv[2]) # gathers command line input


def values_in_bounds(): # checks to see if values are valid

    if abs(current_temp) > 50:
        stdio.writeln("Temperature value out of bounds!")
        exit()

    if  wind_speed < 3 or wind_speed > 120 :
        stdio.writeln("Wind speed value out of bounds!")
        exit()

values_in_bounds()

def wind_chill(): #calculates wind chill

    return 35.74 + (0.6215 * current_temp) + ((0.4275*current_temp - 35.75)*(wind_speed**0.16))

stdio.writeln(f"Temperature = {current_temp}")
stdio.writeln(f"Wind speed = {wind_speed}")
stdio.writeln(f"Wind Chill = {wind_chill()}")
