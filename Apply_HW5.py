#########################################################################
# Program: Apply HW5
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/14/23
#########################################################################

# Project #1: #########################################################################
#
# Property Tax
"""
def main():
    get_prop_value = 0

    # Calling the getPropertyValue function
# Setting property value
    property_value = getPropertyValue(get_prop_value)

    # Calling the assessmentValue function
# Displaying the property value
    print(f"The value of this piece of property is: {assessmentValue(property_value): ,.2f} ")

    # Calling the propertyTax function
# Displaying the property tax
    print(f"The property tax is: {propertyTax(property_value): ,.2f} ")

# Defining the getPropertyValue function
def getPropertyValue(property_value):
    # Getting the value of property
    property_value = float(input("Enter the property value: "))

    return (property_value)

# Defining the assessmentValue function
def assessmentValue(property_value):
    # Calculating the assessment value.
    # (60% of property value)

    assessment_value = (property_value * 0.6)

    return float(assessment_value)

# Defining the propertyTax function
def propertyTax(property_value):
    # Calculating the property tax
    # ($0.72 for each $100)

    tax = (property_value * 0.72 * 0.01)

    return (tax)

# Calling main
main()
"""
"""
# Project #2: #########################################################################
#
# Stadium Seating

def main():
    # Initializing Variables
    A_Seats = 0
    B_Seats = 0
    C_Seats = 0
    income = 0

    # Calling functions:
# Getting/setting the value of each ticket type sold
    A_Seats = getClassASeats()
    B_Seats = getClassBSeats()
    C_Seats = getClassCSeats()

# Calculating the income generated from ticket sales
    income = calcIncome(A_Seats, B_Seats, C_Seats)

# Dislaying the income
    displayIncome(income)

def getClassASeats():
    Class_A_tickets = int(input("Enter the amount of A seats sold: "))

    return (Class_A_tickets)

def getClassBSeats():
    Class_B_tickets = int(input("Enter the amount of B seats sold: "))

    return (Class_B_tickets)

def getClassCSeats():
    Class_C_tickets = int(input("Enter the amount of C seats sold: "))

    return (Class_C_tickets)

def calcIncome(A, B, C):
    # A Seats = $20
    # B Seats = $15
    # C Seats = $10

    total = (A * 20)
    total += (B * 15)
    total += (C * 10)

    return (total)

def displayIncome(income_total):
    print(f"The income generated from the stadium is: ${income_total}")

# Calling main
main()
"""

# Project #3: #########################################################################
#
# Monthly Sales Tax

def main():
    # Calling Functions:
# Getting/setting the total sales for the month
    monthly_sales = getMonthlySales()

# Calculating the Country Sales Tax
    country_sales_tax = calcCountrySalesTax(monthly_sales)

# Caluclating the State Sales Tax
    state_sales_tax = calcStateSalesTax(monthly_sales)

# Displaying the Total Sales Tax (country + state)
    displayTotalTax(country_sales_tax, state_sales_tax, monthly_sales)

def getMonthlySales():
    sales = float(input("Enter the Monthly Sales: $"))
    return (sales)

def calcCountrySalesTax(sales):
    # Country Sales Tax is 2.5% of Monthly Sales
    country_tax = (sales * 0.025)

    return (country_tax)

def calcStateSalesTax(sales):
    # State Sales Tax is 5% of Monthly Sales
    state_tax = (sales * 0.05)

    return (state_tax)

def displayTotalTax(country, state, sales):

    # Calculation for total sales tax
    total = (country + state)
    sales = (sales - total)

    # Display section
    print(f"Country Sales Tax: ${country:,.2f}")
    print(f"State Sales Tax: ${state:,.2f}")
    print(f"The Total sales tax is: ${total:,.2f}")
    print(f"The sales after total taxes collected: ${sales:,.2f}")

# Calling main
main()