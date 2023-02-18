#########################################################################
# Program: Apply: HW1
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
#########################################################################

"""
Description:

    Using the IF Block Structure
    There are 3 projects, each worth 33.3%
    Homework #2 is based on Chapter 3.
    Complete the 3 projects below. Be sure to use the if block structure for all three projects

"""

# Project #1: Quarter of the Year

# Asking user for a month as a number between 1-12.
user_month = int(input("Enter a month as a number between 1-12: "))

# Calculating if the month is:
#   In the 1st quarter...
#   2nd Quarter...
#   3rd Quarter...
#   or 4th Quarter.

# 1st Quarter
if user_month >= 1 and user_month <= 3:
    print("The month is in the 1st quarter.")
# 2nd Quarter
elif user_month >= 4 and user_month <= 6:
    print("The month is in the 2nd quarter.")
# 3rd Quarter
elif user_month >= 7 and user_month <= 9:
    print("The month is in the 3rd quarter.")
# 4th Quarter
elif user_month >= 10 and user_month <= 12:
    print("The month is in the 4th quarter.")
else:
    print("INVALID USER INPUT!")
print("\n\n")

#########################################################################

# Project #2: Hot Dog Cookout Calculator

# Hot Dogs come in packages of 10
# Hot Dogs Buns come in packages of 8

# Asking user of number of people at a cookout
cookout_attendees = int(input("Enter number of cookout attendees: "))

# Asking user for number of hot dogs for each attendees
hotdogs_per_attendees = int(input("Enter number of hotdogs each person will be given: "))

# Calculating the number of packages of hot dogs
# &
# Number of packages of hot dogs buns for a cookout
# With minimum amount of leftovers.

num_of_hotdogs = (cookout_attendees * hotdogs_per_attendees)

min_num_of_HOTDOG_packages = num_of_hotdogs // 10
min_num_of_BUN_packages = num_of_hotdogs // 8

hotdogs_LEFT = num_of_hotdogs - (min_num_of_HOTDOG_packages * 10)
buns_LEFT = num_of_hotdogs - (min_num_of_BUN_packages * 8)

# Displaying Cookout Data
print(f'\nMinimum number of hotdog packages: {min_num_of_HOTDOG_packages}')
print(f'Minimum number of bun packages: {min_num_of_BUN_packages}')
print(f'Number of hotdogs left over: {hotdogs_LEFT}')
print(f'Number of buns left: {buns_LEFT}')
print("\n\n")

#########################################################################

# Project #3: Software Sales

retail = 99.00
discount = 0.00
subtotal = 0.00
purchase_total = 0.00

# Asking user for number of packages purchased
packages_purchased = int(input("Enter the number of packages purchased. "))

# Calculating the discount
if packages_purchased > 9:
    # 10% Discount
        if packages_purchased >= 10 and packages_purchased <= 19:
            discount = .1
    # 20% Discount
        elif packages_purchased >= 20 and packages_purchased <= 49:
            discount = .2
    # 30% Discount
        elif packages_purchased >= 50 and packages_purchased <= 99:
            discount = .3
    # 40% Discount
        else:
            discount = .4
else:
    discount = 0
    print("No Applicable Discount!")

# Calculating for the Total of the purchase
subtotal = (packages_purchased * retail) 
purchase_total = subtotal - (subtotal * discount)

print(f'Amount of the discount: {discount: .0f}')
print(f'Total amount of the purchase: {purchase_total: .2f}')
