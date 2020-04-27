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
Provides testing for the pybearbull/core/moving_average.py functionality.

Classes:

    Test_Simple_Average
    Test_Simple_Moving_Average
"""
from pybearbull.core.moving_average import simple_average, simple_moving_average

class Test_Simple_Average:
    def test_simple_average_empty(self):
        data = []
        assert simple_average(data) == None

    def test_simple_average_both_zero(self):
        data = [0, 0]
        assert simple_average(data) == 0

    def test_simple_average_both_positive(self):
        data = [1, 1]
        assert simple_average(data) == 1

    def test_simple_average_both_negative(self):
        data = [-1, -1]
        assert simple_average(data) == -1

    def test_simple_average_many_zero(self):
        data = [0 for i in range(0, 100)]
        assert simple_average(data) == 0

    def test_simple_average_many_positive(self):
        data = [1 for i in range(0, 20000, 200)]
        assert simple_average(data) == 1

    def test_simple_average_many_negative(self):
        data = [-1 for i in range(0, 20000, 200)]
        assert simple_average(data) == -1

    def test_simple_average_many_large_positive(self):
        data = [i for i in range(20000, 100000, 200)]
        assert simple_average(data) == 59900

    def test_simple_average_many_large_negative(self):
        data = [i for i in range(-20000, -100000, -200)]
        assert simple_average(data) == -59900

    def test_simple_average_many_mixed(self):
        data = [i for i in range(-100000, 101000, 1000)]
        assert simple_average(data) == 0


class Test_Simple_Moving_Average:
    def test_simple_moving_average_empty(self):
        data = {}
        assert simple_moving_average(data, 3) == None

    def test_simple_moving_average_neg1_window_3_data(self):
        data = {"2 days ago": 7001, "1 day ago": 7000, "today": 6999}
        assert simple_moving_average(data, -1) == None

    def test_simple_moving_average_9_window_3_data(self):
        data = {"2 days ago": 7001, "1 day ago": 7000, "today": 6999}
        assert simple_moving_average(data, 9) == None

    def test_simple_moving_average_9_window_9_data(self):
        data = {"8 days ago": 6999, "7 days ago": 7000, "6 days ago": 7001,
                "5 days ago": 7000, "4 days ago": 6999, "3 days ago": 7000,
                "2 days ago": 7001, "1 day ago": 7000, "today": 7000}
        assert simple_moving_average(data, 9) == {"today": 7000}

    def test_simple_moving_average_3_window_9_period(self):
        data = {"8 days ago": 6999, "7 days ago": 7000, "6 days ago": 7001,
                "5 days ago": 7000, "4 days ago": 6999, "3 days ago": 7000,
                "2 days ago": 7001, "1 day ago": 7000, "today": 6999}
        assert simple_moving_average(data, 3) == {"6 days ago": 7000, 
                                               "5 days ago": 7000.333333333333,
                                               "4 days ago": 7000,
                                               "3 days ago": 6999.666666666667,
                                               "2 days ago": 7000,
                                               "1 day ago": 7000.333333333333,
                                               "today": 7000}
