#
# Takes in an array of numbers and returns a simple average of them.
# Parameters:
#               data    -   array of numbers
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

#def simple_moving_average(data, window):
#    pass

#def exponential_moving_average(data, window, smoothing):
#    pass
