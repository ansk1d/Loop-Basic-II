# Biggie Size - Given a list, write a function that changes 
# all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same 
# list, but whose values are now [-1, "big", "big", -5]

def biggieSize(numbers):
    for i in range(0,len(numbers)):
        if numbers[i] > -1:
            numbers[i] = "big"
    return numbers
#########################

# Count Positives - Given a list of numbers, create a function to
#  replace the last value with the number of positive values.
#   (Note that zero is not considered to be a positive number).

def countPositives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
        else:
            continue
    
    list[len(list)-1] = count
    return list
#########################

# Sum Total - Create a function that takes a list and returns
#  the sum of all the values in the list.

def sumTotal(list):
    sum = 0
    for i in list:
        sum += i
    return sum
###############################

# Average - Create a function that takes a list and returns the average of all the values.x


def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

#####################################

# Length - Create a function that takes a list and returns the length of the list.


def length(list):
    return len(list)
###############################

# Minimum - Create a function that takes a list of numbers and returns
#  the minimum value in the list. If the list is empty, have the function return False.

def minimum(list):
    if len(list) == 0:
        return False
    else:
        small = list[0]
        for i in list:
            if i < small:
                small = i
        return small
###########################

# Maximum - Create a function that takes a list and returns the maximum
#  value in the list. If the list is empty, have the function return False.

def maximum(list):
    if len(list) == 0:
        return False
    else:
        small = list[0]
        for i in list:
            if i > small:
                small = i
        return small

#############################

# Ultimate Analysis - Create a function that takes a list and returns 
# a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimateAnalysis(list):
    dict = {
        'sumTotal':sumTotal(list),
        'average':average(list),
        'minimum':minimum(list),
        'maximum':maximum(list),
        'length':length(list)
        }
    return dict
#########################################

# Reverse List - Create a function that takes a list and return that
#  list with values reversed. Do this without creating a second list. 
#  (This challenge is known to appear during basic technical interviews.)

def reverseList(list):
    list = list[::-1]
    return list