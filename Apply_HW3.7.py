#########################################################################
# Program: Class Exercise 3.7
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/3/23
#########################################################################

# Project #1:   #########################################################################
"""
def main():
    get_scores()

    # List Place holder
    test_score = []

    get_total(test_score)

# The get_scores function gets a series of test
# scores from the user and stores them in a list.
# A reference to the list returned. 
def get_scores():
    # Create an empty list.
    test_scores = []

    # Create a varieble to control the loop
    again = 'y'

    # Get the scores from the user and add them to 
    # the list.
    while again == 'y':
        # Get a score and add it to the list.
        value = float(input('Enter a test score: '))
        test_scores.append(value)

    # Outputing the test scores into a text file
        salesfile = open('Test Scores.txt', 'w')
    # Outputing list to text file
        salesfile.write(str(test_scores))

    # Want to do this again?
        print('Do you want to add another score?')
        again = input('y = yes. Anything else = no: ')
        print()

    # Closing File
    salesfile.close()

    # Return the list
    return test_scores

# The get_total function accepts a list as an 
# argument returns the total of the values in 
# the list.
def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Create the total of the list elements.
    for num in value_list:
        total += num

    # Return the total.
    return total

# Call the main function.
if __name__=='__main___':
    main()

# Calling main
main()
"""

# Project #2: #########################################################################
#
# Number Analysis Program

# Initializing list
num_series = []

# Initializing loop variables 
lowest_num = 100
highest_num = 0
num_total = 0
series_avg = 0

for item in range(20):
    num = int(input("Enter a number: "))
    num_series.append(num)

# Calculations
    num_total += num

# Lowest Number
    if lowest_num > num:
        lowest_num = num
# Highest Number
    if highest_num < num:
        highest_num = num
# Average Calculation
series_avg = (num_total /20)

# Displaying 
print(f"Lowest number of the number series: {lowest_num}")
print(f"Highest number of the number series: {highest_num}")
print(f"Total of the number series: {num_total}")
print(f"Average of the number series: {series_avg}")