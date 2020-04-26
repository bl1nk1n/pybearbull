from pybearbull.core.moving_average import simple_average;

class Test_simple_average:
    def test_simple_average_no_data(self):
        data = []
        assert simple_average(data) == None

    def test_simple_average_two_zero(self):
        data = [0, 0]
        assert simple_average(data) == 0

    def test_simple_average_many_zero(self):
        data = [ 0 for i in range(0, 100) ]
        assert simple_average(data) == 0

    def test_simple_average_two_positive(self):
        data = [1, 1]
        assert simple_average(data) == 1

    def test_simple_average_many_small_positive(self):
        data = [ 1 for i in range(0, 20000, 200) ]
        assert simple_average(data) == 1

    def test_simple_average_many_large_positive(self):
        data = [ i for i in range(20000, 100000, 200) ]
        assert simple_average(data) == 59900

    def test_simple_average_two_negative(self):
        data = [-1, -1]
        assert simple_average(data) == -1

    def test_simple_average_many_small_negative(self):
        data = [ -1 for i in range(0, 20000, 200) ]
        assert simple_average(data) == -1

    def test_simple_average_many_large_negative(self):
        data = [ i for i in range(-20000, -100000, -200) ]
        assert simple_average(data) == -59900

    def test_simple_average_many_positive_negative(self):
        data = [i for i in range(-100000, 101000, 1000) ]
        assert simple_average(data) == 0
