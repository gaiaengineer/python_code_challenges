# Import necessary modules
import math
import os
import random
import re
import sys

# Import the 'datetime' module to handle time-related operations
from datetime import datetime

# Define a function named 'timeConversion' that takes a string 's' representing time in 12-hour format
def timeConversion(s):
    # Check if the time is in the morning (AM) and it's 12:00 AM
    if s[-2:] == "AM" and s[:2] == "12": 
        # If so, convert it to 00:00 AM
        return "00" + s[2:-2] 
    
    # Check if the time is in the morning (AM)
    elif s[-2:] == "AM": 
        # If so, remove the AM suffix
        return s[:-2] 
    
    # Check if the time is in the afternoon/evening (PM) and it's 12:00 PM
    elif s[-2:] == "PM" and s[:2] == "12": 
        # If so, keep it as 12:00 PM
        return s[:-2] 
    
    # If the time is in the afternoon/evening (PM)
    else: 
        # Convert the hour part to 24-hour format by adding 12 to it
        return str(int(s[:2]) + 12) + s[2:8]

# Entry point of the program
if __name__ == '__main__':
    # Open a file for writing the output, specified by the environment variable 'OUTPUT_PATH'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the time string from the user
    s = input()

    # Call the 'timeConversion' function with the provided time string as an argument
    result = timeConversion(s)

    # Write the result to the output file
    fptr.write(result + '\n')

    # Close the output file
    fptr.close()