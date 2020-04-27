################################################################################
# This file is part of the ManBearBull/PyBearBull project.                     #
# Copyright (C) 2020 Sam Hentschel (bl1nk1n) and the PyBearBull Contributors   #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU Affero General Public License as published by the #
# Free Software Foundation, either version 3 of the License, or (at your       #
# option) any later version.                                                   #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License #
# for more details.                                                            #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.       #
################################################################################
"""
Provides moving average based technical analysis functions.

Functions:

    simple_average([number]) -> number|None
    simple_moving_average({key:number}, number) -> {key:number}|None
"""

def simple_average(data):
    """
    Takes in an array of numbers and returns a simple average of them.

    Parameters:
            data ([number]): a non-empty array of numbers
    
    Return:
            savg (number): a simple average of all the data in the array 
                           if data is non-empty

            None:          if data is empty
    """
    if (len(data) == 0):
        return None
    savg = sum(data) / len(data)
    return savg

def simple_moving_average(data, window):
    """
    Computes a simple moving average of the data with a given window.

    Parameters:
            data ({key:number}): a non-empty dictionary of keys and numerical
                                 values

            window (number): a positive number less than the number of elements
                             in the data dictionary that denotes the number of
                             elements from the data to include in each simple
                             moving average point

    Returns:
            sma ({key: number}): a dictionary of keys and numerical values that
                                 denote the simple moving average of the data
                                 with the given window
                                 if data is non-empty, and window is a positive
                                 number less than the number of elements in data

            None:                if data is empty; the window is less than or
                                 equal to zero; or the window is greater than
                                 the number of elements in data
    """
    if (len(data) == 0 or window > len(data) or window <= 0):
        return None

    keys = list(data.keys())
    values = list(data.values())
    sma = {}

    for i in range(0, (len(keys) - window) + 1):
        sma[keys[i + (window - 1)]] = simple_average(values[i:i + window])

    return sma
