# This file is part of the ManBearBull/PyBearBull project.
# Copyright (C) 2020 Sam Hentschel (bl1nk1n)
# 
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
# 
# You should have received a copy of the GNU Affero General Public License along 
# with this program.  If not, see <https://www.gnu.org/licenses/>.



#
# Takes in an array of numbers and returns a simple average of them.
# Parameters:
#               data    -   array of numbers
#                       -   must not be empty
#
# Return:
#           - If the number of data elements is greater than 0, returns the
#             average of the numbers in the array.
#           
#           - If the number of data elements is equal to 0, returns None.
#
def simple_average(data):
    if (len(data) == 0):
        return None
    return sum(data) / len(data)

#
# Takes in a dictionary of {time: number} pairs and returns a dictionary of
# {date: simple moving average} pairs.
# Parameters:
#               data    -   dictionary of {time: number} pairs
#                       -   must not be empty
#
#               window  -   number of time periods for this simple moving
#                           average to cover
#                       -   must be greater than 0, but less than or equal to
#                           the size of the data
#
# Return:
#           - If the number of data elements is greater than 0, and the window
#             is greater than 0 but less than or equal to the data size, returns
#             a dictionary of times and simple moving averages.
#
#           - If the number of data elements is equal to 0, the window size is
#             greater than the amount of data, or the window size is less than
#             1, returns None.
#
def simple_moving_average(data, window):
    if (len(data) == 0 or window > len(data) or window <= 0):
        return None

    keys = list(data.keys())
    values = list(data.values())
    sma = {}

    for i in range(0, (len(keys) - window) + 1):
        sma[keys[i + (window - 1)]] = simple_average(values[i:i + window])

    return sma
