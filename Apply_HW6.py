#########################################################################
# Program: Apply HW6
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/24/23
#########################################################################

# Project #1 (Based on Chapter 6 Files and Exceptions) #########################################################################
#
"""
def main():
    # Calling Functions
    #WriteThings()
    ReadThings()

# Function: Writing things to a file
def WriteThings():
    # Opening File to WRITE to
    thingsfile = open("things.txt", "w")

    # User Input of things
    animal = input("Enter the name of an animal: ")
    fruit = input("Enter the name of a fruit: ")
    country = input("Enter the name of a country: ")

    # Writing to Things File
    thingsfile.write(animal + "\n")
    thingsfile.write(fruit + "\n")
    thingsfile.write(country + "\n")
    print("Things have been written to file.")

    # Closing Things File
    thingsfile.close()

# Project #1.1 #########################################################################
#

def ReadThings():
    # Opening things file to READ from
    outfile = open('things.txt', 'r')

    # Reading thigns from the file and setting value
    readThingsFile = outfile.read()

    # Closing file
    outfile.close()

    # Printing contents read from file
    print("\nDisplaying Things from file: \n" + readThingsFile)

    # Calling Main
main()
"""
"""
# Project #1.3 #########################################################################
#

def WriteNumlist():
    num = 1

    # Opening a file to WRITE
    outfile = open("number_list.txt", "w")

    # Using for loop to write numbers 1-100 to file
    for number in range(100):
        outfile.write(str(num) + "\n")
        num += 1    # Incrementing num
    print("Numbers have been written to file.")

    outfile.close()
WriteNumlist()
"""

# Project #2 #########################################################################
# (Create a GUI application)
#

import tkinter as tk                # Import the gui interface controls
from tkinter import messagebox      # Imports the messagebox display

win = tk.Tk()                       # Create the window interface
win.geometry("400x100")             # Width x height in pixels
win.title("Sum of Numbers in File")   # Label for the title

# Function Definitions 
def read():
    # Initializing variable
    file_sum = 0

    with open("numbers.txt", "r") as numfile:
        for each_line in numfile:
            # Calculating the sum of all the
            # numbers in the text file
            file_sum += int(each_line)

    # Displaying sum of file numbers
    messagebox.showinfo("Information,", "The sum of all numbers in the file: " + str(file_sum))

def quit():
    messagebox.showinfo("Information", "Thank you...")
    win.destroy() # closes the interface

                        # Call the function write
btnWrite = tk.Button(win, text = "Read", command = read).grid(column = 1, row = 0) # Button Widget

                        # Command Calls the quit function
btnQuit = tk.Button(win, text = "Quit", command = quit).grid(column = 2, row = 0) # Button Widget

win.mainloop() # Ensure the interfaces stays on window