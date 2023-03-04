#########################################################################
# Program: Class Exercise 3
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/3/23
#########################################################################
"""
# Project #1:   #########################################################################
#
# Distance Traveled 

# Distance = Speed X Time

# Getting the speed of a vehicle in mph
vehicle_speed = float(input("Enter the speed of the vehicle: "))

# Getting the number of hours the vehicle has been traveling
hours_traveling = int(input("Enter how many hours the vehicle has been trveling: "))

# While loop until MAX # of hours has been met
each_hour = 0
while each_hour < hours_traveling:
# Starting at the first hour and not at 0 hours
    each_hour = each_hour + 1

# Calculation for distance of the vehicle 
# has traveled for each hour of that time period
    distance = (vehicle_speed * each_hour)
# Displaying distance traveled for each hour
    print("Hours:\tDistance Traveled:")
    print(f"{each_hour}\t{distance}")
"""
"""
# Project #2:   #########################################################################
#
# Average Rainfall

# Getting the number of year
num_years = int(input("Enter the amount of years: "))

# Initializing accumulator variables
total_rainfall = 0
months = 0
avg_rainfall = 0.0

# Outer Loop will loop for each year
for itemi in range(num_years):
    # Inner Loop iterates 12x for each month of the year
    for itemj in range(12):
    # Getting the amount of rainfall in inches
        rainfall = int(input("Enter the amount of rainfall: "))

    # Calculation for total rainfall
        total_rainfall = (total_rainfall + rainfall)

    # Counting amount of months
        months = (months + 1)

# Calculation for the average amount of rainfall for the entire period
avg_rainfall = (total_rainfall / months)

# Displaying:
print(f"\nNumber of months: {months}")
print(f"Total inches of rainfall: {total_rainfall} in")
print("\nThe average rainfall per month")
print(f"for the entire period: {avg_rainfall:,.2f} in.")
"""

# Project #3: #########################################################################
#
# Sum of Numbers

# Initializing accumulator variables
sum_total = 0

pos_int = 0

# A (-) integer kicks you out this while loop
while pos_int >= 0:
    pos_int = int(input("Enter a positive number: "))
# Calculation for total of each positive integer
    sum_total = (sum_total + pos_int)

# Because the last number is a negative integer...
# subtract the negative number from the series of positve integers...
# before calculating the sum of the series of numbers.
sum_total = (sum_total - pos_int)

# Displaying sum of all positive integers
print(f"The sum of the series of psoitive numbers: {sum_total}")
