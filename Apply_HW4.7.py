#########################################################################
# Program: HW 4.7
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/7/23
#########################################################################

"""
# Project #1: #########################################################################
#
# Initializing the sum for the tuple
sum = 0

# Initializing list of numbers to add up
test_tup = (15, 20, 123, 47, 26, 81)

# Creating for loop to sum numbers in the tuple
for num in test_tup:
    sum += num

# Displaying the sum of the series
print(f"The sum of the tuple is: {sum}")
"""
"""
# Project #2: #########################################################################
#

# Find the largest number in this Tuple 
test_tup = (15, 20, 123, 47, 26, 81)

# Initializing the largest variable 
largest_num = 0

# Looping to find the largest number
for num in test_tup:
# Determining the largest value with an if statement
    if largest_num < num:
        largest_num = num

print(f"The largest value in the Tuple is: {largest_num}")
"""
"""
# Project #3: #########################################################################
#

# Find the sum of all integer numbers in this Tuple
test_tup = ([17, 28], [93, 11], [20, 17])

# Getting the Sum of lists in the tuple
new_tuple = sum(map(sum, test_tup))

# Displaying the sum of the series
print(f"The sum of the tuple is: {new_tuple}")
"""

# Project #4: #########################################################################
#

##Sort this Tuple by the list total
input_tup = [(2, 20), (44, 1), (3, 13)]
# sorted_tup should be  ([3, 13], [2, 20], [44, 1])

# Sorting the tuple of lists
input_tup.sort(key=lambda x:x[0]+x[1])

# Printing result
print("The tuple after sorting lists : " + str(input_tup))
